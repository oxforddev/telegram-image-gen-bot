import os
import asyncio
from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import Command
from aiogram.types import FSInputFile
from dotenv import load_dotenv
import aiohttp

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
API_URL = os.getenv("API_URL", "https://api.mira.ai/generate")

bot = Bot(token=BOT_TOKEN)
router = Router()

@router.message(Command("start"))
async def cmd_start(message: types.Message):
    await message.answer("🎨 Welcome to Image Gen Bot!\n\nSend me a text prompt and I'll generate an image.\n\nExample: "a cat sitting on a beach at sunset"")

@router.message(Command("help"))
async def cmd_help(message: types.Message):
    await message.answer("📖 How to use:\n\n1. Send me any text description\n2. I'll generate an image for you\n\nCommands:\n/start - Start the bot\n/help - Show this help")

@router.message()
async def generate_image(message: types.Message):
    prompt = message.text
    if len(prompt) < 3:
        await message.answer("Please provide a longer description.")
        return
    
    processing_msg = await message.answer("🎨 Generating your image... This may take a moment.")
    
    try:
        async with aiohttp.ClientSession() as session:
            payload = {
                "prompt": prompt,
                "model": "gpt-image-2",
                "aspect_ratio": "2:3"
            }
            async with session.post(API_URL, json=payload) as resp:
                if resp.status == 200:
                    data = await resp.json()
                    image_url = data.get("media_url")
                    if image_url:
                        await bot.download_file_to_disk(
                            FSInputFile.from_url(image_url),
                            f"{message.from_user.id}.png"
                        )
                        photo = FSInputFile(f"{message.from_user.id}.png")
                        await message.answer_photo(photo, caption=f"✨ {prompt}")
                        os.remove(f"{message.from_user.id}.png")
                    else:
                        await message.answer("⚠️ Failed to generate image. Try again.")
                else:
                    await message.answer(f"⚠️ Error: {resp.status}")
    except Exception as e:
        await message.answer(f"⚠️ Error: {str(e)}")
    finally:
        await processing_msg.delete()

async def main():
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())