   # openai-coding-agent

   A command-line coding agent that uses the OpenAI API to read, edit, and run code in a project.

      ## Features
   - Reads and edits files in your project
   - Runs shell commands and shows the output
   - (list what yours actually does)

   ## Requirements
   - Ubuntu / Linux
   - Python 3.11+
   - An OpenAI API key

   ## Installation
   1. Clone the repo:
      ```bash
      git clone https://github.com/nshulabh/openai-coding-agent.git
      cd openai-coding-agent
      ```
   2. Create a virtual environment and install dependencies:
      ```bash
      python3 -m venv .venv
      source .venv/bin/activate
      pip install -r requirements.txt
      ```
   3. Set your API key:
      ```bash
      export OPENAI_API_KEY="your-key-here"
      ```

   ## Usage
   ```bash
   python main.py "add a function that parses CSV files"
   ```

   ## Project structure
   ```text
   openai-coding-agent/
   ├── main.py
   ├── requirements.txt
   └── README.md
   ```

   ## License
   MIT