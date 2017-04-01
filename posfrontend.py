import tkinter as tk
from tkinter import ttk
import idlemanager as im

CurrentDay = 1
CashOnHand = 9999999

LARGE_FONT= ("Verdana", 12)
starttext = """This Game is still in development
Please keep that in mind.
Nothing in this is the final product."""
Idol = im.girl()
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

        for F in (StartPage, News):

            frame = F(container, self)

            self.frames[F] = frame

            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(StartPage)

    def show_frame(self, cont):

        frame = self.frames[cont]
        frame.tkraise()
def nextday():
    global CurrentDay
    CurrentDay = CurrentDay + 1
    print(CurrentDay)

def tT():
    pass
def eT():
    pass
def cT():
    pass
def pT():
    pass
        
class StartPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self,parent)
        label = tk.Label(self, text=starttext, font=LARGE_FONT)
        label.grid(row=1,column=2)

        button = ttk.Button(self, text="New Game",
                            command=lambda: controller.show_frame(News))
        button.grid(row=2,column=1)
        
        #button = ttk.Button(self, text="Load Game\nNot Devloped",
                            #command=lambda: controller.show_frame(News))
        #button.grid(row=2,column=3)


class News(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        button1 = ttk.Button(self, text="Talent Training",
                            command=lambda: controller.show_frame(News))
        button1.grid(row=2,column=1)
        button2 = ttk.Button(self, text="Energy Training",
                            command=lambda: controller.show_frame(Girls))
        button2.grid(row=2,column=2)
        button3 = ttk.Button(self, text="Cuteness Training",
                            command=lambda: controller.show_frame(Staff))
        button3.grid(row=2,column=3)
        button4 = ttk.Button(self, text="Infustucture",
                            command=lambda: controller.show_frame(Infu))
        button4.grid(row=2,column=4)
        button4 = ttk.Button(self, text="Popularity Training",
                            command=lambda: controller.show_frame(Events))
        button4.grid(row=2,column=5)   

        daycount = tk.Label(self, text="Day"+str(CurrentDay), font=LARGE_FONT)
        daycount.grid(row=2,column=7)        
        button5 = ttk.Button(self, text="NextDay",
                            command=nextday)
        button5.grid(row=2,column=8)
#########################################
        #TODO Make this fucker work!!!
        #img = tk.PhotoImage(file="img\girl.jpg")
        #img = img.zoom(ZoomAMT) 
        #img = img.subsample(40)
        #logoPNG = Label(self, image=img).grid(row=3,column=1) 
        #label = tk.Label(image="./img/girl.jpg")
        #label.image = photo # keep a reference!
        #label.grid(row=3,rowspan=,column=1)
#########################################
        NameLabel = tk.Label(self, text="Name:"+Idol.fName+" "+Idol.lName, font=LARGE_FONT)
        NameLabel.grid(row=3,column=2) 
        AgeLabel = tk.Label(self, text="Age:"+str(Idol.age)+" "+Idol.bday, font=LARGE_FONT)
        AgeLabel.grid(row=4,column=2)         
        TalentLabel = tk.Label(self, text="Talent:"+str(Idol.talent)+"/5", font=LARGE_FONT)
        TalentLabel.grid(row=5,column=2) 
        EnergyLabel = tk.Label(self, text="Energy:"+str(Idol.energy)+"/20", font=LARGE_FONT)
        EnergyLabel.grid(row=6,column=2)
        CuteLabel = tk.Label(self, text="Cuteness:"+str(Idol.cuteness)+" /10", font=LARGE_FONT)
        CuteLabel.grid(row=7,column=2)
        PopLabel = tk.Label(self, text="Popularity:"+str(Idol.popularity), font=LARGE_FONT)
        PopLabel.grid(row=8,column=2)
        SignedLabel = tk.Label(self, text="Signed:"+str(Idol.signed), font=LARGE_FONT)
        SignedLabel.grid(row=9,column=2)
        MoneyLabel = tk.Label(self, text="Money:"+"¥"+str(CashOnHand), font=LARGE_FONT)
        MoneyLabel.grid(row=10,column=2)
app = POSIS()
app.mainloop()
