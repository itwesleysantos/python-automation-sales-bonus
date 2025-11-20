# 🐍 Python: Automação de Análise de Vendas e Notificação de Bônus por SMS

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
2.  Ter uma conta **Twilio** ativa.
3.  Instalar as dependências listadas no `requirements.txt`.

### 1. Estrutura de Arquivos

Certifique-se de que todos os arquivos Excel (`janeiro.xlsx`, `fevereiro.xlsx`, etc.) estejam na mesma pasta que o seu arquivo Python (ex: `main.py` ou `vendas_automatica.py`).

### 2. Instalação de Dependências

Abra o terminal na pasta raiz do projeto e instale as bibliotecas necessárias:

```bash
pip install -r requirements.txt
```

### 3. Configuração de Credenciais 🔑

⚠️ ATENÇÃO: O código contém placeholders (valores genéricos) nas credenciais e números de telefone por segurança.

I. Para rodar o projeto, você DEVE editar o arquivo Python e substituir os placeholders (ex: XXXXXXXXX...) pelas suas credenciais e números de telefone válidos da Twilio:

* account_sid e auth_token: Seus tokens Twilio.

* to: Número de telefone do destinatário.

* from_: Seu número de telefone Twilio.

II. Após configurar as credenciais, execute o programa a partir do terminal:

```bash
python main.py ou python outronome.py, dependendo de qual tenha sido o nome dada ao seu arquivo.
```
O programa irá parar a execução assim que o primeiro vendedor for encontrado, respeitando a regra do bônus.

## 🤝 Contato

Desenvolvido por: **Wesley Santos**

| Plataforma | Link |
| :--- | :--- |
| **LinkedIn** | https://www.linkedin.com/in/itwesleysantos/ |
| **GitHub** | https://github.com/itwesleysantos |
