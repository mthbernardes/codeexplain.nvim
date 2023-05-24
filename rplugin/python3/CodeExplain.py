import pynvim

@pynvim.plugin
class CodeExplain(object):
    def __init__(self, nvim):
        self.nvim = nvim
        print("Plugin initialized")  # For debugging
        self.nvim.command("echom 'My plugin is being executed'")

    @pynvim.command('CodeExplain',  nargs='*', range=True)
    def codeExplain(self, args, range):
        selected_text = self.nvim.funcs.getreg('"')
        self.nvim.command(f"echom 'Selected text: {selected_text}'")
        print(selected_text)
