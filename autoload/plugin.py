import neovim

@neovim.plugin
class CodeExplain(object):
    def __init__(self, nvim):
        self.nvim = nvim

    @neovim.autocmd('ExplainCode', pattern='*', eval='')
    def explain_code(self, filename):
        self.vim.current.buffer[0] = 'Hello, Neovim!'
        #self.nvim.out_write('neotags > ' + message + "\n")

