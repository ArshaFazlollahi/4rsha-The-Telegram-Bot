import Token as token
from telegram.ext import *
import Chat as chat

def start_command(update, context):
    update.message.reply_text("Hi! Welcome to the gateway for all of Arsha's links. You can use /content for a list of commands, or you can chat with me 😁")

def content_command(update, context):
    update.message.reply_text("Here's a list of Arsha's links:\n- /github\n- /youtube\n- /linkedin\n- /instagram\n- /discord")

def github_command(update, context):
    update.message.reply_text("Here's a link to Arsha's GitHub:\nhttps://github.com/ArshaFazlollahi")

def youtube_command(update, context):
    update.message.reply_text("Here's a link to Arsha's YouTube channel:\nhttps://www.youtube.com/NutralYT")

def linkedin_command(update, context):
    update.message.reply_text("Here's a link to Arsha's LinkedIn:https://www.linkedin.com/in/arsha-fazlollahi-3a81a4239/")

def instagram_command(update, context):
    update.message.reply_text("Here's a link to Arsha's Instagram:\nhttps://www.instagram.com/yt_neutral/")

def discord_command(update, context):
    update.message.reply_text("Arsha's discord username is: Neutral#1173")

def handle_message(update, context):
    text = str(update.message.text).lower()
    reply = chat.sample_responses(text)
    update.message.reply_text(reply)

def error(update, context):
    print("error")

def bot():
    updater = Updater(token.key, use_context = True)

    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start_command))
    dispatcher.add_handler(CommandHandler("content", content_command))
    dispatcher.add_handler(CommandHandler("github", github_command))
    dispatcher.add_handler(CommandHandler("youtube", youtube_command))
    dispatcher.add_handler(CommandHandler("linkedin", linkedin_command))
    dispatcher.add_handler(CommandHandler("instagram", instagram_command))
    dispatcher.add_handler(CommandHandler("discord", discord_command))

    dispatcher.add_handler(MessageHandler(Filters.text, handle_message))

    dispatcher.add_error_handler(error)

    updater.start_polling()
    updater.idle()

bot()