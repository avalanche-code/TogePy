from textual.app import App
from textual.reactive import reactive

from togepy.tui.screens.create_team import CreateTeamScreen
from togepy.tui.screens.delete_team import DeleteTeamScreen
from togepy.tui.screens.main_menu import MainMenu
from togepy.tui.screens.query_menu import QueryMenu
from togepy.tui.screens.teams_menu import TeamsMenu


class TogePyApp(App):
    """Main application entry point."""
    #Initiierung Teamsliste. Reactive um Textual das aktualisieren in Widgets leichter zu machen
    #Hier, damit andere Screens unter self.app.teams_inapp die gleiche Liste benutzen
    #Anderer approach? Import aus einem Modul hat nicht richtig geklappt
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