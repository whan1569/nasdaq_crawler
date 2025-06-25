import requests
import pandas as pd

def fetch_nasdaq_tickers_json():
    url = "https://api.nasdaq.com/api/screener/stocks?exchange=nasdaq&download=true"
    headers = {"User-Agent": "Mozilla/5.0"}
    response = requests.get(url, headers=headers)
    data = response.json()

    rows = data['data']['rows']
    tickers = [item['symbol'] for item in rows]
    return tickers

def save_tickers_to_csv(tickers, filename="nasdaq_tickers.csv"):
    df = pd.DataFrame(tickers, columns=["Symbol"])
    df.to_csv(filename, index=False)
    print(f"{filename} 파일로 {len(tickers)}개 티커 저장 완료!")

if __name__ == "__main__":
    tickers = fetch_nasdaq_tickers_json()
    save_tickers_to_csv(tickers)
