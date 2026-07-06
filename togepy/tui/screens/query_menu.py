from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Input, Label

from togepy.api.api import APICaller, init_pokemon_obj, sanitize_dict

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
                    label="➕ Add to Team",
                    id="add_toteam",
                    disabled=True
                ),
                Button(
                    "⬅ Back",
                    id="back",
                )
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
        add_button = self.query_one("#add_toteam", Button)

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

        poke_candidate = init_pokemon_obj(sanitize_dict(data))

        info.update(
            f"Pokedex ID: #{poke_candidate.pokedex_id}\n"
            f"Name: {poke_candidate.name}\n"
            f"Primary Type: {poke_candidate.maintype}\n"
            f"Secondary Type: {poke_candidate.sectype}\n"
            f"First ability: {poke_candidate.ability}\n"
            #f"All abilities: {abilities}"
        )
        if self.app.teams_inapp:
            add_button.disabled = False

    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case "back":
                self.app.pop_screen()
            #case "add_toteam":
            #    self.app.push_screen()