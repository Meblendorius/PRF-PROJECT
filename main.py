import cv2
import os
from tkinter import filedialog
import mysql.connector
import tkinter as tk
from tkinter import Label, PhotoImage, filedialog
from tkinter import font
from PIL import ImageTk
import PIL.Image
con = mysql.connector.connect(host='localhost', database='Digital', user='thiago', password='Tmysql@4581')
def escolherDigital():
    caminho = filedialog.askopenfilename(title='Selecione a digital', filetypes=[('JPEG', '*.jpg')])

    f = PIL.Image.open(str(caminho))
    f2 = f.resize((200,200), PIL.Image.ANTIALIAS)
    caminho2 = ImageTk.PhotoImage(f2)
    #=============================================================
    entrada = cv2.imread(caminho)

    if con.is_connected():
        db_info = con.get_server_info()
        print("Conectado ao servidor MySQL versão ", db_info)
        cursor = con.cursor()

        cursor.execute("select * from func;")
        linha = cursor.fetchall()
        idop=""
        for i in linha:

            original = cv2.imread("{}".format(i[6]))

            sift = cv2.xfeatures2d.SIFT_create()

            keypoints_1, descriptors_1 = sift.detectAndCompute(original, None)
            keypoints_2, descriptors_2 = sift.detectAndCompute(entrada, None)

            comp = cv2.FlannBasedMatcher(dict(algorithm=1, trees=10),
                                         dict()).knnMatch(descriptors_1, descriptors_2, k=2)
            ponts = []

            for x, y in comp:
                if x.distance < 0.1 * y.distance:
                    ponts.append(x)
            keypoints = 0
            if len(keypoints_1) <= len(keypoints_2):
                keypoints = len(keypoints_1)
            else:
                keypoints = len(keypoints_2)

            compt = (len(ponts) / keypoints)
            if compt > 0.95:
                idop= i[0]
                nome=i[1]
                idperm= i[2]
                funcao= i[3]
                foto_end=i[4]
        if idop:
            i=0
        else:
            falha = tk.Label(loginF, text='Digital incompativel', fg='red').pack()

        g = PIL.Image.open(str(foto_end))
        g2 = g.resize((300, 200), PIL.Image.ANTIALIAS)
        foto = ImageTk.PhotoImage(g2)


    displayImage(caminho2,idop,nome, idperm,funcao,foto)
    #showbanco(idperm)


def displayImage(the,idop,nome, idperm,funcao,foto):
    displayFrame = tk.Toplevel(login)
    displayFrame.title('Dados do Funcionário')
    displayFrame.geometry('300x600')
    displayFrame.resizable(False, False)
    # Label para dar display na digital

    confirmDigital = tk.Label(displayFrame, image=the)

    confirmDigital.pack(side=tk.BOTTOM)
    # Label para dar display na foto do funcionário
    confirmFoto = tk.Label(displayFrame, image=foto , bg='red')
    confirmFoto.pack()
    nomel=tk.Label(displayFrame, text=nome).pack()
    funcaol = tk.Label(displayFrame, text=funcao).pack()
    ok = tk.Button(displayFrame, text='Acessar banco', relief='solid', command=lambda:showbanco(idperm))
    ok.pack(side=tk.BOTTOM)
    the.show()




def showbanco(idperm):

    cursor = con.cursor()
    cursor.execute("select * from Niveis;")
    row=cursor.fetchall()

    displayFrame = tk.Toplevel(login)
    displayFrame.title('Informações')
    displayFrame.geometry('1300x350')
    displayFrame.resizable(False, False)


    # Label para dar display na foto do funcionário

    cont = 1
    if idperm >= 1:

        for i in row:
            nomec = tk.Label(displayFrame, text="Nome", fg='black').grid(row=0, column=0, padx=10, pady=20,sticky='ew')
            enderecoc = tk.Label(displayFrame, text="Endereco", fg='black').grid(row=0, column=1, padx=10, pady=20)
            produtoc = tk.Label(displayFrame, text="Produto", fg='black').grid(row=0, column=2, padx=10, pady=20)
            ano_kgc = tk.Label(displayFrame, text="Ano_kg", fg='black').grid(row=0, column=3, padx=10, pady=20)
            destinoc = tk.Label(displayFrame, text="Destino", fg='black').grid(row=0, column=4, padx=10, pady=20)
            funcionariosc = tk.Label(displayFrame, text="Funcionarios", fg='black').grid(row=0, column=5, padx=10, pady=20)
            maquinasc = tk.Label(displayFrame, text="Máquinas", fg='black').grid(row=0, column=6, padx=10, pady=20)
            autoc = tk.Label(displayFrame, text="Auto", fg='black').grid(row=0, column=7, padx=10, pady=20)

            #===============================================================================================

            nome = tk.Label(displayFrame, text=i[1]).grid(row=cont,column=0,padx=10,pady=20)
            endereco=tk.Label(displayFrame, text=i[2]).grid(row=cont,column=1,padx=10,pady=20)
            produto = tk.Label(displayFrame, text=i[3]).grid(row=cont,column=2,padx=10,pady=20)
            ano_kg = tk.Label(displayFrame, text=i[4]).grid(row=cont,column=3,padx=10,pady=20)
            destino = tk.Label(displayFrame, text=i[5]).grid(row=cont,column=4,padx=10,pady=20)
            funcionarios = tk.Label(displayFrame, text=i[6]).grid(row=cont,column=5,padx=10,pady=20)
            maquinas = tk.Label(displayFrame, text=i[7]).grid(row=cont,column=6,padx=10,pady=20)
            auto = tk.Label(displayFrame, text=i[8]).grid(row=cont,column=7,padx=10,pady=20)
            if idperm >= 2:
                imp_munc = tk.Label(displayFrame, text="imp_municipal", fg='black').grid(row=0, column=8, padx=10, pady=20)
                imp_estadc = tk.Label(displayFrame, text="imp_estadual", fg='black').grid(row=0, column=9, padx=10, pady=20)
                imp_federalc = tk.Label(displayFrame, text="imp_federal", fg='black').grid(row=0, column=10, padx=10, pady=20)
                taxasc = tk.Label(displayFrame, text="Taxas", fg='black').grid(row=0, column=11, padx=10, pady=20)


                # ===============================================================================================

                imp_mun = tk.Label(displayFrame, text=i[9]).grid(row=cont,column=8,padx=10,pady=20)
                imp_estad = tk.Label(displayFrame, text=i[10]).grid(row=cont,column=9,padx=10,pady=20)
                imp_federal = tk.Label(displayFrame, text=i[11]).grid(row=cont,column=10,padx=10,pady=20)
                taxas = tk.Label(displayFrame, text=i[12]).grid(row=cont,column=11,padx=10,pady=20)
                if idperm == 3:
                    agrotoxicoc = tk.Label(displayFrame, text="Agrotoxico", fg='black').grid(row=0, column=12, padx=10, pady=20)
                    # ===============================================================================================
                    agrotoxico = tk.Label(displayFrame, text=i[13]).grid(row=cont,column=12,padx=10,pady=20)



            cont+=1





login = tk.Tk()
login.title('Login de Funcionário')
login.geometry('400x400')
login.resizable(False, False)

f = font.Font(size=35)

loginF = tk.Frame(master=login, height=100)
loginF.pack()

loginlbl = tk.Label(loginF, text='Iniciar Sessão', fg='black', font=f, pady=100)
loginlbl.pack(side= tk.TOP)


escolherImgBtn = tk.Button(loginF, text='Escolher Arquivo', relief='solid', command=escolherDigital)
escolherImgBtn.pack(side=tk.BOTTOM)

login.mainloop()










