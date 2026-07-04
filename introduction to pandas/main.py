#game-stats-analyser.py
#activity: gaming leader board analyser
#lesson:introduction to pandas

import pandas as pd

#PART 1 - Create a pandas series of top player scores
print('--- PART 1:Pandas Series ---')
scores = [98500,87200,76400,65100,54800]
players = pd.Series(scores, index=['nightwolf','starblaze','pixelking','cyberFox','ironstorm'])
print(players)

#part 2 - create a dataframe of gaming stats
print()
print('--- PART 2:Pandas DataFrame---')
data={
    'player':['nightwolf','starblaze','pixelking','cyberfox','ironstorm'],
    'level':[42,38,35,30,27],
    'score':[98500,87200,76400,65100,54800],
    'wins':[210,185,162,140,118]
}
df = pd.DataFrame(data)
print(df)

#PART 3 - Access rows using .loc
print()
print('---PART 3:Accessing Rows---')
print('Row 0(top player):')
print(df.loc[0])
print()
print('Rows 2 and 3:')
print(df.loc[2:3])

#PART 4 - Load leaderboard.csv and view the data
print()
print('---PART 4:Reading a  CSV file---')
full_df = pd.read_csv('https://docs.google.com/spreadsheets/d/1NEVsIz9hixfs799Yzvm_adpJlcYewybinYIDNp0w7nY/edit?usp=sharing.csv')
print('first 5 rows(head):')
print(full_df.head())
print()
print('last 3 rows(tail):')
print(full_df.tail(3))
print()
print('dataset info:')
print(full_df.info())

#PART 5 - clean the data
print()
print('--PART 5:cleaning data---')
print('rows with missing values removed (dropna):')
clean_df = full_df.dropna()
print(clean_df.to_string())
print()
print('missing values filled with 0(fillna):')
filled_df = full_df.fillna(0)
print(filled_df.to_string())