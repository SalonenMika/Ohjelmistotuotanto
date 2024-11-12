from player_reader import PlayerReader
from statistics_service import StatisticsService


def main():
    player_reader = PlayerReader("https://raw.githubusercontent.com/ohjelmistotuotanto-jyu/tehtavat/refs/heads/main/osa2/stats/players-23-24.txt")

    stats = StatisticsService(player_reader)
    philadelphia_flyers_players = stats.team("PHI")
    top_scorers = stats.top(10)

    print("Philadelphia Flyers:")
    for player in philadelphia_flyers_players:
        print(player)

    print("Top point getters:")
    for player in top_scorers:
        print(player)


if __name__ == "__main__":
    main()
