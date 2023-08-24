class Match:
    def __init__(self, location, team1, team2, timing):
        self.location = location
        self.team1 = team1
        self.team2 = team2
        self.timing = timing

class MatchTable:
    def __init__(self):
        self.matches = []

    def add_match(self, location, team1, team2, timing):
        match = Match(location, team1, team2, timing)
        self.matches.append(match)

    def list_matches_by_team(self, team_name):
        team_matches = [match for match in self.matches if team_name in [match.team1, match.team2]]
        return team_matches

    def list_matches_by_location(self, location):
        location_matches = [match for match in self.matches if match.location == location]
        return location_matches

    def list_matches_by_timing(self, timing):
        timing_matches = [match for match in self.matches if match.timing == timing]
        return timing_matches

def main():
    match_table = MatchTable()

    match_table.add_match("Mumbai", "India", "Sri Lanka", "DAY")
    match_table.add_match("Delhi", "England", "Australia", "DAY-NIGHT")
    match_table.add_match("Chennai", "India", "South Africa", "DAY")
    match_table.add_match("Indore", "England", "Sri Lanka", "DAY-NIGHT")
    match_table.add_match("Mohali", "Australia", "South Africa", "DAY-NIGHT")
    match_table.add_match("Delhi", "India", "Australia", "DAY")

    while True:
        print("Search Options:")
        print("1. List of all the matches of a Team")
        print("2. List of Matches on a Location")
        print("3. List of Matches based on timing")
        print("4. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            team_name = input("Enter the team name: ")
            team_matches = match_table.list_matches_by_team(team_name)
            for match in team_matches:
                print(f"{match.team1} vs {match.team2} at {match.location}, {match.timing}")
        elif choice == "2":
            location = input("Enter the location: ")
            location_matches = match_table.list_matches_by_location(location)
            for match in location_matches:
                print(f"{match.team1} vs {match.team2} at {match.location}, {match.timing}")
        elif choice == "3":
            timing = input("Enter the timing: ")
            timing_matches = match_table.list_matches_by_timing(timing)
            for match in timing_matches:
                print(f"{match.team1} vs {match.team2} at {match.location}, {match.timing}")
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
