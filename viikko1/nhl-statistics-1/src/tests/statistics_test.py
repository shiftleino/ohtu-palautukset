import unittest
from statistics import Statistics, SortBy
from player import Player

class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

class TestStatistics(unittest.TestCase):
    def setUp(self):
        # annetaan Statistics-luokan oliolle "stub"-luokan olio
        self.statistics = Statistics(
            PlayerReaderStub()
        )

    def test_search_player(self):
        name = "Lemieux"
        player = self.statistics.search(name)
        self.assertEqual(name, player.name)

    def test_search_player_missing(self):
        name = "Selanne"
        player = self.statistics.search(name)
        self.assertEqual(None, player)

    def test_get_players_from_team(self):
        team = "EDM"
        players = self.statistics.team(team)
        player_names = [player.name for player in players]
        self.assertListEqual(player_names, ["Semenko", "Kurri", "Gretzky"])

    def test_sorted_players_points(self):
        top_players = self.statistics.top(2, SortBy.POINTS)
        top_players_names = [player.name for player in top_players]
        self.assertListEqual(top_players_names, ["Gretzky", "Lemieux", "Yzerman"])

    def test_sorted_players_default(self):
        top_players = self.statistics.top(2)
        top_players_names = [player.name for player in top_players]
        self.assertListEqual(top_players_names, ["Gretzky", "Lemieux", "Yzerman"])

    def test_sorted_players_goals(self):
        top_players = self.statistics.top(2, SortBy.GOALS)
        top_players_names = [player.name for player in top_players]
        self.assertListEqual(top_players_names, ["Lemieux", "Yzerman", "Kurri"])

    def test_sorted_players_assists(self):
        top_players = self.statistics.top(2, SortBy.ASSISTS)
        top_players_names = [player.name for player in top_players]
        self.assertListEqual(top_players_names, ["Gretzky", "Yzerman", "Lemieux"])
