from WebsiteBrowserController.WebsiteController import WebsiteController


class Logic:
    def __init__(self, website_controller: WebsiteController):
        self.user_is_auth = False
        self.user_library_games = []
        self.websiteController = website_controller

    def refresh_data(self):
        self.user_is_auth = self.check_user_auth()
        self.detect_user_games()
        new_games = self.detect_new_free_games_not_in_library()
        if len(new_games) != 0:
            [self.buy_game(game) for game in new_games]

    def detect_user_games(self):
        self.user_library_games = []

    def detect_new_free_games_not_in_library(self) -> list[str]:
        new_free_games = self.detect_new_free_games()
        new_free_games_for_user = [game for game in new_free_games if game not in self.user_library_games]
        return new_free_games_for_user

    @staticmethod
    def detect_new_free_games() -> list[str]:
        return []

    def buy_game(self, url_game: str):
        pass

    def check_user_auth(self) -> bool:
        pass

    def get_next_distribution(self):
        pass
