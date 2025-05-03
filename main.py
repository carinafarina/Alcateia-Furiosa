import requests
import json
import os


class AlcateiaCSBot: 
  def __init__(self):
    token = '7710789467:AAGTDpqoetCT8X_hKat-QH-nH8o6-FRQDdA'
    self.url_base = f'https://api.telegram.org/bot{token}/'
   # iniciar bot
  def Iniciar(self):
    update_id = None
    while True:
      atualizacao = self.obter_mensagens(update_id)
      mensagens = atualizacao['result']
      if mensagens:
        for mensagem in mensagens:
          update_id = mensagem['update_id']
          chat_id = mensagem['message']['from']['id']
          eh_primeira_mensagem = mensagem['message']['message_id'] == 1
          resposta = self.criar_resposta(mensagem, eh_primeira_mensagem)
          self.responder(resposta, chat_id)
    # obter mensagens
  def obter_mensagens(self, update_id):
    link_requisicao = f'{self.url_base}getUpdates?timeout=100'
    if update_id:
      link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
    resultado = requests.get(link_requisicao)
    return json.loads(resultado.content)
    # criar resposta
  def criar_resposta(self, mensagem, eh_primeira_mensagem):
    mensagem = mensagem['message']['text']
    if eh_primeira_mensagem == True or mensagem.lower() == "opções":
      return f'''Olá, bem vindo ao Alcateia! Digite o que você deseja saber sobre o Alcateia CS.{os.linesep}/Placar{os.linesep}/noticias{os.linesep}/proximojogo'''
    if mensagem == '/Placar':
      return f'''O placar da Alcateia CS é 2x1{os.linesep}Gostaria de saber mais alguma coisa?(s/n)'''
    if mensagem == '/noticias':
      return f'''Novo técnico será o do Furioso.{os.linesep}Gostaria de saber mais alguma coisa?(s/n)'''
    if mensagem == '/proximojogo':
      return f'''O proximo jogo é contra o time Furias{os.linesep}Gostaria de saber mais alguma coisa?(s/n)'''
    
    if mensagem.lower() in ('s','sim'):
      return 'aguarde um momento...'
    else: 
      return 'Gostaria de acessar as outras opções? Digite "opções"'
  
  
  # responder
  def responder(self, resposta, chat_id):
    #enviar mensagem
    link_de_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
    requests.get(link_de_envio)

bot = AlcateiaCSBot()
bot.Iniciar()