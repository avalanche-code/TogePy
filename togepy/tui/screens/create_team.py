from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Input, Label, Static

from togepy.models.pokemon import PokeTeam


#Ich weiß nicht ob hier der richtige Ort für diese Funktion ist
def refresh_teams_prompt(self, teams: list) -> str:
    if not self.app.teams_inapp:
        return "No Teams created."

    prompt = "Existing Teams:\n"
    for team in self.app.teams_inapp:
        prompt += team.team_name + "\n"
    return prompt

class CreateTeamScreen(Screen):
    def compose(self) -> ComposeResult:
        yield Header()

        yield Horizontal(
            Vertical(
                Label("Enter a Team Name:"),
                Input(
                    placeholder="team name here :3",
                    id="teamname_input",
                ),
                Horizontal(
                    Button(
                        "⬅ Back",
                        id="back",
                    ),
                    Button(
                        label="➕ Create Team",
                        id="create_team_button",
                        disabled=True
                    )
                ),
                Static(
                    content="",
                    id="rename_warning",
                    classes="wrap"
                )
            ),
            Vertical(
                Label(
                    refresh_teams_prompt(self, self.app.teams_inapp),
                    id="teams_info",
                )
            )
        )

        yield Footer()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        al_ex_flag = 0
        team_name_suggest = event.value.strip().title()
        info = self.query_one("#teams_info", Label)
        warning = self.query_one("#rename_warning", Static)

        for team in self.app.teams_inapp:
            if team.team_name == team_name_suggest:
                team_name_suggest += "-new" #Hier namechecker logic oder so, prompt to rename, hinweis
                al_ex_flag = 1

        if al_ex_flag:
            warning.update("Team Name already exists. '-new' will be appended to name")

        self.app.teams_inapp += [PokeTeam(team_name_suggest)] #in neuem button. suggestion that reference needs to be updated for reactive
        info.update(refresh_teams_prompt(self, self.app.teams_inapp))

    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case "back":
                self.app.pop_screen()
            case "create_team_button":
                pass    #hinzufügen über button oder enter drücken