from pathlib import Path
from pdfminer.high_level import extract_text

ORIGINAL_PATH = r'data/{}'
DICT_PATH = ORIGINAL_PATH.format(r'original_data/mydict')
ARTICLE_PATH = ORIGINAL_PATH.format(r'original_data/articles')

mydict = Path(DICT_PATH)
articles = Path(ARTICLE_PATH)

mydict_files = sorted(list(mydict.rglob('*.pdf')))
articles_files = sorted(list(articles.rglob('*.pdf')))

articles_names = [i.name for i in articles_files]
mydict_names = [i.name for i in mydict_files]


def extract_txt(path: Path, folder: str, return_value: bool = False) -> str:
    file = extract_text(path)
    result_path = ORIGINAL_PATH.format(f'{folder}\{path.name}'[:-3]+'txt')
    with open(result_path, 'w', encoding='utf-8') as f:
        f.write(file)
    if return_value:
        return result_path


if __name__ == '__main__':
    for path in mydict_files:
        print(path)
        extract_txt(path, folder='mydict_txt')

    for path in articles_files:
        print(path)
        file_number = int(str(path)[23:-5])
        extract_txt(path, folder='articles_txt')


