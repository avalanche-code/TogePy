from textual.app import ComposeResult
from textual.containers import Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Label


class TeamsMenu(Screen):
    """Team management menu."""

    def compose(self) -> ComposeResult:
        yield Header()

        yield Vertical(
            Label("Team Management"),
            Button(
                "📋 View Teams",
                id="view_teams",
                variant="primary",
            ),
            Button(
                "➕ Create Team",
                id="create_team",
                variant="success",
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
                self.app.push_screen("create_team")

            case "back":
                self.app.pop_screen()