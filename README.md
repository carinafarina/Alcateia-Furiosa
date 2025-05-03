# AlcateiaCSBot

Este é um bot simples do Telegram que fornece informações sobre o time da "Alcateia CS". Os usuários podem interagir com o bot para obter o placar, as últimas notícias e informações sobre o próximo jogo através de comandos de barra.

## Funcionalidades

O bot oferece as seguintes funcionalidades através de comandos:

* **/Placar:** Exibe o placar atual da Alcateia CS.
* **/noticias:** Exibe as últimas notícias sobre o time.
* **/proximojogo:** Informa contra qual time será o próximo jogo.
* **Opções Iniciais:** Ao iniciar a conversa ou digitar "opções", o bot apresenta um menu com os comandos disponíveis.
* **Continuação:** Após fornecer uma informação, o bot pergunta se o usuário gostaria de saber mais alguma coisa (`s/n`). Ao digitar `s` ou `sim` (case-insensitive), o bot responde com uma mensagem de espera.
* **Opções Novamente:** Se o usuário digitar qualquer outra coisa que não seja um comando ou a confirmação de continuar, o bot sugere digitar "opções" para ver o menu novamente.

## Como Usar

1.  Certifique-se de ter uma conta no Telegram.
2.  Procure pelo bot `@AlcateiaCSBot` (ou o nome que você definir para o seu bot) no Telegram e inicie uma conversa.
3.  Você pode interagir com o bot das seguintes maneiras:
    * Digite qualquer mensagem para iniciar a interação e ver as opções.
    * Digite `/placar` para obter o placar.
    * Digite `/noticias` para ver as últimas notícias.
    * Digite `/proximojogo` para saber sobre o próximo jogo.
    * Digite `opções` para ver o menu de comandos novamente.
4.  Após receber uma informação, responda com `s` ou `sim` se quiser saber mais alguma coisa.

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
* **Interface Mais Rica:** Explore as funcionalidades da API do Telegram para enviar mensagens com formatação (Markdown ou HTML), botões inline ou de teclado personalizado para uma interação mais intuitiva. Os comandos de barra são um ótimo primeiro passo!
* **Tratamento de Erros:** Implemente tratamento de erros para lidar com falhas na comunicação com a API do Telegram ou outras situações inesperadas.
* **Melhor Tratamento de Entrada:** Considere usar bibliotecas para processamento de linguagem natural ou expressões regulares para entender melhor as entradas dos usuários.
* **Integração com Outras Fontes de Dados:** Busque automaticamente placares e notícias de fontes online para manter o bot sempre atualizado.

## Contribuição

Se você tiver ideias para melhorar este bot, sinta-se à vontade para abrir uma issue ou enviar um pull request.


