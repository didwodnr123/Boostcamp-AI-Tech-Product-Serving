from pandas import read_csv

DATA_PATH = 'AI-it/korean-hate-speech'
DATA_FILES = {
    "train_comments": "train_hate.csv",
    "train_titles": "train_news_title.txt"
}


def retrieve_comments(keyword: str) -> list:
    """Retrieve comments correspond to keyword from unlabeled comments.txt

    Parameters
    ----------
    keyword : name or something you want to find

    Returns
    -------
    list of unlabeled comments contain keyword
    """
    result = []
    df_comments = read_csv('data/unlabeled/unlabeled_comments.txt', header=None, encoding='utf-8')
    for comment in df_comments[0]:
        if type(comment) != str:
            continue
        elif keyword in comment:
            result.append(comment)
        elif keyword[1:] in comment:
            result.append(comment)

    return result


if __name__ == '__main__':
    retrieve_comments('전현무')
