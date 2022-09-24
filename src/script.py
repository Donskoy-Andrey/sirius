import pandas as pd
from src.data_processing.OCR.OCR import get_ocr_file
from src.data_processing.data_transfering import load_articles_data, save_articles_data
from src.data_processing.transrom_pdf import extract_txt
from src.data_processing.txt_file_processing import file_processing
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from src.data_processing.transrom_pdf import articles_names, mydict_names

n_strings = 30
n_search_strings = 200  # n-top terms, where we search variants
n_add_strings = 5

SAMPLE_PATH = r'data/test_folder/{}'
PATH_TO_SAVE = r'result/result.xlsx'
NEW_STOP_PATH = r'data/new_stop.txt'


def start_ocr(check_path: str) -> None:
    print('File unreadable. Use OCR...')
    ocr_path = check_path[:-4] + '.txt'
    text = get_ocr_file(check_path)
    with open(ocr_path, 'w', encoding='utf-8') as file:
        file.write(text)

    df = check_new_file(ocr_path, extension='txt')
    all_names = df.term.head(n_search_strings).values

    df['variants'] = \
        df.term.head(n_strings) \
            .apply(lambda x: ', '.join(
            [i for i in all_names
             if (x in i) and (x != i)][:n_add_strings - 1]
        )
                   )
    df.index = range(1, df.shape[0] + 1)
    df.head(n_strings).to_excel(PATH_TO_SAVE, encoding='utf-8')


def check_new_file(path: str, file_save: bool, extension: str = 'pdf') -> pd.DataFrame():
    new_articles_data = load_articles_data()
    current_file_path = Path(path)
    if extension != 'txt':
        txt_file_path = extract_txt(current_file_path, folder='test_folder', return_value=True)
    else:
        txt_file_path = path
    new_file_txt = file_processing(txt_file_path)
    new_articles_data.append(new_file_txt)

    vectorizer = TfidfVectorizer(ngram_range=(1, 3), max_df=0.9)
    vectors = vectorizer.fit_transform(new_articles_data)

    if file_save:
        """ save new article to data """
        number = len(articles_names) + 1
        articles_names.append(f'article ({number}).txt')
        save_articles_data(new_articles_data, mode='a')

        X = pd.DataFrame(vectors.toarray(),
                         columns=vectorizer.get_feature_names_out(),
                         index=articles_names)

        return X.iloc[-1, :].sort_values(ascending=False)

    xlsx_file = pd.DataFrame(vectors.toarray(),
                             columns=vectorizer.get_feature_names_out(),
                             index=articles_names + [current_file_path.name])
    xlsx_file = xlsx_file.loc[current_file_path.name, :].sort_values(ascending=False)
    return xlsx_file.to_frame().reset_index().rename({'index': 'term', f'{current_file_path.name}': 'value'}, axis=1)


def script(file_save: bool) -> None:
    check_path = SAMPLE_PATH.format(input('Enter file name from test_folder. Example: file.pdf\n'))

    df = check_new_file(check_path, file_save=file_save)
    all_names = df.term.head(n_search_strings).values

    df['variants'] = \
        df.term.head(n_strings)\
            .apply(lambda x: ', '.join(
            [i for i in all_names
                if (x in i) and (x != i)][:n_add_strings-1]
            )
        )
    df.index = range(1, df.shape[0] + 1)
    df.head(n_strings).to_excel(PATH_TO_SAVE, encoding='utf-8')

    if df.loc[1, 'value'] < 0.05:
        start_ocr(check_path)

    print('===== Script finished! =====')


if __name__ == '__main__':
    script(file_save=False)
