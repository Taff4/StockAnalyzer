import tkinter as tk
from tkinter import messagebox


from main import consultar_acoes, listar_acoes_disponiveis, comparar_acoes
print("Inicializando GUI...")

def executar_listar_acoes():
    """
    Exibe uma lista de ações disponíveis.
    """
    acoes = ["AAPL", "MSFT", "GOOGL", "AMZN", "TSLA", "META", "NFLX", "NVDA"]
    messagebox.showinfo("Ações Disponíveis", "\n".join(acoes))


def executar_consultar_acoes():
    """
    Permite ao usuário consultar ações específicas.
    """
    tickers = entrada_tickers.get()
    if not tickers:
        messagebox.showerror("Erro", "Por favor, insira os códigos das ações.")
        return

    try:
        tickers = [ticker.strip().upper() for ticker in tickers.split(",")]
        consultar_acoes(tickers)
        messagebox.showinfo("Sucesso", "Análise concluída! Verifique os relatórios gerados.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro durante a análise:\n{str(e)}")


def executar_comparar_acoes():
    """
    Permite ao usuário comparar o desempenho de ações.
    """
    tickers = entrada_tickers.get()
    if not tickers:
        messagebox.showerror("Erro", "Por favor, insira os códigos das ações para comparar.")
        return

    try:
        tickers = [ticker.strip().upper() for ticker in tickers.split(",")]
        comparar_acoes(tickers)
        messagebox.showinfo("Sucesso", "Comparação concluída! Verifique os resultados.")
    except Exception as e:
        messagebox.showerror("Erro", f"Ocorreu um erro durante a comparação:\n{str(e)}")


def sair_do_programa():
    """
    Encerra a aplicação.
    """
    if messagebox.askyesno("Sair", "Deseja realmente sair?"):
        janela.destroy()


# Criar a janela principal
janela = tk.Tk()
janela.title("Ferramenta de Análise de Ações")
janela.geometry("500x300")  # Ajuste do tamanho da janela

# Adicionar o título
tk.Label(janela, text="Ferramenta de Análise de Ações", font=("Arial", 16, "bold")).pack(pady=10)

# Campo de entrada para os tickers
tk.Label(janela, text="Digite os códigos das ações (separados por vírgula):").pack(pady=5)
entrada_tickers = tk.Entry(janela, width=50)
entrada_tickers.pack(pady=5)

# Botões para funcionalidades do menu
botao_listar = tk.Button(janela, text="Listar Ações Disponíveis", command=executar_listar_acoes, bg="blue", fg="white")
botao_listar.pack(pady=5)

botao_consultar = tk.Button(janela, text="Consultar Ações", command=executar_consultar_acoes, bg="green", fg="white")
botao_consultar.pack(pady=5)

botao_comparar = tk.Button(janela, text="Comparar Ações", command=executar_comparar_acoes, bg="orange", fg="white")
botao_comparar.pack(pady=5)

botao_sair = tk.Button(janela, text="Sair", command=sair_do_programa, bg="red", fg="white")
botao_sair.pack(pady=20)

# Rodar a interface
janela.mainloop()

