import requests
from decouple import config
from fastapi import FastAPI
import os

URL = config('URL')
API_KEY = config('API_KEY')
header = {
    'x-messari-api-key':API_KEY
    }

app = FastAPI()
btc = []
eth = []
@app.get('/')
async def root():
    return {'Hello':'Welcome shopbox api'}


@app.get('/api/market_info')
async def get_market_info():
    value = "?fields=id,slug,symbol,metrics/market_data/price_usd"
    result = requests.get('{url}{value}'.format(url=URL,value=value),headers=header)
    try:
        if result.status_code == 200:
            for index in result.json()['data']:
                if index['symbol'] == "BTC":
                    btc.append(index['metrics']['market_data']['price_usd'])
                elif index['symbol'] == "ETH":
                    eth.append(index['metrics']
                               ['market_data']['price_usd'])

            return result.json()['data']
    except:
        return {'code':404}


@app.get('/api/market_info/{slug}')
async def get_crypto_info(slug:str):

    if slug == "bitcoin":
        crypto_path = config('BITCOIN')
    elif slug == "ethereum":
        crypto_path = config('ETH')
    elif slug == "zcash":
        crypto_path = config('ZEC')
    try:
        result = requests.get(
        '{url}/{path}'.format(url=URL, path=crypto_path), headers=header)
        if result.status_code == 200:
            return result.json()['data']['market_data']
    except:
        return {'code':404}



