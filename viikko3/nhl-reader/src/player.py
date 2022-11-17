class Player:
    def __init__(self, name, team, games, goals, assists, penalties):
        self.name = name
        self.team = team
        self.games = games
        self.goals = goals
        self.assists = assists
        self.penalties = penalties
    
    def __str__(self):
        return f"{self.name} team {self.team} goals {self.goals} assists {self.assists}"