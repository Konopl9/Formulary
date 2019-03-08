# -*- coding: utf-8 -*-

from tkinter import *
from tkinter import tix
import MultiListbox as table

data = [
    ["Petr", "Bílý", "045214/1512", "17. Listopadu", 15, "Ostrava", 70800, "poznamka"],
    ["Jana", "Zelený", "901121/7238", "Vozovna", 54, "Poruba", 78511, ""],
    ["Karel", "Modrý", "800524/5417", "Porubská", 7, "Praha", 11150, ""],
    ["Martin", "Stříbrný", "790407/3652", "Sokolovská", 247, "Brno", 54788, "nic"],

]


class App(object):
    def __init__(self, master):
        self.row = IntVar()
        self.row = None
        self.jmeno = StringVar()
        self.prijmeni = StringVar()
        self.rc = StringVar()
        self.ulice = StringVar()
        self.cp = StringVar()
        self.mesto = StringVar()
        self.psc = StringVar()
        self.menu = Menu(root)
        self.menu.add_command(label="File")
        self.menu.add_command(label="Settings")
        self.menu.add_command(label="Help")
        # box
        self.mlb = table.MultiListbox(master, (('Name', 20), ('Surname', 20), ('Personal number', 12)))
        for i in range(len(data)):
            self.mlb.insert(END, (data[i][0], data[i][1], data[i][2]))
        self.mlb.pack(expand=YES, fill=BOTH, padx=10, pady=10)
        self.mlb.grid_columnconfigure(1, weight=1)
        self.mlb.subscribe(lambda row: self.edit(row))
        self.nb = tix.NoteBook(master)

        # input form
        self.input_frame = Frame(root, relief=GROOVE)
        self.l_name = Label(self.input_frame, text='Name:')
        self.E_name = Entry(self.input_frame)
        self.l_surname = Label(self.input_frame, text='Surname:')
        self.E_surname = Entry(self.input_frame)
        self.l_ID = Label(self.input_frame, text='Personal number:')
        self.E_Id = Entry(self.input_frame, width=10)
        self.l_name.grid(row=1, column=1, padx=2, pady=2, sticky=W + E + N + S)
        self.E_name.grid(row=1, column=2, padx=2, pady=3, sticky=W + E + N + S)
        self.l_surname.grid(row=2, column=1, padx=2, pady=2, sticky=W + E + N + S)
        self.E_surname.grid(row=2, column=2, padx=2, pady=3, sticky=W + E + N + S)
        self.l_ID.grid(row=3, column=1, padx=2, pady=3, sticky=W + E + N + S)
        self.E_Id.grid(row=3, column=2, padx=2, pady=3, sticky=W + N + S)
        self.input_frame.pack(fill=Y, expand=1, padx=4, pady=4)
        self.input_frame.grid_columnconfigure(1, weight=1)
        # Window tix
        self.nb.add("page1", label="Address")
        self.nb.add("page2", label="Note")
        self.p1 = self.nb.subwidget_list["page1"]
        self.p2 = self.nb.subwidget_list["page2"]
        self.nb.pack(fill=BOTH, expand=1, padx=4, pady=4)
        self.nb.grid_columnconfigure(1, weight=1)
        self.nb.grid_rowconfigure(1, weight=1)
        # Address
        self.address_frame = LabelFrame(self.p1, text='Address', relief=GROOVE)
        self.l_street = Label(self.address_frame, text='Street:')
        self.E_street = Entry(self.address_frame, width=20)
        self.l_street.grid(row=1, column=1, pady=5, padx=5, sticky=W + E + N + S)
        self.E_street.grid(row=1, column=2, sticky=W + N + S, pady=5, padx=5)
        self.l_h_m = Label(self.address_frame, text='h.m:', width=20)
        self.E_h_m = Entry(self.address_frame, width=10)
        self.l_h_m.grid(row=1, column=3, pady=5, padx=5, sticky=W + E + N + S)
        self.E_h_m.grid(row=1, column=4, padx=20, pady=5, sticky=W + E + N + S)
        self.l_city = Label(self.address_frame, text='City:')
        self.E_city = Entry(self.address_frame, width=25)
        self.l_city.grid(row=2, column=1, pady=5, padx=5, sticky=W + E + N + S)
        self.E_city.grid(row=2, column=2, pady=5, padx=5, sticky=W + E + N + S)
        self.l_code = Label(self.address_frame, text='Post code:')
        self.E_code = Entry(self.address_frame, width=10)
        self.l_code.grid(row=3, column=1, pady=5, padx=5, sticky=W + E + N + S)
        self.E_code.grid(row=3, column=2, sticky=W + N + S, pady=5, padx=5)
        self.address_frame.pack(fill=BOTH, expand=1, side=LEFT, padx=4, pady=4)
        self.address_frame.grid_columnconfigure(1, weight=1)
        self.address_frame.grid_rowconfigure(1, weight=1)
        # Note
        self.note_frame = LabelFrame(self.p2, text='Note', relief=GROOVE)
        self.l_note = Label(self.note_frame, text='Note:')
        self.E_note = Text(self.note_frame, height=6)
        self.l_note.grid(row=1, column=1, sticky=W + E + N + S)
        self.E_note.grid(row=1, column=2, sticky=W + E + N + S)
        self.note_frame.pack(fill=BOTH, expand=1, side=LEFT, padx=4, pady=4)
        self.note_frame.grid_columnconfigure(1, weight=1)
        # Buttons down
        self.down_frame = Frame(root, relief=GROOVE)
        self.cancel = Button(self.down_frame, text='Cancel', width=15)
        self.new = Button(self.down_frame, text='New record', width=15, command=self.delete_all)
        self.save = Button(self.down_frame, text='Save record', width=15, command=self.add_user)
        self.cancel.grid(row=1, column=1, pady=10, sticky=W + E + N + S)
        self.new.grid(row=1, column=2, pady=10, sticky=W + E + N + S)
        self.save.grid(row=1, column=3, pady=10, sticky=W + E + N + S)
        self.down_frame.pack(fill=Y, expand=1, padx=4, pady=4)
        self.down_frame.grid_columnconfigure(1, weight=1)
        # Chovani GUI
        self.input_frame.rowconfigure(1, weight=1)
        self.input_frame.rowconfigure(2, weight=1)
        self.input_frame.rowconfigure(3, weight=1)
        self.input_frame.columnconfigure(1, weight=1)
        self.input_frame.columnconfigure(2, weight=1)
        self.nb.rowconfigure(1, weight=1)
        self.nb.columnconfigure(1, weight=1)
        self.mlb.rowconfigure(1, weight=1)
        self.mlb.columnconfigure(1, weight=1)
        self.address_frame.rowconfigure(1, weight=1)
        self.address_frame.rowconfigure(2, weight=1)
        self.address_frame.rowconfigure(3, weight=1)
        self.address_frame.columnconfigure(1, weight=1)
        self.address_frame.columnconfigure(2, weight=1)
        self.address_frame.columnconfigure(3, weight=1)
        self.address_frame.columnconfigure(4, weight=1)
        self.note_frame.rowconfigure(1, weight=1)
        self.note_frame.columnconfigure(1, weight=1)
        self.note_frame.columnconfigure(2, weight=1)
        self.nb.grid_columnconfigure(1, weight=1)
        self.nb.grid_rowconfigure(1, weight=1)
        self.mlb.rowconfigure(1, weight=1)
        self.mlb.columnconfigure(1, weight=1)
        self.down_frame.rowconfigure(1, weight=1)
        self.down_frame.columnconfigure(1, weight=1)
        self.down_frame.columnconfigure(2, weight=1)
        self.down_frame.columnconfigure(3, weight=1)
        root.config(menu=self.menu)

    def edit(self, row):
        self.row = row
        print(row)

    def add_user(self):
        buff = []
        self.jmeno = self.E_name.get()
        buff.append(self.jmeno)
        self.prijmeni = self.E_surname.get()
        buff.append(self.prijmeni)
        self.rc = self.E_Id.get()
        buff.append(self.rc)
        data.append(buff)
        self.E_name.delete(0, END)
        self.E_surname.delete(0, END)
        self.E_Id.delete(0, END)
        self.mlb.delete(0, len(data))
        for i in range(len(data)):
            self.mlb.insert(END, (data[i][0], data[i][1], data[i][2]))
        self.mlb.pack(expand=YES, fill=BOTH, padx=10, pady=10)
        self.mlb.grid_columnconfigure(1, weight=1)
        self.mlb.subscribe(lambda row: self.edit(row))

    def delete_all(self):
        self.E_name.delete(0, END)
        self.E_surname.delete(0, END)
        self.E_Id.delete(0, END)
        self.E_Id.delete(0, END)
        self.E_code.delete(0, END)
        self.E_city.delete(0, END)
        self.E_h_m.delete(0, END)



root = tix.Tk()

root.wm_title("Formulář")
app = App(root)
root.mainloop()
