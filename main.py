
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

BOT_TOKEN = "8072737679:AAF7v-BSeteWswqcewp35o9ECd_lu0UlwnA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Willkommen im Los Plugos Casino!\n\nMit /casino kannst du eine Runde drehen.\nMit /meinlink erhältst du deinen Empfehlungslink.\nMit /topref siehst du das Ranking der Werber.")

async def meinlink(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_id = update.effective_user.id
    link = f"https://t.me/{context.bot.username}?start={user_id}"
    await update.message.reply_text(f"Dein persönlicher Invite-Link:\n{link}")

async def topref(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Top-Werber werden bald angezeigt...")

async def casino(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("Demo: Du hast 1 Token eingesetzt. Viel Glück!")

def main():
    logging.basicConfig(level=logging.INFO)
    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("meinlink", meinlink))
    app.add_handler(CommandHandler("topref", topref))
    app.add_handler(CommandHandler("casino", casino))

    app.run_polling()

if __name__ == "__main__":
    main()
