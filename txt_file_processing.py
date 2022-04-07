import nltk
from nltk.corpus import stopwords
import pymorphy2
import re
import string


nltk.download('wordnet')
nltk.download('stopwords')

stopWords = stopwords.words('russian')
wnl = nltk.WordNetLemmatizer()

our_stopWords = [
    'рис', 'табл', 'схема', 'таб', 'издание', 'сборник', 'журнал', 'университет',
    'статья', 'рисунок', 'таблица', 'сайт', 'почта', 'телефон', 'тел', 'адрес'
    ]

stopWords = set(stopWords + our_stopWords)
morph = pymorphy2.MorphAnalyzer()
string.punctuation = string.punctuation.replace('-','')


def file_processing(path, new_stop=[]):
    with open(path, 'r', encoding='utf8') as f:
        text = [line.strip().lower() for line in f.readlines()]
        text = ' '.join(text) \
            .replace('- ', '')
        text = re.sub('[^а-яё -]', '', text)
        text = re.sub(f'[{string.punctuation}]', '', text)
        text = re.sub(r'\s{2,}', ' ', text)

        current_stopWords = set(list(stopWords) + new_stop)

        pymorphy_results = list(map(lambda x: morph.parse(x), text.split()))
        final = ' '.join([
            res[0].normal_form for res in pymorphy_results
            if (res[0].normal_form not in current_stopWords) and
               (len(
                   res[0].normal_form
               ) > 3)
        ])
        return final