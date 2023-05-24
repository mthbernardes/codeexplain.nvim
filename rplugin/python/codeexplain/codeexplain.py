import pynvim

@pynvim.plugin
class CodeExplain(object):
    def __init__(self, nvim):
        self.nvim = nvim
        self.nvim.command("echom 'My plugin is being executed'")

    #@pynvim.autcmd('', pattern='*', eval='', sync=True)
    @pynvim.function('CodeExplain')
    def code_explain(self, filename):
        self.vim.current.buffer[0] = 'Hello, Neovim!'
