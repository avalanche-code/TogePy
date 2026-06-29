from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Label


class MainMenu(Screen):
    """Main menu of the application."""

    def compose(self) -> ComposeResult:
        yield Header()

        yield Horizontal(
            Vertical(
                Button(
                    "🔍 Query Pokemon",
                    id="query_pokemon",
                    variant="primary",
                ),
                Button(
                    "👥 Teams",
                    id="teams",
                    variant="primary",
                ),
                Button(
                    "⚙️ Settings",
                    id="settings",
                    disabled=True,
                ),
            ),
            Vertical(
                Label("Welcome to PokePy Team Builder!"),
                Label("Select an option:"),
            ),
            
        )

        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case "query_pokemon":
                self.app.push_screen("query")

            case "teams":
                self.app.push_screen("teams")

            case "settings":
                pass