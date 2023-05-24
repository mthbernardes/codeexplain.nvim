import pynvim
from IA import IA

@pynvim.plugin
class CodeExplain(object):
    def __init__(self, nvim):
        self.nvim = nvim
        self.codeExplainAI = IA()
        self.nvim.command("echom 'My plugin is being executed'")

    @pynvim.command('CodeExplain',  nargs='*', range=True)
    def codeExplain(self, args, range):
        begin = self.nvim.eval("line(\"'<\")")
        end = self.nvim.eval("line(\"'>\")")
        lines = self.nvim.current.buffer[begin - 1:end]
        selected_text = '\n'.join(lines)
        explained = self.codeExplainAI.run(selected_text)
        self.nvim.command(f"echom '{explained}'")
