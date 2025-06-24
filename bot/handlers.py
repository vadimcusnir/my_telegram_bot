from telegram.ext import CommandHandler, MessageHandler, ContextTypes, filters
from .menu import keyboard

async def start(update, context: ContextTypes.DEFAULT_TYPE):
    print("✅ /start activat de:", update.effective_user.username)
    await update.message.reply_text(
        "Salut, sunt botul oficial Vadim Cușnir.\nAlege o opțiune:",
        reply_markup=keyboard
    )

async def despre(update, context):
    await update.message.reply_text("Sunt Vadim Cușnir – arhitect cognitiv, AI strategist și creator de sisteme educaționale.")

async def servicii(update, context):
    await update.message.reply_text("Servicii: Mentorate, cursuri, AI strategy. Vezi https://stan.store/vadimcusnir")

async def contact(update, context):
    await update.message.reply_text("Contact: vadim.kusnir@gmail.com sau @vadimcusnir")

def register_basic_handlers(app):
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("despre", despre))
    app.add_handler(CommandHandler("servicii", servicii))
    app.add_handler(CommandHandler("contact", contact))
    app.add_handler(MessageHandler(filters.Regex("🔍 Despre Vadim"), despre))
    app.add_handler(MessageHandler(filters.Regex("🎓 Servicii"), servicii))
    app.add_handler(MessageHandler(filters.Regex("📩 Contact"), contact))
