import pynvim

@pynvim.plugin
class CodeExplain(object):
    def __init__(self, nvim):
        self.nvim = nvim
        print("Plugin initialized")  # For debugging
        self.nvim.command("echom 'My plugin is being executed'")

    @pynvim.command('CodeExplain',  nargs='*', range='')
    def codeExplain(self, args, Range):
        print(Range)
        #self.nvim.command(Range)
        #print('Command with range: {}'.format(range))
