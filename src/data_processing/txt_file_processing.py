import pandas as pd
import pymorphy2
import re

STOPWORDS_PATH = r'data/stopwords.txt'
punctuation = r'!\"#$%&\'()*+,./:;<=>?@[\]^_`{|}~'
morph = pymorphy2.MorphAnalyzer()

with open(STOPWORDS_PATH, 'r', encoding='utf-8') as file:
    stop_words = [string.strip() for string in file.readlines()]


def file_processing(path: str) -> str:
    with open(path, 'r', encoding='utf8') as f:
        text = [line.strip() for line in f.readlines()]
        text = ' '.join(text).replace('- ', '')
        text = re.sub('[^а-яё\sА-ЯЁ-]', '', text)

        current_stop_words = set(stop_words)
        pymorphy_results = list(map(lambda x: morph.parse(x), text.split()))
        final = ' '.join([
            res[0].normal_form for res in pymorphy_results
            if (res[0].normal_form not in current_stop_words) and
               (len(res[0].normal_form) > 2)
        ])
        return final
