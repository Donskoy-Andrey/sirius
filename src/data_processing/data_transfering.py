from src.data_processing.txt_file_processing import file_processing
from pathlib import Path


mydict = Path(r'data/mydict_txt')
articles = Path(r'data/articles_txt')
mydict_files = sorted(list(mydict.rglob('*.txt')))
articles_files = sorted(list(articles.rglob('*.txt')))

CLEAR_TEXT = 'data/processed_data/clear_text.txt'


def save_articles_data(articles_data: list, mode='w') -> None:
    if mode == 'w':
        with open(CLEAR_TEXT, 'w', encoding='utf-8') as file:
            file.write('\n'.join(articles_data))
    elif mode == 'a':
        with open(CLEAR_TEXT, 'a', encoding='utf-8') as file:
            file.write('\n' + articles_data[-1])


def articles_data_txt() -> None:
    """ save data as processed txt """
    articles_data = []
    for path in articles_files:
        print(path)
        final = file_processing(path)
        articles_data.append(final)
    save_articles_data(articles_data)


def load_articles_data() -> list[str]:
    """ get all data_txt """
    with open(CLEAR_TEXT, 'r') as file:
        articles_data = file.readlines()
    return articles_data


if __name__ == '__main__':
    articles_data_txt()

