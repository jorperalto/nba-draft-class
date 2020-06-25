import pandas as pd

if __name__ == "__main__":
    stats = [' NAME', ' AGE', ' SALARY', ' PPG_LAST_SEASON', ' APG_LAST_SEASON', ' RPG_LAST_SEASON', ' POSITION']
    df = pd.read_csv('players.csv').filter(items=stats)
    stat = int(input(
        'Which stat does your team need?\n' +
        '1 - AGE\n2 - SALARY\n3 - PPG_LAST_SEASON\n4 - APG_LAST_SEASON\n5 - RPG_LAST_SEASON\n6 - POSITION' +
        '\nYour answer was: '))

    players_sorted = df.sort_values(stats[stat], ascending=False)
    print('\n{} by player:\n {}\n'.format(stats[stat], players_sorted.head()))

    print('Top player by {}:\n{}'.format(stats[stat], players_sorted.iloc[0]))