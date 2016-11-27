#Game statistics reports

def file_prepare(data_file_name):
    with open(data_file_name, "r") as file:
        data_table_to_read = file.readlines()
    final_data_table = []
    for line in data_table_to_read:
        line = line.replace("\n","")
        final_data_table.append(line.split("\t"))
    return final_data_table


def count_games(data_file_name):
    data_table = file_prepare(data_file_name)
    count = len(data_table)
    return count


def decide(data_file_name, year):
    data_table = file_prepare(data_file_name)
    for game in data_table:
        if str(year) in game[2]:
            is_game_from_year = True
            return is_game_from_year
            break
    is_game_from_year = False
    return is_game_from_year


def get_latest(data_file_name):
    data_table = file_prepare(data_file_name)
    years_list = []
    for game in data_table:
        years_list.append(game[2])
    for game in data_table:
        if game[2] == max(years_list):
            latest_game = game[0]
            return latest_game


def count_by_genre(data_file_name, genre):
    data_table = file_prepare(data_file_name)
    how_many_in_genre = 0
    for game in data_table:
        if game[3] == genre:
            how_many_in_genre += 1
    return how_many_in_genre


def get_line_number_by_title(data_file_name, title):
    data_table = file_prepare(data_file_name)
    title_list = []
    for game in data_table:
        title_list.append(game[0])
    game_number = title_list.index(title) + 1
    return game_number


def sort_abc(data_file_name):
    data_table = file_prepare(data_file_name)
    game_names = [data_table[i][0] for i in range(len(data_table))]
    sorted_game_list = [game_names[0]]
    for game in game_names:
        for i in range(len(sorted_game_list)):
            if game.lower() < sorted_game_list[i].lower():
                sorted_game_list.insert(i, game)
                break
            elif game == sorted_game_list[i]:
                break
            else:
                if i == len(sorted_game_list)-1:
                    sorted_game_list.append(game)
                else:
                    continue
    return sorted_game_list


def get_genres(data_file_name):
    data_table = file_prepare(data_file_name)
    genres_list = []
    for game in data_table:
        if game[3] in genres_list:
            continue
        else:
            genres_list.append(game[3])
    genres_list.sort(key=str.lower)
    return genres_list


def when_was_top_sold_fps(data_file_name):
    data_table = file_prepare(data_file_name)
    fps_list = []
    for game in data_table:
        if game[3] == "First-person shooter":
            fps_list.append(game)
    fps_sell_list = [float(fps[1]) for fps in fps_list]
    fps_top_seller_index = fps_sell_list.index(max(fps_sell_list))
    fps_top_sold_year = int(fps_list[fps_top_seller_index][2])
    return fps_top_sold_year

