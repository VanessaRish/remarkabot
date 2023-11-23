from aiogram import Router
from aiogram.types import Message
from aiogram.filters import Command


router = Router()


@router.message(Command("start"))
async def start_handler(msg: Message):
    await msg.answer(f"Привет {msg.from_user.full_name}!")


@router.message()
async def message_handler(msg: Message):
    await msg.answer(f"{msg.from_user.first_name}, ты сегодня молодец!")
