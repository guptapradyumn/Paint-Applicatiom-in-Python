from tkinter import *
from tkinter import messagebox
from PIL import Image,ImageTk,ImageDraw
root=Tk()
root.maxsize(width=800, height=600)
root.title("Paint")
class draw:
    def __init__(self,root):      #init method of class draw
    
        self.root=root
        self.radiobuttonValue = IntVar()
        self.radiobuttonValue.set(1)
        self.colorvalue = IntVar()
        self.colorvalue.set(0)
        self.leftframe=Frame(root)
        self.leftframe.pack(side=LEFT, fill =Y)
        self.canvas=Canvas(root,width=800,height=600,relief=RAISED, borderwidth=5)   
        self.canvas.pack(side = RIGHT)
        self.canvas.bind("<ButtonPress-1>",self.btpress)
        self.canvas.bind("<B1-Motion>",self.line)
        self.canvas.bind("<ButtonRelease-1>",self.make)
        self.filename=''
        self.create()

    def fillcolor(self,x,y,s):         #function for filling colors
        oldcolor=self.img.getpixel((x,y))
        if(oldcolor==s):
            return
        list=[]
        t=(x,y)
        list.append(t)
        while list:
            seed=list.pop(0)
            seedcolor=self.img.getpixel(seed)
            if(seedcolor==oldcolor):
                self.img.putpixel(seed,s)
                x,y=seed[0],seed[1]
                list.append((x+1,y))
                list.append((x,y+1))
                list.append((x-1,y))
                list.append((x,y-1))
        filledimg=ImageTk.PhotoImage(self.img)
        self.colorvalue.set(0)
        return filledimg
            

    def btpress(self,event):
        self.x0=event.x
        self.y0=event.y
        if(self.colorvalue.get() == 1):
            s=(255,0,0)
            self.filled_img=self.fillcolor(event.x,event.y,s)
            self.canvas.create_image(800,600, image=self.filled_img)
        elif(self.colorvalue.get() == 2):
            s=(0,0,0)
            self.filled_img=self.fillcolor(event.x,event.y,s)
            self.canvas.create_image(800,600, image=self.filled_img)
        elif(self.colorvalue.get() == 3):
            s=(0,0,255)
            self.filled_img=self.fillcolor(event.x,event.y,s)
            self.canvas.create_image(800,600, image=self.filled_img)
        elif(self.colorvalue.get() == 4):
            s=(255,255,0)
            self.filled_img=self.fillcolor(event.x,event.y,s)
            self.canvas.create_image(800,600, image=self.filled_img)
        elif(self.colorvalue.get() == 5):
            s=(0,100,0)
            self.filled_img=self.fillcolor(event.x,event.y,s)
            self.canvas.create_image(800,600, image=self.filled_img)
        elif(self.colorvalue.get() == 6):
            s=(255,128,0)
            self.filled_img=self.fillcolor(event.x,event.y,s)
            self.canvas.create_image(800,600, image=self.filled_img)
        
    def delteAll(self):          #fuction of clearing paper
        self.canvas.delete("all")
        self.img=Image.new("RGB",(1600,1200),'white')
        self.use=ImageTk.PhotoImage(self.img)
        self.canvas.img=self.use
        self.canvas.create_image(0,0, image=self.canvas.img)

        
    def line(self,event):            #function for line and pattern 1
        if(self.radiobuttonValue.get() == 5):
            self.draw=ImageDraw.Draw(self.img)
            self.canvas.create_line(self.x0,self.y0,event.x,event.y)
            a=(self.x0,self.y0)
            b=(event.x,event.y)
            c='black'
            self.draw.line((a,b),c)
        if(self.radiobuttonValue.get() == 6):
            self.draw=ImageDraw.Draw(self.img)
            self.canvas.create_line(self.x0,self.y0,event.x,event.y)
            a=(self.x0,self.y0)
            b=(event.x,event.y)
            c='black'
            self.draw.line((a,b),c)
            self.x0=event.x
            self.y0=event.y
    def lets_save(self):
        self.filename=self.new_entry.get()
        if(self.filename==''):
            messagebox.showinfo("Error","plzzz enter file name!!!!")
        else:
            self.img1=self.img.crop((0,0,800,600))
            self.img1.save(self.filename+'.jpg')
        self.new_window.destroy()
    def saveas(self):
        self.new_window=Toplevel(self.root)
        self.new_window.minsize(width=200, height=100)
        self.new_window.title("Save As")
        self.new_label=Label(self.new_window,text="Enter Name to save as").grid(row=2,column=1)
        self.new_entry=Entry(self.new_window)
        self.new_entry.grid(row=3,column=1)
        self.new_button=Button(self.new_window,text="save",command=self.lets_save).grid(row=4,column=1)      
                
    def save(self):             #fuction for saving image to same folder
        if(self.filename==''):
            self.saveas()
        else:
            self.img1=self.img.crop((0,0,800,600))
            self.img1.save(self.filename+'.jpg')
        
    def create(self):   #function for creating widgets
        self.labelThickness = Label(
                            self.leftframe,
                            text = "drawing tools list:",relief=SUNKEN)
        self.labelThickness.grid(row = 0,
                                 column = 0, pady = 2, padx = 3)
        Radiobutton(self.leftframe,
                    text = "line", indicatoron=0,width=10,
                    variable = self.radiobuttonValue,
                    value = 1).grid(padx = 3, pady = 2,
                                    row = 1, column = 0,
                                    sticky = NW
                                    )
        Radiobutton(self.leftframe,
                    text = "Circle",indicatoron=0,width=10,
                    variable = self.radiobuttonValue,
                    value = 2).grid(padx = 3, pady = 2,
                                    row = 2, column = 0,
                                    sticky = NW
                                    )
        Radiobutton(self.leftframe,
                    text = "Triangle",indicatoron=0,width=10,
                    variable = self.radiobuttonValue,
                    value = 3).grid(padx = 3, pady = 2,
                                    row = 3, column = 0,
                                    sticky = NW
                                    )
        Radiobutton(self.leftframe,
                    text = "Rectangle",indicatoron=0,width=10,
                    variable = self.radiobuttonValue,
                    value = 4).grid(padx = 3, pady = 2,
                                    row = 4, column = 0,
                                    sticky = NW
                                    )
        Radiobutton(self.leftframe,
                    text = "Pattern-1",indicatoron=0,width=10,
                    variable = self.radiobuttonValue,
                    value = 5).grid(padx = 3, pady = 2,
                                    row = 5, column = 0,
                                    sticky = NW
                                    )
        Radiobutton(self.leftframe,
                    text = "Pencil",indicatoron=0,width=10,
                    variable = self.radiobuttonValue,
                    value = 6).grid(padx = 3, pady = 2,
                                    row = 6, column = 0,
                                    sticky = NW
                                    )
        self.labelcolor = Label(
                            self.leftframe,
                            text = "colors list:",relief=SUNKEN)
        self.labelcolor.grid(row = 7,
                                 column = 0, pady = 2, padx = 3, sticky=NW)
        
        Radiobutton(self.leftframe,
                    text = "NONE",indicatoron=0,width=10,
                    variable = self.colorvalue,
                    value = 0).grid(padx = 3, pady = 2,
                                    row = 8, column = 0,
                                    sticky = NW
                                    )
        Radiobutton(self.leftframe,
                    text = "RED",indicatoron=0,bg="red",width=10,
                    variable = self.colorvalue,
                    value = 1).grid(padx = 3, pady = 2,
                                    row = 9, column = 0,
                                    sticky = NW
                                    )
        Radiobutton(self.leftframe,
                    text = "BLACK",indicatoron=0,bg="black",fg="white",width=10,
                    variable = self.colorvalue,
                    value = 2).grid(padx = 3, pady = 2,
                                    row = 10, column = 0,
                                    sticky = NW
                                    )
        Radiobutton(self.leftframe,
                    text = "BLUE",indicatoron=0,bg="blue",width=10,
                    variable = self.colorvalue,
                    value = 3).grid(padx = 3, pady = 2,
                                    row = 11, column = 0,
                                    sticky = NW
                                    )
        Radiobutton(self.leftframe,
                    text = "YELLOW",indicatoron=0,bg="yellow",width=10,
                    variable = self.colorvalue,
                    value = 4).grid(padx = 3, pady = 2,
                                    row = 12, column = 0,
                                    sticky = NW
                                    )
        Radiobutton(self.leftframe,
                    text = "GREEN",indicatoron=0,bg="green",width=10,
                    variable = self.colorvalue,
                    value = 5).grid(padx = 3, pady = 2,
                                    row = 13, column = 0,
                                    sticky = NW
                                    )
        Radiobutton(self.leftframe,
                    text = "ORANGE",indicatoron=0,bg="orange",width=10,
                    variable = self.colorvalue,
                    value = 6).grid(padx = 3, pady = 2,
                                    row = 14, column = 0,
                                    sticky = NW
                                    )
        self.clearbt = Button(self.leftframe, text = "clear paper",width=10,
                                      command = self.delteAll)
        self.clearbt.grid(padx = 3, pady = 2,
                                    row = 15 , column = 0,
                                    sticky = NW)
        self.savebt = Button(self.leftframe, text = "save",width=10,
                                      command = self.save)
        self.savebt.grid(padx = 3, pady = 2,
                                    row = 16 , column = 0,
                                    sticky = NW)
        self.save_asbt = Button(self.leftframe, text = "Save As",width=10,
                                      command = self.saveas)
        self.save_asbt.grid(padx = 3, pady = 2,
                                    row = 17 , column = 0,
                                    sticky = NW)
        
        self.img=Image.new("RGB",(1600,1200),'white')
        self.use=ImageTk.PhotoImage(self.img)
        self.canvas.img=self.use
        self.canvas.create_image(0,0, image=self.canvas.img)

    def make(self,event):  #fuction for creating shapes
        if self.radiobuttonValue.get() == 1:
            self.draw=ImageDraw.Draw(self.img)
            self.canvas.create_line(self.x0,self.y0,event.x,event.y)
            a=(self.x0,self.y0)
            b=(event.x,event.y)
            c='black'
            self.draw.line((a,b),c)
            
        elif self.radiobuttonValue.get() == 2:
            self.draw=ImageDraw.Draw(self.img)
            self.canvas.create_oval(self.x0,self.y0,event.x,event.y)
            self.draw.ellipse((self.x0,self.y0,event.x,event.y), outline='black')

        elif self.radiobuttonValue.get() == 3:
            self.draw=ImageDraw.Draw(self.img)
            self.canvas.create_line(self.x0,self.y0,event.x,event.y)
            a=(self.x0,self.y0)
            b=(event.x,event.y)
            c='black'
            self.draw.line((a,b),c)
            self.canvas.create_line(self.x0-(event.x-self.x0),event.y,event.x,event.y)
            a=(self.x0-(event.x-self.x0),event.y)
            b=(event.x,event.y)
            c='black'
            self.draw.line((a,b),c)
            self.canvas.create_line(self.x0,self.y0,self.x0-(event.x-self.x0),event.y)
            a=(self.x0,self.y0)
            b=(self.x0-(event.x-self.x0),event.y)
            c='black'
            self.draw.line((a,b),c)

        elif(self.radiobuttonValue.get() == 4):
            self.draw=ImageDraw.Draw(self.img)
            self.canvas.create_rectangle(self.x0,self.y0,event.x,event.y)
            c='black'
            self.draw.rectangle(((self.x0,self.y0),(event.x,event.y)),outline='black')
            
obj=draw(root)  #creating object of draw class
mainloop()

    
    
