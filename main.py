import pandas as pd
from twilio.rest import Client

# Your Account SID and Auth Token from console.twilio.com
account_sid = "XXXXXXXXXXXXXXXXXXXXXXX"
auth_token  = "XXXXXXXXXXXXXXXXXXXXXXX"
client = Client(account_sid, auth_token)

# Abre os 6 arquivos em Excel
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

# Para cada arquivo, verificar se algum valor na coluna Vendas dos arquivos é maior que 55.000
# Se for maior que 55.000, envia um SMS com o mês, o nome do vendedor e o valor vendido
for mes in lista_meses:
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    if (tabela_vendas['Vendas'] > 55000).any():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        print(f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        message = client.messages.create(
            to="+XXXXXXXXXXX",
            from_="+XXXXXXXXXXX",
            body=f'No mês de {mes} alguém bateu a meta. Vendedor: {vendedor}, Vendas: {vendas}')
        print(message.sid)