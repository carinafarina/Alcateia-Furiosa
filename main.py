
import requests
import time
import json

class TelegramBot:
  def __init__(self):
    token = '7920659594:AAFiT83JQAh8KsQ9bQk6m-amgysEc7bcK8w'
    self.url_base = f'https://api.telegram.org/bot{token}/'

# Iniciar o bot
  def Iniciar(self):
    update_id = None
    while True:
      atualizacao = self.obter_mensagens(update_id)
      if atualizacao is None:
        print("Erro ao obter atualizações. Tentando novamente em 5 segundos...")
        time.sleep(5)
        continue
        
      mensagens = atualizacao.get('result', [])
      if mensagens:
        for mensagem in mensagens          update_id = mensagem['update_id']
          chat_id = mensagem['message']['from']['id']
          resposta = self.criar_resposta()
          self.responder(resposta,chat_id)
  
# Obter mensagens
  def obter_mensagens(self, update_id):    
    link_requisicao = f'{self.url_base}getUpdates?timeout=100'
    if update_id:
        link_requisicao = f'{link_requisicao}&offset={update_id + 1}'
        resultado = requests.get(link_requisicao)
        return json.loads(resultado.content)
# Cria resposta
  def criar_resposta(self):
    return 'Olá, bem vindo ao Alcateia Furiosa!'
# responder
  def responder(self, resposta, chat_id):
    #enviar
    link_de_envio = f'{self.url_base}sendMessage?chat_id={chat_id}&text={resposta}'
    requests.get(link_de_envio)


bot = TelegramBot()
bot.Iniciar()
  

   