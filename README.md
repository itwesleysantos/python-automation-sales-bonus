# 🚀 Análise e Automação de Bônus por Vendas (`AnáliseBonusViagem`)

## 💡 Descrição do Projeto

Este projeto em Python demonstra uma automação de análise de dados. Ele foi desenvolvido para ler relatórios de vendas em Excel de forma sequencial e identificar o **primeiro** vendedor que atingir uma meta de bonificação especial, enviando uma notificação imediata via SMS.

### 🎯 O Desafio

Uma empresa possui 1000 vendedores, com dados de vendas separados em 6 planilhas mensais (Janeiro a Junho). A política é: **o primeiro vendedor que alcançar mais de R$ 55.000,00 em vendas ganha uma viagem**. O sistema deve monitorar os arquivos e alertar o gerente por SMS assim que a meta for batida.

### ✅ Solução Implementada

O script (`main.py`) utiliza a biblioteca **Pandas** para ler os 6 arquivos `.xlsx`. Assim que a condição de vendas > R$ 55.000,00 é atendida, ele captura o nome do vendedor e o valor exato, e utiliza a API **Twilio** para enviar um SMS de alerta.

## 💻 Tecnologias Utilizadas

* **Python 3**
* **Pandas:** Para manipulação e leitura de dados de arquivos Excel (`.xlsx`).
* **Twilio API:** Para o envio programático da mensagem SMS.

## ⚙️ Como Executar o Projeto

### Pré-requisitos
1.  **Python 3** instalado.
2.  Credenciais e um número de telefone da conta **Twilio**.

### 1. Estrutura de Arquivos

Certifique-se de que todos os arquivos Excel (`janeiro.xlsx`, `fevereiro.xlsx`, etc.) estejam na mesma pasta que o arquivo **`main.py`**.

### 2. Instalação de Dependências

Abra o terminal na pasta raiz do projeto (`AnáliseBonusViagem`) e instale as bibliotecas listadas no `requirements.txt`:

```bash
pip install -r requirements.txt
