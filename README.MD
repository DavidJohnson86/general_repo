pip install poetry
poetry new rest_service
poetry shell
poetry add --dev pytest
https://pre-commit.com/

Black:
Configure Your Editor:

Visual Studio Code (VSCode):

Install the "Python" extension by Microsoft if you haven't already.

Open your Python project in VSCode.

Create or edit the .vscode/settings.json file in your project directory (if it doesn't exist).

Add the following settings to enable automatic formatting with Black:

json
Copy code
{
    "editor.formatOnSave": true,
    "python.formatting.provider": "black",
    "python.formatting.blackArgs": ["--config=pyproject.toml"]
}
The "editor.formatOnSave" setting will format your code automatically when you save a Python file.

The "python.formatting.provider" setting specifies Black as the code formatter.

The "python.formatting.blackArgs" setting provides the --config option with the path to your pyproject.toml file