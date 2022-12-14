import asyncio
from pyrogram import filters
from pyrogram.types import Message
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram.errors import MessageNotModified
from NIXA.main import Test, bot as Client
from config import START_PIC, UPDATES_CHANNEL, GROUP_SUPPORT, BOT_USERNAME


ALIVE_PIC = START_PIC
HOME_TEXT = """
ððð¥ð¥ð¨ â¥ï¸ {} 
ð'ð¦ ð ðð®ð¬ð¢ð ðð¨ð­
ðð¥ðð² ðð®ðð¢ð¨ ðð§ð ðð¢ððð¨ ðð¢ð­ð¡ð¨ð®ð­ ððð ð¬  
ðð§ð£ð¨ð² ðð¨ð®ð« ð¦ð®ð¬ð¢ð 24*7
"""

HELP_TEXT = """
ð'ð¦ ð ðð®ð¬ð¢ð ðð¨ð­
ðð¥ðð² ðð®ðð¢ð¨ ðð§ð ðð¢ððð¨ ðð¢ð­ð¡ð¨ð®ð­ ððð ð¬  
ðð§ð£ð¨ð² ðð¨ð®ð« ð¦ð®ð¬ð¢ð 24*7
â¥ï¸ **sá´á´á´á´ É¢á´Éªá´á´** :

\u2022 sá´á´Êá´ á´ á´ á´Éªá´á´ á´Êá´á´ ÉªÉ´ Êá´á´Ê É¢Êá´á´á´.
\u2022 á´á´á´ Êá´á´ IN á´Êá´á´ á´¡Éªá´Ê á´á´á´ÉªÉ´ ÊÉªÉ¢Êá´s.
\u2022 á´á´É´á´ sá´á´á´á´ á´Êá´á´á´ss Êá´á´á´ á´á´á´á´á´É´á´s Êá´Êá´á´¡.
"""



USER_TEXT = """
â¥ï¸ **á´sá´Ês á´á´á´á´á´É´á´s** :

\u2022 /play <Query> á´á´ á´Êá´Ê á´ sá´É´É¢.
\u2022 /vplay <Query> á´á´ á´Êá´Ê á´ Éªá´á´á´.
\u2022 /stream <Live Url> á´á´ á´Êá´Ê ÊÉªá´ á´ sá´Êá´á´á´s\n /song á´á´ á´á´á´¡É´Êá´á´á´ á´ á´á´á´Éªá´ ÒÉªÊá´ ÒÊá´á´ Êá´á´á´á´Êá´. \n /video á´á´ á´á´á´¡É´Êá´á´á´ á´ Éªá´á´á´ ÒÊá´á´ Êá´á´á´á´Êá´\n /lyric á´á´ ÒÉªÉ´á´ ÊÊÊÉªá´s.
"""

SPAM_TEXT = """
Â» **sá´á´á´ Êá´Êá´ á´á´á´ÉªÉ´s á´É´ÊÊ** :

\u2022 /spam <Count> á´á´xá´ á´á´ sá´á´á´ Êá´á´Ê á´á´ssá´É¢á´.
\u2022 /fspam <Count> á´á´xá´ Òá´Ê sá´á´á´á´ÉªÉ´É¢.
\u2022 /delayspam <Count> á´á´xá´ Òá´Ê sá´á´á´á´ÉªÉ´É¢.
"""

RAID_TEXT = """
Â» **Êá´Éªá´ á´á´á´á´á´É´á´s sá´á´á´ á´É´ÊÊ** :

\u2022 /vcraid <chatid> - É¢á´á´ á´ á´ á´Êá´á´ Éªá´ á´Êsá´ á´sá´ÊÉ´á´á´á´ á´á´ á´ á´Éªá´á´ Êá´Éªá´.
\u2022 /vraid <chatid + Êá´á´ÊÊ á´á´ á´ Éªá´á´á´ ÒÉªÊá´> - á´á´ Êá´Éªá´ á´ Éªá´á´á´.
\u2022 /raidpause - á´á´ á´á´á´sá´ Êá´Éªá´.
\u2022 /raidresume á´á´ Êá´sá´á´á´ Êá´Éªá´.
\u2022 /raidend <chatid> á´á´ á´É´á´ á´á´á´Éªá´/á´ Éªá´á´á´ Êá´Éªá´.
"""

ADMIN = """
Â» **á´á´á´ÉªÉ´s á´á´á´á´á´É´á´s** :

\u2022 /userbotjoin á´á´ ÉªÉ´á´ Éªá´á´ á´ssÉªsá´á´É´á´ á´á´ Êá´á´Ê á´Êá´á´.
\u2022 /end á´á´ á´É´á´ sá´Êá´á´á´ÉªÉ´É¢.
\u2022 /pause á´á´ á´á´á´sá´ sá´Êá´á´á´.
\u2022 /resume á´á´ Êá´sá´á´á´ sá´Êá´á´á´.
\u2022 /volume á´á´ sá´á´ á´ á´Êá´á´á´.
\u2022 /skip á´á´ sá´Éªá´ á´Êá´á´á´s.
"""

@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.data=="help":
        buttons = [
            [
                InlineKeyboardButton("ð® á´á´¡É´á´Ê", url="https://te.legra.ph/ã¤-09-04"),
                InlineKeyboardButton("ð¨ï¸ á´ê±á´Êê±", callback_data="users"),
            ],
            
            [
                InlineKeyboardButton("Â» Êá´á´á´ Â«", callback_data="home"),
                InlineKeyboardButton("â¢ á´Êá´ê±á´â¢ ", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HELP_TEXT,
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="home":
        get_me = await client.get_me()
        USERNAME = get_me.username
        buttons = [
            [
                InlineKeyboardButton("â á´á´á´ á´á´ á´á´ Êá´á´Ê á´Êá´á´ â", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ],
            [
                InlineKeyboardButton("ð¥ sá´á´á´á´Êá´", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton("ð¢ á´Êá´É´É´á´Ê", url=f"https://t.me/{UPDATES_CHANNEL}"),
            ],
            
            [
                InlineKeyboardButton("ð Êá´Êá´ & á´á´á´á´á´É´á´ê±", callback_data="help"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                HOME_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="users":
        buttons = [
            [
                InlineKeyboardButton("Â» Êá´á´á´ Â«", callback_data="help"),
                InlineKeyboardButton("â¢ á´Êá´ê±á´ â¢", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                USER_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="admins":
        buttons = [
            [
                InlineKeyboardButton("Â» Êá´á´á´ Â«", callback_data="help"),
                InlineKeyboardButton("â¢ á´Êá´ê±á´ â¢", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(ADMIN, reply_markup=reply_markup)
        except MessageNotModified:
            pass

    elif query.data=="raid":
        buttons = [
            [
                InlineKeyboardButton("Â» Êá´á´á´ Â«", callback_data="help"),
                InlineKeyboardButton("â¢ á´Êá´ê±á´ â¢", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                RAID_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="spam":
        buttons = [
            [
                InlineKeyboardButton("Â» Êá´á´á´ Â«", callback_data="help"),
                InlineKeyboardButton("â¢ á´Êá´ê±á´ â¢", callback_data="close"),
            ]
            ]
        reply_markup = InlineKeyboardMarkup(buttons)
        try:
            await query.edit_message_text(
                SPAM_TEXT.format(query.from_user.first_name, query.from_user.id),
                reply_markup=reply_markup
            )
        except MessageNotModified:
            pass

    elif query.data=="close":
        try:
            await query.message.delete()
            await query.message.reply_to_message.delete()
        except:
            pass


@Client.on_message(filters.command(["start"]) & filters.private)
async def start(client: Client, message: Message):
    get_me = await client.get_me()
    USERNAME = get_me.username
    buttons =  [
            [
                InlineKeyboardButton("â á´á´á´ á´á´ á´á´ Êá´á´Ê á´Êá´á´ â", url=f"https://t.me/{BOT_USERNAME}?startgroup=true"),
            ],
            [
                InlineKeyboardButton("ð¥ sá´á´á´á´Êá´", url=f"https://t.me/{GROUP_SUPPORT}"),
                InlineKeyboardButton("ð¢ á´Êá´É´É´á´Ê", url=f"https://t.me/{UPDATES_CHANNEL}"),
            ],
            
            [
                InlineKeyboardButton("ð Êá´Êá´ & á´á´á´á´á´É´á´ê±", callback_data="help"),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo=f"{ALIVE_PIC}", caption=HOME_TEXT.format(message.from_user.first_name, message.from_user.id), reply_markup=reply_markup)

@Client.on_message(filters.command(["help"]) & filters.private)
async def help(client: Client, message: Message):
    get_me = await client.get_me()
    self.username = get_me.username
    buttons =  [
            [
                InlineKeyboardButton("ð® á´á´¡É´á´Ê", url="https://te.legra.ph/ã¤-09-04"),
                InlineKeyboardButton("ð¨ï¸ á´ê±á´Êê±", callback_data="users"),
            ],
            
            [
                InlineKeyboardButton("Â» Êá´á´á´ Â«", callback_data="home"),
                InlineKeyboardButton("â¢ á´Êá´ê±á´â¢ ", callback_data="close"),
            ]
            ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply_photo(photo=f"{ALIVE_PIC}", caption=f"{HELP_TEXT}", reply_markup=reply_markup)
