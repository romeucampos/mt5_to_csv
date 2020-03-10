## mt5 to csv
Script para converter os dados do metratrader5 em csv.\
Forex ou B3.

### Installation
```bash
git clone https://github.com/romeucampos/mt5_to_csv.git
cd mt5_to_csv
pip install -r requirements.txt
```
### Basic Usage
Abra o metatrader5, depois execulte o script, na primeira vez
que execultar, provavelmente ira demorar um pouco, por que o metatrader5 ira baixar os dados das barras para seu banco de dados interno. Mas nas próximas vezes será em segundos.
```bash
python mt5_to_csv.py
```

### Config
Pode-se configurar os seguites parâmetros, no arquivo mt5_to_csv.py. 

```python
TEST = True # Testar se o metatrader5 consegue carregar as barras. Recomendado na primeira vez que for rodar o script.
TIME_FRAME = mt5.TIMEFRAME_D1  # Timeframe que desejar. Veja no link https://www.mql5.com/en/docs/integration/python_metatrader5/mt5copyratesfrom_py
BARS = 1000 # Número de barras
```

### Symbols
Pode-se usar os symbols dos ativos que estão disponíveis na metatrader5 seja FOREX ou B3. Pode adicionar ou remover os símbolos que precisar no arquivo symbols.txt dentro dos colchetes.
```txt
[

"AUDCAD", 
"AUDUSD",
"EURAUD",
"EURCAD",
"EURCHF",
"EURGBP",
"EURJPY",
"EURUSD",
"GBPCHF",
"GBPJPY",
"GBPUSD",
"USDCAD",
"USDCHF",
"USDJPY"

]
```