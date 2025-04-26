from telegram.ext import Application
from handlers.start_handler import start_handler  # Importando o handler
from handlers.button_handler import button_handler_instance  # Importando o handler para os botões
from config.config import TOKEN

# Inicialização do bot
if __name__ == '__main__':
    app = Application.builder().token(TOKEN).build()

    # Registrando os handlers
    app.add_handler(start_handler)  # Passando o handler para o comando /start
    app.add_handler(button_handler_instance)  # Passando o handler para os botões

    # Iniciando o bot
    print("Bot iniciado...")
    app.run_polling()