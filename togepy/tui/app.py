from textual.app import App
from textual.reactive import reactive

from togepy.tui.screens.create_team import CreateTeamScreen
from togepy.tui.screens.delete_team import DeleteTeamScreen
from togepy.tui.screens.main_menu import MainMenu
from togepy.tui.screens.query_menu import QueryMenu
from togepy.tui.screens.teams_menu import TeamsMenu


class TogePyApp(App):
    """Main application entry point."""
    teams_inapp = reactive([])

    BINDINGS = [
        ("ctrl+q", "quit", "Quit"),
    ]

    SCREENS = {
        "main": MainMenu,
        "query": QueryMenu,
        "teamsmenu": TeamsMenu,
        "createteamscreen": CreateTeamScreen,
        "deleteteamscreen": DeleteTeamScreen
    }

    def on_mount(self) -> None:
        self.theme = "gruvbox"
        self.title = "TogePy Team Builder"

        self.push_screen("main")

    def action_quit(self) -> None:
        self.exit()

#Entry point is in togepy.__main__
# if __name__ == "__main__":
#     app = TogePyApp()
#     app.run()