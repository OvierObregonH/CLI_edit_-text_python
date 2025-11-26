from textual.app import App, ComposeResult
from textual.widgets import Input, TextArea, Footer
from textual.containers import Vertical

class MiniVimStage1(App):
    def __init__(self):
        super().__init__()
        self.buffer = []       # almacena las líneas
        self.mode = "COMMAND"  # modos: COMMAND o INSERT

    def compose(self) -> ComposeResult:
        yield Vertical(
            TextArea(id="editor", language="plain"),
            Input(placeholder=":% escribe comandos con >", id="cmd"),
            Footer()
        )

    def on_input_submitted(self, event: Input.Submitted) -> None:
        text = event.value.strip()
        editor = self.query_one("#editor", TextArea)

        if text.startswith(">"):  # es un comando
            cmd = text[1:]
            if cmd == "insert":
                self.insert = "INSERT"
                editor.insert("-- Modo inserción --")
            elif cmd == "quit":
                self.exit()
            else:
                editor.insert(f"Comando desconocido: {cmd}")
        else:
            # si estamos en modo inserción, añadimos al buffer
            if self.mode == "INSERT":
                self.buffer.append(text)
                editor.insert(text)
            else:
                editor.insert("Usa >insert para escribir texto")

        event.input.value = ""  # limpiar input

if __name__ == "__main__":
    MiniVimStage1().run()