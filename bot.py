#(©)Codexbotz
import pyrogram.utils

pyrogram.utils.MIN_CHANNEL_ID = -1009147483647

from aiohttp import web
from plugins import web_server

import pyromod.listen
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime

import pyrogram.utils

pyrogram.utils.MIN_CHANNEL_ID = -1009147483647

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, CHANNEL_ID, PORT
from dataconfig import FORCE_SUB_CHANNEL_1, FORCE_SUB_CHANNEL_2, FORCE_SUB_CHANNEL_3, FORCE_SUB_CHANNEL_4

class Bot(Client):
    

    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={
                "root": "plugins"
            },
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        if FORCE_SUB_CHANNEL_1:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL_1)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL_1)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL_1)).invite_link
                self.FSUBLINK1 = link
            except Exception as e:
                error_message = (
                    f"Bot encountered an issue:\n{e}\n"
                    "Bot can't export the invite link from the Force Sub Channel! "
                    "Please double-check the FORCE_SUB_CHANNEL_1 value and make sure "
                    "the bot has Admin permission with 'Invite Users via Link' enabled.\n"
                    f"Current Force Sub Channel Value: {FORCE_SUB_CHANNEL_1}"
                )
                self.LOGGER(__name__).warning(e)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL_1 value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL_1}")
                self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/weebs_support for support")
                await self.send_message(chat_id=7195990500, text=error_message)
        if FORCE_SUB_CHANNEL_2:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL_2)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL_2)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL_2)).invite_link
                self.FSUBLINK2 = link
            except Exception as e:
                error_message = (
                    f"Bot encountered an issue:\n{e}\n"
                    "Bot can't export the invite link from the Force Sub Channel! "
                    "Please double-check the FORCE_SUB_CHANNEL_1 value and make sure "
                    "the bot has Admin permission with 'Invite Users via Link' enabled.\n"
                    f"Current Force Sub Channel Value: {FORCE_SUB_CHANNEL_1}"
                )
                self.LOGGER(__name__).warning(e)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL_2 value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL_2}")
                self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/weebs_support for support")
                await self.send_message(chat_id=7195990500, text=error_message)
        if FORCE_SUB_CHANNEL_3:
            try:
                # Generate a join request link for FORCE_SUB_CHANNEL_3
                invite_link = await self.create_chat_invite_link(FORCE_SUB_CHANNEL_3, creates_join_request=True)
                self.FSUBLINK3 = invite_link.invite_link  # Store the join request link
            except Exception as e:
                error_message = (
                    f"Bot encountered an issue:\n{e}\n"
                    "Bot can't export the invite link from the Force Sub Channel! "
                    "Please double-check the FORCE_SUB_CHANNEL_1 value and make sure "
                    "the bot has Admin permission with 'Invite Users via Link' enabled.\n"
                    f"Current Force Sub Channel Value: {FORCE_SUB_CHANNEL_1}"
                )
                
                self.LOGGER(__name__).warning(e)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL_3 value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL_3}")
                self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/weebs_support for support")
                await self.send_message(chat_id=7195990500, text=error_message)
        if FORCE_SUB_CHANNEL_4:
            try:
                # Generate a join request link for FORCE_SUB_CHANNEL_3
                invite_link = await self.create_chat_invite_link(FORCE_SUB_CHANNEL_4, creates_join_request=True)
                self.FSUBLINK4 = invite_link.invite_link  # Store the join request link
            except Exception as e:
                error_message = (
                    f"Bot encountered an issue:\n{e}\n"
                    "Bot can't export the invite link from the Force Sub Channel! "
                    "Please double-check the FORCE_SUB_CHANNEL_1 value and make sure "
                    "the bot has Admin permission with 'Invite Users via Link' enabled.\n"
                    f"Current Force Sub Channel Value: {FORCE_SUB_CHANNEL_1}"
                )
                self.LOGGER(__name__).warning(e)
                self.LOGGER(__name__).warning("Bot can't Export Invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"Please Double check the FORCE_SUB_CHANNEL_4 value and Make sure Bot is Admin in channel with Invite Users via Link Permission, Current Force Sub Channel Value: {FORCE_SUB_CHANNEL_4}")
                self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/weebs_support for support")
                await self.send_message(chat_id=7195990500, text=error_message)
        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id = db_channel.id, text = "Test Message")
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(e)
            self.LOGGER(__name__).warning(f"Make Sure bot is Admin in DB Channel, and Double check the CHANNEL_ID Value, Current Value {CHANNEL_ID}")
            self.LOGGER(__name__).info("\nBot Stopped. Join https://t.me/weebs_support for support")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"Bot Running..!\n\nCreated by \nhttps://t.me/codeflix_bots")
        self.LOGGER(__name__).info(f"""       


  ___ ___  ___  ___ ___ _    _____  _____  ___ _____ ___ 
 / __/ _ \|   \| __| __| |  |_ _\ \/ / _ )/ _ \_   _/ __|
| (_| (_) | |) | _|| _|| |__ | | >  <| _ \ (_) || | \__ \
 \___\___/|___/|___|_| |____|___/_/\_\___/\___/ |_| |___/
                                                         
 
                                          """)
        self.username = usr_bot_me.username
        #web-response
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("Bot stopped.")
