import yfinance as yf
import time

def coletar_dados_acao(ticker: str, periodo="6mo"):
    """
    Coleta dados históricos da ação usando o yfinance.

    Parâmetros:
    - ticker (str): Código do ativo (ex.: 'AAPL').
    - periodo (str): Período para coleta (ex.: '6mo', '1y').

    Retorna:
    - DataFrame com os dados históricos.
    """
    try:
        print(f"Coletando dados para {ticker}...")
        acao = yf.Ticker(ticker)
        df = acao.history(period=periodo)

        # Validar se os dados retornaram algo
        if df.empty:
            print(f"Erro: Não foram encontrados dados para o ticker '{ticker}'.")
            return None

        # Resetar índice e retornar o DataFrame
        df.reset_index(inplace=True)
        time.sleep(1)  # Tempo de espera entre requisições
        return df

    except Exception as e:
        print(f"Erro ao coletar dados para {ticker}: {e}")
        return None

