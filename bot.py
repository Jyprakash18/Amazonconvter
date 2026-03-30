import re
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
import config

# Regex to find Amazon links
AMAZON_REGEX = r"(https?://www.amazon.[a-z.]+/dp/[A-Z0-9]+|https?://amzn.to/[a-zA-Z0-9]+)"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("👋 Welcome! Send me an Amazon link and I'll convert it to your affiliate link.")

async def convert_link(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    # Simplified logic: Replace or append the tag
    if "amazon" in text or "amzn.to" in text:
        # In a real bot, you'd fetch the user's saved tag from a database here
        user_tag = "sumandealsx-21" 
        
        # Logic to clean and append tag
        new_link = f"{text.split('?')[0]}?tag={user_tag}"
        await update.message.reply_text(f"✅ Your converted link:\n{new_link}")

if __name__ == '__main__':
    app = ApplicationBuilder().token(config.BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), convert_link))
    app.run_polling()
