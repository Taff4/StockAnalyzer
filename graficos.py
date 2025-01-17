import matplotlib.pyplot as plt
import matplotlib.dates as mdates

def gerar_grafico(df, ticker):
    """
    Gera um gráfico com os preços de fechamento e indicadores técnicos.
    """
    plt.figure(figsize=(12, 6))

    # Plotando preços e indicadores
    plt.plot(df['Date'], df['Close'], label='Preço de Fechamento', color='blue', linewidth=2)
    if 'SMA_20' in df.columns:
        plt.plot(df['Date'], df['SMA_20'], label='Média Móvel 20', linestyle='--', color='green', linewidth=2)
    if 'SMA_50' in df.columns:
        plt.plot(df['Date'], df['SMA_50'], label='Média Móvel 50', linestyle='--', color='orange', linewidth=2)
    if 'Upper_BB' in df.columns and 'Lower_BB' in df.columns:
        plt.fill_between(df['Date'], df['Upper_BB'], df['Lower_BB'], color='red', alpha=0.1, label='Bandas de Bollinger')

    # Ajustando eixo de datas
    plt.gca().xaxis.set_major_locator(mdates.AutoDateLocator())
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m-%Y'))
    plt.gcf().autofmt_xdate()

    # Adicionando títulos e legendas
    plt.title(f"Análise de Ação - {ticker}", fontsize=16)
    plt.xlabel("Data", fontsize=12)
    plt.ylabel("Preço / Indicadores", fontsize=12)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.5)
    plt.tight_layout()

    # Salvando o gráfico
    plt.savefig(f"grafico_{ticker}.png")
    plt.close()

