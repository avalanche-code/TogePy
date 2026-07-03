from textual.app import App

#from togepy.tui.app_old import TogePyAppOld
from togepy.tui.screens.main_menu import MainMenu
from togepy.tui.screens.query_menu import QueryMenu
from togepy.tui.screens.teams_menu import TeamsMenu
#from togepy.tui.screens.teams_view import TeamsView if done then uncomment TODO


class TogePyApp(App):
    """Main application entry point."""

    BINDINGS = [
        ("ctrl+q", "quit", "Quit"),
    ]

    SCREENS = {
        "main": MainMenu,
        "query": QueryMenu,
        "teamsmenu": TeamsMenu,
        #"teamsview": TeamsView if done then uncomment TODO
    }

    def on_mount(self) -> None:
        self.theme = "gruvbox"
        self.title = "PokePy Team Builder"

        self.push_screen("main")

    def action_quit(self) -> None:
        self.exit()

#Entry point is in togepy.__main__
# if __name__ == "__main__":
#     app = TogePyApp()
#     app.run()