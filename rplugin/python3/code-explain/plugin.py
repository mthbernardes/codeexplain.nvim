import pynvim

@pynvim.plugin
class CodeExplain(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @pynvim.command('CodeExplain', pattern='*', eval='', sync=True)
    def code_explain(self, filename):
        self.vim.current.buffer[0] = 'Hello, Neovim!'
