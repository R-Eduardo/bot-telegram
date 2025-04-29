Bot Telegram - FURIA Community Bot

Este é um bot para o Telegram feito para ajudar a divulgar:

A Loja Oficial da FURIA.

A Comunidade da FURIA no WhatsApp e Discord.

O Calendário de eventos futuros.

Inclui botões interativos e navegação amigável para o usuário.

Estrutura de Pastas

bot-telegram/
|
|├―― bot-telegram.py       # Arquivo principal que inicia o bot
|
|├―― handlers/             # Diretório de handlers (respostas dos botões)
|    ├―― button_handler.py  # Lida com os botões de navegação
|    └―― start_handler.py   # Lida com a mensagem de boas-vindas e menu inicial
|
└―― README.md              # Este arquivo de instruções

Como Instalar e Rodar

Clone o repositório:

git clone https://github.com/seu-usuario/bot-telegram.git
cd bot-telegram

Crie um ambiente virtual (opcional, mas recomendado):

python -m venv venv
source venv/bin/activate  # Linux / Mac
venv\Scripts\activate     # Windows

Instale as dependências:

pip install python-telegram-bot==20.0

Atenção: Este bot usa python-telegram-bot versão 20+, que é totalmente assíncrono (async/await).

Configure seu token do bot:

No arquivo bot-telegram.py, adicione o seu token do BotFather:

TOKEN = "SEU_TOKEN_AQUI"

Rode o bot:

python bot-telegram.py

Funcionalidades

Mensagem de boas-vindas personalizada: Saudando o usuário como "Furioso".

Menu Principal:

Loja: Botão para visitar o site oficial.

Comunidade: Botões diretos para o WhatsApp e o Discord.

Calendário: Lista de eventos com datas e horários.

Botão de Voltar: Sempre possível retornar ao menu principal.

Tecnologias Usadas

Python 3.11+

python-telegram-bot 20+

Autor

Desenvolvido por [CODE RED FALL]

Licença

Este projeto está sob a licença MIT - veja o arquivo LICENSE para detalhes.
