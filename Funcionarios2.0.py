import pandas as pd
import tkinter as tk
from tkinter import *
import awesometkinter as atk
from os import replace
from tkinter import messagebox
import smtplib
import email.message


# Criando janela -------------------------------------------------------
janela = tk.Tk()
janela.title('Funcinarios Central')
janela.geometry('400x490')
janela.configure( bg='#fff')
lista = pd.read_excel('Central_de_funcionarios_T.xlsx')
janela.resizable(width=False, height=False)

# Cadastrar ------------------------------------------------------

def Cadastrar():

    janela2 = tk.Toplevel()
    janela2.title('cadastrar funcionario')
    janela2.geometry('400x490')
    janela2.configure( bg='#fff')
    janela2.resizable(width=False, height=False)
    
    
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
            try:
                del lista['Unnamed: 0']
            except:
                pass
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
    janela3.title('procurar funcionario')
    janela3.geometry('400x490')
    janela3.configure( bg='#eee')
    janela3.resizable(width=False, height=False)
    
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
        lista = pd.read_excel('Central_de_funcionarios_T.xlsx')
        
        try:
            procurar = p_entry.get()
            try:
                del lista['Unnamed: 0']
            except:
                pass
        
            cpf_df = lista.loc[lista['CPF'] == f'{procurar}']
            numero = int(cpf_df['INDEX'])
            
            n = cpf_df['NOME']
            nome = n[numero]
            i = cpf_df['IDADE']
            idade= i[numero]
            cpf_lista = cpf_df['CPF']
            cpf= cpf_lista[numero]
            e = cpf_df['END']
            endereco = e[numero]
            em = cpf_df['EMA']
            email = em[numero]
            t = cpf_df['TELEFONE']
            telefone = t[numero]
            s = cpf_df['S']
            salario = s[numero]
            f = cpf_df['F']
            funcao = f[numero]
            c = cpf_df['CON']
            contratacao = c[numero]

            messagebox.showinfo(title='Sucesso!', message=f'Funcionaro {nome} encontrado!')

            limpar_label = tk.Label(frame2, text=f'', bg='#eee', fg='#000', font='Alereya 8 bold', width=400, height=300)
            limpar_label.place(x=0, y=150)
            p_n_label = tk.Label(frame2, text=f'Nome: {nome}', bg='#eee', fg='#000', font='Alereya 8 bold')
            p_n_label.place(x=0, y=150)
            p_i_label = tk.Label(frame2, text=f'Idade: {idade}', bg='#eee', fg='#000', font='Alereya 8 bold')
            p_i_label.place(x=0, y=170)
            p_cpf_label = tk.Label(frame2, text=f'CPF: {cpf}', bg='#eee', fg='#000', font='Alereya 8 bold')
            p_cpf_label.place(x=0, y=190)
            p_e_label = tk.Label(frame2, text=f'Endereço: {endereco}', bg='#eee', fg='#000', font='Alereya 8 bold')
            p_e_label.place(x=0, y=210)
            p_em_label = tk.Label(frame2, text=f'E-mail: {email}', bg='#eee', fg='#000', font='Alereya 8 bold')
            p_em_label.place(x=0, y=230)
            p_t_label = tk.Label(frame2, text=f'Telefone: {telefone}', bg='#eee', fg='#000', font='Alereya 8 bold')
            p_t_label.place(x=0, y=250)
            p_f_label = tk.Label(frame2, text=f'Função: {funcao}', bg='#eee', fg='#000', font='Alereya 8 bold')
            p_f_label.place(x=0, y=270)
            p_s_label = tk.Label(frame2, text=f'Saláro: R$ {salario}', bg='#eee', fg='#000', font='Alereya 8 bold')
            p_s_label.place(x=0, y=290)
            p_c_label = tk.Label(frame2, text=f'Contratação: {contratacao}', bg='#eee', fg='#000', font='Alereya 8 bold')
            p_c_label.place(x=0, y=310)
            
            def editar():
                janela4 = tk.Toplevel()
                janela4.title('EDITAR INFORMAÇÕES')
                janela4.geometry('400x490')
                janela4.configure( bg='#eee')
                janela4.resizable(width=False, height=False)
                
                def editar_nome():
                    lista = pd.read_excel('Central_de_funcionarios_T.xlsx')
                    try:
                        del lista['Unnamed: 0']
                    except:
                        pass
                    janela5 = tk.Toplevel()
                    janela5.title('EDITAR NOME')
                    janela5.geometry('400x290')
                    janela5.configure( bg='#eee')
                    janela5.resizable(width=False, height=False)
                    
                    n_entry = tk.Entry(janela5, width=20, justify='center')
                    n_entry.place(x = 140, y = 100)

                    def aplicar():
                        novo = n_entry.get()
                        lista.iat[numero, 1] = novo
                        lista.to_excel('Central_de_funcionarios_T.xlsx')
                        messagebox.showinfo( title='Sucesso', message=f'{nome} foi editado com sucesso!')
                        janela4.destroy()
                        janela5.destroy()
                        
                    b_aplicar = atk.Button3d(janela5, text='Aplicar', bg='#000', command=aplicar)
                    b_aplicar.place(x=155, y=160)
                        
                def editar_idade():
                    lista = pd.read_excel('Central_de_funcionarios_T.xlsx')
                    try:
                        del lista['Unnamed: 0']
                    except:
                        pass
                    janela5 = tk.Toplevel()
                    janela5.title('EDITAR IDADE')
                    janela5.geometry('400x290')
                    janela5.configure( bg='#eee')
                    janela5.resizable(width=False, height=False)
                    
                    n_entry = tk.Entry(janela5, width=20, justify='center')
                    n_entry.place(x = 140, y = 100)

                    def aplicar():
                        novo = n_entry.get()
                        lista.iat[numero, 2] = novo
                        lista.to_excel('Central_de_funcionarios_T.xlsx')
                        messagebox.showinfo( title='Sucesso', message=f'{nome} foi editado com sucesso!')
                        janela4.destroy()
                        janela5.destroy()
                    
                    b_aplicar = atk.Button3d(janela5, text='Aplicar', bg='#000', command=aplicar)
                    b_aplicar.place(x=155, y=160)
                        
                def editar_cpf():
                    lista = pd.read_excel('Central_de_funcionarios_T.xlsx')
                    try:
                        del lista['Unnamed: 0']
                    except:
                        pass
                    janela5 = tk.Toplevel()
                    janela5.title('EDITAR CPF')
                    janela5.geometry('400x290')
                    janela5.configure( bg='#eee')
                    janela5.resizable(width=False, height=False)
                    
                    n_entry = tk.Entry(janela5, width=20, justify='center')
                    n_entry.place(x = 140, y = 100)

                    def aplicar():
                        novo = n_entry.get()
                        lista.iat[numero, 3] = novo
                        lista.to_excel('Central_de_funcionarios_T.xlsx')
                        messagebox.showinfo( title='Sucesso', message=f'{nome} foi editado com sucesso!')
                        janela4.destroy()
                        janela5.destroy()
                        
                    b_aplicar = atk.Button3d(janela5, text='Aplicar', bg='#000', command=aplicar)
                    b_aplicar.place(x=155, y=160)
                        
                def editar_endereco():
                    lista = pd.read_excel('Central_de_funcionarios_T.xlsx')
                    try:
                        del lista['Unnamed: 0']
                    except:
                        pass
                    janela5 = tk.Toplevel()
                    janela5.title('EDITAR ENDEREÇO')
                    janela5.geometry('400x290')
                    janela5.configure( bg='#eee')
                    janela5.resizable(width=False, height=False)
                    
                    n_entry = tk.Entry(janela5, width=20, justify='center')
                    n_entry.place(x = 140, y = 100)

                    def aplicar():
                        novo = n_entry.get()
                        lista.iat[numero, 4] = novo
                        lista.to_excel('Central_de_funcionarios_T.xlsx')
                        messagebox.showinfo( title='Sucesso', message=f'{nome} foi editado com sucesso!')
                        janela4.destroy()
                        janela5.destroy()
                        
                    b_aplicar = atk.Button3d(janela5, text='Aplicar', bg='#000', command=aplicar)
                    b_aplicar.place(x=155, y=160)
                        
                def editar_email():
                    lista = pd.read_excel('Central_de_funcionarios_T.xlsx')
                    try:
                        del lista['Unnamed: 0']
                    except:
                        pass
                    janela5 = tk.Toplevel()
                    janela5.title('EDITAR EMAIL')
                    janela5.geometry('400x290')
                    janela5.configure( bg='#eee')
                    janela5.resizable(width=False, height=False)
                    
                    n_entry = tk.Entry(janela5, width=20, justify='center')
                    n_entry.place(x = 140, y = 100)

                    def aplicar():
                        novo = n_entry.get()
                        lista.iat[numero, 5] = novo
                        lista.to_excel('Central_de_funcionarios_T.xlsx')
                        messagebox.showinfo( title='Sucesso', message=f'{nome} foi editado com sucesso!')
                        janela4.destroy()
                        janela5.destroy()
                        
                    b_aplicar = atk.Button3d(janela5, text='Aplicar', bg='#000', command=aplicar)
                    b_aplicar.place(x=155, y=160)
                        
                def editar_telefone():
                    lista = pd.read_excel('Central_de_funcionarios_T.xlsx')
                    try:
                        del lista['Unnamed: 0']
                    except:
                        pass
                    janela5 = tk.Toplevel()
                    janela5.title('EDITAR TELEFONE')
                    janela5.geometry('400x290')
                    janela5.configure( bg='#eee')
                    janela5.resizable(width=False, height=False)
                    
                    n_entry = tk.Entry(janela5, width=20, justify='center')
                    n_entry.place(x = 140, y = 100)

                    def aplicar():
                        novo = n_entry.get()
                        lista.iat[numero, 6] = novo
                        lista.to_excel('Central_de_funcionarios_T.xlsx')
                        messagebox.showinfo( title='Sucesso', message=f'{nome} foi editado com sucesso!')
                        janela4.destroy()
                        janela5.destroy()
                        
                    b_aplicar = atk.Button3d(janela5, text='Aplicar', bg='#000', command=aplicar)
                    b_aplicar.place(x=155, y=160)
                        
                def editar_salario():
                    lista = pd.read_excel('Central_de_funcionarios_T.xlsx')
                    try:
                        del lista['Unnamed: 0']
                    except:
                        pass
                    janela5 = tk.Toplevel()
                    janela5.title('EDITAR SALÁRIO')
                    janela5.geometry('400x290')
                    janela5.configure( bg='#eee')
                    janela5.resizable(width=False, height=False)
                    
                    n_entry = tk.Entry(janela5, width=20, justify='center')
                    n_entry.place(x = 140, y = 100)

                    def aplicar():
                        novo = n_entry.get()
                        lista.iat[numero, 7] = novo
                        lista.to_excel('Central_de_funcionarios_T.xlsx')
                        messagebox.showinfo( title='Sucesso', message=f'{nome} foi editado com sucesso!')
                        janela4.destroy()
                        janela5.destroy()
                        
                    b_aplicar = atk.Button3d(janela5, text='Aplicar', bg='#000', command=aplicar)
                    b_aplicar.place(x=155, y=160)
                        
                def editar_funcao():
                    lista = pd.read_excel('Central_de_funcionarios_T.xlsx')
                    try:
                        del lista['Unnamed: 0']
                    except:
                        pass
                    janela5 = tk.Toplevel()
                    janela5.title('EDITAR FUNÇÃO')
                    janela5.geometry('400x290')
                    janela5.configure( bg='#eee')
                    janela5.resizable(width=False, height=False)
                    
                    n_entry = tk.Entry(janela5, width=20, justify='center')
                    n_entry.place(x = 140, y = 100)

                    def aplicar():
                        novo = n_entry.get()
                        lista.iat[numero, 8] = novo
                        lista.to_excel('Central_de_funcionarios_T.xlsx')
                        messagebox.showinfo( title='Sucesso', message=f'{nome} foi editado com sucesso!')
                        janela4.destroy()
                        janela5.destroy()
                        
                    b_aplicar = atk.Button3d(janela5, text='Aplicar', bg='#000', command=aplicar)
                    b_aplicar.place(x=155, y=160)
                        
                def editar_contratacao():
                    lista = pd.read_excel('Central_de_funcionarios_T.xlsx')
                    try:
                        del lista['Unnamed: 0']
                    except:
                        pass
                    janela5 = tk.Toplevel()
                    janela5.title('EDITAR CONTRATAÇÃO')
                    janela5.geometry('400x290')
                    janela5.configure( bg='#eee')
                    janela5.resizable(width=False, height=False)
                    
                    n_entry = tk.Entry(janela5, width=20, justify='center')
                    n_entry.place(x = 140, y = 100)

                    def aplicar():
                        novo = n_entry.get()
                        lista.iat[numero, 9] = novo
                        lista.to_excel('Central_de_funcionarios_T.xlsx')
                        messagebox.showinfo( title='Sucesso', message=f'{nome} foi editado com sucesso!')
                        janela4.destroy()
                        janela5.destroy()
                        
                    b_aplicar = atk.Button3d(janela5, text='Aplicar', bg='#000', command=aplicar)
                    b_aplicar.place(x=155, y=160)
                    
                # Frame cima 1 -----------------------------------------------------------

                frame1 = Frame(janela4, width=400, height=49, bg='#000')
                frame1.place(x=0, y=0)
                l_titulo = Label(frame1, text='EDIÇÃO DE INFORMAÇÕES', bg='#000', fg='#fff', font='Anton 16 bold')
                l_titulo.place(x=55, y=14)

                # Frame meio 1 -----------------------------------------------------------

                frame2 = Frame(janela4, width=400, height=401, bg='#eee')
                frame2.place(x=0, y=49)

                n_button = atk.Button3d(frame2, text='Nome*', bg='#000', command=editar_nome)
                n_button.place(x=55, y=49)

                i_button = atk.Button3d(frame2, text='Idade*', bg='#000', command=editar_idade)
                i_button.place(x=55, y=95)
                
                cpf_button = atk.Button3d(frame2, text='CPF*', bg='#000', command=editar_cpf)
                cpf_button.place(x=55, y=150)
                
                e_button = atk.Button3d(frame2, text='Endereço*', bg='#000', command=editar_endereco)
                e_button.place(x=55, y=205)
                
                em_button = atk.Button3d(frame2, text='E-mail*', bg='#000', command=editar_email)
                em_button.place(x=55, y=260)
                
                t_button = atk.Button3d(frame2, text='Telefone*', bg='#000', command=editar_telefone)
                t_button.place(x=55, y=315)
                
                s_button = atk.Button3d(frame2, text='Salario*', bg='#000', command=editar_salario)
                s_button.place(x=245, y=49)

                f_button = atk.Button3d(frame2, text='Função*', bg='#000', command=editar_funcao)
                f_button.place(x=245, y=95)
                
                c_button = atk.Button3d(frame2, text='Contratação*', bg='#000', command=editar_contratacao)
                c_button.place(x=245, y=150)

                # Frame baixo 1 -----------------------------------------------------------

                frame3 = Frame(janela4, width=400, height=40, bg='#000')
                frame3.place(x=0, y=450)

                l_rodape= Label(frame3, bg='#000', fg='#fff', text='created by Edmar Lelis L. JR.', font='Alereya 8 bold italic')
                l_rodape.place(x=120, y=10)       
                     
            editar_b = atk.Button3d(frame2, text='Editar', bg='#000', fg='#fff', command= editar)
            editar_b.place(x=155, y=340)

        except:
            limpar_label = tk.Label(frame2, text=f'', bg='#eee', fg='#000', font='Alereya 8 bold', width=400, height=300)
            limpar_label.place(x=0, y=150)
            messagebox.showerror(title='ERRO', message='Não encntrado! Lembre-se de colocar os "." e o "-" de forma correta!')

    p_button = atk.Button3d(frame2, text= 'Procurar', bg='#000', fg='#fff', command= procura)
    p_button.place(x=155, y=90)

    # Frame baixo 3 -----------------------------------------------------------

    frame3 = Frame(janela3, width=400, height=40, bg='#000')
    frame3.place(x=0, y=450)

    l_rodape= Label(frame3, bg='#000', fg='#fff', text='created by Edmar Lelis L. JR.', font='Alereya 8 bold italic')
    l_rodape.place(x=120, y=10)

# contato  -----------------------------------------------------------

def Contato():
    
    janela6 = tk.Toplevel()
    janela6.title('Contato')
    janela6.geometry('400x490')
    janela6.configure( bg='#fff')
    janela6.resizable(width=False, height=False)
    
    
    # Frame cima 4 -----------------------------------------------------------

    frame1 = Frame(janela6, width=400, height=49, bg='#000')
    frame1.place(x=0, y=0)
    l_titulo = Label(frame1, text='Contato', bg='#000', fg='#fff', font='Anton 16 bold')
    l_titulo.place(x=150, y=14)

    # Frame meio 4 -----------------------------------------------------------

    frame2 = Frame(janela6, width=400, height=401, bg='#eee')
    frame2.place(x=0, y=49)
    
    info = tk.Label(frame2, text=
    """Olá! Eu me chamo Edmar Lelis;
Nasci em 2004 e programo desde muito novo;
        Sou um programador do DF; 
Caso queira me contatar diretamente use este email:
      edmarlelis.lourenco@gmail.com.
    """, bg='#eee', fg='#000', font='Anton 8 bold')
    info.place(x=50, y=10)
    
    gmail_l= tk.Label(frame2, text="Seu gmail:", bg='#eee', fg='#000', font='Anton 8')
    gmail_l.place(x=10, y=100)
    
    gmail_e = tk.Entry(frame2, width=40, justify="center")
    gmail_e.place(x=10, y = 120)
    
    email_l= tk.Label(frame2, text="Mensagem:", bg='#eee', fg='#000', font='Anton 8')
    email_l.place(x=10, y=150)
    
    email_t = tk.Text(frame2)
    email_t.place(x=10, y=170, width=380, height=160)
    
    
    # enviar email -------------------------------------------------------
    
    def enviar_email():  
        try:
            corpo_email = f"""
            <p>email de resposta: {gmail_e.get()}</p>
            <p>Mensagem:</p>
            <p>{email_t.get(1.0, "end-1c")}</p>
            """

            msg = email.message.Message()
            msg['Subject'] = "Contato pelo app de Gerenciamento de Funcionarios."
            msg['From'] = 'projetocontato956@gmail.com'
            msg['To'] = 'projetocontato956@gmail.com'
            password = 'parcozwvqkzqgbch' 
            msg.add_header('Content-Type', 'text/html')
            msg.set_payload(corpo_email )

            s = smtplib.SMTP('smtp.gmail.com: 587')
            s.starttls()
            # Login Credentials for sending the mail
            s.login(msg['From'], password)
            s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8'))
            messagebox.showinfo( title='Sucesso', message='Seu email foi enviado com sucesso!')
        except:
            messagebox.showerror( title='Falha!', message='Seu email Não foi enviado! É possivel que esta opção não esteja mais ativa por motivos de segurança, pois o codigo desta aplicação é publico')



    contato = atk.Button3d(frame2, text= 'Enviar', bg='#000', fg='#fff', command= enviar_email)
    contato.place(x=160, y=334)

    # Frame baixo 4 -----------------------------------------------------------

    frame3 = Frame(janela6, width=400, height=40, bg='#000')
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

contato = atk.Button3d(frame2, text= 'Contato', bg='#000', fg='#fff', command= Contato)
contato.place(x=160, y=264)

# Frame baixo 1 -----------------------------------------------------------

frame3 = Frame(janela, width=400, height=40, bg='#000')
frame3.place(x=0, y=450)

l_rodape= Label(frame3, bg='#000', fg='#fff', text='created by Edmar Lelis L. JR.', font='Alereya 8 bold italic')
l_rodape.place(x=120, y=10)

janela.mainloop()