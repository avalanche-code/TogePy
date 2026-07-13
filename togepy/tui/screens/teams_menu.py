from textual.app import ComposeResult
from textual.containers import Container
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Label

from togepy.tui.screens.create_team import CreateTeamScreen
from togepy.tui.screens.delete_team import DeleteTeamScreen


class TeamsMenu(Screen):
    """Team management menu"""

    #Header isnt centered with Label? Idk why not. seperate label already has margin to next container? wegen \n
    CSS = """
    Label {
        width: 100%;
        align: center top;
        content-align: center top;
        margin-top: 1;
        margin-bottom: 1;
    }
    Container {
        align: center top;
        content-align: center top;
        width: 100%;
    }
    Button {
        width: 25%;
        content-align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()
        yield Label("What do you want to do?")
        yield Container(
            Button(
                "📋 View Teams",
                id="view_teams",
                variant="primary",
                classes="button_mid",
                disabled=True
            ),
            Button(
                "➕ Create Team",
                id="create_team",
                variant="success",
            ),
            Button(
                "🚮 Delete Team",
                id="delete_team",
                variant="warning",
            ),
            Button(
                "⬅ Back",
                id="back",
            ),
        )

        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:

            case "view_teams":
                self.app.push_screen("team_list")

            case "create_team":
                self.app.push_screen(CreateTeamScreen())    #create_team

            case "delete_team":
                # "hack": destroying screen and always new building so that mount gets used, speicheroptimierung?
                self.app.push_screen(DeleteTeamScreen())

            case "back":
                self.app.pop_screen()