import pandas as pd

def calcular_sma_20(df, periodo=20):
    if 'Close' not in df.columns:
        raise ValueError("A coluna 'Close' é necessária para calcular a SMA.")
    return calcular_medias_moveis(df, janela_sma=periodo)

def calcular_rsi(df, periodo=14):
    if 'Close' not in df.columns:
        raise ValueError("A coluna 'Close' é necessária para calcular o RSI.")
    delta = df['Close'].diff()
    ganho = delta.where(delta > 0, 0).rolling(window=periodo).mean()
    perda = -delta.where(delta < 0, 0).rolling(window=periodo).mean()
    rs = ganho / perda
    df['RSI'] = 100 - (100 / (1 + rs))
    return df

def calcular_bandas_bollinger(df, periodo=20):
    if 'Close' not in df.columns:
        raise ValueError("A coluna 'Close' é necessária para calcular as Bandas de Bollinger.")
    media = df['Close'].rolling(window=periodo).mean()
    std = df['Close'].rolling(window=periodo).std()
    df['Upper_BB'] = media + 2 * std
    df['Lower_BB'] = media - 2 * std
    return df

def calcular_medias_moveis(df, janela_sma=20):
    if 'Close' not in df.columns:
        raise ValueError("A coluna 'Close' é necessária para calcular as médias móveis.")
    df[f'SMA_{janela_sma}'] = df['Close'].rolling(window=janela_sma).mean()
    return df

