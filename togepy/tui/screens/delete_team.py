import base64

from textual.app import ComposeResult
from textual.containers import (
    Container,
    Horizontal,
    Vertical,
    VerticalScroll,
)
from textual.css.query import NoMatches
from textual.screen import Screen
from textual.widgets import Button, Collapsible, Footer, Header, Input, Label, Static


#margin außerhalb, padding innerhalb
class DeleteTeamScreen(Screen):
    CSS = """
    Header {
        margin-bottom: 1;
    }
    Input {
        margin-top: 1;
        margin-bottom: 1;
    }
    VerticalScroll {
        width: 100%;
        align: center bottom;
    }
    Footer {
        margin-top: 1;
    }
        Static {
        align: center middle;
        padding-left: 1;
    }
    """

    def compose(self) -> ComposeResult:
        yield Header()

        yield Container(
            Vertical(
                Label("Enter a Team Name:"),
                Input(
                    placeholder="team name here :(",
                    id="teamname_input",
                ),
                Horizontal(
                    Button(
                        "⬅ Back",
                        id="back",
                    ),
                    Static(
                        "", 
                        id="warning_static"
                    )
                )
                )
            )
        yield VerticalScroll(id="teams_container")
        yield Footer()

    def on_mount(self):
        teams_container = self.query_one("#teams_container", VerticalScroll)

        if not self.app.teams_inapp:
            teams_container.mount(Label("No Teams created.")) #no other logic (try except) needed for querying if label is shown then hide and then make new collapsibles below

        for team in self.app.teams_inapp:
            teams_container.mount(Collapsible(Static("Team members here"), collapsed=True, title=team.team_name, id="b64-"+str(base64.b16encode(team.team_name.encode("utf-8")))[2:-1]))

    def on_input_submitted(self, event: Input.Submitted) -> None:
        #teams_container = self.query_one("#teams_container", VerticalScroll)
        warning = self.query_one("#warning_static", Static)
        to_delete = event.value.strip().title()

        #Es wurde ja sichergestellt dass pro Element in teamslist hier ein collapsible ist, demnach kann ich ohne prüfung auch das element aus liste löschen
        #durch die erstellung des collapsible wissen wir ja dass es das gibt.
        try:
            collapsible_hit = self.query_one(f"#{'b64-' + str(base64.b16encode(to_delete.encode("utf-8")))[2:-1]}", Collapsible)
        except NoMatches:
            warning.update("Team Name not found.")
            return
        else:
            collapsible_hit.remove()
            warning.update(f"Team {to_delete} deleted.")
            for team in self.app.teams_inapp:
                if team.team_name == to_delete:
                    self.app.teams_inapp.remove(team)
                    return  #so? oder lieber fertig laufen lassen

    def on_button_pressed(self, event: Button.Pressed) -> None:
        match event.button.id:
            case "back":
                self.app.pop_screen() #Since this screen is a new instance it gets destroyed at pop