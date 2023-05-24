import pynvim

@pynvim.plugin
class CodeExplain(object):
    def __init__(self, nvim):
        self.nvim = nvim
        print("Plugin initialized")  # For debugging
        self.nvim.command("echom 'My plugin is being executed'")

    @pynvim.command('CodeExplain', range: True, sync: True)
    
    def codeExplain(self,start, stop):
        print(self.nvim.current.buffer.lines[start-1:stop-1])
        self.nvim.command("echom 'My plugin is being executed'")
