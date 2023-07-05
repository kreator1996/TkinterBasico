from tkinter import *
import tkinter.filedialog
import tkinter.messagebox

APP_TITLE =  'Aplicação'
root = Tk()

def sair(event=None):
  if tkinter.messagebox.askokcancel('Sair', 'Deseja realmente sair?'):
    root.destroy()

def showJanela(event=None):
  tkinter.messagebox.showinfo('Sobre', 'Esta é uma opção')

def showSobre(event=None):
  tkinter.messagebox.showinfo('Sobre', 
                            '{}{}'.format(APP_TITLE, '\nEsta é minha aplicaçãográfica \npython com gráfico.'))

def montarMenu():
  menu_bar = Menu(root)
  arq_menu = Menu(menu_bar, tearoff=0)
  aux_menu = Menu(menu_bar, tearoff=0)
  menu_bar.add_cascade(label='Arquivo', underline=0, menu=arq_menu)
  menu_bar.add_cascade(label='Auxílio', underline=0, menu=aux_menu)
  root.config(menu=menu_bar)

  arq_menu.add_command(label='Opção l', compound='left', command=showJanela)
  arq_menu.add_separator()
  arq_menu.add_command(label='Sair',accelerator='Alt+F4', compound='left', command=sair)
  aux_menu.add_command(label='Sobre', compound='left', command=showSobre)



def principal():
  montarMenu()
  root.protocol("WM_DELETE_WINDOW", sair)
  root.title(APP_TITLE)
  root.geometry("500x400")
  root.mainloop()

if __name__ == '__main__':
  principal()