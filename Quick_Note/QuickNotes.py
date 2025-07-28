from tkinter import *

color_bg = "White"
color_fg = "Black"
Menu_bg = "Black"

MainWindow = Tk()
MainWindow.geometry('350x200')
MainWindow.title("Quick Notes")
MainWindow.wm_resizable(False, False)

def Change_appearance(color_bg, color_fg):
    NotesArea['bg'] = color_bg
    NotesArea['fg'] = color_fg
    
def white_on_black():
    global Menu_bg
    color_bg = "Black"
    color_fg = "White"
    Menubar['bg'] = Menu_bg
    NotesArea.configure(insertbackground="White")
    Change_appearance(color_bg, color_fg)
    
def Default():
    global color_bg, color_fg, Menu_bg
    Menubar['bg'] = Menu_bg
    Change_appearance(color_bg, color_fg)

def Black_on_orange():
    color_bg = "Orange"
    color_fg = "Black"
    Menubar['bg'] = "green"
    Change_appearance(color_bg, color_fg)
    
def Change_color(Name,textcolor):
    NotesArea.tag_configure(f"{Name}", foreground=textcolor)
    try:
        NotesArea.tag_add(f"{Name}", "sel.first", "sel.last")
    except Exception as e:
        pass
    
def Color_green():
    Name = "green_color"
    text_color = "Green"
    Change_color(Name, text_color)

def Color_Red():
    Name = "Red_color"
    text_color = "Red"
    Change_color(Name, text_color)
    
def Color_blue():
    Name = "Blue_color"
    text_color = "Blue"
    Change_color(Name, text_color)

Menubar =  Menu(MainWindow, bg=Menu_bg)
Appearance = Menu(Menubar)
Menubar.add_cascade(label="Appearance", menu=Appearance)
Appearance.add_command(label="White on black", command=white_on_black)
Appearance.add_command(label="Default", command=Default)
Appearance.add_command(label="Black on orange", command=Black_on_orange)

Text_color = Menu(Menubar, tearoff=0)
Menubar.add_cascade(label="Text Color", menu=Text_color)
Text_color.add_command(label="Green", command=Color_green)
Text_color.add_command(label="Red", command=Color_Red)
Text_color.add_command(label="Blue", command=Color_blue)

MainWindow.config(menu=Menubar)

NotesArea = Text(MainWindow, bg=color_bg, fg=color_fg, font="Ubuntu 15 bold")
NotesArea.pack(fill=BOTH)

MainWindow.mainloop()