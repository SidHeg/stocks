from yfinance import Ticker
import csv
from os import curdir, walk
from re import match

# msft = yf.Ticker("MSFT")
# print(msft.info)
portfolio_path = curdir + '/resources/'

def main():
    files = []
    for dirpath, dirnames, filenames in walk(portfolio_path):
        files.extend(filenames)
        
    for file in files:
        total_investment = 0
        total_profit = 0
        with open(portfolio_path+file, newline='') as csvfile:
            csv_reader = csv.reader(csvfile, dialect='excel')
            # next(csv_reader) # skip header
            for row in csv_reader:
                if not is_valid_row(row):
                    continue
                stock = Ticker(row[2])
                current_price: float = stock.info['regularMarketPrice']
                bought_price: float = float(row[14][1:])
                quantity: float = float(row[4])
                total_investment = total_investment + bought_price * quantity
                profit_per_share: float = current_price - bought_price
                profit: float = profit_per_share * quantity
                total_profit = total_profit + profit
                profit_percentage: float = ((profit_per_share/bought_price)*100)
                print(row[1]+', '+row[2]+', '+row[3]+', '+row[4]+', '+'{:.2f}'.format(bought_price)+', '+'{:.2f}'.format(current_price)+', '+'{:.2f}'.format(profit)+', '+'{:.2f}'.format(profit_percentage))

            print('Investment, Profit, Profit%');
            profit_percentage = (total_profit/total_investment) * 100
            print('{:.2f}'.format(total_investment)+', '+'{:.2f}'.format(total_profit)+', '+ '{:.2f}'.format(profit_percentage))
            print('\n\n***********************\n\n')

def is_valid_row(row) -> bool:
    if(len(row) < 3):
        return False
    if row[2] == 'Symbol':
        print(row[1]+', '+row[2]+', '+row[3]+', '+row[4]+', '+row[14]+', '+'Current Price'+', '+'Profit Value'+', '+'Profit Percentage')
        return False
    if not match('^[a-zA-Z]+$', row[2]):
        return False
    return True



if __name__ == "__main__":
    main()




