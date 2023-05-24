# Code Explain

## Python dependencies
```bash
pip install pynvim langchain pygpt4all llama-cpp-python pygments
```

## Model
```bash
mkdir -p "$HOME/.codeexplain/"
curl -o "$HOME/.codeexplain/model.bin" https://gpt4all.io/models/ggml-gpt4all-j-v1.3-groovy.bin
```

## Packer
``` 
  use { 'mthbernardes/codeexplain.nvim', run = ':UpdateRemotePlugins' }
```

## vim-plug
``` 
  Plug 'mthbernardes/codeexplain.nvim', { 'do': ':UpdateRemotePlugins' }
```

## Usage
Select the piece of code and invoke the command `CodeExplain`
