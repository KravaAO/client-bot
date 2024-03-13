import sqlite3 as sq


async def db_start():
    global db, cur
    db = sq.connect('accounts_bd')
    cur = db.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS accounts("
                "id INTEGER PRIMARY KEY AUTOINCREMENT, "
                "tg_id INTEGER,"
                "exchanges TEXT)"
                )
    db.commit()


async def cmd_start_db(user_id):
    user = cur.execute("SELECT * FROM accounts WHERE tg_id == {key}".format(key=user_id)).fetchone()
    if not user:
        cur.execute("INSERT INTO accounts (tg_id) VALUES ({key})".format(key=user_id))
        db.commit()


def show_data_profile(user_id):
    result = cur.execute("SELECT tg_id FROM accounts WHERE tg_id == {key}".format(key=user_id))
    return result.fetchone()[0]
