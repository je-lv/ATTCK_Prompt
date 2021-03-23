# ATT&CK Prompt

Simple cli app to search and learn MITRE ATT&CK's techinques.

* Two use modes:

![Mode Selection](/imgs/select_mode.png)

## Search Mode

Searches techniques names from user supplied input. Uses a fuzzy match completer to help the user find the desired technique faster.

![Technique Search suggestions](/imgs/search_technique.png)

* Technique information printed on terminal.

![Technique Information](/imgs/technique_info.png)


## Random Mode

On 'ENTER' key, as the name implies, it randomly displays a technique's information.
Useful for learning sessions.

![Random Mode](/imgs/random_mode.png)

### Usage

#### Data building

In the data directory of this repo there is a companion script that gets the ATT&CK oficial data, parses it and builds up a json file to be used by the ATT&CK prompt.

This script can build up the json file with the retrieved data as it is (suited to create md files) or it can clean the 'description' text a bit for better readbility in the ATT&CK prompt.

This repo includes a 'description' cleaned file.

**Works only with python3**

```bash
pip3 install prompt_toolkit==3.0.8

chmod +x attck_prompt.py

./attck_prompt.py
```

To close the prompt, CTRL+Shift+C from main section or typing 'quit' when in search_mode or random_mode.

When in search_mode or random_mode, CTRL+Shift+C will make the user go back to the main section (mode switching).

