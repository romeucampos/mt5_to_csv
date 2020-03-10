from datetime import datetime
import json

import pandas as pd
import MetaTrader5 as mt5

TEST = True # Testar se o metatrader5 consegue carregar as barras. Recomendado na primeira vez que for rodar o script.
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


def test_symbols(timeframe=mt5.TIMEFRAME_D1, bars=1000):
    print('Init test bars...')
    [print(symbol, mt5.copy_rates_from_pos(symbol, timeframe, 0, bars)[-1][4], '"BARS OK"') for symbol in symbols]


def convert_csv(timeframe=mt5.TIMEFRAME_D1, bars=1000):
    print('Convert...')
    symbol_one = pd.DataFrame(mt5.copy_rates_from_pos(symbols[0], timeframe, 0, bars))
    time_tickers = pd.to_datetime(symbol_one['time'], unit='s')

    tickers_close = [pd.DataFrame(mt5.copy_rates_from_pos(symbol, mt5.TIMEFRAME_D1, 0, bars))['close'].rename(index=symbol) for symbol in symbols]

    mt5.shutdown()

    df = pd.DataFrame(tickers_close).T

    df['TIME'] = time_tickers
    df.set_index('TIME', inplace=True)
    df.to_csv(f'{str(datetime.now().replace(microsecond=0)).replace(":", "-")}.csv')
    
    print(df.columns.tolist())
    print('Conclusion...')


if __name__ == '__main__':
    symbols = init()

    if TEST:
        test_symbols(TIME_FRAME, BARS)
    convert_csv(TIME_FRAME, BARS)
