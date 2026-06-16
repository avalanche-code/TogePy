from textual.app import App, ComposeResult
from textual.containers import (
    Container,
    Horizontal,
    HorizontalGroup,
    HorizontalScroll,
    Vertical,
    VerticalGroup,
    VerticalScroll,
)
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Input, Label


class MainMenuButtons(Vertical):
    def compose(self) -> ComposeResult:
        yield Button("Show Teams", id="sh_teams", variant="primary", disabled=True)
        yield Button("Query Pokemon", id="q_pokemon", variant="primary")

class MainMenuText(Vertical):
    def compose(self) -> ComposeResult:
        yield Label("Example/Introductory text here")

class MainMenu(Screen):
    def compose(self) -> ComposeResult:
        yield Horizontal(MainMenuButtons(), MainMenuText())
        yield Header(name="PokePy Team Builder")
        yield Footer()

    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "q_pokemon":
            self.app.push_screen("query")

class QueryMenu(Screen):
    def compose(self) -> ComposeResult:
        yield Horizontal(
            Vertical(
                Label(id="label1", content="Enter a Pokemon name you want to query:"),
                Input(placeholder="e.g.: Ditto"),
            ),
            Vertical(Label(id="label2", content="Info will be displayed here")),
        )
        # instead of
        # yield Label(id= "label1", content="Enter a Pokemon name you want to query:")
        # yield Input(placeholder="e.g.: Ditto")
        # yield Label(id= "label2", content="Info will be displayed here")
        # if name in responses.key

    def on_input_submitted(self, event: Input.Submitted) -> None:
        self.query_one("#label2", Label).update(f"You entered {event.value}")


class TogePyApp(App):
    """PokePy Team Builder: Main TUI App entry point"""
    BINDINGS = [("ctrl+q", "quit", "Quit PokePy")]
    SCREENS = {
        "main": MainMenu,
        "query": QueryMenu}

    def on_mount(self) -> None:
        self.push_screen("main")
        self.theme = "gruvbox"
        self.title = "PokePy: A Pokemon Team Builder"

    def action_quit(self) -> None:
        self.exit()

if __name__ == "__main__":
    app = TogePyApp()
    app.run()