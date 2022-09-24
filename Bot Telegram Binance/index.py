from binance.client import Client
import pandas as pd
import datetime
from datetime import datetime, timezone
import time
from tqdm import tqdm
from requests_oauthlib import OAuth1Session
import requests
import os
import json
import telegram
from telegram import Update
from telegram.ext import Updater, CommandHandler
from telegram.ext.callbackcontext import CallbackContext
import yaml




if __name__ == '__main__':

    stream = open("config.yaml", 'r')
    c = yaml.safe_load(stream)

#telegram
TELEGRAM_BOT_TOKEN = c['bot_token']
TELEGRAM_CHAT_ID = c['bot_chat_id'] 

#api binance
api_key = c['api_key']
api_secret = c['api_secret']


client = Client(api_key, api_secret)

bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)


def telegram_bot_sendtext(bot_message, num_try = 0):
    global bot
    try:
        return bot.send_message(chat_id=TELEGRAM_CHAT_ID, text=bot_message)
    except:
        if num_try == 1:
            bot = telegram.Bot(token=TELEGRAM_BOT_TOKEN)
            return telegram_bot_sendtext(bot_message, 1)
        return 0


def cotacao_usd(data_compra_ativo):
    requisicao = requests.get(f'https://economia.awesomeapi.com.br/json/daily/USD-BRL/?start_date={data_compra_ativo}&end_date={data_compra_ativo}')
    cotacao = requisicao.json()
    cotacao_usd_brl = cotacao[0]['bid']
    
    return cotacao_usd_brl


def var_percentual(valor_pago, valor_atual):
    
    valor_lucro = (valor_atual/valor_pago)-1

    valor_lucro = "{:.2%}".format(valor_lucro)

    return valor_lucro



telegram_bot_sendtext('🤖 BOT INICIALIZADO...')



def main():
    rep = True
    tickers = ['BTCUSDT','BTCBRL']
    count = 0  

    os.system('CLS')

    print('''
    ======== Bem vindo ===========

    Este bot verifica a cada 2 horas se o valor do BTC pago está lucrando ou não.
    Após a verificação é enviado para o usuário uma mensagem no Telegram,
    indicando o preço do BTC no momento, a variação percentual e variação em quantidade.

    Se o usuário estiver lucrando, será enviada uma mensagem informando o lucro.
    
    ''')

    time.sleep(3)

    #Valor inicial
    print('Quando foi comprado o ativo?')
    data_compra = input()
    cotacao_compra = cotacao_usd(data_compra)

    print(f'A cotação USD-BRL na data {data_compra} foi de R$ {cotacao_compra}')

    print('Em que moeda está o valor do ativo? (0) BRL ou (1)USD')
    moeda_cotacao = input()

    if moeda_cotacao == 0:
        print('[BRL] Insira o valor do ativo: ')
        btc_preco_brl = input()
        btc_preco_usd = btc_preco_brl/cotacao_compra
    elif moeda_cotacao == 1:
        print('[USD] Insira o valor do ativo: ')
        btc_preco_usd = input()
        btc_preco_brl = btc_preco_usd*cotacao_compra
    else:
        print('Opção inválida, inicie o programa novamente.')
        exit()

    

    while rep:
        while count < len(tickers):

            for x in range(len(tickers)):   
                btc_price_change = client.get_ticker(symbol=tickers[x])
                btc_float_price = float(btc_price_change["lastPrice"])
                datetime_obj_open = btc_price_change["openTime"]/1000
                data_abertura = datetime.fromtimestamp(int(datetime_obj_open))
                data_abertura = data_abertura.strftime("%d.%m.%y %H:%M:%S")
                datetime_obj_fechamento  = btc_price_change["closeTime"]/1000
                data_fechamento = datetime.fromtimestamp(int(datetime_obj_fechamento))
                data_fechamento = data_fechamento.strftime("%d.%m.%y %H:%M:%S")
                var_percent_lucro = var_percentual(btc_preco_brl,btc_float_price)
                
                if tickers[x] == 'BTCBRL':
                    lucro_brl = var_percent_lucro*btc_float_price

                telegram_bot_sendtext(f'🤖 💸 {tickers[x]} 💰 🤑 \n PREÇO DO BITCOIN AGORA {data_fechamento}: ${btc_price_change["lastPrice"]} \n MUDANÇA DE PREÇO NAS ÚLTIMAS 24 HRS: ${btc_price_change["priceChange"]} \n MUDANÇA DE PREÇO NAS ÚLTIMAS 24 HRS: {btc_price_change["priceChangePercent"]}%')
                
                if (btc_float_price > btc_preco_usd and tickers[x] == 'BTCUSDT') or (btc_float_price > btc_preco_brl and tickers[x] == 'BTCBRL'):
                    telegram_bot_sendtext('🤑🤑🤑🤑 @Nimloth1 TU TA LUCRANTE 🤑🤑🤑🤑')
                    if tickers[x] == 'BTCBRL':
                        telegram_bot_sendtext(f'Lucro de: R$ {lucro_brl} || {var_percent_lucro}')
                count += 1
    time.sleep(7200) #espera 2 hrs
    #time.sleep(3600) #espera 1 hrs

main()