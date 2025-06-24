import os
from dotenv import load_dotenv
from telegram.ext import ApplicationBuilder
from handlers import register_basic_handlers
from abonare import register_abonare_handler

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")
WEBHOOK_URL = os.getenv("WEBHOOK_URL")
MAKE_WEBHOOK_URL = os.getenv("MAKE_WEBHOOK_URL")

app = ApplicationBuilder().token(TOKEN).build()
print("👂 Listening on:", WEBHOOK_URL)

register_basic_handlers(app)
register_abonare_handler(app, MAKE_WEBHOOK_URL)

if __name__ == "__main__":
    import asyncio

    async def main():
        print("🚀 Pornit în mod WEBHOOK")
        await app.initialize()
        await app.start()
        await app.updater.start_webhook(
            listen="0.0.0.0",
            port=8000,
            url_path="/webhook",
            webhook_url=WEBHOOK_URL
        )
        print("🌐 Webhook activ. Railway blocat.")
        await asyncio.Event().wait()

    asyncio.run(main())
