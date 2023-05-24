import pynvim

@pynvim.plugin
class CodeExplain(object):
    def __init__(self, nvim):
        self.nvim = nvim
        self.nvim.command("echom 'My plugin is being executed'")

    @pynvim.command('CodeExplain',  nargs='*', range=True)
    def codeExplain(self, args, range):
        begin = self.nvim.eval("line(\"'<\")")
        end = self.nvim.eval("line(\"'>\")")
        lines = self.nvim.current.buffer[begin - 1:end]
        selected_text = '\n'.join(lines)
        print(f"begin: {begin}")
        print(f"end: {end}")
        print(f"lines: {lines}")
        print(f"selected_text: {selected_text}")

