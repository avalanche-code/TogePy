from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Input, Label
from togepy.helpers import APICaller

# instancing object of api caller class. keeps connection open
my_apicaller = APICaller()

class QueryMenu(Screen):
    """Search for a Pokemon."""

    def compose(self) -> ComposeResult:
        yield Header()

        yield Horizontal(
            Vertical(
                Label("Enter a Pokémon name:"),
                Input(
                    placeholder="e.g. Pikachu",
                    id="pokemon_input",
                ),
                Button(
                    "⬅ Back",
                    id="back",
                ),
            ),
            Vertical(
                Label(
                    "Pokemon information will appear here.",
                    id="pokemon_info",
                )
            ),
        )

        yield Footer()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        pokemon_name = event.value.strip()

        if not pokemon_name:
            return

        info = self.query_one("#pokemon_info", Label)

        info.update(
            f"Searching for: {pokemon_name}"
        )
        try:
            data = my_apicaller.get_pokemon_name(pokemon_name)
        except Exception as e:
            info.update(f"Error occurred: {e}")
            return

        if not data:
            info.update("Pokemon not found ❌")
            return

        # abilities extrahieren 
        abilities = [
            a["ability"]["name"]
            for a in data.get("abilities", [])
        ]

        first_ability = abilities[0] if abilities else "None"

        info.update(
            f"Name: {data['name']}\n"
            f"First ability: {first_ability}\n"
            f"All abilities: {abilities}"
        )
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "back":
            self.app.pop_screen()