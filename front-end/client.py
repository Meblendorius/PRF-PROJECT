import tkinter as tk
from tkinter import Label, PhotoImage, filedialog
from tkinter import font
from PIL import ImageTk
import PIL.Image

def escolherDigital():
    digital = filedialog.askopenfilename(title='Selecione a digital', filetypes=[('JPEG', '*.jpg')])
    print(digital)
    f = PIL.Image.open(str(digital))
    f2 = f.resize((200,200), PIL.Image.ANTIALIAS)
    digt = ImageTk.PhotoImage(f2)
    displayImage(digt)


# O que for colocar na tela da digital (2ª tela), colocar dentro da função "displayImage"
def displayImage(the):
    displayFrame = tk.Toplevel(login)
    displayFrame.title('Dados do Funcionário')
    displayFrame.geometry('800x600')
    displayFrame.resizable(False, False)
    # Label para dar display na digital
    confirmDigital = tk.Label(displayFrame, image=the)
    confirmDigital.pack(side=tk.BOTTOM)
    # Label para dar display na foto do funcionário
    # confirmFoto = tk.Label(displayFrame, image=the , bg='red')
    # confirmFoto.pack()
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