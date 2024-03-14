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
    cur.execute("SELECT * FROM accounts WHERE tg_id = ?", (user_id,))
    user = cur.fetchall()

    if not user:
        cur.execute("INSERT INTO accounts (tg_id, exchanges) VALUES (?, ?)", (user_id, "mexc"))
        db.commit()


async def add_exchanges(user_id, selected_exchange):
    user = cur.execute("SELECT * FROM accounts WHERE tg_id == {key}".format(key=user_id)).fetchone()
    if user:
        exchanges_index = 2
        current_exchanges = user[exchanges_index]

        if selected_exchange in current_exchanges.split(","):
            updated_exchanges = ",".join(ex for ex in current_exchanges.split(",") if ex != selected_exchange)
        else:
            updated_exchanges = current_exchanges + "," + selected_exchange if current_exchanges else selected_exchange

        cur.execute("UPDATE accounts SET exchanges = ? WHERE tg_id = ?", (updated_exchanges, user_id))
        db.commit()


async def check_exchange(user_id, exchange):
    user = cur.execute("SELECT * FROM accounts WHERE tg_id = ?", (user_id,)).fetchone()
    if user:
        exchanges = user[2]
        if exchange in exchanges.split(','):
            return True
    return False


def show_data_profile(user_id):
    result = cur.execute("SELECT tg_id FROM accounts WHERE tg_id == {key}".format(key=user_id))
    return result.fetchone()[0]
