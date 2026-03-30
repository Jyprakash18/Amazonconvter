import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

# 1. Logging setup (taki hume errors dikhein)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# 2. Token fetch karna (Render Environment Variables se)
TOKEN = os.environ.get("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    welcome_text = (
        "👋 *Welcome to Amazon Converter Bot!*\n\n"
        "🔹 *Status:* Active ✅\n"
        "🔹 *Tag:* `Not Set`\n\n"
        "Link bhejiye, main convert kar dunga!"
    )
    await update.message.reply_text(welcome_text, parse_mode='Markdown')

async def converter(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if "amazon" in text or "amzn.to" in text:
        # Example conversion (Simple logic)
        tag = "sumandealsx-21"
        new_link = f"{text.split('?')[0]}?tag={tag}"
        await update.message.reply_text(f"✅ *Converted:* \n{new_link}", parse_mode='Markdown')

if __name__ == '__main__':
    # Token check loop
    if not TOKEN:
        print("❌ ERROR: BOT_TOKEN is missing in Render Settings!")
    else:
        app = ApplicationBuilder().token(TOKEN).build()
        
        app.add_handler(CommandHandler("start", start))
        app.add_handler(MessageHandler(filters.TEXT & (~filters.COMMAND), converter))
        
        print("🚀 Bot is starting...")
        app.run_polling()
