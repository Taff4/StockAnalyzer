import pandas as pd
import os

def exportar_para_csv(dados: dict, pasta_saida: str = "dados_acoes"):
    """
    Exporta os dados de múltiplas ações para arquivos CSV.

    Parâmetros:
    - dados (dict): Dicionário com os dados das ações, onde a chave é o ticker e o valor é o DataFrame.
    - pasta_saida (str): Caminho onde os arquivos CSV serão salvos.
    """
    try:
        # Verifica se há dados para exportar
        if not dados:
            print("Nenhum dado disponível para exportação.")
            return

        # Cria o diretório se não existir
        if not os.path.exists(pasta_saida):
            os.makedirs(pasta_saida)
            print(f"Pasta '{pasta_saida}' criada para salvar os arquivos CSV.")

        # Salva cada DataFrame em um arquivo CSV
        for ticker, df in dados.items():
            if df.empty:
                print(f"Dados para o ticker '{ticker}' estão vazios. Pulando exportação.")
                continue

            # Converter colunas datetime para string
            for col in df.select_dtypes(include=["datetime"]):
                df[col] = df[col].astype(str)

            # Caminho do arquivo CSV
            caminho_arquivo = os.path.join(pasta_saida, f"{ticker}.csv")

            # Exporta para CSV
            df.to_csv(caminho_arquivo, index=False)
            print(f"Arquivo CSV gerado: {caminho_arquivo} com {len(df)} linhas.")

        print("Exportação para CSV concluída com sucesso!")

    except Exception as e:
        print(f"Erro ao exportar dados: {e}")

