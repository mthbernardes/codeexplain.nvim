import pynvim

@pynvim.plugin
class CodeExplain(object):
    def __init__(self, nvim):
        self.nvim = nvim
        self.nvim.command("echom 'My plugin is being executed'")

    @pynvim.function('CodeExplain',sync=True)
    def code_explain(self, filename):
        self.nvim.command("echom 'My plugin is being executed'")
        self.vim.current.buffer[0] = 'Hello, Neovim!'
