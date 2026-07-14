from textual.app import ComposeResult
from textual.containers import Horizontal, Vertical
from textual.screen import Screen
from textual.widgets import Button, Footer, Header, Input, Label, Static

from togepy.models.pokemon import PokeTeam


#Ich weiß nicht ob hier der richtige Ort für diese Funktion ist
#sonst self.app.teams_inapp nicht abrufbar wenn in modul
def refresh_teams_prompt(self) -> str:
    if not self.app.teams_inapp:
        return "No Teams created."

    prompt = "Existing Teams:\n\n"
    for team in self.app.teams_inapp:
        prompt += team.team_name + "\n"
    return prompt

class CreateTeamScreen(Screen):

    CSS = """
    Header {
        margin-bottom: 1;
    }
    Input {
        margin-top: 1;
        margin-bottom: 1;
        width: 100%;
    }
    Vertical {
        padding-left: 1;
        padding-right: 1;
    }
    Static {
        align: center middle;
        padding-left: 1;
    }
    """
    def compose(self) -> ComposeResult:
        yield Header()

        yield Horizontal(
            Vertical(
                Label("Enter a Team Name:"),
                Input(
                    placeholder="team name here :3 ('Enter to submit')",
                    id="teamname_input",
                ),
                Horizontal(
                    Button(
                        "⬅ Back",
                        id="back",
                    ),
                    Static(content="", id="rename_warning", classes="wrap"),
                ),
            id="leftside"),
            Vertical(
                Label(
                    refresh_teams_prompt(self),
                    id="teams_info",
                )
            ),
        )

        yield Footer()

    def on_input_submitted(self, event: Input.Submitted) -> None:
        al_ex_flag = 0
        team_name_suggest = event.value.strip().title()

        info = self.query_one("#teams_info", Label)
        warning = self.query_one("#rename_warning", Static)

        if not team_name_suggest:
            warning.update("Warning:\nno blankies ://")
            return

        for team in self.app.teams_inapp:
            if team.team_name == team_name_suggest:
                #team_name_suggest += "-new" #Hier namechecker logic oder so, prompt to rename, hinweis
                #I don't know why this worked to produce -new-new
                #geht ein team weiter prüft dann auf -new, sieht gibt, noch ein new dran
                #somehow aber wenn ich a entfernt hab ging a-new nicht entfernbar. dann konnte ich neues a und a-new erstellen,
                #war dann zweimal da... i dont fucking know wtf is happening tbh
                #duplicate entries in teamslist
                al_ex_flag = 1

        if al_ex_flag:
            #warning.update("Team Name already exists. '-new' will be appended to name")
            warning.update("Warning:\nTeam Name already exists...\nThink of something new!")
            return #this doesnt rename automatically. maybe fix some other time

        self.app.teams_inapp += [PokeTeam(team_name_suggest)] #in neuem button. suggestion that reference needs to be updated for reactive
        info.update(refresh_teams_prompt(self))

    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case "back":
                self.app.pop_screen()
            case "create_team_button":
                pass    #hinzufügen über button oder enter drücken