from aiogram import types
from aiogram.filters import Text
from loader import *
from aiogram.utils.keyboard import InlineKeyboardBuilder

@router.message(Text('удалить задачу'))
async def del_task(message: types.Message):
    id_user = message.chat.id
    cursor.execute('SELECT * FROM task WHERE id = (?)', [id_user])
    data = cursor.fetchall()[0]
    task_list = []
    for i in range(2, len(data)):
        if data[i] != '-':
            task_list.append(f'task_{i - 1}')
    if len(task_list) == 0:
        await message.answer('список задач пуст')
        return
    builder = InlineKeyboardBuilder()
    for task in task_list:
        cursor.execute(f'SELECT {task} FORM task WHERE id = (?)', [id_user])
        data = cursor.fetchall()[0][0]
        builder.add(
            types.InlineKeyboardButton(
                text=f'{data}',
                callback=f'del {task}')
            )
    builder.adjust(1)
    await message.answer(text=f'какую задачу удаляем?',
                         reply_markup=builder.as_markup(resize_keyboard=True))


@router.callback_query(Text(startswith='del '))
async def clear_task(callback: types.CallbackQuery):
    id_user = callback.message.chat.id
    task = callback.data.split()[-1]
    cursor.execute(f'UPDATE task SET {task} = (?) WHERE id = (?)', ['-', id_user])
    con.commit()
    await callback.message.answer('задача успешно удалена')