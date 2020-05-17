import pandas as pd


def read_save():
    data = pd.read_csv('title.basics.tsv', sep='\t')
    data = data.head(100)
    data.to_csv('head_100.csv')


if __name__ == "__main__":
    read_save()
