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


#code =  """ 
#(defn scan* [opts]
#  (let [code-structures (diplomat.code-reader/code-structure-from-clj-files-in-directory! opts)
#        rules (rules.loader/init! opts)
#        scans-results (->> code-structures
#                           (pmap #(check-rules-in-code-structure % rules))
#                           (reduce concat))
#        scan-result-output (output/output scans-results opts)]
#    scan-result-output))
#"""
#
#print(CHAIN.run(code))
