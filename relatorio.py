from fpdf import FPDF

def gerar_relatorio(ticker: str, caminho_grafico: str):
    """
    Gera um relatório em PDF com informações detalhadas e gráficos.
    """
    pdf = FPDF()
    pdf.add_page()

    pdf.set_font("Arial", "B", 16)
    pdf.cell(0, 10, f"Relatório de Análise: {ticker}", ln=True, align="C")

    pdf.set_font("Arial", size=12)
    pdf.ln(10)
    pdf.cell(0, 10, f"Maior preço de fechamento: 150.00 (Exemplo)", ln=True)
    pdf.cell(0, 10, f"Menor preço de fechamento: 100.00 (Exemplo)", ln=True)
    pdf.cell(0, 10, f"Média de fechamento: 120.00 (Exemplo)", ln=True)

    pdf.ln(10)
    pdf.cell(0, 10, "Gráfico de desempenho:", ln=True)
    pdf.image(caminho_grafico, x=10, y=pdf.get_y(), w=180)

    pdf.output(f"relatorio_{ticker}.pdf")
    print(f"Relatório gerado: relatorio_{ticker}.pdf")

