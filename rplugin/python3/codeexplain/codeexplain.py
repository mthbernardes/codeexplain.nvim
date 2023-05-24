import pynvim

@pynvim.plugin
class CodeExplain(object):
    def __init__(self, nvim):
        self.nvim.command("echom 'My plugin is being executed'")
        self.nvim = nvim

    #@pynvim.autcmd('', pattern='*', eval='', sync=True)
    @pynvim.command('CodeExplain', range='', nargs='*', sync=True)
    def code_explain(self, filename):
        self.vim.current.buffer[0] = 'Hello, Neovim!'
