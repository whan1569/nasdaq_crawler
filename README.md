# NASDAQ 데이터 크롤링 프로젝트

이 프로젝트는 NASDAQ 주식 시장의 개별 주식과 주요 지수 데이터를 자동으로 수집하고 저장하는 Python 기반 크롤링 도구입니다.

## 📋 목차

- [기능](#기능)
- [설치 및 설정](#설치-및-설정)
- [사용법](#사용법)
- [데이터 저장 형식](#데이터-저장-형식)
- [크롤링 요령](#크롤링-요령)
- [파일 구조](#파일-구조)
- [데이터 활용 예시](#데이터-활용-예시)

## 🚀 기능

### 1. NASDAQ 티커 목록 수집
- NASDAQ 공식 API를 통해 상장된 모든 주식 티커를 자동으로 수집
- `nasdaq_tickers.csv` 파일로 저장

### 2. 개별 주식 데이터 크롤링
- 3,900개 이상의 NASDAQ 상장 주식 데이터 수집
- Yahoo Finance API를 통한 안정적인 데이터 수집
- 다양한 시간 단위 지원 (1m, 5m, 15m, 1h, 1d 등)
- 자동 오류 처리 및 재시도 로직

### 3. 주요 지수 데이터 크롤링
- NASDAQ Composite, NASDAQ-100, S&P 500, Dow Jones 등 8개 주요 지수
- 장기간 히스토리 데이터 제공 (1971년부터 현재까지)

### 4. 데이터 시각화 도구
- Chart.js, TradingView 기반 차트 뷰어
- 실시간 데이터 확인 가능

## 📦 설치 및 설정

### 1. 의존성 설치
```bash
pip install -r requirements.txt
```

### 2. 필요한 패키지
- `pandas>=1.3.0`: 데이터 처리
- `requests>=2.25.0`: HTTP 요청
- `yfinance>=0.2.18`: Yahoo Finance API

## 🎯 사용법

### 1. NASDAQ 티커 목록 수집
```bash
python nasdaq_ticker_fetch.py
```
- NASDAQ 공식 API에서 상장 주식 목록을 가져와 `nasdaq_tickers.csv`에 저장
- 약 3,900개의 티커가 수집됩니다

### 2. 개별 주식 데이터 크롤링
```bash
python nasdaq_stock_crawler.py
```
실행 시 다음 정보를 입력하세요:
- **데이터 조회 기간**: `max` (전체 기간), `1y` (1년), `6mo` (6개월), `30d` (30일) 등
- **저장할 봉 단위**: `1m`, `2m`, `5m`, `15m`, `1h`, `1d` 등

### 3. 주요 지수 데이터 크롤링
```bash
python nasdaq_index_crawler.py
```
실행 시 다음 정보를 입력하세요:
- **조회 기간**: `1y`, `5y`, `10y`, `max` 등
- **봉 단위**: `1d`, `1wk`, `1mo` 등

## 📊 데이터 저장 형식

### 개별 주식 데이터 (`nasdaq_stock_data/` 폴더)
파일명: `{TICKER}_{INTERVAL}.csv`

| 컬럼명 | 설명 | 데이터 타입 |
|--------|------|-------------|
| Date | 날짜 및 시간 (타임존 포함) | datetime |
| Open | 시가 | float |
| High | 고가 | float |
| Low | 저가 | float |
| Close | 종가 | float |
| Volume | 거래량 | int |
| Dividends | 배당금 | float |
| Stock Splits | 주식 분할 | float |

**예시 파일**: `AAPL_1d.csv`
```csv
Date,Open,High,Low,Close,Volume,Dividends,Stock Splits
1980-12-12 00:00:00-05:00,0.128348,0.128348,0.128348,0.128348,117258400,0.0,0.0
1980-12-15 00:00:00-05:00,0.122767,0.122767,0.122767,0.122767,43971200,0.0,0.0
...
```

### 주요 지수 데이터 (`nasdaq_index_data/` 폴더)
파일명: `{INDEX_NAME}_{INTERVAL}.csv`

| 컬럼명 | 설명 | 데이터 타입 |
|--------|------|-------------|
| Date | 날짜 | date |
| Open | 시가 | float |
| High | 고가 | float |
| Low | 저가 | float |
| Close | 종가 | float |
| Volume | 거래량 | int |

**예시 파일**: `NASDAQ_Composite_1d.csv`
```csv
Date,Open,High,Low,Close,Volume
1971-02-05,100.0,100.0,100.0,100.0,0
1971-02-08,100.83999633789062,100.83999633789062,100.83999633789062,100.83999633789062,0
...
```

## ⚡ 크롤링 요령

### 1. 효율적인 크롤링 전략

#### 시간 단위별 권장 설정
- **일봉 데이터 (1d)**: 전체 기간 (`max`) - 백테스팅, 장기 분석용
- **시간봉 데이터 (1h)**: 1-2년 (`1y`, `2y`) - 중기 분석용
- **분봉 데이터 (1m, 5m, 15m)**: 1-6개월 (`1mo`, `3mo`, `6mo`) - 단기 분석용

#### 크롤링 순서 권장
1. 먼저 티커 목록 수집: `python nasdaq_ticker_fetch.py`
2. 주요 지수 데이터 수집: `python nasdaq_index_crawler.py`
3. 개별 주식 데이터 수집: `python nasdaq_stock_crawler.py`

### 2. 오류 처리 및 재시도
- 네트워크 오류 시 자동 재시도
- 데이터가 없는 티커는 `no_data_tickers.csv`에 별도 저장
- 각 요청 사이에 1초 지연으로 API 제한 방지

### 3. 메모리 및 저장 공간 관리
- **일봉 데이터**: 약 3,900개 파일, 총 용량 ~500MB
- **시간봉 데이터**: 약 3,900개 파일, 총 용량 ~2GB
- **분봉 데이터**: 용량이 매우 클 수 있으므로 필요한 기간만 수집 권장

## 📁 파일 구조

```
nasdaq_data/
├── nasdaq_ticker_fetch.py      # NASDAQ 티커 목록 수집
├── nasdaq_stock_crawler.py     # 개별 주식 데이터 크롤링
├── nasdaq_index_crawler.py     # 주요 지수 데이터 크롤링
├── requirements.txt            # Python 의존성
├── nasdaq_tickers.csv          # 수집된 티커 목록
├── no_data_tickers.csv         # 데이터 없는 티커 목록
├── nasdaq_stock_data/          # 개별 주식 데이터 저장 폴더
│   ├── AAPL_1d.csv
│   ├── MSFT_1d.csv
│   └── ...
├── nasdaq_index_data/          # 주요 지수 데이터 저장 폴더
│   ├── NASDAQ_Composite_1d.csv
│   ├── SP500_1d.csv
│   └── ...
├── viewer3.html               # Chart.js 기반 차트 뷰어
├── TradingView.html           # TradingView 기반 차트 뷰어
└── Chart_js.html              # 기본 Chart.js 뷰어
```

## 💡 데이터 활용 예시

### 1. Python에서 데이터 로드
```python
import pandas as pd

# 개별 주식 데이터 로드
df = pd.read_csv('nasdaq_stock_data/AAPL_1d.csv')
df['Date'] = pd.to_datetime(df['Date'])
df.set_index('Date', inplace=True)

# 주요 지수 데이터 로드
index_df = pd.read_csv('nasdaq_index_data/NASDAQ_Composite_1d.csv')
index_df['Date'] = pd.to_datetime(index_df['Date'])
index_df.set_index('Date', inplace=True)
```

### 2. 기술적 분석
```python
# 이동평균 계산
df['MA20'] = df['Close'].rolling(window=20).mean()
df['MA50'] = df['Close'].rolling(window=50).mean()

# RSI 계산
def calculate_rsi(prices, period=14):
    delta = prices.diff()
    gain = (delta.where(delta > 0, 0)).rolling(window=period).mean()
    loss = (-delta.where(delta < 0, 0)).rolling(window=period).mean()
    rs = gain / loss
    return 100 - (100 / (1 + rs))

df['RSI'] = calculate_rsi(df['Close'])
```

### 3. 백테스팅
```python
# 간단한 이동평균 크로스오버 전략
def backtest_ma_crossover(df):
    df['Signal'] = 0
    df.loc[df['MA20'] > df['MA50'], 'Signal'] = 1
    df.loc[df['MA20'] < df['MA50'], 'Signal'] = -1
    
    # 수익률 계산
    df['Returns'] = df['Close'].pct_change()
    df['Strategy_Returns'] = df['Signal'].shift(1) * df['Returns']
    
    return df['Strategy_Returns'].cumsum()
```

### 4. 데이터 시각화
```python
import matplotlib.pyplot as plt

# 가격 차트와 이동평균
plt.figure(figsize=(12, 6))
plt.plot(df.index, df['Close'], label='Close Price')
plt.plot(df.index, df['MA20'], label='20-day MA')
plt.plot(df.index, df['MA50'], label='50-day MA')
plt.title('AAPL Stock Price with Moving Averages')
plt.legend()
plt.show()
```

## ⚠️ 주의사항

1. **API 제한**: Yahoo Finance API는 요청 빈도에 제한이 있을 수 있습니다
2. **데이터 정확성**: 수집된 데이터는 참고용이며, 투자 결정 시 공식 데이터를 확인하세요
3. **저장 공간**: 대용량 데이터 수집 시 충분한 디스크 공간을 확보하세요
4. **네트워크**: 안정적인 인터넷 연결이 필요합니다

## 🔄 업데이트

데이터를 최신 상태로 유지하려면 정기적으로 크롤링을 실행하세요:
- **일봉 데이터**: 매일 장 마감 후
- **시간봉/분봉 데이터**: 실시간 또는 필요시

## 📞 문의

프로젝트 관련 문의사항이나 개선 제안이 있으시면 이슈를 등록해 주세요. 