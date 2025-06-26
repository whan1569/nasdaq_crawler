import pandas as pd

# 주요 지수 딕셔너리
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

def save_index_tickers(output_path="index_tickers.csv"):
    rows = []
    for ticker, (display_name, save_name) in major_indices.items():
        rows.append({
            "Ticker": ticker,
            "DisplayName": display_name,
            "SaveName": save_name
        })
    
    df = pd.DataFrame(rows)
    df.to_csv(output_path, index=False, encoding='utf-8-sig')
    print(f"✅ 저장 완료: {output_path} ({len(df)}개 인덱스)")

if __name__ == "__main__":
    save_index_tickers()
