from binance.spot import Spot
import telebot
import dotenv as _dotenv
import os as _os

_dotenv.load_dotenv()

##################################################################################################################################
############################################################## DATA ##############################################################
##################################################################################################################################

B_API_KEY = _os.environ["BINANCE_API_KEY"]
B_API_SECURITY = _os.environ["BINANCE_API_SECURITY"]
T_TOKEN_BALANCE = _os.environ["TELEGRAM_TOKEN_BALANCE"]

client = Spot(B_API_KEY, B_API_SECURITY)

BUSD = round((float(client.account()['balances'][188]['free']) + float(client.account()['balances'][188]['locked'])),)
USDT = round((float(client.account()['balances'][11]['free']) + float(client.account()['balances'][11]['locked'])),)
BTC = round((float(client.account()['balances'][0]['free']) + float(client.account()['balances'][0]['locked'])),5)
ETH = round((float(client.account()['balances'][2]['free']) + float(client.account()['balances'][2]['locked'])),2)
BNB = round((float(client.account()['balances'][4]['free']) + float(client.account()['balances'][4]['locked'])),2)
LINK = round((float(client.account()['balances'][32]['free']) + float(client.account()['balances'][32]['locked'])),2)
DOT = round((float(client.account()['balances'][257]['free']) + float(client.account()['balances'][257]['locked'])),2)
NEAR = round((float(client.account()['balances'][317]['free']) + float(client.account()['balances'][317]['locked'])),2)
ETC = round((float(client.account()['balances'][44]['free']) + float(client.account()['balances'][44]['locked'])),2)
FIL = round((float(client.account()['balances'][320]['free']) + float(client.account()['balances'][320]['locked'])),2)
SOL = round((float(client.account()['balances'][232]['free']) + float(client.account()['balances'][232]['locked'])),2)
MATIC = round((float(client.account()['balances'][168]['free']) + float(client.account()['balances'][168]['locked'])),2)
ALGO = round((float(client.account()['balances'][177]['free']) + float(client.account()['balances'][177]['locked'])),2)

# print("Balance fondo")
# print("BUSD: " f"{BUSD}")
# print("BTC: " f"{BTC}")
# print("USDT: " f"{USDT}")
# print("ETH: " f"{ETH}")
# print("DOT: " f"{DOT}")
# print("NEAR: " f"{NEAR}")
# print("LINK: " f"{LINK}")
# print("ETC: " f"{ETC}")
# print("FIL: " f"{FIL}")
# print("SOL: " f"{SOL}")
# print("MATIC: " f"{MATIC}")
# print("ALGO: " f"{ALGO}")
# print("BNB: " f"{BNB}")

balance_total = BUSD + USDT + round(BTC * round(float(client.ticker_price("BTCUSDT")['price']),)) + round(ETH * round(float(client.ticker_price("ETHUSDT")['price']),)) + round(BNB * round(float(client.ticker_price("BNBUSDT")['price']),)) + round(LINK * round(float(client.ticker_price("LINKUSDT")['price']),))  + round(DOT * round(float(client.ticker_price("DOTUSDT")['price']),)) + round(NEAR * round(float(client.ticker_price("NEARUSDT")['price']),)) + round(ETC * round(float(client.ticker_price("ETCUSDT")['price']),)) + round(FIL * round(float(client.ticker_price("FILUSDT")['price']),)) + round(SOL * round(float(client.ticker_price("SOLUSDT")['price']),)) + round(MATIC * round(float(client.ticker_price("MATICUSDT")['price']),)) + round(ALGO * round(float(client.ticker_price("ALGOUSDT")['price']),))
# print(balance_total)

balance = ("### Balance fondo ###\n"
        "BUSD: " f"{BUSD}\n"
        "USDT: " f"{USDT}\n"
        "BTC: " f"{BTC}\n"
        "ETH: " f"{ETH}\n"
        "BNB: " f"{BNB}\n"
        "LINK: " f"{LINK}\n"
        "DOT: " f"{DOT}\n"
        "NEAR: " f"{NEAR}\n"
        "ETC: " f"{ETC}\n"
        "FIL: " f"{FIL}\n"
        "SOL: " f"{SOL}\n"
        "MATIC: " f"{MATIC}\n"
        "ALGO: " f"{ALGO}\n"
        "\n"
        "#################\n"
        "Balance total\n"
        "USD: " f"{balance_total}")

##################################################################################################################################
############################################################## TELEGRAM ##########################################################
##################################################################################################################################

bot_telegram = telebot.TeleBot(T_TOKEN_BALANCE)

@bot_telegram.message_handler(commands=["balance"])
def cmd_start(message):
    bot_telegram.reply_to(message, balance)

if __name__ == '__main__':
    print('Iniciando el bot')
    bot_telegram.infinity_polling()
