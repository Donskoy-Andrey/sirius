from check_file import check_new_file
from time import sleep
from txt_file_processing import file_processing


def script(resave=False, new_stop=[]):
    # check_path = r'.\data\test_folder\2 (2).pdf'
    SAMPLE_PATH = r'.\data\test_folder\{}'
    check_path = SAMPLE_PATH.format(input('Enter file name. Example: file.pdf\n'))

    n_strings = 30
    n_search_strings = 200  # n-top terms, where we search variants
    n_add_strings = 5

    df = check_new_file(check_path, resave=resave, new_stop=new_stop)
    all_names = df.term.head(n_search_strings).values

    df['variants'] = \
        df.term.head(n_strings)\
            .apply(lambda x: ', '.join(
            [i for i in all_names
                if (x in i) and (x != i)][:n_add_strings-1]
            )
        )
    df.index = range(1, df.shape[0]+1)
    df.head(n_strings).to_excel(r'.\data\test_folder\result.xlsx', encoding='utf-8')
    print('===== Script finished! =====')
    sleep(30)


if __name__ == '__main__':
    new_stop = []
    new_stop_path = r'new_stop.txt'
    with open(new_stop_path, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            new_stop.extend([i for i in line.strip().split()])
    with open(new_stop_path, 'w', encoding='utf-8') as file:
        file.write(' '.join(new_stop))
    new_stop = [i for i in file_processing(new_stop_path).split()]
    script(resave=False, new_stop=new_stop)
