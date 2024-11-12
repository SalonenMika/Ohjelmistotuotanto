import unittest
from statistics_service import StatisticsService
from player import Player

# Stub-luokka, joka palauttaa kovakoodatun pelaajalistan
class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
        ]

# Testiluokka StatisticsService-luokalle
class TestStatisticsService(unittest.TestCase):
    
    def setUp(self):
        # Injektoimme PlayerReaderStubin StatisticsService-luokkaan
        self.stats = StatisticsService(PlayerReaderStub())

    def test_search_existing_player(self):
        # Testaa, että olemassa oleva pelaaja löytyy
        player = self.stats.search("Lemieux")
        self.assertIsNotNone(player)
        self.assertEqual(player.name, "Lemieux")
        self.assertEqual(player.team, "PIT")

    def test_search_non_existing_player(self):
        # Testaa, että ei-olemassa olevaa pelaajaa ei löydy
        player = self.stats.search("Unknown")
        self.assertIsNone(player)

    def test_team(self):
        # Testaa, että oikeat pelaajat kuuluvat oikeaan joukkueeseen
        edmonton_players = self.stats.team("EDM")
        self.assertEqual(len(edmonton_players), 3)
        self.assertTrue(all(player.team == "EDM" for player in edmonton_players))

    def test_empty_team(self):
        # Testaa, että jos joukkueella ei ole pelaajia, lista on tyhjä
        empty_team = self.stats.team("BUF")  # Buffalo on tyhjä tässä esimerkissä
        self.assertEqual(len(empty_team), 0)

# Suoritetaan testit, kun tämä tiedosto ajetaan
if __name__ == "__main__":
    unittest.main()
