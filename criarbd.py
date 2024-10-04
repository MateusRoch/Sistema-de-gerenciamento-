#importando sqlite
import sqlite3 as lite

#criando conexão
con = lite.connect("dados.db")

#criando tabela
with con:
    cursor = con.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS inventorio(id INTEGER PRIMARY KEY AUTOINCREMENT, nome TEXT, local TEXT, descrição TEXT, marca TEXT, data_da_compra DATE, valor_da_compra DECIMAL, serie TEXT, imagem TEXT)")