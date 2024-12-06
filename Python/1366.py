from collections import defaultdict

class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        n = len(votes[0])  # Number of teams
        
        # Create a dictionary where each team has a list to count votes at each position
        rank_count = defaultdict(lambda: [0] * n)
        
        # Count the votes
        for vote in votes:
            for i, team in enumerate(vote):
                rank_count[team][i] += 1
        
        # Sort the teams by their rank count. If counts tie, fall back to alphabetical order.
        teams = list(votes[0])  # All teams are listed in the first vote
        teams.sort(key=lambda team: (rank_count[team], -ord(team)), reverse=True)
        
        return ''.join(teams)
