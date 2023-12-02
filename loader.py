from aiogram import Bot, Dispatcher, Router
import sqlite3

token = '6652328511:AAFqdxLmmkP49gEMXO0HtXy_nRYdLngMcuc'
router = Router()
dp = Dispatcher()
dp.include_router(router)
bot = Bot(token, parse_mode='HTML')
con = sqlite3.connect('data/data.db')
cursor = con.cursor()

from apscheduler.schedulers.asyncio import AsyncIOScheduler
scheduler = AsyncIOScheduler(timezone='Europe/Moscow')