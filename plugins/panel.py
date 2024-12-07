from pyrogram import Client, filters
from database.database import set_variable, get_variable
from dataconfig import ADMINS
from config import OWNER
import os, sys, time, asyncio, logging, datetime
import pyrogram.utils

pyrogram.utils.MIN_CHANNEL_ID = -1009147483647

# Helper function to check if a user is an admin
def is_admin(user_id):
    return user_id in ADMINS

from database.database import get_variable

# Function to retrieve configuration values with a fallback to environment variables
def get_config_value(key: str, default: str):
    return get_variable(key, os.environ.get(key, default))
    

@Client.on_message(filters.command("admin") & filters.user(OWNER))
async def update_admins(client, message):
    try:
        action, user_id = message.text.split()[1], int(message.text.split()[2])
        admins_list = get_variable("ADMINS", "0").split()
        
        if action.lower() == "add":
            if str(user_id) not in admins_list:
                admins_list.append(str(user_id))
                response = f"User `{user_id}` has been added to ADMINS."
            else:
                response = f"User `{user_id}` is already an admin."
        elif action.lower() == "remove":
            if str(user_id) in admins_list:
                admins_list.remove(str(user_id))
                response = f"User `{user_id}` has been removed from ADMINS."
            else:
                response = f"User `{user_id}` is not in the ADMINS list."
        else:
            response = "Invalid action. Use `add` or `remove`."

        # Update ADMINS in the database
        set_variable("ADMINS", " ".join(admins_list))
        updated_admins = get_variable("ADMINS", "0")
        await message.reply_text(f"{response}\n\nCurrent ADMINS: `{updated_admins}`")

    except (IndexError, ValueError):
        await message.reply_text("Usage: `/admin <add|remove> <user_id>`")
    except Exception as e:
        await message.reply_text(f"Error: {str(e)}")


@Client.on_message(filters.command("Fsub1") & filters.user(ADMINS))
async def update_fsub1(client, message):
    try:
        new_value = int(message.text.split()[1])
        set_variable("FORCE_SUB_CHANNEL_1", new_value)
        await message.reply_text(f"FORCE_SUB_CHANNEL_1 updated to: `{new_value}`")
    except (IndexError, ValueError):
        await message.reply_text("Usage: `/Fsub1 <new_channel_id>`")


@Client.on_message(filters.command("Fsub2") & filters.user(ADMINS))
async def update_fsub2(client, message):
    try:
        new_value = int(message.text.split()[1])
        set_variable("FORCE_SUB_CHANNEL_2", new_value)
        await message.reply_text(f"FORCE_SUB_CHANNEL_2 updated to: `{new_value}`")
    except (IndexError, ValueError):
        await message.reply_text("Usage: `/Fsub2 <new_channel_id>`")


@Client.on_message(filters.command("Fsub3") & filters.user(ADMINS))
async def update_fsub3(client, message):
    try:
        new_value = int(message.text.split()[1])
        set_variable("FORCE_SUB_CHANNEL_3", new_value)
        await message.reply_text(f"FORCE_SUB_CHANNEL_3 updated to: `{new_value}`")
    except (IndexError, ValueError):
        await message.reply_text("Usage: `/Fsub3 <new_channel_id>`")


@Client.on_message(filters.command("Fsub4") & filters.user(ADMINS))
async def update_fsub4(client, message):
    try:
        new_value = int(message.text.split()[1])
        set_variable("FORCE_SUB_CHANNEL_4", new_value)
        await message.reply_text(f"FORCE_SUB_CHANNEL_4 updated to: `{new_value}`")
    except (IndexError, ValueError):
        await message.reply_text("Usage: `/Fsub4 <new_channel_id>`")

is_restarting = False
@Client.on_message(filters.private & filters.command("restart") & filters.user(ADMINS))
async def restart_bot(b, m):
    global is_restarting
    if not is_restarting:
        is_restarting = True
        await m.reply_text("**Restarting.....**")

        # Gracefully stop the bot's event loop
        b.stop()
        time.sleep(2)  # Adjust the delay duration based on your bot's shutdown time

        # Restart the bot process
        os.execl(sys.executable, sys.executable, *sys.argv)

is_closing = False

@Client.on_message(filters.private & filters.command("close") & filters.user(ADMINS))
async def close_bot(b, m):
    global is_closing
    if not is_closing:
        is_closing = True
        await m.reply_text("**Closing the bot...**")

        # Gracefully stop the bot's event loop
        b.stop()





@Client.on_message(filters.command("del_timer") & filters.user(OWNER))
async def update_del_timer(client, message):
    try:
        new_value = int(message.text.split()[1])
        set_variable("DELETE_TIME", new_value)
        await message.reply_text(f"DELETE_TIME updated to: `{new_value}` seconds")
    except (IndexError, ValueError):
        await message.reply_text("Usage: `/del_timer <new_delete_time_in_seconds>`")

@Client.on_message(filters.command("auto_del") & filters.user(OWNER))
async def update_auto_del(client, message):
    try:
        input_value = message.text.split()[1].strip().lower()
        if input_value in ["true", "1", "yes"]:
            new_value = True
        elif input_value in ["false", "0", "no"]:
            new_value = False
        else:
            raise ValueError("Invalid input")
        
        set_variable("AUTO_DELETE", new_value)
        await message.reply_text(f"AUTO_DELETE updated to: `{new_value}`")
    except (IndexError, ValueError):
        await message.reply_text("Usage: `/auto_del <true/false>`")



@Client.on_message(filters.command("sudo") & filters.user(OWNER))
async def get_admin_list(client, message):
    admins = get_variable("ADMINS", "[]")  # Default to an empty list if ADMINS is not set
    await message.reply_text(f"Current Admins: ``{admins}``")


@Client.on_message(filters.command("f_img") & filters.user(OWNER))
async def update_fsub_img(client, message):
    try:
        new_value = message.text.split(maxsplit=1)[1]
        set_variable("FSUB_IMG", new_value)
        await message.reply_text(f"FSUB_IMG updated to: `{new_value}`")
    except IndexError:
        await message.reply_text("Usage: `/f_img <new_fsub_img_url>`")

@Client.on_message(filters.command("s_img") & filters.user(OWNER))
async def update_start_img(client, message):
    try:
        new_value = message.text.split(maxsplit=1)[1]
        set_variable("START_IMG", new_value)
        await message.reply_text(f"START_IMG updated to: `{new_value}`")
    except IndexError:
        await message.reply_text("Usage: `/s_img <new_start_img_url>`")
