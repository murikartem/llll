from aiogram import types
from aiogram.filters import Text
from loader import *

@router.message(Text('Список задач'))
async def get_task(message: types.Message):
    id_user = message.chat.id
    cursor.execute('SELECT * FROM task WHERE id = (?)', [id_user])
    data = cursor.fetchall()[0]
    text = ''
    num = 1
    for i in range(2, len(data)):
        text += f'{num}) {data[i]}.\n'
        num += 1
    if text:
        await message.answer(text=f'Ваш список задач:\n{text}')
    else:
        await message.answer(text=f'Ваш список задач пуст')