class Player:
    def __init__(self, player_name):
        self.player_name = player_name
class Tournament:
    def __init__(self, runs_list):
        self.runs_list = runs_list
    def total_runs(self):
        return sum(self.runs_list)
    def matches_played(self):
        return len(self.runs_list)
    def average_runs(self):
        return self.total_runs() / self.matches_played()
    def generate_report(self, player):
        print("=" * 50)
        print("       PLAYER PERFORMANCE REPORT")
        print("=" * 50)
        print()
        print(f"Player Name    : {player.player_name}")
        print()
        print(f"Total Runs     : {self.total_runs()}")
        print(f"Matches Played : {self.matches_played()}")
        print(f"Average Runs   : {self.average_runs()}")
        print()
        print("=" * 50)
player = Player("Arjun")
runs = [50, 75, 100]
tournament = Tournament(runs)
tournament.generate_report(player)