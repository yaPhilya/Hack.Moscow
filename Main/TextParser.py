import pymorphy2
import json


class TextParser:

    def __init__(self, stored_names, stored_paths):
        self.morph = pymorphy2.MorphAnalyzer()
        self.stored_names = stored_names
        self.stored_paths = {key: value for key, value in zip(stored_names, stored_paths)}

    def parse(self, text):
        text = [[self.morph.parse(word)[0].normal_form for word in line.split(' ')]
                for line in text.split(',')]
        main_part = []
        for line in text:
            main_part.append({'noun': 'none', 'adj': []})
            for word in line:
                if len(word) == 0:
                    continue
                if self.morph.parse(word)[0].tag.POS == 'NOUN':
                    main_part[-1]['noun'] = word
                else:
                    main_part[-1]['adj'].append(word)
        return main_part

    def get_real_synonymous(self, text):
        '''return reduced extract with noun that compare to models'''
        extract = self.parse(text)
        data = []
        for line in extract:
            noun = line['noun']
            if noun not in self.stored_names:
                continue
            data.append({})
            data[-1]['model_path'] = self.stored_paths[noun]
            data[-1]['effects'] = []

        return json.dumps(data)