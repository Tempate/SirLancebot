# SirLancebot

This project is an attempt at making a Python Bot for which it's very easy to write plugins.


## Running the code

Install the requirements:
```
pip install -r requirements.txt
```

Run the code:
```
python main.py
```


## Code's Structure

There are three main files:
1. **Bot.py**: Handles sockets and connections.
2. **Plugin.py**: States the main structure every plugin should follow.
3. **main.py**: Interacts with Bot.py and links all plugins together.


## Config file

This file must be added to the repository for the bot to work.

```
{
    "conf" : {
        "irc": "irc.libera.chat",
        "port": 6667,
        "nick": "SirLancebot",
        "user": "SirLancebot",
        "real": "SirLancebot",
        "pass": "",
        "chans": [""]
    },

    "Lichess" : {
        "lichess_usernames" : {}
    },

    "Weather" : {
        "key": ""
    }
}
```
