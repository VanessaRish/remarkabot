import logging

from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command

from db_setup import users_collection, phrases_collection
from chatgpt import get_generated_phrase


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
            {"user_id": user_info["user_id"]}, {"$set": {"status": "active"}}
        )
        await msg.reply("Я рада, что ты вернулась!")
    else:
        users_collection.insert_one(user_info)
        await msg.answer(f"Привет {msg.from_user.full_name}!")


@router.message()
async def message_handler(msg: Message):
    try:
        generated_answer = await get_generated_phrase()
        await msg.answer(f'{msg.from_user.first_name}, {generated_answer}')
    except Exception as e:
        logging.debug(f"Failed getting answer from chatgpt.")
        logging.error(e)
        await msg.answer(
            f'{msg.from_user.first_name}, {next(phrases_collection.aggregate([{"$sample": {"size": 1}}]), {}).get("phrase")}'
        )
