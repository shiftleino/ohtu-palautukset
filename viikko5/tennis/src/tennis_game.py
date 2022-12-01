TEXTUAL_SCORES = ["Love", "Fifteen", "Thirty", "Forty"]
DEUCE_IDX = 3
WIN_IDX = 4


class TennisGame:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.player1_score_idx = 0
        self.player2_score_idx = 0
        self.deuce_count = 0

    def won_point(self, player_name):
        if self.player1_score_idx >= DEUCE_IDX and self.player2_score_idx >= DEUCE_IDX:
            point_difference = self.player1_score_idx - self.player2_score_idx
            if player_name == self.player1_name:
                if point_difference != -1:
                    self.player1_score_idx += 1
                else:
                    self.player2_score_idx = DEUCE_IDX
                    self.deuce_count += 1
            elif player_name == self.player2_name:
                if point_difference != 1:
                    self.player2_score_idx += 1
                else:
                    self.player1_score_idx = DEUCE_IDX
                    self.deuce_count += 1

        else:
            if player_name == self.player1_name:
                self.player1_score_idx += 1
            else:
                self.player2_score_idx += 1
            
            if self.player1_score_idx == DEUCE_IDX and self.player2_score_idx == DEUCE_IDX:
                self.deuce_count += 1

    def get_winner(self):
        point_difference = abs(self.player1_score_idx - self.player2_score_idx)
        if self.player1_score_idx >= WIN_IDX and point_difference > 1:
            return self.player1_name
        elif self.player2_score_idx >= WIN_IDX and point_difference > 1:
            return self.player2_name
        return None

    def get_advantage(self):
        if self.player1_score_idx >= WIN_IDX:
            return self.player1_name
        elif self.player2_score_idx >= WIN_IDX:
            return self.player2_name
        return None

    def get_deuce(self):
        if self.deuce_count > 1:
            return True
        return False

    def get_score(self):
        winner = self.get_winner()
        if winner:
            return f"Win for {winner}"
        advantage_player = self.get_advantage()
        if advantage_player:
            return f"Advantage {advantage_player}"
        elif self.get_deuce():
            return "Deuce"
        elif self.player1_score_idx == self.player2_score_idx:
            return f"{TEXTUAL_SCORES[self.player1_score_idx]}-All"
        return f"{TEXTUAL_SCORES[self.player1_score_idx]}-{TEXTUAL_SCORES[self.player2_score_idx]}"