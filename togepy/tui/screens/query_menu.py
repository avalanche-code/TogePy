from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import (
    Button,
    Footer,
    Header,
    Input,
    Label,
    OptionList,
    Static,
)
from textual.widgets.option_list import Option

from togepy.api.api import APICaller, init_pokemon_obj, sanitize_dict

MAX_TEAM_SIZE = 6

# instancing object of api caller class. keeps connection open
my_apicaller = APICaller()

class QueryMenu(Screen):
    """Search for a Pokemon."""
    CSS = """
    Footer {
        margin-top: 1;
    }
    """
    pokemon_candidate = None

    def compose(self) -> ComposeResult:
        yield Header()

        yield Horizontal(
            Vertical(
                Label("Enter a Pokémon name:"),
                Input(
                    placeholder="e.g. Pikachu",
                    id="pokemon_input",
                ),
                Horizontal(
                    Button(
                        "⬅ Back",
                        id="back",
                    ),
                    Button(label="➕ Add to Team", id="add_toteam", disabled=True),
                ),
                Horizontal(
                    Vertical(
                        Static("", id="warning_static"),
                        OptionList(
                            id="teams_selector",
                        )
                    ),
                    Vertical(
                        Static("Team info", id="team_info"),
                    )
                )
            ),
            Vertical(
                Label(
                    "Pokemon information will appear here.",
                    id="pokemon_info",
                )
            )
        )

        yield Footer()

    def refresh_teams_overview(self, teamname: str):
        team_info = self.query_one("#team_info", Static)
        info = f"Team ’{teamname}’:\n\n"
        # Wenn ich eh schon den namen hab kann ich auch direkt zugreifen statt iterieren? delete_team ja genauso
        for team in self.app.teams_inapp:
            if team.team_name == teamname:
                for pokemon in team.pokemons:
                    info += f"- {pokemon.name}\n"

        team_info.update(info)

    def on_mount(self) -> None:
        teams_selector = self.query_one("#teams_selector", OptionList)

        if not self.app.teams_inapp:
            teams_selector.disabled = True
            teams_selector.add_options([
                Option("Warning:"),
                None,
                Option("No teams found!"),
                Option("Go Create some first..."),
                None
            ])
        for team in self.app.teams_inapp:
            teams_selector.disabled = False
            teams_selector.add_option(option=team.team_name)

    def on_option_list_option_selected(self, event: OptionList.OptionSelected) -> None:
        #outsource this function to use again when a pokemon has been added
        teamname= event.option.prompt
        self.refresh_teams_overview(teamname)


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
        except Exception as e:  #duplicate? error check in func?
            info.update(f"Error occurred: {e}")
            return

        if not data:
            info.update("Pokemon not found ❌")
            return

        poke_candidate = init_pokemon_obj(sanitize_dict(data))
        self.pokemon_candidate = poke_candidate

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

    #Es würde auch gehen dass wenn man element aus liste wählt dann der button highlighted wird, aber das schwer
    #Dann muss man schauen dass pokemon vorher queried wurde oder auch erfüllt wird.
    #More streamlined wie ein Fluss würde die pokemon addition auch gehen. Query, dann add team, dann screen mit teams, yes/no button

    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case "back":
                self.app.pop_screen()
            case "add_toteam":
                #self.app.push_screen()
                warning_static = self.query_one("#warning_static", Static)
                teams_selector = self.query_one("#teams_selector", OptionList)

                if teams_selector.highlighted_option:
                    warning_static.update(f"DEBUG ADD {teams_selector.highlighted_option.prompt}")  #id would be better but base16 has to be implemented as external func
                    #warnung kann ignoriert werden. wir haben garantiert immer nur options nach vorgegebenem Prinzip
                    for team in self.app.teams_inapp:
                        if team.team_name == teams_selector.highlighted_option.prompt:  #error handling if none? eig nicht benötigt
                            if len(team.pokemons) == MAX_TEAM_SIZE:    #früher checken? oder externe func. oder jeweils halt hioer bei add, sonstwo bei delete
                                warning_static.update(f"DA SIND SCHON {MAX_TEAM_SIZE}")
                                return

                            #use cached version from above here... no new api call: done by using class var
                            team.pokemons.append(self.pokemon_candidate)
                            self.refresh_teams_overview(team.team_name)
                            #TODO This moves the selector down. fix in css
                            warning_static.update(f"Pokemon '{self.pokemon_candidate.name}' was added to team '{team.team_name}'.")
                            return
                    
                else:
                    warning_static.update("Choose a team first!")
                    return