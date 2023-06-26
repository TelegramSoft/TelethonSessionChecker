# TelethonSessionChecker
#### Tool for checking telethon session

# Using

## From exe
- Download SessionChecker.exe from [releases](https://github.com/TelegramSoft/TelethonSessionChecker/releases)
- Launch it in the directory with files .session + .json
- All bad sessions will be moved in bad_sessions directory

## From sources
- Download zip from [releases](https://github.com/TelegramSoft/TelethonSessionChecker/releases) page and extract all files
- Install [python3.8+](https://www.python.org/downloads/)
- Install libraries

#### On Windows
```commandline
pip install -r requirements.txt
```

#### On Linux
```commandline
pip3 install -r requirements.txt
```

- add All session files in directory with main.py file
- Launch main.py
#### On Windows
```commandline
python main.py
```

#### On Linux
```commandline
python3 main.py
```

- All bad sessions will be moved in bad_sessions directory
