from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart, Command
from app.keyboards import (main, first_group, second_group,)
from .schedule import (FIRST_GROUP_MN, FIRST_GROUP_TU,
                        FIRST_GROUP_WD, FIRST_GROUP_TH,
                        FIRST_GROUP_FR, FIRST_GROUP_SD,
                        SECOND_GROUP_MN, SECOND_GROUP_TU,
                        SECOND_GROUP_WD, SECOND_GROUP_TH,
                        SECOND_GROUP_FR, SECOND_GROUP_SD,)

router = Router()


@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Приветствую, первокурсник! Выбери группу:",
                         reply_markup=main)

@router.message(F.text == "1 группа")
async def cmd_start(message: Message):
    await message.answer("Распеса 1 группы",
                         reply_markup=first_group)

@router.message(F.text == "Понедельник_1")
async def cmd_start(message: Message):
    await message.answer(FIRST_GROUP_MN,
                         reply_markup=main)

@router.message(F.text == "Вторник_1")
async def cmd_start(message: Message):
    await message.answer(FIRST_GROUP_TU,
                         reply_markup=main)

@router.message(F.text == "Среда_1")
async def cmd_start(message: Message):
    await message.answer(FIRST_GROUP_TH,
                         reply_markup=main)

@router.message(F.text == "Четверг_1")
async def cmd_start(message: Message):
    await message.answer(FIRST_GROUP_WD,
                         reply_markup=main)

@router.message(F.text == "Пятница_1")
async def cmd_start(message: Message):
    await message.answer(FIRST_GROUP_FR,
                         reply_markup=main)

@router.message(F.text == "Суббота_1")
async def cmd_start(message: Message):
    await message.answer(FIRST_GROUP_SD,
                         reply_markup=main)

@router.message(F.text == "2 группа")
async def cmd_start(message: Message):
    await message.answer("Распеса 2 группы",
                         reply_markup=second_group)

@router.message(F.text == "Понедельник_2")
async def cmd_start(message: Message):
    await message.answer(SECOND_GROUP_MN,
                         reply_markup=main)

@router.message(F.text == "Вторник_2")
async def cmd_start(message: Message):
    await message.answer(SECOND_GROUP_TU,
                         reply_markup=main)

@router.message(F.text == "Среда_2")
async def cmd_start(message: Message):
    await message.answer(SECOND_GROUP_WD,
                         reply_markup=main)

@router.message(F.text == "Четверг_2")
async def cmd_start(message: Message):
    await message.answer(SECOND_GROUP_TH,
                         reply_markup=main)

@router.message(F.text == "Пятница_2")
async def cmd_start(message: Message):
    await message.answer(SECOND_GROUP_FR,
                         reply_markup=main)

@router.message(F.text == "Суббота_2")
async def cmd_start(message: Message):
    await message.answer(SECOND_GROUP_SD,
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
