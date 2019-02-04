# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter import Label,Tk
from PIL import Image, ImageTk
import numpy as n
#root = Tk()

class openWindow(Tk):
    def __init__(self):
        super(openWindow, self).__init__()
        self.title("Haloooo!! saya Irfandio Daffa A dari kelas PCD")
        self.minsize(640, 400)
        """ Ini digunakan untuk membuat frame yang berisi button untuk melakukan browse file
        """
        self.labelFrame = ttk.LabelFrame(self, text = "Mau Edit Foto?")
        self.labelFrame.grid(column = 0, row = 1, padx = 20, pady = 20)
        
        self.button()
        self.buttonGreyScale()
        self.image = Image
        
    """button ini dipake buat memanggil function fileDialog biar bisa cari foto"""    
    def button(self):
        self.button = ttk.Button(self.labelFrame, text = "Cari File Fotonya Di sini", command = self.fileDialog)
        self.button.grid(column = 1, row = 1)
    
    """nah kalo fileDialog ini buat nge browse file fotonya"""
    def fileDialog(self):
        self.filename = filedialog.askopenfilename(initialdir = "/", title = "Select A File", filetypes = (("jpeg", "*.jpg"), ("All Files", "*.*")))
        path = self.filename
        gambar = Image.open(path)
        
        tkimage = ImageTk.PhotoImage(gambar)                #mulai dari proses ini digunakan untuk
        gbr = Label(root,image = tkimage)                   #menampilkan gambar yang udah dicari
        gbr.image = tkimage
        gbr.grid(column = 1, row = 2)
        
        self.image = gambar
        
    def buttonGreyScale(self):
        self.button = ttk.Button(self.labelFrame, text = "Teken ini aja biar jadi abu-abu", command = self.greyScale)
        self.button.grid(column = 2, row = 1)
        
    def greyScale(self):
        gbrBaru = self.image.convert("RGBA")
        imgArray = n.asarray(gbrBaru)
        
        red = imgArray[:, :, 1]
        green = imgArray[:, :, 2]
        blue = imgArray[:, :, 3]
        
        sRed = n.sum(red)
        sGreen = n.sum(green)
        sBlue = n.sum(blue)
        sAll = sRed + sGreen + sBlue
        
        grayArray = (sRed / sAll * red) + (sGreen / sAll * green) + (sBlue / sAll * blue)
        
        newImg = Image.fromarray(grayArray)
        
        tkimage = ImageTk.PhotoImage(newImg)                #mulai dari proses ini digunakan untuk
        gbr = Label(root,image = tkimage)                   #menampilkan gambar yang diubah ke bentuk greyScale
        gbr.image = tkimage
        gbr.grid(column = 1, row = 2)
        
        

if __name__ == '__main__':
    root = openWindow()
    root.mainloop()
    