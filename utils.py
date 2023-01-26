import sqlite3


def get_all(query: str):
    """

    :param query:
    :return:
    """

    with sqlite3.connect("netflix.bd") as conn:
        conn.row_factory = sqlite3.Row
        result = []

        for item in conn.execute(query).fetchall():
            s = dict(item)
            result.append(s)

        return result

def get_one(query: str):
    """

    :param query:
    :return:
    """

    with sqlite3.connect("netflix.bd") as conn:
        conn.row_factory = sqlite3.Row
        res = conn.execute(query).fetchone()

        if res is None:
            return None

        else:
            return dict(res)

