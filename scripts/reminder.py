from loader import Bot, cursor


async def reminder(bot: Bot):
    cursor.execute('SELECT * FROM task')
    data = cursor.fetchall()
    text_message = 'vctavai erjan'
    for user in data:
        for i in range(2, len(user)):
            if user[i] != '-':
                user_id = user[1]