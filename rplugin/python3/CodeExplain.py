import pynvim

@pynvim.plugin
class CodeExplain(object):
    def __init__(self, nvim):
        self.nvim = nvim
        print("Plugin initialized")  # For debugging
        self.nvim.command("echom 'My plugin is being executed'")

    @pynvim.command('CodeExplain', sync=True)
    def codeExplain(self, filename):
        self.nvim.command("echom 'My plugin is being executed'")
        self.vim.current.buffer[0] = 'Hello, Neovim!'
