from scraping import obtendo_dados
from mongo import salvando

dados = obtendo_dados()
print("Dados obtidos com sucesso.")
salvando(dados)
print("Processo de salvamento concluído.")
