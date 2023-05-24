import neovim

@neovim.plugin
class CodeExplain(object):

    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.command("CodeExplain", range='', nargs='*')
    def code_explain(self, args, range):
        self.vim.current.buffer[0] = 'Hello, Neovim!'
