from textual.app import ComposeResult
from textual.containers import Container, Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Label, Static
from togepy.tui.screens.delete_team import DeleteTeamScreen


class TeamsMenu(Screen):
    """Team management menu."""

    CSS = """
    Label {
        width: 100%;
        align: center top;
        text-align: center;
    }
    Container {
        align: center top;
        content-align: center top;
        width: 100%;
        margin-top: 1
    }
    Button {
        width: 25%;
        content-align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()

        yield Container(
            Label("Team Management Screen\n"),
            Button(
                "📋 View Teams",
                id="view_teams",
                variant="primary",
                classes="button_mid",
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
                self.app.push_screen("createteamscreen")    #create_team

            case "delete_team":
                # hack: destroying screen and always new building so that mount gets used
                self.app.push_screen(DeleteTeamScreen())

            case "back":
                self.app.pop_screen()