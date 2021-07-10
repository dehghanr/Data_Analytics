import numpy as np
import pandas as pd

''' Read title_rating.tsc file '''


def read_title_rating():
    film_names1 = []
    ratings1 = []
    with open('title_rating.tsv', 'r+') as f:
        ''' Skip first line '''
        first_line = f.readline()
        for line in f:
            counter = 0
            row = line.split()
            film_names1.append(row[0])
            ratings1.append(float(row[1]))
    print('title_rating.tsv Has been loaded')
    film_names_ratings1 = pd.DataFrame(film_names1, columns=['Film name'])
    film_names_ratings1['Rating'] = ratings1
    # print(film_names_ratings)
    return film_names_ratings1, film_names1, ratings1


film_names_ratings, film_names, ratings = read_title_rating()
# print(film_names_ratings)
# print('Ratings')

''' Read title_crew.tsc file '''


def read_title_crew():
    film_names_crew1 = []
    directors_id_crew1 = []
    with open('title_crew.tsv', 'r+') as f:
        ''' Skip first line '''
        first_line = f.readline()
        for line in f:
            counter = 0
            row = line.split()
            film_names_crew1.append(row[0])
            row_list = row[1].split(',')
            directors_id_crew1.append(row_list)
            # print(row_list)
            # print(type(directors_id_crew1))
    # list(map(str, directors_id_crew1))
    # print(type(directors_id_crew))
    print('title_crew.tsv Has been loaded')
    film_names_directors_id1 = pd.DataFrame(film_names_crew1, columns=['Film name'])
    film_names_directors_id1['Director id'] = directors_id_crew1
    return film_names_directors_id1, film_names_crew1, directors_id_crew1


film_names_directors_id, film_names_crew, directors_id_crew = read_title_crew()
# print(film_names_directors_id)
# print('CREW')

''' Read name_basics.tsc file '''


def read_name_basics():
    directors_id_basics1 = []
    directors_names_basics1 = []
    with open('name_basics.tsv', 'r+') as f:
        ''' Skip first line '''
        first_line = f.readline()
        for line in f:
            counter = 0
            row = line.split()
            directors_id_basics1.append(row[0])
            name = str(row[1]) + ' ' + str(row[2])
            directors_names_basics1.append(name)
    print('name_basics.tsv Has been loaded')
    directors_id_name1 = pd.DataFrame(directors_id_basics1, columns=['Director id'])
    directors_id_name1['Director names'] = directors_names_basics1
    # print(directors_id_name1)
    return directors_id_name1, directors_id_basics1, directors_names_basics1


# directors_id_name = read_name_basics()
# print(directors_id_name)
# print('Director names')

''' ِ Dictionary of director ids and their films '''
print('Making dictionary of director ids and their films ...')
directors_id_dict = {}
for i in range(len(directors_id_crew)):
    film_name_value = film_names_crew[i]
    for j in range(len(directors_id_crew[i])):
        director_id = directors_id_crew[i][j]
        keys_dict = directors_id_dict.keys()
        if director_id not in keys_dict:
            directors_id_dict[director_id] = [film_name_value]
        else:
            directors_id_dict[director_id].append(film_name_value)

directors_id_dict_df = pd.DataFrame(list(directors_id_dict.items()), columns=['Director id', 'Films list'])

''' ِ Dictionary of director ids and their films '''
film_names_ratings_dict = dict(zip(film_names, ratings))
print('film_names_ratings_dict')
counter = 0
for i, j in film_names_ratings_dict.items():
    print(i, j)
    counter += 1
    if counter >= 5:
        break

print('directors_id_dict')
counter = 0
for i, j in directors_id_dict.items():
    print(i, j)
    counter += 1
    if counter >= 5:
        break
# print('Dictionary of director ids and their films')
# print(film_names_ratings)

# print(directors_id_dict_df)
# directors_id_dict_df['Sum of Ratings'] = 0
# print(directors_id_dict_df)
film_ids_ratings = {}
for i, j in directors_id_dict.items():
    constant = 0
    for k in range(len(j)):
        if i not in film_ids_ratings.keys():
            if j[k] in film_names_ratings_dict.keys():
                constant = film_names_ratings_dict[j[k]]
                film_ids_ratings[i] = constant
        else:
            if j[k] in film_names_ratings_dict.keys():
                film_ids_ratings[i] += film_names_ratings_dict[j[k]]
    if i in film_ids_ratings.keys():
        film_ids_ratings[i] /= len(j)

print('film_ids_ratings')
counter = 0
for i, j in film_ids_ratings.items():
    print(i, j)
    counter += 1
    if counter >= 5:
        break

print('director Names loading ...')
directors_id_name, directors_id_basics, directors_names_basics = read_name_basics()
directors_id_name_dict = dict(zip(directors_id_basics, directors_names_basics))

print('directors_id_name_dict')
counter = 0
for i, j in directors_id_name_dict.items():
    print(i, j)
    counter += 1
    if counter >= 5:
        break

director_names_ratings_dict = {}
for i, j in film_ids_ratings.items():
    if i in directors_id_name_dict.keys():
        director_names_ratings_dict[directors_id_name_dict[i]] = j

print('director_names_ratings_dict')
counter = 0
for i, j in director_names_ratings_dict.items():
    print(i, j)
    counter += 1
    if counter >= 5:
        break

''' Final data frame '''
import operator
sorted_list = sorted(director_names_ratings_dict.items(), key=operator.itemgetter(1), reverse=True)
df_final = pd.DataFrame(sorted_list, columns=['Director Name', 'Rate ratio'])
print(df_final)


