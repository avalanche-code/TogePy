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
from textual.widgets import Button, Footer, Header, Label


class MainMenuButtons(Vertical):
    def compose(self) -> ComposeResult:
        yield Button("Show Teams", id="sh_teams", variant="primary")
        yield Button("Query Pokemon", id="q_pokemon", variant="primary")

class MainMenuText(Vertical):
    def compose(self) -> ComposeResult:
        yield Label("Example/Introductory text here")

class PokePyApp(App):
    """PokePy Team Builder: Main TUI App entry point"""
    BINDINGS = [("ctrl+q", "quit", "Quit PokePy")]

    def compose(self) -> ComposeResult:
        yield Horizontal(MainMenuButtons(), MainMenuText())
        yield Header(name="PokePy Team Builder")
        yield Footer()

    def on_mount(self) -> None:
        self.theme = "gruvbox"
        self.title = "PokePy: A Pokemon Team Builder"

    def action_quit(self) -> None:
        self.exit()

if __name__ == "__main__":
    app = PokePyApp()
    app.run()