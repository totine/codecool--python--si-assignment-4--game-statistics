from reports import *
import sys
import os


def separator():
    print("\n")
    print("*" * 100)
    print("\n")


def little_separator():
    print("-" * 70)


def welcome_text():
    separator()
    print("Welcome to the game information archive. \nWhat would you want to know?\nEnter the number of question")


def list_of_questions(questions_list):
    little_separator()
    questions_to_display = [questions_list[i][1] for i in range(len(questions_list))]
    list_with_numbers(questions_to_display)
    little_separator()
    return questions_list


def list_with_numbers(list_to_display):
    step = 10

    if len(list_to_display) < step:

        text_to_display = ""
        for line in list_to_display:
            text_to_display += "[" + str(list_to_display.index(line) + 1) + "]" + ". " + line + "\n"
        little_separator()
        print(text_to_display)
        little_separator()
        return text_to_display

    else:
        i = 0
        while True:

            for j in range(i * step, i * step + step):
                if j == len(list_to_display):
                    break
                print("[" + str(j + 1) + "]" + ". " + list_to_display[j])
            if j != len(list_to_display):
                print("...")
            if j == len(list_to_display):
                little_separator()
                next_page = input("You are on the end of the list. Enter any key to end or [b] to back: ")
                little_separator()
                if next_page == "b":
                    i -= 1
                    continue
                elif next_page.isnumeric() and int(next_page) in range(1, len(list_to_display) + 1):
                    return next_page

                else:
                    break
            little_separator()
            next_page = input("Enter any key to display next %d entries of %d or [b] to back to previous: "
                              % (step, len(list_to_display)))
            if next_page == "b":
                if i == 0:
                    little_separator()
                    print("You are on the beginning of list, you couldn't go back: ")
                    little_separator()
                    i = 0
                else:
                    i -= 1
            elif next_page.isnumeric() and int(next_page) in range(1, i * step + step + 1):
                return next_page
            else:
                i += 1

            little_separator()

        return list_to_display



def display_help():
    print("help here    ")


def input_prepare(input_text, split_words=False):
    input_text = (input_text.lower()).strip(" " "\t")
    input_text = input_text.replace("  ", " ")
    if input_text == "exit" or input_text == "x":
        sys.exit("Thank you for using game information archive. See you next time.")
    if input_text == "h":
        display_help()
    if input_text == "b":
        pass
    if split_words:
        input_text = input_text.split(" ")
    return input_text


def lower_content(list_to_lower):
    lower_names = [line.lower() for line in list_to_lower]
    return lower_names


def games_title_variants_to_dict(game_list):
    games_title_dict = {}
    games_versions_switch = [[" 3", " iii"], [" 2", " ii"], [" 4", " iv"], [" 8", " viii"], [" 7", " vii"],
                             [" 6", " vi"], [" 5", " v"], [" 9", " ix"]]
    for game in game_list:
        games_title_dict[game] = [game.lower()]
        if "-" in game:
            games_title_dict[game] += [(game.lower()).replace("-", "")]
        for i in range(len(games_title_dict[game])):
            for j in range(len(games_versions_switch)):
                if games_versions_switch[j][0] in game:
                    games_title_dict[game] += [
                        games_title_dict[game][i].replace(games_versions_switch[j][0], games_versions_switch[j][1])]

                    games_title_dict[game] += [
                        games_title_dict[game][i].replace(games_versions_switch[j][1], games_versions_switch[j][0])]

    return games_title_dict


def list_from_name_begining(begining_string, list_to_compare):
    output_list = []
    for i in range(len(list_to_compare)):
        if (list_to_compare[i].lower()).startswith(begining_string):
            output_list.append(list_to_compare[i])
    return output_list


def when_input_number_is_too_high(list_to_compare):
    if len(list_to_compare) == 1:
        output_number = input("You can enter all name or input number 1. ")
        return output_number
    else:
        output_number = input(
            "You can enter full name or the corresponding number between 1 and %d." % len(list_to_compare))
        return output_number


def repeat_question(functions, questions, function_name, resume=False):
    separator()
    if resume == False:
        print("Your question is: ", end="")
    else:
        print("Your previous question was: ", end="")
    for key in functions:
        if function_name in str(functions[key]):
            function_number = key
    questions_index = [questions[i][0] for i in range(len(questions))]
    question = questions[questions_index.index(function_number)][1]
    print(question)


def count_games_print(data_file_name):
    count = count_games(data_file_name)
    text_to_display = "There are %d games in the archive." % count
    print(text_to_display)
    return text_to_display


def decide_print(data_file_name):
    game_data = file_prepare(data_file_name)
    max_year = max([int(game[2]) for game in game_data])
    min_year = min([int(game[2]) for game in game_data])
    while True:
        while True:
            year = input("Enter the year: ")
            if year == "b":
                break
            year = input_prepare(year)
            if year.isnumeric() and len(year) == 4:
                year = int(year)
                if year > max_year or year < min_year:
                    print("Enter year beetwen %d and %d." % (min_year, max_year))
                    continue

                break
            print("Input correct year, please.")

        if year == "b":
            text_to_display = "You left this question"
            year = None
            break
        is_game = decide(data_file_name, year)
        if is_game == True:
            text_to_display = "Yes, there is at least one game from %s year in archive." % year
            print(text_to_display)
        else:
            text_to_display = "No, there is no a game from %s year in archive." % year
            print(text_to_display)
        next_step = input("Enter any key to leave or [n] to enter another year: ")
        if next_step == "n":
            continue
        else:
            break
    return text_to_display, year


def get_latest_print(data_file_name):
    latest_game = get_latest(data_file_name)
    text_to_display = "The latest game in archive is %s." % latest_game
    print(text_to_display)
    return text_to_display


def count_by_genre_print(data_file_name):
    text_to_display, genre = "", ""

    while True:
        genre = input("Enter genre to count or press [g] to display genre list: ")
        genre = input_prepare(genre)
        genre_list = get_genres(data_file_name)
        if genre == "g":

            get_genres_print(data_file_name)
            genre = input("\nTo view the number of games in the genre, enter name of genre or corresponding number: ")
            genre = input_prepare(genre)
            if genre.isnumeric():
                genre = int(genre)
                genre = genre_list[genre - 1]
        elif genre == "b" or genre == "back":
            text_to_display = "You left this question"
            genre = None
            break
        elif genre not in genre_list:
            print("There is no genre %s in archive" % genre)
        how_many_in_genre = count_by_genre(data_file_name, genre)
        if how_many_in_genre == 1:
            text_to_display = "There is %d game in genre: %s." % (how_many_in_genre, genre)
            print(text_to_display)
        else:
            text_to_display = "There are %d games in genre: %s." % (how_many_in_genre, genre)
            print(text_to_display)
        next_question = input(
            "Do you want to check another genre? Enter [y] if you want or any key, if you want to go to question list")
        if next_question != "y":
            break
    return text_to_display, genre


def get_line_number_by_title_print(data_file_name):
    text_to_display, game_title = "", ""
    sorted_game = sort_abc_print(data_file_name, only_return=True)
    game_names_dict = games_title_variants_to_dict(sorted_game)

    while True:
        while True:
            game_title = input(
                "You can:\nEnter the whole game title\nEnter first character of title"
                "\nEnter phrase which is in title\nEnter [.] (dot) to display all titles list:\n")
            game_title = input_prepare(game_title)
            if game_title == ".":
                little_separator()
                print("List of all games titles:")
                game_title = sort_abc_print(data_file_name)
                if not game_title.isnumeric():
                    game_title = input("You can enter full name or the corresponding number.")
                game_title = sorted_game[int(game_title) - 1]
                game_line_number = get_line_number_by_title(data_file_name, game_title)
                break
            else:
                if len(game_title) == 1:
                    little_separator()
                    print("You've chosen displaying titles starting with '%s'" % game_title)
                    little_separator()
                title_prompt = list_from_name_begining(game_title, sorted_game)
                not_sort = len(title_prompt)
                if len(game_title) == 1 and len(title_prompt) == 0:
                    cause = "There is no game in archive starting with %s. Enter another phrase." % game_title
                    print(cause)
                    little_separator()
                    continue
                game_title = input_prepare(game_title, split_words=True)
                cause = "There is no game with entered phrase in archive. Try again."
                for game in game_names_dict:

                    if len(game_title) == 1:
                        if len(game_title[0]) == 1:
                            break
                        for i in range(len(game_names_dict[game])):
                            if game_title[0] in (game_names_dict[game])[i]:
                                if game in title_prompt:
                                    break
                                else:
                                    title_prompt.append(game)

                    else:
                        print(game_title)
                        print([len(phrase) for phrase in game_title])
                        if max([len(phrase) for phrase in game_title]) == 1:
                            print(max([len(phrase) for phrase in game]))
                            cause = "Your phrase is too short. Try again."
                            break
                        for i in range(len(game_names_dict[game])):
                            for j in range(len(game_title)):
                                print(game_title[j])
                                print((game_names_dict[game])[i])
                                if game_title[j] not in (game_names_dict[game])[i]:
                                    break
                                if j == len(game_title) - 1:
                                    if game in title_prompt:
                                        break

                                    else:
                                        title_prompt.append(game)

                title_prompt = title_prompt[:not_sort] + sorted(title_prompt[not_sort:])

                if title_prompt:
                    title_promt_lower = [game.lower() for game in title_prompt]
                    print("List of games titles that meet conditions:")
                    list_with_numbers(title_prompt)
                    game_title = input("You can enter full name or the corresponding number: ")
                    if game_title == ".":
                        print("You've cancelled this searching. You can try again.")
                        little_separator()
                        continue
                    while True:
                        if game_title.isnumeric():
                            game_title = int(game_title)
                            if game_title > len(title_prompt):
                                game_title = when_input_number_is_too_high(title_prompt)
                                continue
                            else:
                                game_title = title_prompt[game_title - 1]
                                break
                        elif game_title.lower() in title_promt_lower:
                            game_title = title_prompt[title_promt_lower.index(game_title.lower())]
                            break
                        else:
                            game_title = input("Enter full name or the corresponding number: ")
                    game_line_number = get_line_number_by_title(data_file_name, game_title)
                    break
                else:
                    print(cause)
                    little_separator()
        text_to_display = "Game '%s' has number %d in archive." % (game_title, game_line_number)
        print(text_to_display)
        little_separator()
        next_title = input("If you want to ask about another game type [n]. If not - type anything else.")
        if next_title == "n":
            continue
        else:
            break

    return text_to_display, game_title


def sort_abc_print(data_file_name, only_return=False):
    sorted_games = sort_abc(data_file_name)
    if only_return == False:
        little_separator()
        print("List of game titles in alphabetical order:")
        little_separator()
        if_selected = list_with_numbers(sorted_games)
        little_separator()
        return if_selected
    return sorted_games


def get_genres_print(data_file_name):
    little_separator()
    print("List of genres:")
    little_separator()
    genres_list = get_genres(data_file_name)
    text_to_display = list_with_numbers(genres_list)
    little_separator()
    return text_to_display


def when_was_top_sold_fps_print(data_file_name):
    top_fps_year = when_was_top_sold_fps(data_file_name)
    text_to_display = "The top sold FPS game was released in %d." % top_fps_year
    print(text_to_display)
    return text_to_display


def main():
    print(dir())
    functions_dict = {"function 1": count_games_print,
                      "function 2": decide_print,
                      "function 3": get_latest_print,
                      "function 4": count_by_genre_print,
                      "function 5": get_line_number_by_title_print,
                      "function 6": sort_abc_print,
                      "function 7": get_genres_print,
                      "function 8": when_was_top_sold_fps_print}

    questions_list = [["function 1", "How many games are in the archive?"],
                      ["function 2", "Is there a game from a given year?"],
                      ["function 3", "Which was the latest game?"],
                      ["function 4", "How many games do we have by genre?"],
                      ["function 5", "What is the line number of the given game (by title)?"],
                      ["function 6", "What is the alphabetical ordered list of the titles?"],
                      ["function 7", "What are the genres?"],
                      ["function 8", "What is the release date of the top sold 'First-person shooter' (FPS) game?"]]
    using_keys = ["a", "c", "h", "x", "exit", "help", "add", "r", "remove", "b", "back"]

    file_with_games = "game_stat.txt"
    os.system("clear")
    welcome_text()
    how_to_do = ""
    while True:
        separator()
        print("You can ask the following questions:")
        questions_list = list_of_questions(questions_list)
        # how_to_do = input("Choose the question number (or type [h] for help or [x] to exit): ")
        # how_to_do = input_prepare(how_to_do)
        while not how_to_do.isnumeric() or how_to_do not in using_keys:
            how_to_do = input("Choose the question number (or type [h] for help or [x] to exit): ")
            how_to_do = input_prepare(how_to_do)
            if how_to_do.isnumeric():
                how_to_do = int(how_to_do)
                if how_to_do <= len(questions_list):
                    break
                else:
                    how_to_do = input(
                        "Choose the question number between 1 and %d (or type [h] for help or [x] to exit): " % len(
                            questions_list))
        if type(how_to_do) == int or how_to_do.isnumeric():
            how_to_do = int(how_to_do)
            function_key = questions_list[how_to_do - 1][0]
            function_name = functions_dict[function_key].__name__
            os.system("clear")
            repeat_question(functions_dict, questions_list, function_name)
            little_separator()
            resume = functions_dict[function_key](file_with_games)
            separator()
            how_to_do = input("\nPress any key to ask another question or enter [x] to end the program: ")
            os.system("clear")
            repeat_question(functions_dict, questions_list, function_name, resume=True)
            if type(resume) != tuple:
                print(resume)
            else:
                print("You choose: " + str(resume[1]))
                print(resume[0])
            print("\nNow you can ask another question.")

        # how_to_do = input("\nPress any key to ask another question or enter [x] to end the program: ")
        # how_to_do = input_prepare(how_to_do)
        separator()


main()
