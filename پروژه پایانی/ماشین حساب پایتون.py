from tkinter import*

def fCalc(source, side):
    appObj = Frame(source, borderwidth=5, bd=5,bg = "light blue")
    appObj.pack(side=side, expand=YES, fill=BOTH)
    return appObj

def button(source, side, text, command=None):
    appObj = Button(source, text=text, command=command)
    appObj.pack(side=side, expand=YES, fill=BOTH)
    return appObj

class app(Frame):
    def __init__(self, root = Tk(), width=420, height=540):
        Frame.__init__(self)
        self.option_add("*Font", 'arial 20 bold')
        self.pack(expand=YES, fill=BOTH)
        self.master.title("Calculator")
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
               
        display = StringVar()
        Entry(self, relief= RAISED,      
               textvariable=display, state=DISABLED, justify='right', bd=20, bg="light blue").pack(side=TOP, expand=YES,
                            fill=BOTH)
        clrChar = "C"
        button(self, TOP, clrChar, lambda appObj=display, i=clrChar: appObj.set(''))
        
        for btnNum in ("789/", "456*", "123-", "0.+"):

            FunctionNum = fCalc(self, TOP)
            for fEquals in btnNum:
                button(FunctionNum, LEFT, fEquals,
                        lambda appObj=display, i=fEquals: appObj.set(appObj.get() + i))
                EqualsButton = fCalc(self, TOP)
                
        for fEquals in "=":
            if fEquals == "=":
                btnEquals = button(EqualsButton, LEFT, fEquals)
                btnEquals.bind('<ButtonRelease-1>',
                                lambda e, s=self, appObj=display: s.result(appObj), "+")

            else:
                btnEquals = button(EqualsButton, LEFT, fEquals,
                        lambda appObj=display, s=" %s "%fEquals: appObj.set(appObj.get()+s))
    def result(self, display):
        try:
            display.set(eval(display.get()))
        except:
            display.set("UNDEFINED")
       

            


if __name__ == '__main__':
    app().mainloop()


