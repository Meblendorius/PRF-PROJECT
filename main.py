import cv2
import os
from tkinter import filedialog
import mysql.connector
import tkinter as tk
from tkinter import Label, PhotoImage, filedialog
from tkinter import font
from PIL import ImageTk
import PIL.Image

def escolherDigital():
    caminho = filedialog.askopenfilename(title='Selecione a digital', filetypes=[('JPEG', '*.jpg')])

    f = PIL.Image.open(str(caminho))
    f2 = f.resize((200,200), PIL.Image.ANTIALIAS)
    caminho2 = ImageTk.PhotoImage(f2)
    #=============================================================
    entrada = cv2.imread(caminho)
    con = mysql.connector.connect(host='localhost', database='Digital', user='thiago', password='Tmysql@4581')
    if con.is_connected():
        db_info = con.get_server_info()
        print("Conectado ao servidor MySQL versão ", db_info)
        cursor = con.cursor()

        cursor.execute("select * from func;")
        linha = cursor.fetchall()
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

        print(idop,nome, idperm,funcao,foto_end)

        g = PIL.Image.open(str(foto_end))
        g2 = g.resize((300, 200), PIL.Image.ANTIALIAS)

        foto = ImageTk.PhotoImage(g2)


    displayImage(caminho2,idop,nome, idperm,funcao,foto)


def displayImage(the,idop,nome, idperm,funcao,foto):
    print(foto)
    print(the)

    displayFrame = tk.Toplevel(login)
    displayFrame.title('Dados do Funcionário')
    displayFrame.geometry('800x600')
    displayFrame.resizable(False, False)
    # Label para dar display na digital

    confirmDigital = tk.Label(displayFrame, image=the)

    confirmDigital.pack(side=tk.BOTTOM)
    # Label para dar display na foto do funcionário
    confirmFoto = tk.Label(displayFrame, image=foto , bg='red')
    confirmFoto.pack()
    nomel=tk.Label(displayFrame, text=nome).pack()
    funcaol = tk.Label(displayFrame, text=funcao).pack()
    the.show()


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










