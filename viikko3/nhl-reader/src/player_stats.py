class PlayerStats:
    def __init__(self, reader):
        self.reader = reader
        self.players = reader.get_players()

    def top_scorers_by_nationality(self, nationality):
        filtered_players = filter(lambda x: x.nationality == nationality, self.players)
        sorted_players = sorted(filtered_players, key=lambda x: x.points, reverse=True)
        return sorted_players