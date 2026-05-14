import csv

def load_players():
    players = []

    with open("nba_players.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            players.append(row)

    return players
