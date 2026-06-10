class Player:
    def __init__(self, player_name):
        self.player_name = player_name

class Match:
    def __init__(self, scores):
        self.scores = scores

class Tournament:
    def final_score(self, match):
        return sum(match.scores)

    def generate_report(self, player, match):
        score = self.final_score(match)

        print("=" * 50)
        print("            TOURNAMENT REPORT")
        print("=" * 50)
        print()
        print(f"Player Name : {player.player_name}")
        print()
        print(f"Final Score : {score}")
        print()
        print("Rank Status : QUALIFIED")
        print()
        print("=" * 50)

player = Player("Leo")
match = Match([100, 150, 200])

tournament = Tournament()
tournament.generate_report(player, match)