# ET574-M-HW5-TIBURCIO
# NBA Player Stats Visualizer

## Project Overview

This project is a simple NBA player statistics visualizer. The program uses a small dataset of NBA players and displays their points, rebounds, and assists. The user can choose a player from a wxPython GUI window and view a Matplotlib bar chart of that player's stats.

## Setup Instructions

1. Install Python.
2. Install wxPython.
3. Install Matplotlib.
4. Download or clone this repository.
5. Run the program from `main.py`.

## Usage Details

Open the program and select an NBA player from the dropdown menu. The program will display the player's team, points, rebounds, and assists. Click the chart button to create a bar chart showing the player's stats.

## Dataset Information

The dataset is stored in `nba_players.csv`. It contains selected NBA players, their teams, and three basic statistics: points, rebounds, and assists.

## Files

- `main.py` starts the program.
- `gui.py` creates the wxPython GUI window.
- `data.py` loads the NBA player dataset.
- `charts.py` creates the Matplotlib chart.
- `nba_players.csv` stores the dataset.
