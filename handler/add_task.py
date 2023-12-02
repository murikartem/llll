from aiogram import types
from aiogram.filters import Text, Command
from loader import *
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from keys.key import kb_menu
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup


class Task_form(StatesGroup):
    task = State()


@router.message(Command('cancel'))
async def cancel(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer('действие отменено')


@router.message(Text('Добавить задачу'))
async def add_task(message: types.Message, state: FSMContext):
    id_user = message.chat.id
    cursor.execute('SELECT * FROM task WHERE id = (?)', [id_user])
    data = cursor.fetchall()[0]
    free_place = []
    for i in range(2, len(data)):
        if data[i] == '-':
            free_place.append(i)
    if len(free_place) == 0:
        await message.answer(text='нет свободного места для задачи')
        return
    await state.set_state(Task_form.task)
    await message.answer('напиши и отправи задачу. /cancel для отмены',
                         reply_markup=types.ReplyKeyboardRemove())


@router.message(Task_form.task)
async def save_task(message: types.Message, state: FSMContext):
    await state.update_data(task=message.text)
    id_user = message.chat.id
    data_task = await state.get_data()
    text_task = data_task['task']
    cursor.execute('SELECT * FROM task WHERE id = (?)', [id_user])
    data = cursor.fetchall()[0]
    for i in range(2, len(data)):
        if data[i] == '-':
            num_task ='task_' + str(i - 1)
            cursor.execute(f'UPDATE task SET {num_task} = (?) WHERE id = (?)', [text_task, id_user])
            con.commit()
            break
    await state.clear()
    builder = ReplyKeyboardBuilder()
    for button in kb_menu:
        builder.add(button)
    builder.adjust(1)
    await message.answer(text='задача успешно добавлена в список',
                         reply_markup=builder.as_markup(resize_keyboard=True))


