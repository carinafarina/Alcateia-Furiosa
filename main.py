import requests
import time
import json
import os

  
class AlcateiaCSBot:
  def __init__(self):
    token = '7710789467:AAGTDpqoetCT8X_hKat-QH-nH8o6-FRQDdA'
    self.url_base = f'http://api.telegram.org/bot{token}/'
    time.sleep(10)
               
  # Iniciar o bot

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
          resposta = self.criar_resposta(mensagem,eh_primeira_mensagem)
          self.responder(resposta, chat_id)

# Obter mensagens

  def obter_mensagens(self, update_id):
    link_requisicao = f'{self.url_base}getUpdates?timeout=100'
    if update_id:
      link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
    resultado = requests.get(link_requisicao)
    return json.loads(resultado.content)

# Cria resposta

  def criar_resposta(self,mensagem,eh_primeira_mensagem):
    mensagem = mensagem['message']['text']
    
    if eh_primeira_mensagem == True or mensagem.lower() == 'menu':
      return f'''Olá, bem vindo ao Alcateia Furiosa. 
Digite sobre o que você quer saber:{os.linesep}placar{os.linesep}noticias{os.linesep}proximojogo'''
      
    if mensagem == 'placar':
      return f'''O placar do jogo é 2x1{os.linesep} Gostaria de saber mais alguma coisa?(s/n)'''
    if mensagem == 'noticias':
      return f'''Aqui estão as noticias{os.linesep} Gostaria de saber mais alguma coisa?(s/n)'''
    if mensagem == 'proximojogo':
      return f'''O proximo jogo é contra o time Furias{os.linesep} Gostaria de saber mais alguma coisa?(s/n)'''

    if mensagem.lower() in ('S','sim'):
      return 'Digite sobre o que você quer saber:'

     else:
      return'Gostaria de acessar o menu?Digite "menu"  '

    
# responder

  def responder(self, resposta, chat_id):
    #enviar
    link_de_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
    requests.get(link_de_envio)


bot = AlcateiaCSBot()
bot.Iniciar()
