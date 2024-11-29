from bot import Bot
from pyrogram.types import Message
from pyrogram import filters, Client
from config import BOT_STATS_TEXT, USER_REPLY_TEXT
from datetime import datetime
from helper_func import get_readable_time
from dataconfig import ADMINS
from datetime import datetime

@Bot.on_message(filters.command('stats') & filters.user(ADMINS))
async def stats(bot: Bot, message: Message):
    now = datetime.now()
    delta = now - bot.uptime
    time = get_readable_time(delta.seconds)
    await message.reply(BOT_STATS_TEXT.format(uptime=time))


@Bot.on_message(filters.private & filters.incoming)
async def useless(_,message: Message):
    if USER_REPLY_TEXT:
        await message.reply(USER_REPLY_TEXT)



@Bot.on_message(filters.command("ping"))
def ping_command(client, message):
    start_time = datetime.now()
    sent_message = message.reply_text("Pinging...")
    end_time = datetime.now()
    ping_time = (end_time - start_time).microseconds / 1000  # Convert to milliseconds
    sent_message.edit_text(f"Pong! 🏓\nResponse time: `{ping_time} ms`")
