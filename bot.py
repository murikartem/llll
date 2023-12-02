import logging
import asyncio
from loader import *
import handler.start
import handler.get_task
import handler.add_task
import handler.del_task
from scripts.creat_db import creat_db



async def main():

    await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())



if __name__ == '__main__':
    creat_db()
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())