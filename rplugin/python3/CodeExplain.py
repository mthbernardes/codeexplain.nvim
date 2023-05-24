import pynvim

@pynvim.plugin
class CodeExplain(object):
    def __init__(self, nvim):
        self.nvim = nvim
        print("Plugin initialized")  # For debugging
        self.nvim.command("echom 'My plugin is being executed'")

    @pynvim.command('CodeExplain',  nargs='*', range=True)
    def codeExplain(self, args, range):
        self.nvim.command("normal! gv\"ay")
        selection = self.nvim.eval("@a")
        print(selection)
        #self.nvim.out_write('Command with args: {}, range: {}'.format(args, range))

        #self.nvim.command(Range)
        #print('Command with range: {}'.format(range))

