from aiogram import types
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from loader import *
from keys.key import kb_menu


@router.message(Command('start'))
async def start(message: types.Message):
    id_user = message.chat.id
    cursor.execute('SELECT * FROM task WHERE id = (?)', [id_user])
    data = cursor.fetchall()
    if len(data) == 0:
        cursor.execute(f'INSERT INTO task (id) VALUES (?)', [id_user])
        con.commit()
    builder = ReplyKeyboardBuilder
    for button in kb_menu:
        builder.add(button)
    builder.adjust(1)
    await message.answer(text='Что дальше?',
                         reply_markup=builder.as_markup(resize_keyboard=True))