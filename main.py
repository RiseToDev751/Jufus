import tkinter
from tkinter import *
from tkinter import filedialog
from modules import usb_find as usb
from modules import write_iso as wiso

root = Tk()
root.title("Jufus - Yet another image writer")
root.geometry("550x230")
root.eval("tk::PlaceWindow . center")
root.resizable(width=False,height=False)

file_label = Label(text="File",fg="red",font=("Arial",15))
file_label.place(x=1,y=12)

iso_locale = StringVar()

iso_name = Entry(width=40,textvariable=iso_locale)
iso_name.place(x=5,y=42)

def select_file():
    filetypes = (
    ('Image Files', '*.iso'),
    ('All files', '*.*')
    )
    filename = filedialog.askopenfilename(
    title="Select file",
    initialdir="/home/",
    filetypes=filetypes
    )
    iso_name.insert(0,filename)

select_button = Button(text="Select iso file",command=select_file)
select_button.place(x=405, y=39)

device_label = Label(text="Device",fg="red",font=("Arial",15))
device_label.place(x=1,y=79)

menu = StringVar()
menu.set("Select Any Device")

devices_menu = OptionMenu(root,menu,*usb.usb_drive(show_all=False))
devices_menu.place(x=1,y=119)

def writing():
    wiso.write(locale=iso_locale.get(),device=menu.get())

burn_button = Button(text="Write ISO file",width=57,command=writing)
burn_button.place(x=1,y=155)

root.mainloop()