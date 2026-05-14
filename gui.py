import wx
from data import load_players
from charts import show_chart

class NBAFrame(wx.Frame):

    def __init__(self):
        wx.Frame.__init__(self, None, title="NBA Player Stats Visualizer", size=(400, 300))

        self.players = load_players()

        panel = wx.Panel(self)

        title = wx.StaticText(panel, label="Choose an NBA Player")

        self.player_box = wx.ComboBox(
            panel,
            choices=self.get_player_names()
        )

        self.info_text = wx.StaticText(
            panel,
            label="Player stats will appear here."
        )

        chart_button = wx.Button(
            panel,
            label="Show Stats Chart"
        )

        chart_button.Bind(wx.EVT_BUTTON, self.show_player_chart)

        box = wx.BoxSizer(wx.VERTICAL)

        box.Add(title, 0, wx.ALL, 10)
        box.Add(self.player_box, 0, wx.ALL, 10)
        box.Add(self.info_text, 0, wx.ALL, 10)
        box.Add(chart_button, 0, wx.ALL, 10)

        panel.SetSizer(box)

        self.player_box.Bind(wx.EVT_COMBOBOX, self.show_player_info)

    def get_player_names(self):

        names = []

        for player in self.players:
            names.append(player["Player"])

        return names

    def show_player_info(self, event):

        selected_name = self.player_box.GetValue()

        for player in self.players:

            if player["Player"] == selected_name:

                info = "Team: " + player["Team"]

                info += "\nPoints: " + player["Points"]

                info += "\nRebounds: " + player["Rebounds"]

                info += "\nAssists: " + player["Assists"]

                self.info_text.SetLabel(info)

    def show_player_chart(self, event):

        selected_name = self.player_box.GetValue()

        for player in self.players:

            if player["Player"] == selected_name:

                show_chart(player)