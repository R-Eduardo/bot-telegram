from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import CommandHandler, ContextTypes

# Função de boas-vindas (menu inicial)
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🛍 Loja", callback_data='loja')],
        [InlineKeyboardButton("👥 Comunidade", callback_data='comunidade')],
        [InlineKeyboardButton("🗓 Calendário", callback_data='calendario')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.message.reply_text(
        "Bem-vindo Furioso(a), quer ficar por dentro do que está rolando na Furia?",
        reply_markup=reply_markup
    )

# Função para exibir a tela inicial (ao pressionar o botão "Voltar")
async def voltar(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton("🛍 Loja", callback_data='loja')],
        [InlineKeyboardButton("👥 Comunidade", callback_data='comunidade')],
        [InlineKeyboardButton("🗓 Calendário", callback_data='calendario')],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    await update.callback_query.edit_message_text(
        "Bem-vindo Furioso(a), quer ficar por dentro do que está rolando na Furia?",
        reply_markup=reply_markup
    )

# Registrando o handler para o comando /start
start_handler = CommandHandler('start', start)