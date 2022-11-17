class Player:
    def __init__(self, name, team, games, goals, assists, penalties):
        self.name = name
        self.team = team
        self.games = games
        self.goals = goals
        self.assists = assists
        self.penalties = penalties

    @property
    def points(self):
        return self.goals + self.assists
    
    def __str__(self):
        return f"{self.name:25}{self.team:5} {self.goals} + {self.assists} = {self.points}"