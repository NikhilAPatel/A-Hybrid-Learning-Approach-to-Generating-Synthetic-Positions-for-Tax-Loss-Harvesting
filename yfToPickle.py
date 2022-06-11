import pickle
import yfinance as yf
from statistics import mode

start_date = "2021-01-09"  # TODO choose real start date
end_date = "2022-01-10"  # TODO choose real end date

snp_comp_file = open('snp_composition.obj', 'rb')
snp_composition = pickle.load(snp_comp_file)
snp_comp_file.close()
all_tickers = snp_composition.keys()

data = {}
price_history = {}
i = 0
num_tickers = len(all_tickers)
for symbol in all_tickers:
    price_history[symbol] = yf.Ticker(symbol).history(start=start_date, end=end_date)
    print(str(i) + "/" + str(num_tickers))
    i += 1

days = []

# Get total number of days
for ticker in price_history.keys():
    days.append(len(price_history[ticker]))

num_days = mode(days)

unavailable = []

# Verify that the ticker has data for the entire range
for ticker in price_history.keys():
    if len(price_history[ticker]) != num_days:
        unavailable.append(ticker)

for ticker in unavailable:
    print("Removing " + ticker + " due to insufficient data")
    price_history.pop(ticker)
    snp_composition.pop(ticker)

snp_price_file = open('snp_price.obj', 'wb')
pickle.dump(price_history, snp_price_file)
snp_price_file.close()

file_snp_comp = open('snp_composition.obj', 'wb')
pickle.dump(snp_composition, file_snp_comp)
file_snp_comp.close()