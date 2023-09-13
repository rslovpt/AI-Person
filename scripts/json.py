from decouple import config
import json

class json_ex:
    def __init__(self, var):
        self.var = var
        
    def load_var(self):
        return json.load(config(self.var))

    def load_file(self):
        f = open(self.var)
        data = json.load(f)
        f.close()
        return data
