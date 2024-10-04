#importando sqlite
import sqlite3 as lite

#criando conexão
con = lite.connect("dados.db")


#Inserir dados
def inserir_form(i):
    with con:
        cursor = con.cursor()
        query = ("INSERT INTO inventorio(nome, local, descrição, marca, data_da_compra, valor_da_compra, serie, "
                 "imagem) VALUES(?,?,?,?,?,?,?,?)")
        cursor.execute(query, i)

 #Atualizar dados
def atualizar_form(i):
    with con:
        cursor = con.cursor()
        query = ("UPDATE inventorio SET nome=?, local=?, descrição=?, marca=?, data_da_compra=?, valor_da_compra=?, "
                 "serie=?,"
                 "imagem=? WHERE id=?")
        cursor.execute(query, i)


#Deletar dados
def deletar_form(i):
    with con:
        cursor = con.cursor()
        query = "DELETE FROM inventorio WHERE id=?"
        cursor.execute(query, i)


#Ver dados
def ver_form():
    ver_dados = []
    with con:
        cursor = con.cursor()
        query = "SELECT * FROM inventorio"
        cursor.execute(query)

        filas = cursor.fetchall()
        for fila in filas:
            ver_dados.append(fila)
    return ver_dados


#Ver dados individual
def ver_item(id):
    ver_dados_individuais = []
    with con:
        cursor = con.cursor()
        query = "SELECT * FROM inventorio WHERE id=?"
        cursor.execute(query, id)

        filas = cursor.fetchall()
        for fila in filas:
            ver_dados_individuais.append(fila)
    return ver_dados_individuais