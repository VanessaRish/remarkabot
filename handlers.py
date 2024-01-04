from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

import random
from phrases import PHRASES
from db_setup import users_collection


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    user_info = {
        "user_id": msg.from_user.id,
        "username": msg.from_user.full_name,
        "chat_id": msg.chat.id,
        "status": "active",
    }
    existing_user = users_collection.find_one({"user_id": user_info["user_id"]})

    if existing_user:
        users_collection.update_one(
            {"user_id": user_info["user_id"]},
            {"$set": {"status": "active"}}
        )
        await msg.reply("Я рада, что ты вернулась!")
    else:
        users_collection.insert_one(user_info)
        await msg.answer(f"Привет {msg.from_user.full_name}!")


@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"{msg.from_user.first_name}, {random.choice(PHRASES)}")
