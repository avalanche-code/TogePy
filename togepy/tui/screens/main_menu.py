from textual.app import ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Static

from togepy.tui.screens.query_menu import QueryMenu

GREETING = ("Welcome to TogePy Team Builder!\n\nIn this application you can manage "
          "and build Pokemon Teams using data queried from the 'PokeAPI', a popular RESTful API for getting "
          "Pokemon-related information.\n\nPlease select an option:")

class MainMenu(Screen):
    """Main menu of the application."""
    #left and right or only right? margin or padding
    CSS = """
    Header {
        content-align: center middle;
    }
    Vertical {
        padding-right: 1;
        padding-left: 1;
    }
    Horizontal {
        margin-top: 1;
    }
    Container {
        align: center top;
    }
    Button {
        width: 50%;
        content-align: center middle;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()

        yield Horizontal(
            Vertical(
                Container(
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
                    )
                )
            ),
            Vertical(
                Static(GREETING, classes="wrap", id="greeting")
            ),
        )

        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case "query_pokemon":
                self.app.push_screen(QueryMenu())   #abuse mount() for list initiation

            case "teams":
                self.app.push_screen("teamsmenu")

            case "settings":
                pass