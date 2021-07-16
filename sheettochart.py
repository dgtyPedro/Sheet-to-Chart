from tkinter import *
from tkinter.ttk import *
import pandas as pd
import plotly.express as px
import pyautogui
import time
import os
import tkinter as tk
import tkinter.ttk as ttk

root=Tk()
root.title("SheetToChart")
root.resizable(False, False)
num=1

def pathOpen():
    path = "C:/AutoGraphPath/Tabela"
    path = os.path.realpath(path)
    os.startfile(path)

        
def sendGen():
    tabela=pd.read_csv("C:/AutoGraphPath/Tabela/"+nameVar.get())   
    
    if variable.get()=='Bar':       
        for coluna in tabela:
            grafico=px.bar(tabela, x=archivePrim.get(), y=coluna, title=archivePrim.get()+" x "+coluna)
            grafico.update_traces(marker_line_width=0.8)
            grafico.show()
    
    if variable.get()=='Line':
        for coluna in tabela:
            grafico=px.line(tabela, x=archivePrim.get(), y=coluna, title=archivePrim.get()+" x "+coluna)
            grafico.update_traces(marker_line_width=0.8)
            grafico.show()
    
    if variable.get()=='Pie':
        for coluna in tabela:
            grafico=px.pie(tabela, values=coluna, names=archivePrim.get(), title=archivePrim.get()+" x "+coluna)
            grafico.update_traces(marker_line_width=0.8)
            grafico.show()    
            
if not os.path.exists("C:/AutoGraphPath"):
    os.mkdir("C:/AutoGraphPath")
if not os.path.exists("C:/AutoGraphPath/Tabela"):
    os.mkdir("C:/AutoGraphPath/Tabela")


myLabel1=Label(root,text="Please, fill out the form below")
myLabel1.grid(row=0, pady=10, columnspan=2)

nameVar=tk.StringVar(root)
archiveName=Entry(root, textvariable=nameVar, width=40)
archiveName.grid(row=1, column=0, padx=10, pady=10)
archiveName.insert (0, "File Name. Example: sheet.csv")

archiveOpen=Button(root, text="Open folder to insert spreadsheet", command=pathOpen, width=30)
archiveOpen.grid (row=1, column=1, padx=10, pady=10)

archivePrim=Entry(root, width=74)
archivePrim.grid(row=2, column=0, columnspan=2, padx=10, pady=10)
archivePrim.insert (0, "Write the exact reference column name")

myLabel2=Label(root,text="Choose the type of chart:")
myLabel2.grid(row=4, column=0, pady=10, padx=5)
        
choices = ['Bar', 'Bar', 'Line', 'Pie']
variable = StringVar(root)
variable.set('Bar')
typeChart = OptionMenu(root, variable, *choices)
typeChart.grid(row=4, column=0, columnspan=2)

sendGen=Button(root, text="Send & Generate", command=sendGen, width=30)
sendGen.grid(row=5, column=0, pady=10, columnspan=2)

root.mainloop()


