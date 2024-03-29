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

    stream = open("Bot Telegram Binance\config.yaml", 'r')
    c = yaml.safe_load(stream)

#telegram
TELEGRAM_BOT_TOKEN = c['bot_token']
TELEGRAM_CHAT_ID = c['bot_chat_id'] 

#api binance
api_key_binance = c['api_key']
api_secret_binance = c['api_secret']


client_binance = Client(api_key_binance, api_secret_binance)

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

    #valor_lucro = "{:.2%}".format(valor_lucro)

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
    print('Quando foi comprado o ativo? formato: YYYYMMDD')
    data_compra = input()
    cotacao_compra = float(cotacao_usd(data_compra))

    print('Quanto de BTC foi comprado? formato: X.XXXXXXXX 8 casas decimais')
    qtd_compra = float(input())

    print(f'A cotação USD-BRL na data {data_compra} foi de R$ {cotacao_compra}')

    
    while True:
        try:
            print('Em que moeda está o valor do ativo? (0) BRL ou (1)USD')
            moeda_cotacao = int(input())
            if moeda_cotacao != 0 or moeda_cotacao != 1:
                print('Insira uma opção válida. (0) BRL ou (1)USD')
                continue    
        except ValueError:
            print('Insira uma opção válida. (0) BRL ou (1)USD')
            continue
        else:
            break

    if moeda_cotacao == 0:
        print('[BRL] Insira o valor do ativo: ')
        btc_preco_brl = int(input())
        btc_preco_usd = btc_preco_brl/cotacao_compra
    elif moeda_cotacao == 1:
        print('[USD] Insira o valor do ativo: ')
        btc_preco_usd = int(input())
        btc_preco_brl = btc_preco_usd*cotacao_compra
    else:
        print('Opção inválida, inicie o programa novamente.')
        exit()

    print('Qual frequencia você deseja receber um update sobre a cotação do ativo? (em horas)')
    hr_update = int(input())

    while rep:
        while count < len(tickers):

            for x in range(len(tickers)):   
                btc_price_change = client_binance.get_ticker(symbol=tickers[x])
                btc_float_price = float(btc_price_change["lastPrice"])
                datetime_obj_open = btc_price_change["openTime"]/1000
                data_abertura = datetime.fromtimestamp(int(datetime_obj_open))
                data_abertura = data_abertura.strftime("%d.%m.%y %H:%M:%S")
                datetime_obj_fechamento  = btc_price_change["closeTime"]/1000
                data_fechamento = datetime.fromtimestamp(int(datetime_obj_fechamento))
                data_fechamento = data_fechamento.strftime("%d.%m.%y %H:%M:%S")
                
                var_percent_lucro = var_percentual(btc_preco_brl,btc_float_price)
                var_percent_lucro_formatado = "{:.2%}".format(var_percent_lucro)

                valor_lucro_btc = qtd_compra*var_percent_lucro
                

                if tickers[x] == 'BTCUSDT':
                    lucro_usd = valor_lucro_btc*btc_float_price
                elif tickers[x] == 'BTCBRL':
                    lucro_brl = valor_lucro_btc*btc_float_price
                

                telegram_bot_sendtext(f'''
                🤖 💸 {tickers[x]} 💰 🤑 \n PREÇO DO BITCOIN AGORA {data_fechamento}: ${btc_price_change["lastPrice"]} \n
                 MUDANÇA DE PREÇO NAS ÚLTIMAS 24 HRS: ${btc_price_change["priceChange"]} \n 
                 MUDANÇA DE PREÇO NAS ÚLTIMAS 24 HRS: {btc_price_change["priceChangePercent"]}% \n
                
                ''')
                
                if (btc_float_price > btc_preco_usd and tickers[x] == 'BTCUSDT') or \
                    (btc_float_price > btc_preco_brl and tickers[x] == 'BTCBRL'):
                    telegram_bot_sendtext('🤑🤑🤑🤑 @Nimloth1 TU TA LUCRANTE 🤑🤑🤑🤑')
                    
                    if tickers[x] == 'BTCUSDT':
                        telegram_bot_sendtext(f'Lucro de: $ {lucro_usd} || {var_percent_lucro_formatado}')
                        continue
                    elif tickers[x] == 'BTCBRL':
                        telegram_bot_sendtext(f'Lucro de: R$ {"{:.3}".format(lucro_brl)} || {var_percent_lucro_formatado}')
                    else:
                        continue
                count += 1

    time.sleep(hr_update*3600) #espera x hrs
    #time.sleep(3600) #espera 1 hrs

main()