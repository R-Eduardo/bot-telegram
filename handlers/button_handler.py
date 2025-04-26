from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import CallbackQueryHandler, ContextTypes
from handlers.start_handler import voltar  # Importando a função de voltar

# Função que lida com os botões (Loja, Comunidade, Calendário)
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # Exibe as informações da Loja com botão para o site
    if query.data == 'loja':
        keyboard = [
            [InlineKeyboardButton("🛒 Visite a Loja", url="https://www.furia.gg/")],
            [InlineKeyboardButton("🔙 Voltar", callback_data='voltar')]  # Botão de Voltar
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "Confira nossos produtos oficiais na loja da FURIA!",
            reply_markup=reply_markup
        )
    
    # Exibe as informações da Comunidade com botões WhatsApp e Discord
    elif query.data == 'comunidade':
        keyboard = [
            [InlineKeyboardButton("💬 WhatsApp", url="https://chat.whatsapp.com/E9FUE3v9n6LAN8xKKP7DAR")],
            [InlineKeyboardButton("🎮 Discord", url="https://discord.gg/furia")],
            [InlineKeyboardButton("🔙 Voltar", callback_data='voltar')]  # Botão de Voltar
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "Entre na comunidade através dos links abaixo:",
            reply_markup=reply_markup
        )
    
    # Exibe as informações do Calendário
    elif query.data == 'calendario':
        eventos = [
            "📅 28/04/2025 - Rio de Janeiro - 18h",
            "📅 01/05/2025 - São Paulo - 20h",
        ]
        keyboard = [
            [InlineKeyboardButton("🔙 Voltar", callback_data='voltar')]  # Botão de Voltar
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)
        await query.edit_message_text(
            "Eventos confirmados:\n\n" + "\n".join(eventos),
            reply_markup=reply_markup
        )
    
    # Exibe o menu principal ao clicar no botão Voltar
    elif query.data == 'voltar':
        await voltar(update, context)

# Registrando o handler para os botões
button_handler_instance = CallbackQueryHandler(button_handler)