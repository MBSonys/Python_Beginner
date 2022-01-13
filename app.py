from tkinter import *
from directions import *
from Flightprice import *
from fuelprice import kainuoja
import webbrowser as wb
from PIL import ImageTk, Image
import time

# Globalus duomenys

Flight_edit = False
Direction_edit = False
get_all_Flight()
get_all_directions()
time1 = ''
kaina = ''

# Sukuriamos funkcijos skirtos atlikti komandas

def skaicioja():
    while True:
        pinigai1 = get_all_profit()
        return pinigai1


def update_F():
    boksas2.delete(0, END)
    boksas2.insert(END, *get_all_Flight())
    laukas1.delete(0, 'end')
    laukas2.delete(0, 'end')
    laukas3.delete(0, 'end')
    laukas4.delete(0, 'end')
    laukas1.focus()

def skrydis():
    global kaina
    Flight_edit = get_all_directions()[boksas22.curselection()[0]]
    update_F()
    laukas1.insert(0, Flight_edit.direction)
    laukas4.insert(0, Flight_edit.range)
    kaina = Flight_edit.price
    komanda["text"] = "Pasirinkta"



def add_F(event):
    global Flight_edit
    if Flight_edit:
        update_Flight(Flight_edit.id, laukas1.get(), laukas2.get(), laukas3.get(), laukas4.get())
        Flight_edit = False
    elif laukas3.get() == '':
        laukas3.insert(0, round((int(laukas2.get()) * kaina)  - (kainuoja * int(laukas4.get()))))
        add_Flight(laukas1.get(), laukas2.get(), laukas3.get(), laukas4.get())
    else:
        add_Flight(laukas1.get(), laukas2.get(), laukas3.get(), laukas4.get())
    update_F()
    balanso_uzrasas["text"] = "Balansas: " + str(skaicioja())
    komanda["text"] = "Ivestas skrydis"

def delete_F():
    Acitve_Flight = get_all_Flight()[boksas2.curselection()[0]]
    delete_Flight(Acitve_Flight.id)
    update_F()
    balanso_uzrasas["text"] = "Balansas: " + str(skaicioja())
    komanda["text"] = "Istrintas skrydis"

def edit_F():
    global Flight_edit
    Flight_edit = get_all_Flight()[boksas2.curselection()[0]]
    update_F()
    balanso_uzrasas["text"] = "Balansas: " + str(skaicioja())
    laukas1.insert(0, Flight_edit.flight)
    laukas2.insert(0, Flight_edit.passengers)
    laukas3.insert(0, Flight_edit.profit)
    laukas4.insert(0, Flight_edit.distance)
    komanda["text"] = "Redaguojamas skrydis"



def update_D():
    boksas22.delete(0, END)
    boksas22.insert(END, *get_all_directions())
    laukas12.delete(0, 'end')
    laukas22.delete(0, 'end')
    laukas32.delete(0, 'end')
    laukas12.focus()

def add_D(event):
    global Direction_edit
    if Direction_edit:
        update_direction(Direction_edit.id, laukas12.get(), laukas22.get(), laukas32.get())
        Direction_edit = False
    else:
        add_direction(laukas12.get(), laukas22.get(), laukas32.get())
    update_D()
    komanda["text"] = "Ivesta skrydzio info"


def delete_D():
    Acitve_Direction = get_all_directions()[boksas22.curselection()[0]]
    delete_direction(Acitve_Direction.id)
    update_D()
    komanda["text"] = "Istrinta skrydzo informacija"

def edit_D():
    global Direction_edit
    Direction_edit = get_all_directions()[boksas22.curselection()[0]]
    update_D()
    laukas12.insert(0, Direction_edit.direction)
    laukas22.insert(0, Direction_edit.range)
    laukas32.insert(0, Direction_edit.price)
    komanda["text"] = "Redaguojami skrydzio duomenys"

def internetas():
    wb.open_new("https://www.ryanair.com/lt/lt")

def internetas2():
    wb.open_new("https://www.airmilescalculator.com/")


def close_window():
    main_langas.destroy()

        
    
# def extra_window():
#     extra_langas = Toplevel(main_langas)
#     extra_langas.title("Skrydziu kryptis")
#     extra_langas.geometry("800x600")
#     extra_langas.iconbitmap(r"ryanair_icona.ico")
#     top_frame2 = Frame(extra_langas)
#     buttom_frame2 = Frame(extra_langas)
#     uzrasas12 = Label(top_frame2, text="Skrydzio kriptis")
#     laukas12 = Entry(top_frame2)

#     laukas12_str = Label(top_frame2, text="Kriptis:")
#     uzrasas12.grid(row=1, columnspan=2)

#     laukas12_str.grid(row=2, column=0)
#     laukas12.grid(row=2, column=1)  
#     top_frame2.pack()
#     buttom_frame2.pack() 


# Sukuriamas Tkinter grafinis atvaizdavimas

main_langas = Tk()
main_langas.title("Ryanair programa")
top_frame = Frame(main_langas)
buttom_frame = Frame(main_langas)

# main_langas.config(bg='systemTransparent')
# bg1 = PhotoImage(file="Ryanair.ppm")
# fotke = Label(top_frame, image=bg1)
# fotke.place(x=0, y=0, relwidth=1, relheight=1)

# main_langas.geometry("1024x768")
# fotke = ImageTk.PhotoImage(Image.open("Ryanair.ppm"))
# uzpildymas = Label(main_langas, image = fotke)
# uzpildymas.place(x=0, y=0, relwidth=1, relheight=1)

# Pridedama ikona

main_langas.iconbitmap(r'ryanair_icona.ico')

laikrodis = Label(buttom_frame, bg='lightblue', relief=GROOVE)

# Laikordzio funkcija

def laikas():
    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        laikrodis.config(text=time2)
    laikrodis.after(200, laikas)

laikas()

# Sukuriami grafikos sasajos objektai

boksas22 = Listbox(buttom_frame, selectmode=SINGLE)
boksas22.insert(END, *get_all_directions())

boksas2 = Listbox(top_frame, selectmode=SINGLE)
boksas2.insert(END, *get_all_Flight())

uzrasas1 = Label(top_frame, text="Skrydzio kriptis")
laukas1 = Entry(top_frame)
laukas1_str = Label(top_frame, text="Kriptis:")

uzrasas2 = Label(top_frame, text="Keleiviu kiekis")
laukas2 = Entry(top_frame)
laukas2_str = Label(top_frame, text="Iveskite keleiviu kieki:")

uzrasas3 = Label(top_frame, text="Pelnas")
laukas3 = Entry(top_frame)
laukas3_str = Label(top_frame, text="Kuro ir nupirktu bilietu santikis")

uzrasas4 = Label(top_frame, text="Atstumas tarp oro uostu")
laukas4 = Entry(top_frame)
laukas4_str = Label(top_frame, text="Atstumas (KM)")

button1 = Button(top_frame, text="Ivesti", bg='lightblue')
button1.bind("<Button-1>", add_F)

button2 = Button(top_frame, text="Redaguoti", bg='lightblue', command=edit_F)
# button2.bind("<Button-1>", update_F)

button3 = Button(top_frame, text="Trinti", bg='lightblue', command=delete_F)
# button3.bind("<Button-1>", delete_F)

button4 = Button(top_frame, text="Pasirinkti skridi", bg='red', command=skrydis)

# Meniu langas

meniu1 = Menu(main_langas)
main_langas.config(menu=meniu1)
submeniu1 = Menu(meniu1, tearoff= 0)
meniu1.add_cascade(label="Meniu", menu=submeniu1)
submeniu1.add_command(label="Ryanair skrydziai", command=internetas)
submeniu1.add_command(label="Skrydzio atsutmai", command=internetas2)
submeniu1.add_separator()
submeniu1.add_command(label="Uzdaryti programa", command=close_window)

laukas12 = Entry(buttom_frame)
uzrasas12 = Label(buttom_frame, text="Skrydzio kriptis")
laukas12_str = Label(buttom_frame, text="Kryptis:")

laukas22 = Entry(buttom_frame)
uzrasas22 = Label(buttom_frame, text="Atstumas")
laukas22_str = Label(buttom_frame, text="Iveskite atstuma tarp oro uostu:")

laukas32 = Entry(buttom_frame)
uzrasas32 = Label(buttom_frame, text="Skrydio bilieto kaina")
laukas32_str = Label(buttom_frame, text="Iveskite kaina (EU):")

scrolbaras1 = Scrollbar(buttom_frame)
scrolbaras1.config(command=boksas22.yview)

scrolbaras2 = Scrollbar(top_frame)
scrolbaras2.config(command=boksas2.yview)
scrolbaras3 = Scrollbar(top_frame)
scrolbaras3.config(orient=HORIZONTAL, command=boksas2.xview)

button12 = Button(buttom_frame, text="Ivesti", bg='gold1')
button12.bind("<Button-1>", add_D)

button22 = Button(buttom_frame, text="Redaguoti", bg='gold1', command=edit_D)
# button22.bind("<Button-1>", update_D)

button32 = Button(buttom_frame, text="Trinti", bg='gold1', command=delete_D)
# button32.bind("<Button-1>", delete_D)

uzrasas111 = Label(top_frame, text="-----------------------------------")

status = Label(buttom_frame, bd=1, relief=SUNKEN, anchor=E, bg='lightblue')

balanso_uzrasas = Label(buttom_frame, bg="lightblue", borderwidth=0, relief=RIDGE, text="Balansas: " + str(skaicioja()))

komanda = Label(buttom_frame, bg='lightblue', borderwidth=0, highlightthickness=0)

# GUI formavimas

uzrasas1.grid(row=1, column=1, columnspan=2)
laukas1_str.grid(row=2, column=0)
laukas1.grid(row=2, column=1, columnspan=2)

uzrasas2.grid(row=3, column=1, columnspan=2)
laukas2_str.grid(row=4, column=0)
laukas2.grid(row=4, column=1, columnspan=2)

uzrasas3.grid(row=5, column=1, columnspan=2)
laukas3.grid(row=6, column=1, columnspan=2)
laukas3_str.grid(row=6, column=0)

uzrasas4.grid(row=7, column=1, columnspan=2)
laukas4.grid(row=8, column=1, columnspan=2)
laukas4_str.grid(row=8, column=0)

button1.grid(row=3, column=3)
button2.grid(row=5, column=3)
button3.grid(row=7, column=3)

uzrasas12.grid(row=10, column=1, columnspan=2)
laukas12_str.grid(row=11, column=0)
laukas12.grid(row=11, column=1, columnspan=2)

uzrasas22.grid(row=12, column=1, columnspan=2)
laukas22_str.grid(row=13, column=0)
laukas22.grid(row=13, column=1, columnspan=2)

uzrasas32.grid(row=14, column=1, columnspan=2)
laukas32_str.grid(row=15, column=0)
laukas32.grid(row=15, column=1, columnspan=2)

boksas22.grid(row=11, column=6, rowspan=6)
scrolbaras1.grid(row=11, column=7, rowspan=6, sticky=N+S)

boksas2.grid(row=0, column=6, rowspan=8)
scrolbaras2.grid(row=1, column=7, rowspan=7, sticky=N+S)
scrolbaras3.grid(row=8, column=6, sticky=W+E)

button12.grid(row=11, column=3)
button22.grid(row=13, column=3)
button32.grid(row=15, column=3)

uzrasas111.grid(row=9 , column=0, columnspan=10)
button4.grid(row=9, column=6)

balanso_uzrasas.grid(row=20, column=3)
status.grid(row=20, columnspan=4, sticky=W+E)
laikrodis.grid(row=20, column=6, columnspan=2, sticky=W+E)
komanda.grid(row=20, column=0, columnspan=3, sticky=W)

top_frame.pack()
buttom_frame.pack()


if __name__ == '__main__':
    main_langas.mainloop()
