from tkinter import*
from tkinter import Tk, StringVar, ttk, messagebox
from tkinter import filedialog as fd
from PIL import Image, ImageTk
from tkcalendar import Calendar, DateEntry
from datetime import date

# importando view
from view import *

#cores

co0 = "#2e2d2b"  # Preta
co1 = "#feffff"  # branca
co2 = "#4fa882"  # Verde
co3 = "#38576b"  # valor
co4 = "#403d33"  # letra
co5 = "#e06636"  # profit
co6 = "#038cfc"  # azul
co7 = "#3fbfb9"  # verde
co8 = "#263238"  # + verde
co9 = "#e9edf5"  # + verde

# criando janela
janela = Tk()
janela.title(" ")
janela.geometry("900x600")
janela.configure(background=co9)
janela.resizable(width=FALSE, height=FALSE)

style = ttk.Style(janela)
style.theme_use("clam")

#criando framers
frameCima = Frame(janela, width=1043, height=50, background=co1, relief=FLAT)
frameCima.grid(row=0, column=0)

frameMeio = Frame(janela, width=1043, height=303, background=co1, pady=20, relief=FLAT)
frameMeio.grid(row=1, column=0, pady=1, padx=0, sticky=NSEW)

frameBaixo = Frame(janela, width=1043, height=300, background=co1, relief=FLAT)
frameBaixo.grid(row=2, column=0, pady=0, padx=1, sticky=NSEW)


# criando funções----------
global tree

# FUNÇÃO INSERIR
def inserir():
    global imagem, imagem_string, l_imagem
    nome = e_nome.get()
    local = e_Area.get()
    descricao = e_descricao.get()
    modelo = e_modelo.get()
    data = e_cal.get()
    valor = e_valor.get()
    serie = e_serie.get()
    imagem = imagem_string

    lista_inserir = [nome, local, descricao, modelo, data, valor, serie, imagem]
    for i in lista_inserir:
        if i == "":
            messagebox.showerror("Erro", "Preencha todos os campos")
            return
    inserir_form(lista_inserir)
    messagebox.showinfo("Sucesso", "Os dados foram inseridos com sucesso")

    e_nome.delete(0, "end")
    e_Area.delete(0, "end")
    e_descricao.delete(0, "end")
    e_modelo.delete(0, "end")
    e_cal.delete(0, "end")
    e_valor.delete(0, "end")
    e_serie.delete(0, "end")


    mostrar()

# Função atualizar
def atualizar():
    global imagem, imagem_string, l_imagem
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        teev_lista = treev_dicionario["values"]

        valor = teev_lista[0]
        e_nome.delete(0, "end")
        e_Area.delete(0, "end")
        e_descricao.delete(0, "end")
        e_modelo.delete(0, "end")
        e_cal.delete(0, "end")
        e_valor.delete(0, "end")
        e_serie.delete(0, "end")

        id = int(teev_lista[0])
        e_nome.insert(0, teev_lista[1])
        e_Area.insert(0, teev_lista[2])
        e_descricao.insert(0, teev_lista[3])
        e_modelo.insert(0, teev_lista[4])
        e_cal.insert(0, teev_lista[5])
        e_valor.insert(0, teev_lista[6])
        e_serie.insert(0, teev_lista[7])
        imagem_string = teev_lista[8]

        def update():
            global imagem, imagem_string, l_imagem
            nome = e_nome.get()
            local = e_Area.get()
            descricao = e_descricao.get()
            modelo = e_modelo.get()
            data = e_cal.get()
            valor = e_valor.get()
            serie = e_serie.get()
            imagem = imagem_string

            if imagem == "":
                imagem = e_serie.insert(0, teev_lista[7])
            lista_atualizar = [nome, local, descricao, modelo, data, valor, serie, imagem, id]

            for i in lista_atualizar:
                if i=="":
                    messagebox.showerror("Erro", "Preencha todos os campos")
                    return
            atualizar_form(lista_atualizar)
            messagebox.showinfo("Sucesso", "Os dados foram atualizados com sucesso")

            e_nome.delete(0, "end")
            e_Area.delete(0, "end")
            e_descricao.delete(0, "end")
            e_modelo.delete(0, "end")
            e_cal.delete(0, "end")
            e_valor.delete(0, "end")
            e_serie.delete(0, "end")

            butao_confirmar.destroy()
            mostrar()

        butao_confirmar = Button(frameMeio, command=update, width=13,text="  Confirmar".upper(), overrelief=RIDGE,font=("Ivy 8 bold"), bg=co2, fg=co1)
        butao_confirmar.place(x=330, y=185)

    except IndexError:
        messagebox.showerror("Erro", "Seleciona um dos dados na tabela")


def deletar():
    global imagem, imagem_string, l_imagem
    try:
        treev_dados = tree.focus()
        treev_dicionario = tree.item(treev_dados)
        teev_lista = treev_dicionario["values"]

        valor = teev_lista[0]

        deletar_form([valor])

        messagebox.showinfo("Sucesso", "Os dados foram deletados com sucesso")

        mostrar()

    except IndexError:
        messagebox.showerror("Erro", "Seleciona um dos dados na tabela")


# função para ver imagem
global imagem, imagem_string, l_imagem
def ver_imagem():
    global imagem, imagem_string, l_imagem
    treev_dados = tree.focus()
    treev_dicionario = tree.item(treev_dados)
    teev_lista = treev_dicionario["values"]

    valor = [int(teev_lista[0])]

    iten = ver_item(valor)
    imagem = iten[0][8]

    imagem = Image.open(imagem)
    imagem = imagem.resize((170, 170))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frameMeio, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=700, y=10)


# Função para escolher imagem
global imagem, imagem_string, l_imagem
def escolher_imagem():
    global imagem, imagem_string, l_imagem
    imagem = fd.askopenfilename()
    imagem_string = imagem

    imagem = Image.open(imagem)
    imagem = imagem.resize((170, 170))
    imagem = ImageTk.PhotoImage(imagem)
    l_imagem = Label(frameMeio, image=imagem, bg=co1, fg=co4)
    l_imagem.place(x=700, y=10)


# trabalhando no frame cima



#Abrindo imagem
abri_imagem = Image.open("iconi.png")
abri_imagem = abri_imagem.resize((45,45))
abri_imagem = ImageTk.PhotoImage(abri_imagem)
app_logo = Label(frameCima, image=abri_imagem, text=" Sistema de Gerenciamento", width=900, compound=LEFT, relief=RAISED, anchor=NW, font=("Verdana 20 bold"), bg=co1, fg=co4)
app_logo.place(x=0, y=0)

# trabalhando no frame meio

# criando entradas
l_nome = Label(frameMeio, text="Nome", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_nome.place(x=10, y=10)
e_nome = Entry(frameMeio, width=30, justify="left", relief=SOLID)
e_nome.place(x=130, y=11)

l_Area = Label(frameMeio, text="Área", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_Area.place(x=10, y=40)
e_Area = Entry(frameMeio, width=30, justify="left", relief=SOLID)
e_Area.place(x=130, y=41)

l_descricao = Label(frameMeio, text="Descrição", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_descricao.place(x=10, y=70)
e_descricao = Entry(frameMeio, width=30, justify="left", relief=SOLID)
e_descricao.place(x=130, y=71)

l_modelo = Label(frameMeio, text="Marca/Modelo", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_modelo.place(x=10, y=100)
e_modelo = Entry(frameMeio, width=30, justify="left", relief=SOLID)
e_modelo.place(x=130, y=101)

l_cal = Label(frameMeio, text="Data da compra", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_cal.place(x=10, y=130)
e_cal = DateEntry(frameMeio, width=12, background="darkblue", bordewidth=2, year=2024)
e_cal.place(x=130, y=131)

l_valor = Label(frameMeio, text="Valor da Compra", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_valor.place(x=10, y=160)
e_valor = Entry(frameMeio, width=30, justify="left", relief=SOLID)
e_valor.place(x=130, y=161)

l_serie = Label(frameMeio, text="Número da série", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_serie.place(x=10, y=190)
e_serie = Entry(frameMeio, width=30, justify="left", relief=SOLID)
e_serie.place(x=130, y=191)

# criando botões

# botão carregar
l_carregar = Label(frameMeio, text="Imagem do item", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co1, fg=co4)
l_carregar.place(x=10, y=220)
butao_carregar = Button(frameMeio,command=escolher_imagem, width=29, text="carregar".upper(), compound=CENTER, anchor=CENTER, overrelief=RIDGE, font=("Ivy 8"), bg=co1, fg=co0)
butao_carregar.place(x=130, y=221)

# botão inserir
imagem_adicionar = Image.open("Adicionar.png")
imagem_adicionar = imagem_adicionar.resize((20,20))
imagem_adicionar= ImageTk.PhotoImage(imagem_adicionar)

butao_inserir = Button(frameMeio,command=inserir, image=imagem_adicionar, width=95, text="  Adicionar".upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=("Ivy 8"), bg=co1, fg=co0)
butao_inserir.place(x=330, y=10)

# botão atualizar
imagem_atualizar = Image.open("Atualizar.png")
imagem_atualizar = imagem_atualizar.resize((20,20))
imagem_atualizar= ImageTk.PhotoImage(imagem_atualizar)

butao_atualizar = Button(frameMeio, command=atualizar, image=imagem_atualizar, width=95, text="  Atualizar".upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=("Ivy 8"), bg=co1, fg=co0)
butao_atualizar.place(x=330, y=50)

# botão deletar
imagem_deletar = Image.open("Deletar.png")
imagem_deletar = imagem_deletar.resize((20,20))
imagem_deletar = ImageTk.PhotoImage(imagem_deletar)

butao_atualizar = Button(frameMeio,command=deletar, image=imagem_deletar, width=95, text="  Deletar".upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=("Ivy 8"), bg=co1, fg=co0)
butao_atualizar.place(x=330, y=90)

# botão ver imagem
imagem_item = Image.open("Ver imagem.png")
imagem_item = imagem_item.resize((20,20))
imagem_item = ImageTk.PhotoImage(imagem_item)

butao_item = Button(frameMeio,command=ver_imagem, image=imagem_item, width=95, text="  Ver item".upper(), compound=LEFT, anchor=NW, overrelief=RIDGE, font=("Ivy 8"), bg=co1, fg=co0)
butao_item.place(x=330, y=221)

# Labels Quantidade total de Valores
l_total = Label(frameMeio, text="", width=14, height=2, anchor=CENTER, font=("Ivy 17 bold"), bg=co2, fg=co1)
l_total.place(x=450, y=17)
l_total_ = Label(frameMeio, text="  Valor Total de todos os itens  ", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co2, fg=co1)
l_total_.place(x=450, y=12)


l_quantidade = Label(frameMeio, text="", width=14, height=2, pady=5, anchor=CENTER, font=("Ivy 17 bold"), bg=co2, fg=co1)
l_quantidade.place(x=450, y=90)
l_quantidade_ = Label(frameMeio, text="  Quantidade total de itens  ", height=1, anchor=NW, font=("Ivy 10 bold"), bg=co2, fg=co1)
l_quantidade_.place(x=450, y=92)

# tabela
def mostrar():
    global tree

    #criando uma visualização em árvore com barras de rolagem duplas
    tabela_head = ['#Item','Nome',  'Área','Descrição', 'Marca/Modelo', 'Data da compra','Valor da compra', 'Número de série']

    lista_itens = ver_form()


    tree = ttk.Treeview(frameBaixo, selectmode="extended",columns=tabela_head, show="headings")

    #barra de rolagem vertical
    vsb = ttk.Scrollbar(frameBaixo, orient="vertical", command=tree.yview)

    #barra de rolagem horizontal
    hsb = ttk.Scrollbar(frameBaixo, orient="horizontal", command=tree.xview)

    tree.configure(yscrollcommand=vsb.set, xscrollcommand=hsb.set)
    tree.grid(column=0, row=0, sticky='nsew')
    vsb.grid(column=1, row=0, sticky='ns')
    hsb.grid(column=0, row=1, sticky='ew')
    frameBaixo.grid_rowconfigure(0, weight=12)

    hd=["center","center","center","center","center","center","center", 'center']
    h=[40,150,100,160,130,100,100, 100]
    n=0

    for col in tabela_head:
        tree.heading(col, text=col.title(), anchor=CENTER)
        #ajuste a largura da coluna para a string do cabeçalho
        tree.column(col, width=h[n],anchor=hd[n])
        n+=1


    #inserindo os itens dentro da tabela
    for item in lista_itens:
        tree.insert('', 'end', values=item)


    quantidade = []

    for iten in lista_itens:
        quantidade.append(iten[6])

    Total_valor = sum(quantidade)
    Total_itens = len(quantidade)

    l_total['text'] = 'R$ {:,.2f}'.format(Total_valor)
    l_quantidade['text'] = Total_itens

mostrar()

janela.mainloop()