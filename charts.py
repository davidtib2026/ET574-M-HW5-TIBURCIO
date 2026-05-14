import matplotlib.pyplot as plt

def show_chart(player):

    stats = [
        float(player["Points"]),
        float(player["Rebounds"]),
        float(player["Assists"])
    ]

    labels = ["Points", "Rebounds", "Assists"]

    colors = ["gold", "green", "blue"]

    plt.bar(labels, stats, color=colors)

    plt.title(player["Player"] + " Stats")

    plt.xlabel("Stat Categories")

    plt.ylabel("Stat Numbers")

    plt.show()