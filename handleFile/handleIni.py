import configparser
from configparser import ConfigParser
from collections import defaultdict


class HandleIni:

    def __init__(self, path=None) -> None:
        '''
        "session":[(k,v),
                    (k,v)]
                    }
        '''
        self.data = {}
        if path is not None:
            configp = ConfigParser()
            configp.read(path)
            for session in configp.sections():
                self.data[session] = configp.items(session)

    def load_ini(self, ini_path: str) -> dict:

        configp = ConfigParser()
        configp.read(ini_path)
        for session in configp.sections():
            self.data[session] = configp.items(session)



    def write_to_ini(ini_path: str, data: dict):
        '''
            "session":[(k,v),
                        (k,v)]
                        }
        '''
        conf = ConfigParser()
        for session, items in data:
            conf.add_section(session)
            for value in items:
                conf.set(session, *value)
        with open(ini_path,'w',encoding='utf-8') as f:
            conf.write(f)
