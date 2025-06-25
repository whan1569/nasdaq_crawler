import pandas as pd
import yfinance as yf
import os
import time

def load_tickers(filename="nasdaq_tickers.csv"):
    df = pd.read_csv(filename)
    return df['Symbol'].tolist()

def fetch_and_save_stock_data(ticker, period, interval, save_dir="nasdaq_stock_data"):
    os.makedirs(save_dir, exist_ok=True)
    try:
        stock = yf.Ticker(ticker)
        try:
            hist = stock.history(period=period, interval=interval)
        except Exception:
            # period 방식 실패 시 start-end 방식 재시도
            hist = stock.history(start='1900-01-01', end='2099-12-31', interval=interval)

        if hist.empty:
            print(f"{ticker}: 데이터 없음")
            return False

        start_date = hist.index.min().strftime("%Y-%m-%d")
        end_date = hist.index.max().strftime("%Y-%m-%d")
        filepath = os.path.join(save_dir, f"{ticker}_{interval}.csv")
        hist.to_csv(filepath)
        print(f"{ticker}: 저장 완료 ({interval}), 기간: {start_date} ~ {end_date}")
        return True

    except Exception as e:
        print(f"{ticker}: 오류 발생 - {e}")
        return False

def main():
    period = input("데이터 조회 기간 입력 (예: max, 1y, 6mo, 30d): ").strip()
    interval = input("저장할 봉 단위 입력 (예: 1m, 2m, 5m, 15m, 1h, 1d): ").strip()

    tickers = load_tickers()
    total = len(tickers)
    saved_count = 0
    no_data_tickers = []  # 데이터 없는 티커 리스트

    print(f"총 {total}개 티커 로드됨")
    print(f"조회 기간: {period}, 저장 단위: {interval}")
    print("크롤링 시작...")

    for idx, ticker in enumerate(tickers, start=1):
        success = fetch_and_save_stock_data(ticker, period, interval)
        if success:
            saved_count += 1
        else:
            no_data_tickers.append(ticker)
        print(f"[{idx}/{total}] 진행 중... 저장 완료: {saved_count}")
        time.sleep(1)

    print(f"크롤링 완료. 총 저장된 티커: {saved_count}/{total}")

    # 데이터 없는 티커 목록 저장
    if no_data_tickers:
        no_data_df = pd.DataFrame(no_data_tickers, columns=['Symbol'])
        no_data_df.to_csv("no_data_tickers.csv", index=False)
        print(f"데이터 없는 티커 {len(no_data_tickers)}개를 'no_data_tickers.csv' 파일로 저장했습니다.")

if __name__ == "__main__":
    main()
