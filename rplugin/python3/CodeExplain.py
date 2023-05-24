import pynvim
import langchain
from langchain.cache import InMemoryCache
from langchain.llms import LlamaCpp
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.memory import ConversationBufferMemory
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

class IA():
    def __init__(self,):
        langchain.llm_cache = InMemoryCache()
        LLAMA_EMBEDDINGS_MODEL = '/Users/matheus.bernardes/dev/mthbernardes/code-query/models/ggml-model-q4_0.bin' 
        MODEL_N_CTX = 1000
        CALLBACKS = [StreamingStdOutCallbackHandler()]
        PROMPT_TEMPLATE = """Act as a expert software engineer with high skill in software quality, performance and security. I will provide a piece of code to you and it is your job to explain it. If you can not explain the code just answer with "Sorry I was unable to understand it." 
        ```
        {code}
        ```
        """
        PROMPT = PromptTemplate(template=PROMPT_TEMPLATE, input_variables=["code"])
        LLM = LlamaCpp(model_path=LLAMA_EMBEDDINGS_MODEL, n_ctx=MODEL_N_CTX, verbose=False)
        self.CHAIN = LLMChain(llm=LLM, prompt=PROMPT,memory=ConversationBufferMemory())

    def run(self,code):
        return self.CHAIN.run(code)

@pynvim.plugin
class CodeExplain(object):
    def __init__(self, nvim):
        self.nvim = nvim
        self.codeExplainAI = IA()
        self.nvim.command("echom \"My plugin is being executed\"")

    @pynvim.command('CodeExplain', nargs='*',range=True, sync=True)
    def codeExplain(self,args,range):
        begin = self.nvim.eval("line(\"'<\")")
        end = self.nvim.eval("line(\"'>\")")
        lines = self.nvim.current.buffer[begin - 1:end]
        selected_text = '\n'.join(lines)
        explained = self.codeExplainAI.run(selected_text)
        lines = explained.split('\n')
        lines = [self.nvim.funcs.escape(line, '\"\\') for line in lines]
        bufnr = self.nvim.api.create_buf(False, True)
        winnr = self.nvim.api.open_win(bufnr, True, {
            'relative': 'editor',
            'width': 80,
            'height': 20,
            'row': 10,
            'col': 10
        })
        self.nvim.api.buf_set_lines(bufnr, 0, -1, True, lines)

        #self.nvim.command(f"call popup_create({lines}, {{}})")
