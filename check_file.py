from data_transfering import load_articles_data, save_articles_data
from transrom_pdf import extract_txt
from txt_file_processing import file_processing
from pathlib import Path
from sklearn.feature_extraction.text import TfidfVectorizer
from transrom_pdf import articles_names, mydict_names
import pandas as pd


def check_new_file(path, resave=False, new_stop=[]):
    new_articles_data = load_articles_data()
    current_file_path = Path(path)
    txt_file_path = extract_txt(current_file_path, folder='test_folder', return_value=True)
    new_file_txt = file_processing(txt_file_path, new_stop=new_stop)
    new_articles_data.append(new_file_txt)

    vectorizer = TfidfVectorizer(ngram_range=(1, 3), max_df=0.9)
    vectors = vectorizer.fit_transform(new_articles_data)

    if resave:
        """ save new article to data """
        number = len(articles_names) + 1
        articles_names.append(f'article ({number}).txt')
        save_articles_data(new_articles_data, mode='a')

        X = pd.DataFrame(vectors.toarray(),
                         columns=vectorizer.get_feature_names_out(),
                         index=articles_names)

        return X.iloc[-1, :].sort_values(ascending=False)

    X = pd.DataFrame(vectors.toarray(),
                     columns=vectorizer.get_feature_names_out(),
                     index=articles_names + [current_file_path.name])
    X = X.loc[current_file_path.name, :].sort_values(ascending=False)
    return X.to_frame().reset_index().rename({'index': 'term', f'{current_file_path.name}': 'value'}, axis=1)