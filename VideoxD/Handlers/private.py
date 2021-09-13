from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup, Message

from .. import HELP, bot

# basic commands


@bot.on_message(filters.command("alive"))
async def startxd(client, message):
    return await message.reply("Zinda Hu Vai")


@bot.on_message(filters.command(["start", "help"]) & filters.private)
async def start(client, message):
    sender_mention = message.from_user.mention
    return await message.reply(
        f"Hi! {sender_mention}, This is a video streaming bot.",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        text="Updates",
                        url="t.me/Zer0ByteOfficial",
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="Commands", callback_data="commands"
                    )
                ],
                [
                    InlineKeyboardButton(
                        text="Support",
                        url="t.me/Beluga_Chat",
                    )
                ],
            ]
        ),
    )


@bot.on_callback_query(filters.regex("commands"))
async def command_(_, cb):
    await bot.send_message(cb.message.chat.id, text=HELP)
    return await cb.message.delete()
