import yfinance as yf
import os

SECTOR_MAP = {
    'XLC': 'Communication Services',
    'XLY': 'Consumer Discretionary',
    'XLP': 'Consumer Staples',
    'XLE': 'Energy',
    'XLF': 'Financials',
    'XLV': 'Health Care',
    'XLI': 'Industrials',
    'XLK': 'Information Technology',
    'XLB': 'Materials',
    'XLRE': 'Real Estate',
    'XLU': 'Utilities'
}

def fetch_etf_data(ticker, sector_name, period, interval, save_dir="etf_data"):
    os.makedirs(save_dir, exist_ok=True)
    try:
        data = yf.download(ticker, period=period, interval=interval, progress=False)
        if data.empty:
            print(f"[{ticker}] 데이터 없음")
            return False
        filename = f"{ticker}_{interval}.csv"
        filepath = os.path.join(save_dir, filename)
        data.to_csv(filepath)
        print(f"[{ticker} ({sector_name})] 저장 완료 → {filename} ({len(data)}행)")
        return True
    except Exception as e:
        print(f"[{ticker}] 오류: {e}")
        return False

def main():
    print("ETF 섹터별 데이터 다운로드 시작")
    period = input("조회 기간 입력 (예: 1y, 5y, 10y, max): ").strip()
    interval = input("봉 단위 입력 (예: 1d, 1wk, 1mo): ").strip()

    print(f"\n조회 기간: {period}, 봉 단위: {interval}\n")

    for ticker, sector_name in SECTOR_MAP.items():
        fetch_etf_data(ticker, sector_name, period, interval)

    print("\n✅ 모든 ETF 데이터 다운로드 완료.")

if __name__ == "__main__":
    main()
