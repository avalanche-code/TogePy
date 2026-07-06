
from textual import events
from textual.app import ComposeResult
from textual.containers import Container, Horizontal, Vertical
from textual.events import Show
from textual.reactive import reactive
from textual.screen import Screen
from textual.widgets import Button, Collapsible, Footer, Header, Input, Label, Static

from togepy.models.pokemon import PokeTeam


def refresh_teams_prompt(self, teams: list) -> str:
    if not self.app.teams_inapp:
        return "No Teams created."

    prompt = "Existing Teams:\n"
    for team in self.app.teams_inapp:
        prompt += team.team_name + "\n"
    return prompt

#Ich weiß nicht ob hier der richtige Ort für diese Funktion ist
class DeleteTeamScreen(Screen):

    def compose(self) -> ComposeResult:
        yield Header()

        yield Container(
            Vertical(
                Label("Enter a Team Name:"),
                Input(
                    placeholder="team name here :(",
                    id="teamname_input",
                ),
                Button(
                        "⬅ Back",
                        id="back",
                )
            )
        )
        yield Label(
                    refresh_teams_prompt(self, self.app.teams_inapp),
                    id="allteams",
        )
        yield Footer()

    def on_mount(self):
        self.query_one("#allteams", Label).update(refresh_teams_prompt(self, self.app.teams_inapp))

    def on_input_submitted(self, event: Input.Submitted) -> None:
        self.query_one("#allteams", Label).update(event.value)

    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case "back":
                self.app.pop_screen() #Since this screen is a new instance it gets destroyed at pop
            case "create_team_button":
                pass    #hinzufügen über button oder enter drücken