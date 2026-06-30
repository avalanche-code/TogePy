from textual.app import App

#from togepy.tui.app_old import TogePyAppOld
from togepy.tui.screens.main_menu import MainMenu
from togepy.tui.screens.query_menu import QueryMenu
from togepy.tui.screens.teams_menu import TeamsMenu


class TogePyApp(App):
    """Main application entry point."""

    BINDINGS = [
        ("ctrl+q", "quit", "Quit"),
    ]

    SCREENS = {
        "main": MainMenu,
        "query": QueryMenu,
        "teams": TeamsMenu,
    }

    def on_mount(self) -> None:
        self.theme = "gruvbox"
        self.title = "PokePy Team Builder"

        self.push_screen("main")

    def action_quit(self) -> None:
        self.exit()


if __name__ == "__main__":
    app = TogePyApp()
    app.run()