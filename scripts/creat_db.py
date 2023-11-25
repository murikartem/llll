from loader import cursor


def creat_db():
    try:
        cursor.execute('''CREATE TABLE task
                    (№ INTEGER PRIMARY KEY AUTOINCREMENT,
                    id INTEGER,
                    task_1 TEXT DEFAULT '-',
                    task_2 TEXT DEFAULT '-',
                    task_3 TEXT DEFAULT '-',
                    task_4 TEXT DEFAULT '-',
                    task_5 TEXT DEFAULT '-')
                    ''')
    except:
        pass
