from stegano import lsb
from tkinter import filedialog
from tkinter import *

class Main:
    def __init__(self, window):
        window.geometry('320x66');
        window.title('crypt');
        window.resizable(0, 0)
        self.text = StringVar(value="Сообщение")
        self.file = StringVar(value="Файл")
        Button(window, text='Load', width=10, font=('Times', 10), command=self.load).place(x=0,y=0)
        Button(window, text='Crypt', width=10, font=('Times', 10), command=self.cr).place(x=90, y=0)
        Button(window, text='enCrypt', width=10, font=('Times', 10), command=self.encr).place(x=180, y=0)
        self.entr_m = Entry(textvariable=self.text, width=52)
        self.entr_m.place(x=0,y=25)
        self.entr_file = Entry(textvariable=self.file, width=52)
        self.entr_file.place(x=0, y=45)
    def load(self):
        files = filedialog.askopenfilename()
        self.formating_files(files)
    def formating_files(self, file):
        ext =  file[-3:-1]+file[-1]
        if ext.upper() == "PNG" or ext.upper() == "JPG" or ext.upper() == "EPG":
            self.file.set(file)
    def cr(self):
        if self.file.get()!="Файл" and self.text.get()!="Сообщение":
            print(self.file.get())
            c = lsb.hide(self.file.get(), self.text.get())
            c.save("1-1.png")
            print("зашифровал")
    def encr(self):
        if self.file.get() != "Файл":
            print("Начал")
            self.text.set(lsb.reveal(self.file.get()))
            print("готово")

root = Tk()
app = Main(root)
root.mainloop()



