import pandas as pd
import tkinter as tk
from tkinter import *
import awesometkinter as atk
from tkinter import messagebox


# Criando janela -------------------------------------------------------
janela = tk.Tk()
janela.title('Funcinarios Central')
janela.geometry('400x490')
janela.configure( bg='#fff')
lista = pd.read_excel('Central_de_funcionarios_T.xlsx')

# Cadastrar ------------------------------------------------------

def Cadastrar():

    janela2 = tk.Toplevel()
    janela2.title('cadastrar funcionario')
    janela2.geometry('400x490')
    janela2.configure( bg='#fff')
    
    # Frame cima 2 -----------------------------------------------------------

    frame1 = Frame(janela2, width=400, height=49, bg='#000')
    frame1.place(x=0, y=0)
    l_titulo = Label(frame1, text='CADASTRO', bg='#000', fg='#fff', font='Anton 16 bold')
    l_titulo.place(x=150, y=14)

    # Frame meio 2 -----------------------------------------------------------

    frame2 = Frame(janela2, width=400, height=401, bg='#eee')
    frame2.place(x=0, y=49)

    n_label = tk.Label(frame2, text='Nome*', bg='#eee', justify='center', width=15)
    n_label.place(x=55, y=35)

    n_entry = tk.Entry(frame2, width=20, justify='center')
    n_entry.place(x=45,y=55)

    i_label = tk.Label(frame2, text='Idade*', bg='#eee', justify='center', width=15)
    i_label.place(x=55, y=80)

    i_entry = tk.Entry(frame2,  width=20, justify='center')
    i_entry.place(x=45, y=100)
    
    cpf_label = tk.Label(frame2, text='CPF*', bg='#eee', justify='center', width=15)
    cpf_label.place(x=55, y=125)

    cpf_entry = tk.Entry(frame2,  width=20, justify='center')
    cpf_entry.place(x=45, y=145)
    
    e_label = tk.Label(frame2, text='Endereço*', bg='#eee', justify='center', width=15)
    e_label.place(x=55, y=170)

    e_entry = tk.Entry(frame2,  width=20, justify='center')
    e_entry.place(x=45, y=190)
    
    em_label = tk.Label(frame2, text='E-mail*', bg='#eee', justify='center', width=15)
    em_label.place(x=55, y=215)

    em_entry = tk.Entry(frame2,  width=20, justify='center')
    em_entry.place(x=45, y=235)
    
    t_label = tk.Label(frame2, text='Telefone*', bg='#eee', justify='center', width=15)
    t_label.place(x=55, y=260)

    t_entry = tk.Entry(frame2,  width=20, justify='center')
    t_entry.place(x=45, y=280)
    
    s_label = tk.Label(frame2, text='Salario*', bg='#eee', justify='center', width=15)
    s_label.place(x=245, y=35)

    s_entry = tk.Entry(frame2, width=20, justify='center')
    s_entry.place(x=235,y=55)

    f_label = tk.Label(frame2, text='Função*', bg='#eee', justify='center', width=15)
    f_label.place(x=245, y=80)

    f_entry = tk.Entry(frame2, width=20, justify='center')
    f_entry.place(x=235, y=100)
    
    c_label = tk.Label(frame2, text='Contratação*', bg='#eee', justify='center', width=15)
    c_label.place(x=245, y=125)

    c_entry = tk.Entry(frame2, width=20, justify='center')
    c_entry.place(x=235, y=145)

    # Frame baixo 2 -----------------------------------------------------------

    frame3 = Frame(janela2, width=400, height=40, bg='#000')
    frame3.place(x=0, y=450)

    l_rodape= Label(frame3, bg='#000', fg='#fff', text='created by Edmar Lelis L. JR.', font='Alereya 8 bold italic')
    l_rodape.place(x=120, y=10)
    
# configurando 2° etapa ------------------------------------------------------

    def segundaEtapa():
        try:
            nome = n_entry.get()
            idade = i_entry.get()
            cpf = cpf_entry.get()
            endereco = e_entry.get()
            email = em_entry.get()
            telefone = t_entry.get()
            salario = s_entry.get()
            funcao = f_entry.get()
            contratacao = c_entry.get()

            lista = pd.read_excel('Central_de_funcionarios_T.xlsx')
            lista.loc[len(lista)] = [len(lista),nome, int(idade),  cpf, endereco, email, telefone,int(salario), funcao, contratacao]
            del lista['Unnamed: 0']
            lista.to_excel('Central_de_funcionarios_T.xlsx')
            messagebox.showinfo( title='Sucesso', message=f'{nome} foi cadastrado com sucesso!')
            janela2.destroy()
            
        except:
            messagebox.showerror( title='erro', message=f'Não foi possível cadastrar, houve um erro!')

# finalizar cadastros ------------------------------------------------------

    b_proximo = atk.Button3d(frame2, text= 'Cadastrar', bg='#000', fg='#fff', command= segundaEtapa)
    b_proximo.place(x=160, y=340)


# Procurar ------------------------------------------------------

def Procurar():
    janela3 = tk.Toplevel()
    janela3.title('cadastrar funcionario')
    janela3.geometry('400x490')
    janela3.configure( bg='#eee')

    # Frame cima 3 -----------------------------------------------------------

    frame1 = Frame(janela3, width=400, height=49, bg='#000')
    frame1.place(x=0, y=0)
    l_titulo = Label(frame1, text='Procurar Funcinario', bg='#000', fg='#fff', font='Anton 16 bold')
    l_titulo.place(x=100, y=14)

    # Frame meio 3 -----------------------------------------------------------

    frame2 = Frame(janela3, width=400, height=401, bg='#eee')
    frame2.place(x=0, y=49)

    p_label = tk.Label(frame2, text='CPF*', bg='#eee', fg='#000', font='Alereya 8 bold')
    p_label.place(x=190, y=40)
    p_entry = tk.Entry(frame2, width=20, justify='center')
    p_entry.place(x=140, y=60)

    def procura():
        #try:
        procurar = p_entry.get()
        try:
            del lista['Unnamed: 0']
        except:
            passkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkkk
        cpf_df = lista.loc[lista['CPF'] == f'{procurar}']
        print(cpf_df)


        n = cpf_df['NOME']
        nome = n[0]
        i = cpf_df['IDADE']
        idade= i[0]
        cpf_lista = cpf_df['CPF']
        cpf= cpf_lista[0]
        #e = cpf_df['ENDERECO']
        #endereco = e[0]
        #em = cpf_df['EMAIL']
        #email = em[0]
        t = cpf_df['TELEFONE']
        telefone = t[0]
        #s = cpf_df['SALARIO']
        #salario = s[0]
        #f = cpf_df['FUNCAO']
        #funcao = f[0]
        c = cpf_df['CONTRATACAO']
        contratacao = c[0]

        messagebox.showinfo(title='Sucesso!', message=f'Funcionaro {nome} encontrado!')

        limpar_label = tk.Label(frame2, text=f'', bg='#eee', fg='#000', font='Alereya 8 bold', width=400, height=300)
        limpar_label.place(x=0, y=150)
        p_n_label = tk.Label(frame2, text=f'Nome: {nome}', bg='#eee', fg='#000', font='Alereya 8 bold')
        p_n_label.place(x=0, y=150)
        p_i_label = tk.Label(frame2, text=f'Idade: {idade}', bg='#eee', fg='#000', font='Alereya 8 bold')
        p_i_label.place(x=0, y=170)
        p_cpf_label = tk.Label(frame2, text=f'CPF: {cpf}', bg='#eee', fg='#000', font='Alereya 8 bold')
        p_cpf_label.place(x=0, y=190)
        #p_e_label = tk.Label(frame2, text=f'Endereço: {endereco}', bg='#eee', fg='#000', font='Alereya 8 bold')
        #p_e_label.place(x=0, y=210)
        #p_em_label = tk.Label(frame2, text=f'E-mail: {email}', bg='#eee', fg='#000', font='Alereya 8 bold')
        #p_em_label.place(x=0, y=230)
        p_t_label = tk.Label(frame2, text=f'Telefone: {telefone}', bg='#eee', fg='#000', font='Alereya 8 bold')
        p_t_label.place(x=0, y=250)
        p_f_label = tk.Label(frame2, text=f'Função: {funcao}', bg='#eee', fg='#000', font='Alereya 8 bold')
        p_f_label.place(x=0, y=270)
        #p_s_label = tk.Label(frame2, text=f'Saláro: {salario}', bg='#eee', fg='#000', font='Alereya 8 bold')
        #p_s_label.place(x=0, y=290)
        p_c_label = tk.Label(frame2, text=f'Contratação: {contratacao}', bg='#eee', fg='#000', font='Alereya 8 bold')
        p_c_label.place(x=0, y=310)

        #except:
            #limpar_label = tk.Label(frame2, text=f'', bg='#eee', fg='#000', font='Alereya 8 bold', width=400, height=300)
            #limpar_label.place(x=0, y=150)
            #messagebox.showerror(title='ERRO', message='Não encntrado! Lembre-se de colocar os "." e o "-" de forma correta!')

    # possivelmente colocar informações em outro frame.

    p_button = atk.Button3d(frame2, text= 'Procurar', bg='#000', fg='#fff', command= procura)
    p_button.place(x=155, y=90)

    # Frame baixo 3 -----------------------------------------------------------

    frame3 = Frame(janela3, width=400, height=40, bg='#000')
    frame3.place(x=0, y=450)

    l_rodape= Label(frame3, bg='#000', fg='#fff', text='created by Edmar Lelis L. JR.', font='Alereya 8 bold italic')
    l_rodape.place(x=120, y=10)


# Frame cima 1 -----------------------------------------------------------

frame1 = Frame(janela, width=400, height=49, bg='#000')
frame1.place(x=0, y=0)
l_titulo = Label(frame1, text='CENTRAL DE FUNCIONÁRIOS', bg='#000', fg='#fff', font='Anton 16 bold')
l_titulo.place(x=55, y=14)

# Frame meio 1 -----------------------------------------------------------

frame2 = Frame(janela, width=400, height=401, bg='#eee')
frame2.place(x=0, y=49)

cadatrar = atk.Button3d(frame2, text= 'Cadastrar', bg='#000', fg='#fff', command= Cadastrar)
cadatrar.place(x=160, y=64)

procurar = atk.Button3d(frame2, text= 'Procurar', bg='#000', fg='#fff', command= Procurar)
procurar.place(x=160, y=164)

contato = atk.Button3d(frame2, text= 'Contato', bg='#000', fg='#fff', command= Cadastrar)
contato.place(x=160, y=264)

# Frame baixo 1 -----------------------------------------------------------

frame3 = Frame(janela, width=400, height=40, bg='#000')
frame3.place(x=0, y=450)

l_rodape= Label(frame3, bg='#000', fg='#fff', text='created by Edmar Lelis L. JR.', font='Alereya 8 bold italic')
l_rodape.place(x=120, y=10)

janela.mainloop()