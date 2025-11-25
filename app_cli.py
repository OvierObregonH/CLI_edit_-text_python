from textual.app import App, ComposeResult 
from textual.widgets import Input, TextLog, Footer 
from textual.containers import Vertical  


class MiniVimStage1(App): 
    def __init__(self): 
        super().__init__()  
        self.buffer = []        # alamcena las lineas 
        self.mode = "COMMAND"   # modos: COMMAND o INSERT 

    def compose(self) -> ComposeResult: 
        yield Vertical(
            TextLog(id="editor", highlight=True)
            
        )

        