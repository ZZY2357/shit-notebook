# Handle the settings

import json

config_file = 'settings.json'

def read_settings():
    with open(config_file, 'r') as f:
        settings = json.loads(f.read(), encoding='utf-8')
    return settings

def save_settings(data: dict):
    content = json.dumps(data, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ': '), encoding="utf-8")
    with open(config_file, 'w') as f:
        f.write(content)

def setValue(key: str, value: str):
    settings = read_settings()
    settings[key] = value
    save_settings(settings)

def getValue(key: str):
    settings = read_settings()
    return settings[key]
