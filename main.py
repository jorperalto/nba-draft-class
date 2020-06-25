import pandas as pd

if __name__ == "__main__":
    df, stats = pd.read_csv('players.csv'), ['PPG', 'RPG', 'APG', 'Position']
    stat = int(input('Which stat does your team need?\n1 - PPG\n2 - RPG\n3 - APG\n4 - Position\nYour answer was: '))

    players_sorted = df.sort_values(stats[stat-1], ascending=False)
    print('\n{} by player:\n {}\n'.format(stats[stat-1], players_sorted))

    print('Top player by {}:\n{}'.format(stats[stat-1], players_sorted.iloc[0]))