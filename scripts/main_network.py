from scripts.json import json_ex
from difflib import SequenceMatcher
import os, importlib
class network:
    def __init__(self):
        self.attitude = []

        self.character_avoidance = ['.', '/', '[', ']', '"', "'", '!', '?', ',']

    def network_addition(self, word, context):
        return

    def generate_response(self, context_table):
        return

    def attain_analyze_files(self):
        files = {}
        for path_distribute in os.listdir(os.path.join("scripts","network_analyze")):
            for c_file in os.listdir(os.path.join("scripts","network_analyze", path_distribute)):
                if c_file[c_file.find('.'):] == ".py":
                    module = importlib.import_module('scripts.network_analyze.'+str(path_distribute)+'.'+str(c_file[:c_file.find('.')]), package=None)
                    files[path_distribute] = module.NET
                else:
                    pass
        return files

    def analyze(self, k_words):
        anlz_files = self.attain_analyze_files()
        response = []
        for i in k_words:
            if k_words.index(i)+1 != len(k_words):
                context = i[1]
                if 'STARTUP' in context:
                    if 'GREETING' in context:
                        print(context) # WORKING HERE

        return response

    def format_language(self, k_words):
        returned_list = []
        cancelled_list = []
        json_mem = json_ex('mem\set\dict.json').load_file()

        for y in k_words:
            for _,v in json_mem.items():
                for i in v:
                    if v.index(i) == 0:
                        for z in i:
                            similarity_ratio = SequenceMatcher(None, y.lower(), z.lower()).ratio()
                            if similarity_ratio > 0.8:
                                data_list = [z.lower(), v[1]]
                                returned_list.append(data_list)
                            else:
                                if y.lower() not in cancelled_list:
                                    cancelled_list.append(y.lower())
        returned_list.append(cancelled_list)
        return returned_list

    def input_recieved(self, text):
        k_words = []
        current_k_word = ""

        for i in text:
            if i != " ":
                if i in self.character_avoidance:
                    pass
                else:
                    if text.index(i) == len(text)-1 or text[text.index(i)+1] in self.character_avoidance:
                        current_k_word += i

                        k_words.append(current_k_word)
                        current_k_word = ""
                    else:
                        current_k_word += i
            else:
                k_words.append(current_k_word)
                current_k_word = ""

        if current_k_word != "":
            k_words.append(current_k_word)
            current_k_word = ""

        established_words = self.format_language(k_words)
        self.analyze(established_words)
