from check_file import check_new_file

check_path = r'.\data\test_folder\2 (2).pdf'

n_strings = 30
n_search_strings = 200  # n-top terms, where we search variants
n_add_strings = 5

df = check_new_file(check_path, resave=False)
all_names = df.term.head(n_search_strings).values

df['variants'] = \
    df.term.head(n_strings)\
        .apply(lambda x: ', '.join(
        [i for i in all_names
            if (x in i) and (x != i)][:n_add_strings-1]
        )
    )

df.head(n_strings).to_csv(r'.\result.csv')
