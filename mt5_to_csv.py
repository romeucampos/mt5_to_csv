from datetime import datetime
import json

import pandas as pd
import MetaTrader5 as mt5

TIME_FRAME = mt5.TIMEFRAME_D1  # Timeframe que deseja. Veja no link https://www.mql5.com/en/docs/integration/python_metatrader5/mt5copyratesfrom_py
BARS = 1000 # Número de barras


def init():
    with open('symbols.txt') as file:
        symbols = json.load(file)

    if not mt5.initialize():
        print("initialize() failed, error code =", mt5.last_error())
        quit()
    
    print('Loading symbols...')
    
    return symbols

 
def convert_csv(timeframe=mt5.TIMEFRAME_D1, bars=1000):
    def load_data(symbol):
        try:
            ticker = pd.DataFrame(mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_D1, 0, bars))['close'].rename(index=symbol)
            print(f'Symbol {symbol} Bars {BARS} ok')
        
        except RuntimeError:
            print(f'ERRO NO SYMBOL "{symbol}"')
            mt5.shutdown()
            quit()

        return ticker
    

    tickers_close = [load_data(symbol) for symbol in symbols]

    symbol_one = pd.DataFrame(mt5.copy_rates_from_pos(symbols[0], timeframe, 0, bars))
    time_tickers = pd.to_datetime(symbol_one['time'], unit='s')

    mt5.shutdown()

    df = pd.DataFrame(tickers_close).T

    df['TIME'] = time_tickers
    df.set_index('TIME', inplace=True)

    df.to_csv(f'{str(datetime.now().replace(microsecond=0)).replace(":", "-")}.csv')

    print(f'From {str(time_tickers.iloc[0]).split(" ")[0]} to {str(time_tickers.iloc[-1]).split(" ")[0]}')


if __name__ == '__main__':
    symbols = init()
    convert_csv(TIME_FRAME, BARS)
