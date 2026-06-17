from textual.app import App

from tui.screens.main_menu import MainMenu
from tui.screens.query_menu import QueryMenu
from tui.screens.teams_menu import TeamsMenu


class PokePyApp(App):
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
    app = PokePyApp()
    app.run()