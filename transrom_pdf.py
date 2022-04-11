from pathlib import Path
from pdfminer.high_level import extract_text

mydict = Path(r'.\data\mydict')
articles = Path(r'.\data\articles')

mydict_files = sorted(list(mydict.rglob('*.pdf')))
articles_files = sorted(list(articles.rglob('*.pdf')))

articles_names = [i.name for i in articles_files]
mydict_names = [i.name for i in mydict_files]


def extract_txt(path, folder, return_value=False):
    file = extract_text(path)
    result_path = f'.\data\{folder}\{path.name}'[:-3]+'txt'
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
        # if file_number == 545:
        #     continue
        extract_txt(path, folder='articles_txt')


