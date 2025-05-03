# AlcateiaCSBot

Este é um bot simples do Telegram que fornece informações sobre o time de "Alcateia CS". Os usuários podem interagir com o bot para obter o placar, as últimas notícias e informações sobre o próximo jogo.

## Funcionalidades

O bot oferece as seguintes funcionalidades:

* **Opções Iniciais:** Ao iniciar a conversa ou digitar "opções", o bot apresenta um menu com as seguintes opções:
    * `1` - Placar
    * `2` - Notícias
    * `3` - Próximo Jogo
* **Placar:** Ao digitar `1`, o bot informa o placar atual da Alcateia CS.
* **Notícias:** Ao digitar `2`, o bot exibe as últimas notícias sobre o time.
* **Próximo Jogo:** Ao digitar `3`, o bot informa contra qual time será o próximo jogo.
* **Continuação:** Após fornecer uma informação, o bot pergunta se o usuário gostaria de saber mais alguma coisa (`s/n`). Ao digitar `s` ou `sim` (case-insensitive), o bot responde com uma mensagem de espera.
* **Opções Novamente:** Se o usuário digitar qualquer outra coisa que não seja uma das opções ou a confirmação de continuar, o bot sugere digitar "opções" para ver o menu novamente.

## Como Usar

1.  Certifique-se de ter uma conta no Telegram.
2.  Procure pelo bot `@AlcateiaCSBot` (ou o nome que você definir para o seu bot) no Telegram e inicie uma conversa.
3.  Envie qualquer mensagem para iniciar a interação. O bot responderá com as opções disponíveis.
4.  Digite o número correspondente à informação que você deseja obter (1, 2 ou 3).
5.  Siga as instruções do bot para continuar interagindo ou voltar ao menu principal.

## Pré-requisitos

Para executar este bot, você precisará ter o seguinte instalado:

* **Python 3:** A linguagem de programação utilizada para desenvolver o bot.
* **Biblioteca `requests`:** Utilizada para fazer requisições HTTP para a API do Telegram. Você pode instalá-la usando o pip:
    ```bash
    pip install requests
    ```
* **Biblioteca `json`:** Utilizada para trabalhar com dados JSON recebidos da API do Telegram (geralmente já incluída na instalação padrão do Python).
* **Variável de Ambiente (Opcional, mas recomendado para segurança):** Considere armazenar o token do seu bot do Telegram como uma variável de ambiente em vez de diretamente no código.

## Configuração

1.  **Obtenha um Token do Bot do Telegram:**
    * Converse com o BotFather no Telegram (@BotFather).
    * Siga as instruções para criar um novo bot.
    * O BotFather fornecerá um token de acesso HTTP API. **Mantenha este token em segurança!**
2.  **Atualize o Código (se necessário):**
    * No arquivo `AlcateiaCSBot.py`, certifique-se de que a variável `token` na linha do `__init__` esteja configurada com o seu token do bot.
    * **Recomendação:** Para maior segurança, você pode ler o token de uma variável de ambiente:
        ```python
        import os
        # ... dentro da classe AlcateiaCSBot no método __init__
        token = os.environ.get('TELEGRAM_BOT_TOKEN')
        self.url_base = f'[https://api.telegram.org/bot](https://api.telegram.org/bot){token}/'
        ```
        E então, defina a variável de ambiente `TELEGRAM_BOT_TOKEN` no seu sistema ou plataforma de hospedagem.

## Execução

Para executar o bot localmente:

1.  Salve o código em um arquivo chamado `AlcateiaCSBot.py`.
2.  Abra um terminal ou prompt de comando.
3.  Navegue até o diretório onde você salvou o arquivo.
4.  Execute o seguinte comando:
    ```bash
    python AlcateiaCSBot.py
    ```
    O bot começará a rodar e aguardará por mensagens no Telegram.

## Próximos Passos e Melhorias

Este é um bot básico com funcionalidades limitadas. Aqui estão algumas ideias para melhorias futuras:

* **Persistência de Dados:** Atualmente, as informações (placar, notícias, próximo jogo) estão codificadas no bot. Considere usar um banco de dados ou um arquivo externo para armazenar e atualizar esses dados dinamicamente.
* **Interface Mais Rica:** Explore as funcionalidades da API do Telegram para enviar mensagens com formatação, botões inline ou de teclado personalizado para uma interação mais intuitiva.
* **Tratamento de Erros:** Implemente tratamento de erros para lidar com falhas na comunicação com a API do Telegram ou outras situações inesperadas.
* **Comandos Específicos:** Em vez de depender apenas de números, utilize comandos específicos (por exemplo, `/placar`, `/noticias`, `/proximojogo`) para acionar as funcionalidades do bot.
* **Integração com Outras Fontes de Dados:** Busque automaticamente placares e notícias de fontes online para manter o bot sempre atualizado.

## Contribuição

Se você tiver ideias para melhorar este bot, sinta-se à vontade para abrir uma issue ou enviar um pull request.

## Licença

[Aqui você pode adicionar informações sobre a licença do seu projeto, por exemplo, MIT License.]
