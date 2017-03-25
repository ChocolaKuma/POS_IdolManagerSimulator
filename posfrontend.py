import tkinter as tk
from tkinter import ttk

day = 1
LARGE_FONT= ("Verdana", 12)
starttext = """This Game is still in development
Please keep that in mind.
Nothing in this is the final product."""
def nextday():
    global day
    day = day + 1
    print(day)

class POSIS(tk.Tk):

    def __init__(self, *args, **kwargs):
        
        tk.Tk.__init__(self, *args, **kwargs)
        tk.Tk.iconbitmap(self,default="src/icons/icon.ico")
        tk.Tk.wm_title(self,"Piece of Sh!t Idol Manager Simulator © 2017")
        container = tk.Frame(self)
        container.pack(side="top", fill="both", expand = True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}

        for F in (StartPage, News, Girls,Staff,Infu,Events):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()

        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text=starttext, font=LARGE_FONT)
        label.grid(row=1,column=2)

        button = ttk.Button(self, text="New Game",
                            command=lambda: controller.show_frame(News))
        button.grid(row=2,column=1)
        
        button = ttk.Button(self, text="Load Game\nNot Devloped",
                            command=lambda: controller.show_frame(News))
        button.grid(row=2,column=3)


class News(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button1 = ttk.Button(self, text="News",
                            command=lambda: controller.show_frame(News))
        button1.grid(row=2,column=1)
        button2 = ttk.Button(self, text="Girls",
                            command=lambda: controller.show_frame(Girls))
        button2.grid(row=2,column=2)
        button3 = ttk.Button(self, text="Staff",
                            command=lambda: controller.show_frame(Staff))
        button3.grid(row=2,column=3)
        button4 = ttk.Button(self, text="Infustucture",
                            command=lambda: controller.show_frame(Infu))
        button4.grid(row=2,column=4)
        button4 = ttk.Button(self, text="Events",
                            command=lambda: controller.show_frame(Events))
        button4.grid(row=2,column=5)   
        currentselection = tk.Label(self, text="News", font=LARGE_FONT)
        currentselection.grid(row=2,column=6)
        daycount = tk.Label(self, text="Day"+str(day), font=LARGE_FONT)
        daycount.grid(row=2,column=7)        
        button5 = ttk.Button(self, text="NextDay",
                            command=nextday)
        button5.grid(row=2,column=8)         
class Girls(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button1 = ttk.Button(self, text="News",
                            command=lambda: controller.show_frame(News))
        button1.grid(row=2,column=1)
        button2 = ttk.Button(self, text="Girls",
                            command=lambda: controller.show_frame(Girls))
        button2.grid(row=2,column=2)
        button3 = ttk.Button(self, text="Staff",
                            command=lambda: controller.show_frame(Staff))
        button3.grid(row=2,column=3)
        button4 = ttk.Button(self, text="Infustucture",
                            command=lambda: controller.show_frame(Infu))
        button4.grid(row=2,column=4)
        button4 = ttk.Button(self, text="Events",
                            command=lambda: controller.show_frame(Events))
        button4.grid(row=2,column=5)   
        currentselection = tk.Label(self, text="Girls", font=LARGE_FONT)
        currentselection.grid(row=2,column=6)
        button5 = ttk.Button(self, text="NextDay",
                            command=nextday)
        button5.grid(row=2,column=8)
        daycount = tk.Label(self, text="Day"+str(day), font=LARGE_FONT)
        daycount.grid(row=2,column=7) 
        ##TODO Add multigirl Support
        

class Staff(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button1 = ttk.Button(self, text="News",
                            command=lambda: controller.show_frame(News))
        button1.grid(row=2,column=1)
        button2 = ttk.Button(self, text="Girls",
                            command=lambda: controller.show_frame(Girls))
        button2.grid(row=2,column=2)
        button3 = ttk.Button(self, text="Staff",
                            command=lambda: controller.show_frame(Staff))
        button3.grid(row=2,column=3)
        button4 = ttk.Button(self, text="Infustucture",
                            command=lambda: controller.show_frame(Infu))
        button4.grid(row=2,column=4)
        button4 = ttk.Button(self, text="Events",
                            command=lambda: controller.show_frame(Events))
        button4.grid(row=2,column=5)   
        currentselection = tk.Label(self, text="Staff", font=LARGE_FONT)
        currentselection.grid(row=2,column=6)
        button5 = ttk.Button(self, text="NextDay",
                            command=nextday)
        button5.grid(row=2,column=8)
        daycount = tk.Label(self, text="Day"+str(day), font=LARGE_FONT)
        daycount.grid(row=2,column=7) 
class Infu(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button1 = ttk.Button(self, text="News",
                            command=lambda: controller.show_frame(News))
        button1.grid(row=2,column=1)
        button2 = ttk.Button(self, text="Girls",
                            command=lambda: controller.show_frame(Girls))
        button2.grid(row=2,column=2)
        button3 = ttk.Button(self, text="Staff",
                            command=lambda: controller.show_frame(Staff))
        button3.grid(row=2,column=3)
        button4 = ttk.Button(self, text="Infustucture",
                            command=lambda: controller.show_frame(Infu))
        button4.grid(row=2,column=4)
        button4 = ttk.Button(self, text="Events",
                            command=lambda: controller.show_frame(Events))
        button4.grid(row=2,column=5)   
        currentselection = tk.Label(self, text="Infustucture", font=LARGE_FONT)
        currentselection.grid(row=2,column=6)
        button5 = ttk.Button(self, text="NextDay",
                            command=nextday)
        button5.grid(row=2,column=8)
        daycount = tk.Label(self, text="Day"+str(day), font=LARGE_FONT)
        daycount.grid(row=2,column=7) 
class Events(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button1 = ttk.Button(self, text="News",
                            command=lambda: controller.show_frame(News))
        button1.grid(row=2,column=1)
        button2 = ttk.Button(self, text="Girls",
                            command=lambda: controller.show_frame(Girls))
        button2.grid(row=2,column=2)
        button3 = ttk.Button(self, text="Staff",
                            command=lambda: controller.show_frame(Staff))
        button3.grid(row=2,column=3)
        button4 = ttk.Button(self, text="Infustucture",
                            command=lambda: controller.show_frame(Infu))
        button4.grid(row=2,column=4)
        button4 = ttk.Button(self, text="Events",
                            command=lambda: controller.show_frame(Events))
        button4.grid(row=2,column=5)   
        currentselection = tk.Label(self, text="Events", font=LARGE_FONT)
        currentselection.grid(row=2,column=6)
        button5 = ttk.Button(self, text="NextDay",
                            command=nextday)
        button5.grid(row=2,column=8)
        daycount = tk.Label(self, text="Day"+str(day), font=LARGE_FONT)
        daycount.grid(row=2,column=7) 
app = POSIS()
app.mainloop()
