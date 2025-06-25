import yfinance as yf
import pandas as pd
import os

# 주요 지수 목록 (야후 파이낸스 티커) + 저장용 영문 이름 매핑
major_indices = {
    "^IXIC": ("NASDAQ Composite", "NASDAQ_Composite"),
    "^NDX": ("NASDAQ-100", "NASDAQ_100"),
    "^GSPC": ("S&P 500", "SP500"),
    "^DJI": ("Dow Jones 30", "Dow_Jones_30"),
    "^RUT": ("Russell 2000", "Russell_2000"),
    "^NYA": ("NYSE Composite", "NYSE_Composite"),
    "^W5000": ("Wilshire 5000", "Wilshire_5000"),
    "^VIX": ("VIX Volatility", "VIX")
}

def fetch_index_data(ticker, display_name, save_name, period, interval, save_dir="nasdaq_index_data"):
    os.makedirs(save_dir, exist_ok=True)
    try:
        data = yf.download(ticker, period=period, interval=interval)
        if data.empty:
            print(f"[{ticker}] 데이터 없음")
            return False
        filename = f"{save_name}_{interval}.csv"
        filepath = os.path.join(save_dir, filename)
        data.to_csv(filepath)
        print(f"[{ticker}] 저장 완료 → {filename} ({len(data)}행)")
        return True
    except Exception as e:
        print(f"[{ticker}] 오류: {e}")
        return False

def main():
    print("미국 주요 지수 다운로드 시작")
    period = input("조회 기간 입력 (예: 1y, 5y, 10y, max): ").strip()
    interval = input("봉 단위 입력 (예: 1d, 1wk, 1mo): ").strip()
    
    print(f"\n조회 기간: {period}, 봉 단위: {interval}\n")
    for ticker, (display_name, save_name) in major_indices.items():
        fetch_index_data(ticker, display_name, save_name, period, interval)

    print("\n✅ 모든 지수 다운로드 완료.")

if __name__ == "__main__":
    main()
