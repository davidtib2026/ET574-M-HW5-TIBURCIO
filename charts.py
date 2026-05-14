import matplotlib.pyplot as plt

def show_chart(player):

    stats = [
        float(player["Points"]),
        float(player["Rebounds"]),
        float(player["Assists"])
    ]

    labels = ["Points", "Rebounds", "Assists"]

    plt.bar(labels, stats)

    plt.title(player["Player"] + " Stats")

    plt.show()