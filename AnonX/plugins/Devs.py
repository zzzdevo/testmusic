import asyncio
from pyrogram import Client, filters
from strings.filters import command
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from AnonX import app, Telegram
import random
@app.on_message(
    command(["صورص","سورس","السورس","سورس حياه", "haya"])
)
async def huhh(client: Client, message: Message):
    await message.reply_photo(
        photo=f"https://telegra.ph/file/4c0e63af8a410d9a53fa0.jpg",
        caption=f"""
 [𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼](https://t.me/HL_BG)
 —————————————
 [𓏺𝙒𝙃𝙄𝙎𝙆𓏺𝙎𝞝𝙔](https://t.me/BP_BP)
 
 [𓏺𝙂𝙍𝙊𝙐𝙋 𝙃𝞝𝙇𝙋](https://t.me/HL_BG)
  
 [⍟𓏺𝙒𝞝𝙇𝘾𝙊𝙈𝙀 𝙏𝙊 𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼](https://t.me/HL_BG)
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "𝙒𝙃𝙄𝙎𝙆𓏺𝙎𝞝𝙔♡", url=f"https://t.me/bP_bP"), 
                ],[
                    InlineKeyboardButton(
                        "𓏺𝙎𝙊𝙐𝙍𝘾𝞝 𝙃𝘼𝙔𝘼", url=f"t.me/HL_BG"),
                ],

            ]

        ),

    )

@app.on_message(command([f"غنيلي", "غني", "غ", "{BOT_USERNAME} غنيلي"]))
async def ihd(client: Client, message: Message):
    rl = random.randint(8,20)
    url = f"https://t.me/iV_P_Nl/{rl}"
    await client.send_voice(message.chat.id,url,caption="`🔥 ¦ تـم اختيـار الاغـنـية لـك`",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )
    
@app.on_message(command(["صورة","صور"]))
async def ihd(client: Client, message: Message):
    rs = random.randint(39,148)
    url = f"https://t.me/GTTUTY/{rs}"
    await client.send_photo(message.chat.id,url,caption="`💕 ¦ تـم اختيـار الصوره لـك`",
    reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        message.from_user.first_name, url=f"https://t.me/{message.from_user.username}")
                ],
            ]
        )
    )

                        


