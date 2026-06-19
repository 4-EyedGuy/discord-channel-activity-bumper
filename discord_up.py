import asyncio
import discord
from discord.ext import tasks, commands

TOKEN = "[.env файл с токеном бота]"
CHANNEL_ID = "[.env файл с ID канала]"
INTERVAL = 10

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Бот {bot.user.name} успешно подключился к Discord!")
    bot.loop.create_task(bump_channel())

async def bump_channel():
    await bot.wait_until_ready()
    channel = bot.get_channel(CHANNEL_ID)
    
    if channel is None:
        print(f"Ошибка: Не удалось найти канал с ID {CHANNEL_ID}. Проверьте ID и права бота.")
        return

    while not bot.is_closed():
        try:
            msg = await channel.send("‌Опа, уведомление! :)")
            print(f"Сообщение отправлено в канал {channel.name}")
            
            await asyncio.sleep(1)
            
            await msg.delete()
            print("Сообщение успешно удалено.")
            
        except discord.Forbidden:
            print("Ошибка: У бота нет прав на отправку или удаление сообщений в этом канале!")
        except Exception as e:
            print(f"Произошла ошибка: {e}")
            
        print(f"Ожидание {INTERVAL} секунд...")
        await asyncio.sleep(INTERVAL)

bot.run(TOKEN)