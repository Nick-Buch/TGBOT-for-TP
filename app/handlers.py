from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from app.keyboards import main


router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Приветствую, первокурсник! Выбери группу:",
                         reply_markup=main)

@router.message(F.text == "1 группа")
async def cmd_start(message: Message):
    await message.answer("Распеса 1 группы",
                         reply_markup=main)

@router.message(F.text == "2 группа")
async def cmd_start(message: Message):
    await message.answer("Распеса 2 группы",
                         reply_markup=main)

@router.message(F.text == "3 группа")
async def cmd_start(message: Message):
    await message.answer("Распеса 3 группы",
                         reply_markup=main)

@router.message(F.text == "4 группа")
async def cmd_start(message: Message):
    await message.answer("Распеса 4 группы",
                         reply_markup=main)

@router.message(F.text == "5 группа")
async def cmd_start(message: Message):
    await message.answer("Распеса 5 группы",
                         reply_markup=main)

@router.message(F.text == "6 группа")
async def cmd_start(message: Message):
    await message.answer("Распеса 6 группы",
                         reply_markup=main)

@router.message(F.text == "7 группа")
async def cmd_start(message: Message):
    await message.answer("Распеса 7 группы",
                         reply_markup=main)

@router.message(F.text == "8 группа")
async def cmd_start(message: Message):
    await message.answer("Распеса 8 группы",
                         reply_markup=main)

@router.message(F.text == "9 группа")
async def cmd_start(message: Message):
    await message.answer("Распеса 9 группы",
                         reply_markup=main)
