import numpy as np
import pandas as pd
import os
import os.path

""" Extract all csv files from the dataset """
all_dirs = []
for root, dirs, files in os.walk("espana-master"):
    for file in files:
        if file.endswith(".csv"):
            # print(os.path.join(root, file))
            new_dir = os.path.join(root, file)
            all_dirs.append(new_dir)

print('Number of total CSV files: ', len(all_dirs))

''' Merge all CSV files to a single CSV file named: total_table.csv '''
fname = 'total_table.csv'  # A single file to save all the records

# Check if file exists, delete it
if os.path.isfile(fname):
    os.remove(fname)

# Add all files to fname csv file
fout = open(fname, "a")
# first file:
for line in open(all_dirs[0]):
    fout.write(line)
# now the rest:
for num in range(len(all_dirs) - 1):
    with open(all_dirs[num + 1], "r+") as f:
        f.readline()  # skip the header
        for line in f:
            fout.write(line)
        f.close()  # not really needed
fout.close()

''' Extract data from csv file '''
df = pd.read_csv('total_table.csv')

""" Delete unused rows """
df = df.drop(['Date', 'HT', 'Round'], 1)
print(df)
print('Done 1')

""" Uniquing the team names """
df['Team 1'] = df['Team 1'].apply(lambda x: x[0:x.find('(') - 1])
df['Team 2'] = df['Team 2'].apply(lambda x: x[0:x.find('(') - 1])

""" Create goal difference column """
df['Diff point'] = df['FT'].apply(lambda x: int(x[0:x.find('-')]) - int(x[x.find('-') + 1:len(x)]))
print(df)
print('Done 2')

""" All teams to Data frame """
teams_names = df['Team 1'].unique()
print('Number of teams', len(teams_names))
final_df = pd.DataFrame(teams_names, columns=['Teams'])
final_df['Points'] = float(0)
print(final_df)
teams_names_dict = dict.fromkeys(teams_names, 0)
# print(teams_names_dict)
# df.columns = ['Teams', 'points']
# final_df['points'] = df.apply(lambda row: final_df[0].iloc[row['Team 1']] is 3)

print('Working on Final df ...')
for index in df.iterrows():
    diff_point = index[1]['Diff point']
    team_name_1 = index[1]['Team 1']
    team_name_2 = index[1]['Team 2']
    teams_names_dict[team_name_1] += 1
    teams_names_dict[team_name_2] += 1
    if diff_point > 0:
        a = final_df.index[final_df['Teams'] == team_name_1].tolist()[0]
        final_df.at[a, 'Points'] += 3
    elif diff_point < 0:
        a = final_df.index[final_df['Teams'] == team_name_2].tolist()[0]
        final_df.at[a, 'Points'] += 3
    else:
        a = final_df.index[final_df['Teams'] == team_name_2].tolist()[0]
        final_df.at[a, 'Points'] += 1
        a = final_df.index[final_df['Teams'] == team_name_1].tolist()[0]
        final_df.at[a, 'Points'] += 1
print('Final df finished')

''' Sort values by Points '''
final_df = final_df.sort_values(['Points'], ascending=False)
print('Sort values by Points')
print(final_df)
# print(teams_names_dict)

''' Sort values by Points ratio '''
print('Sort values by Points ratio')
final_df['Points ratio'] = final_df['Points']
for key, value in teams_names_dict.items():
    a = final_df.index[final_df['Teams'] == key].tolist()[0]
    final_df.at[a, 'Points ratio'] /= value

final_df = final_df.sort_values(['Points ratio'], ascending=False)
print(final_df)
