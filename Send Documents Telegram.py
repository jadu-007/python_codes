
import telegram
TOKEN = ' '  ##Enter your telegram bot token 
bot = telegram.Bot(TOKEN)
bot.sendDocument(chat_id="@stockmarketip", document=open(("generated/New1.jpg"), 'rb'))
