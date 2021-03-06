import json
from errorclass import MSMSError
def get_settings(obj:str):
    settingsf = open("settings.json")
    settings = dict(json.loads(settingsf.read()))
    settingsf.close()
    r = str(settings[obj])
    return r