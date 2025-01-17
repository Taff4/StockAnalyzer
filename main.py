import os
from coleta_dados import coletar_dados_acao
from Indicadores import calcular_rsi, calcular_bandas_bollinger, calcular_sma_20, calcular_medias_moveis
from graficos import gerar_grafico
from relatorio import gerar_relatorio
from exportar_dados import exportar_para_csv


def limpar_tela():
    """
    Limpa a tela do console.
    """
    os.system('cls' if os.name == 'nt' else 'clear')


def listar_acoes_disponiveis():
    """
    Exibe uma lista de ações populares para consulta.
    """
    limpar_tela()
    acoes = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NFLX", "NVDA"]
    print("\nAções disponíveis para consulta:")
    for acao in acoes:
        print(f"- {acao}")
    input("\n\nPressione Enter para voltar ao menu...")  # Adiciona um espaço antes


def consultar_acoes(tickers):
    """
    Executa o fluxo principal para uma ou mais ações específicas.
    """
    limpar_tela()
    dados_acoes = {}
    for ticker in tickers:
        print(f"\nIniciando análise para a ação: {ticker}")

        # Coleta os dados históricos da ação
        print("Coletando dados...")
        df = coletar_dados_acao(ticker)

        # Calcular indicadores
        print("Calculando indicadores técnicos...")
        df = calcular_sma_20(df)
        df = calcular_medias_moveis(df, janela_sma=50)
        df = calcular_rsi(df)
        df = calcular_bandas_bollinger(df)

        # Remover fuso horário, se houver
        for col in df.select_dtypes(include=['datetime']):
            if df[col].dt.tz is not None:
                df[col] = df[col].dt.tz_localize(None)

        # Gerar gráfico
        print("Gerando gráfico de desempenho...")
        gerar_grafico(df, ticker)

        # Gerar relatório PDF
        print("Criando relatório em PDF...")
        gerar_relatorio(ticker, f"grafico_{ticker}.png")

        # Armazenar o DataFrame atualizado
        dados_acoes[ticker] = df

    # Exportar dados para CSV
    print("\nExportando dados para arquivos CSV...")
    exportar_para_csv(dados_acoes)

    print("\nAnálise concluída! Verifique os relatórios PDF e os arquivos CSV gerados.")
    input("\n\nPressione Enter para voltar ao menu...")  # Adiciona um espaço antes


def abrir_gui():
    """
    Abre a interface gráfica.
    """
    limpar_tela()
    print("Abrindo GUI...")
    try:
        from gui import main  # Certifique-se de que o GUI tem uma função chamada "main"
        main()
    except ImportError as e:
        print(f"Erro ao importar o GUI: {e}")
    except Exception as e:
        print(f"Ocorreu um erro ao abrir o GUI: {e}")
    input("\n\nPressione Enter para voltar ao menu...")  # Adiciona um espaço antes


def menu():
    """
    Menu interativo do programa.
    """
    while True:
        limpar_tela()
        print("\nMenu Principal")
        print("1. Listar ações disponíveis")
        print("2. Consultar ações específicas")
        print("3. Abrir interface gráfica (GUI)")
        print("4. Sair")
        opcao = input("\nEscolha uma opção: ")

        if opcao == "1":
            listar_acoes_disponiveis()
        elif opcao == "2":
            tickers = input("Digite os códigos das ações separados por vírgula: ").upper().split(",")
            tickers = [ticker.strip() for ticker in tickers]
            consultar_acoes(tickers)
        elif opcao == "3":
            abrir_gui()
        elif opcao == "4":
            print("Saindo do programa. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")
            input("\n\nPressione Enter para continuar...")  # Adiciona um espaço antes


if __name__ == "__main__":
    menu()

