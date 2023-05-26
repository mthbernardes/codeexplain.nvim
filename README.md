# codeexplain.nvim

codeexplain.nvim is a NeoVim plugin that uses the powerful [GPT4ALL](https://gpt4all.io/) language model to provide on-the-fly, line-by-line explanations and potential security vulnerabilities for selected code directly in your NeoVim editor. It's like having your personal code assistant right inside your editor without leaking your codebase to any company.

![Demo](https://github.com/mthbernardes/codeexplain.nvim/assets/12648924/734f1687-d506-4b0b-9dd0-6e9232284e09)

## Features
- No internet necessary
- Automatic language detection for explaining code.
- Supports a wide range of programming languages.
- Powered by [GPT4ALL](https://gpt4all.io/) for code explanation.
- Identification of potential security vulnerabilities.
- Creates a new NeoVim window to display the explanations.

## Installation

## Requirements
- NeoVim
- Python3
- langchain
- llama-cpp-python
- Pygments
- pynvim

```bash
pip install -r langchain==0.0.177 llama-cpp-python==0.1.48 Pygments==2.15.1 pynvim==0.4.3
```
### Download the GPT4ALL model
Before installing the plugin, download the GPT4ALL model and save it in your home directory:

```bash
mkdir -p "$HOME/.codeexplain/"
curl -o "$HOME/.codeexplain/model.bin" https://gpt4all.io/models/ggml-vicuna-7b-1.1-q4_2.bin
```

### vim-plug

Add the following line to your `init.vim`:

```vim
Plug 'mthbernardes/codeexplain.nvim'
```

Then run the following commands in your NeoVim editor:

```vim
:source %
:PlugInstall
```

### packer.nvim

Add the following to your `plugins.lua` file:

```lua
use 'mthbernardes/codeexplain.nvim'
```

Then run `PackerSync` in your NeoVim editor.

### Other package managers

Please refer to your package manager's documentation for installation instructions. The general process involves adding a line to your `init.vim` (or equivalent configuration file) and running an installation command.

### Post-install
Once installed execute the command `:UpdateRemotePlugins`

## Usage
You can use the plugin by selecting a piece of code in Visual mode and running the `CodeExplain` command:

```vim
:CodeExplain
```

A new window will be opened in your NeoVim editor, displaying line-by-line explanations of the selected code and potential security vulnerabilities.


## Contributions

Contributions are welcome! Please feel free to submit a pull request.

## License

codeexplain.nvim is open-source software licensed under the [MIT license](LICENSE).

## Disclaimer

This plugin uses GPT-4all to provide line-by-line explanations and to point out potential security vulnerabilities in your code. While it strives to be helpful, it's not a replacement for understanding your code or manually checking for security vulnerabilities. Always verify the information provided by this plugin.
