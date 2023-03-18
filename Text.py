


import discord
from discord.ext import commands
import json
import pickle
import os
from discord.ui import *
from discord import *


wrong_words = ["!experience", "!stats"]

intents = discord.Intents.default()
intents.members = True
intents.message_content = True

client = discord.Client(intents=intents)


@client.event
async def on_message(mess):
    if mess.content.startswith("!hello"):
        await mess.channel.send('Hello, World!')

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')
    # DiscordComponents(client)


# Путь к файлу с данными о пользователях
DATA_FILE = 'users.pickle'

# Если файл с данными существует, загружаем его
if os.path.exists(DATA_FILE):
    with open(DATA_FILE, 'rb') as f:
        users = pickle.load(f)
# Если файл не существует, создаем пустой словарь
else:
    users = {}

# Сохраняем данные о пользователях в файл
def save_users():
    with open(DATA_FILE, 'wb') as f:
        pickle.dump(users, f)

# Функция добавления опыта пользователю
def add_experience(user, exp):
    if not user.id in users:
        users[user.id] = {"name": str(user), "experience": exp, "total_experience": exp}
    else:
        users[user.id]["experience"] += exp
        users[user.id]["total_experience"] += exp

    save_users()

# Функция вывода уровня пользователя
def get_level(user):
    if not user.id in users:
        return 0

    exp = users[user.id]["experience"]
    level = 0
    while exp >= 100:
        level += 1
        exp -= 100
    users[user.id]["experience"] = exp

    save_users()

    return level

# Обработчик события "сообщение получено"
@client.event
async def on_message(message):
    if not message.author.bot:
        # Проверяем, не содержит ли сообщение запрещенных слов
        contains_wrong_word = any(word in message.content.lower() for word in wrong_words)
        if not contains_wrong_word:
            add_experience(message.author, 10)

    await client.process_commands(message)

def get_experience(user):
    if not user.id in users:
        return 0

    return users[user.id]["experience"]



# Функция вывода всего опыта пользователя
def get_total_experience(user):
    if not user.id in users:
        return 0

    total_experience = users[user.id]["total_experience"]

    return total_experience


@client.event
async def on_message(message):
    if message.content.startswith('!stats'):
        author = message.author
        level = get_level(author)
        experience = get_experience(author)
        total_exp = get_total_experience(author)
        await message.channel.send(f"""{author.mention} - текущий уровень: {level},
текущее количество опыта: {experience}, 
общее количество опыта: {total_exp}""")
