#(©)Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data
    if data == "about":
        await query.message.edit_text(
            text = (f"<b>⟦⟧ Hi There Vro!💫\n┏━━━━━━━❪❂❫━━━━━━━━\n◈ ᴄʀᴇᴀᴛᴏʀ: <a href=https://t.me/LUFFY1JOYBOY>ŦrαfͥαlͣgͫαrŁαw</a>\n◈ ꜰᴏᴜɴᴅᴇʀ ᴏꜰ : <a href=https://t.me/Anime_Madness>ᴀɴɪᴍᴇ ᴍᴀᴅɴᴇss</a>\n◈ ᴏɴɢᴏɪɴɢ ᴄʜᴀɴɴᴇʟ : <a href=https://t.me/Ongoing_Madness>ᴏɴɢᴏɪɴɢ ᴍᴀᴅɴᴇss</a>\n◈ Lɪʙʀᴀʀy : <a href=https://github.com/pyrogram>Pyʀᴏɢʀᴀᴍ</a>\n◈ ᴍʏ ꜱᴇʀᴠᴇʀ : <a href=https://dashboard.heroku.com>Heroku</a>\n◈ ᴅᴇᴠᴇʟᴏᴘᴇʀ : <a href=https://t.me/Anime_Madness>αηιмє мαяηєѕѕ</a>\n┗━━━━━━━❪❂❫━━━━━━━━</b>"),
            disable_web_page_preview = True,
            reply_markup = InlineKeyboardMarkup(
                [
                    [
                    InlineKeyboardButton("⚡️ Help", callback_data = "help"),
                    InlineKeyboardButton('🍁 ᴀɴɪᴍᴇ', url='https://t.me/Anime_Madness')
                    ]
                ]
            )
        )
    elif data == "help":
        commands = """
        » ʙᴏᴛ ᴄᴏᴍᴍᴀɴᴅs
        ❏ ᴄᴏᴍᴍᴀɴᴅs ғᴏʀ ʙᴏᴛ ᴀᴅᴍɪɴs
        » /start : sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴏʀ ɢᴇᴛ ᴘᴏsᴛs
        » /batch : ᴄʀᴇᴀᴛᴇ ʟɪɴᴋ ᴏғ ᴍᴜʟᴛɪᴘʟᴇ ᴍᴇssᴀɢᴇ
        » /genlink : ᴄʀᴇᴀᴛᴇ ʟɪɴᴋ ғᴏʀ ᴏɴᴇ ᴘᴏsᴛ
        » /addadmin : ᴛᴏ ᴀᴅᴅ ʙᴏᴛ ᴀᴅᴍɪɴ
        » /deladmin : ᴅᴇʟᴇᴛᴇ ᴀᴅᴍɪɴs
        » /fsub{number} : ᴀᴅᴅ ғᴏʀᴄᴇ sᴜʙ ᴄʜᴀɴɴᴇʟ 1
        » /users : ᴠɪᴇᴡ ʙᴏᴛ sᴛᴀᴛɪsᴛɪᴄs
        » /broadcast : ʙʀᴏᴀᴅᴄᴀsᴛ ᴍᴇssᴀɢᴇ
        » /channels : ᴛᴏ sᴇᴇ ғsᴜʙ ᴄʜᴀɴɴᴇʟs
        » /sudo : ᴛᴏ ᴄʜᴇᴄᴋ ᴀᴅᴍɪɴ ʟɪsᴛ
        » /s_img : ᴛᴏ ᴄʜᴀɴɢᴇ sᴛᴀʀᴛ ᴍᴇssᴀɢᴇ ɪᴍᴀɢᴇ
        » /f_img : ᴛᴏ ᴄʜᴀɴɢᴇ ғᴏʀᴄᴇ sᴜʙ ᴍᴇssᴀɢᴇ ɪᴍᴀɢᴇ
        » /auto_del : ᴛᴏ ᴇɴᴀʙʟᴇ ᴏʀ ᴅɪsᴀʙʟᴇ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛɪᴏɴ ᴏғ ᴍᴇssᴀɢᴇs
        » /del_timer : ᴛᴏ sᴇᴛ ᴀᴜᴛᴏ ᴅᴇʟᴇᴛᴇ ᴛɪᴍᴇʀ
        » /pbroadcast : ʙʀᴏᴀᴅᴄᴀsᴛ ᴀɴʏ ᴍᴇssᴀɢᴇs ᴛᴏ ʙᴏᴛ ᴜsᴇʀs ᴀɴᴅ ᴘɪɴ ᴍᴇ ᴍᴇssᴀɢᴇ ɪɴ ʀᴇsᴘᴇᴄᴛɪᴠᴇ ᴄʜᴀᴛs
        » /ping : ᴄʜᴇᴄᴋɪɴɢ ʏᴏᴜʀ ʙᴏᴛ ᴜᴘᴛɪᴍᴇ
        »» sɪᴍᴘʟʏ ᴄʟɪᴄᴋ ᴏɴ ʟɪɴᴋ ᴀɴᴅ sᴛᴀʀᴛ ᴛʜᴇ ʙᴏᴛ ᴊᴏɪɴ ᴀʟʟ ᴄʜᴀɴɴᴇʟs ᴀɴᴅ ᴛʀʏ ᴀɢᴀɪɴ ᴛʜᴀᴛs ɪᴛ.....!
        » ᴅᴇᴠᴇʟᴏᴘᴇᴅ ʙʏ <a href="http://t.me/LUFFY1JOYBOY">Ŧrαf‌αl‌g‌αrŁαw</a>
        """

        await query.message.edit_text(
            text=commands,
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("⚡️ ᴄʟᴏsᴇ", callback_data="close"),
                        InlineKeyboardButton('🍁 ᴀɴɪᴍᴇ', url='https://t.me/Anime_Madness')
                    ]
                ]
            )
        )

    elif data == "close":
        await query.message.delete()
        try:
            await query.message.reply_to_message.delete()
        except:
            pass
