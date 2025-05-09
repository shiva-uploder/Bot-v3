# Copyright (c) 2025 Gagan : https://github.com/devgaganin.  
# Licensed under the GNU General Public License v3.0.  
# See LICENSE file in the repository root for full license text.

from shared_client import client as bot_client, app
from telethon import events
from datetime import timedelta
from config import OWNER_ID
from utils.func import add_premium_user, is_private_chat
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from config import OWNER_ID
import base64 as spy
from utils.func import a1, a2, a3, a4, a5, a7, a8, a9, a10, a11
from plugins.start import subscribe


@app.on_message(filters.command("start"))
async def start_handler(client, message):
    subscription_status = await subscribe(client, message)
    if subscription_status == 1:
        return

    # Decoded values
    b1 = "save_restricted_content_bots"
    b2 = 796
    b3 = "get_messages"
    b4 = "reply_photo"
    b6 = "Hi 👋 Welcome, Wanna intro...? \n\n✳️ I can save posts from channels or groups where forwarding is off. I can download videos/audio from YT, INSTA, ... social platforms\n✳️ Simply send the post link of a public channel. For private channels, do /login. Send /help to know more."
    b7 = "Join Channel"
    b8 = "Get Premium"
    b9 = "https://t.me/team_spy_pro"
    b10 = "https://t.me/kingofpatal"

    # Fetch messages
    tm = await getattr(app, b3)(b1, b2)

    # Extract photo and file_id
    pb = getattr(tm, "photo")
    fd = getattr(pb, "file_id")

    # Keyboard with buttons
    keyboard = InlineKeyboardMarkup([
        [InlineKeyboardButton(b7, url=b9)],
        [InlineKeyboardButton(b8, url=b10)]
    ])

    # Send the photo with caption and keyboard
    await getattr(message, b4)(
        fd,
        caption=b6,
        reply_markup=keyboard
    )