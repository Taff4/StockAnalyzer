# StockAnalyzer 📈

🚧 **Projeto em Construção** 🚧  
Este projeto está em desenvolvimento e novas funcionalidades serão adicionadas em breve.

---

## **Descrição**
O **StockAnalyzer** é uma ferramenta Python projetada para analisar dados financeiros de ações. Ele coleta dados, calcula indicadores técnicos, gera gráficos e cria relatórios detalhados para auxiliar na tomada de decisões no mercado financeiro.

---

## **Recursos**
- **Coleta de Dados**: Integração com a API `yfinance` para busca de dados históricos.
- **Indicadores Técnicos**:
  - RSI (Índice de Força Relativa)
  - Bandas de Bollinger
  - Médias Móveis Simples (SMA)
- **Visualização Gráfica**: Criação de gráficos interativos com `matplotlib`.
- **Relatórios em PDF**: Relatórios detalhados com gráficos e análises.
- **Interface Gráfica**: Interface construída com `tkinter`.

---

## **Status do Projeto**
🚧 Este projeto está em desenvolvimento. Algumas funcionalidades podem estar incompletas ou sujeitas a alterações.

---

## **Estrutura do Projeto**

Abaixo está a estrutura principal do projeto:

```plaintext
StockAnalyzer/
├── src/
│   ├── main.py              # Ponto de entrada do programa
│   ├── coleta_dados.py      # Módulo para coleta de dados via yfinance
│   ├── indicadores.py       # Funções para cálculo de indicadores técnicos
│   ├── graficos.py          # Funções para geração de gráficos
│   ├── relatorios.py        # Criação de relatórios em PDF
│   ├── gui.py               # Interface gráfica do programa
│   ├── exportar_dados.py    # Funções para exportação de dados em CSV
├── tests/                   # Pasta para testes unitários
│   ├── test_coleta_dados.py
│   ├── test_indicadores.py
├── .gitignore               # Arquivo de exclusões do Git
├── LICENSE                  # Licença do projeto
├── README.md                # Documentação principal
├── requirements.txt         # Lista de dependências

---

## **Como Usar**

### **1. Pré-requisitos**
- Tenha o Python 3.7 ou superior instalado em seu sistema.
- Instale as dependências do projeto executando o seguinte comando no terminal:
  ```bash
  pip install -r requirements.txt
  python src/main.py
  python src/gui.py

---

Esse trecho está formatado para renderizar corretamente no GitHub, com blocos de código destacados e divisões claras entre as seções. Copie e cole diretamente no seu arquivo `README.md`. Se precisar de mais ajuda, é só pedir! 😊



