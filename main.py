import requests
import schedule


def crypto_tracker():
    response = requests.get(
        url='https://api.kucoin.com/api/v1/market/stats?symbol=BTC-USDT')
    data = response.json()
    btc_price = data.get('data').get('last')
    print(f"Last price on BTC|USDT: {btc_price}$")


if __name__ == '__main__':
    schedule.every().day.at('08:00').do(crypto_tracker)
    while True:
        schedule.run_pending()
