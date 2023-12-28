import turtle as t

class Disk:
    def __init__(self, name="", x=0, y=0, height=20, width=40):
        self.dname = name
        self.dxpos = x
        self.dypos = y
        self.dheight = height
        self.dwidth = width
        self.t = t.Turtle()
    
    def showdisk(self):
        self.t.penup()
        self.t.goto(self.dxpos, self.dypos)
        self.t.setheading(0)
        
        
        self.t.fillcolor("brown")
        self.t.begin_fill()
        self.t.pendown()
        self.t.forward(self.dwidth/2)
        self.t.left(90)
        self.t.forward(self.dheight)
        self.t.left(90)
        self.t.forward(self.dwidth)
        self.t.left(90)
        self.t.forward(self.dheight)
        self.t.left(90)
        self.t.forward(self.dwidth/2)
        self.t.end_fill()
        self.t.penup()
        self.t.setheading(0)
        self.t.goto(self.dxpos, self.dypos)
    
    def newpos(self, x, y):
        self.dxpos = x
        self.dypos = y
    
    def cleardisk(self):
        self.t.setheading(0) 
        self.t.goto(self.dxpos, self.dypos) 
        self.t.clear()  
        self.t.setheading(0)  
        self.t.goto(self.dxpos, self.dypos) 

class Pole:
    def __init__(self,name="", xpos=0, ypos=0, length=100, thick=10):
        self.pname = name
        self.pxpos = xpos
        self.pypos = ypos
        self.plength = length
        self.pthick = thick
        self.stack = []
        self.toppos = 0
        
    def showpole(self):
        t.penup()
        t.goto(self.pxpos, self.pypos)
        t.setheading(0)
        t.pendown()
        t.fillcolor("black")
        t.begin_fill()
        for i in range(2):
            t.forward(self.pthick/2)
            t.left(90)
            t.forward(self.plength)
            t.left(90)
        t.end_fill()
        t.penup()
        t.setheading(0)
    
    def pushdisk(self, disk):
        if not self.stack or disk.dwidth < self.stack[-1].dwidth:
            disk.newpos(self.pxpos, self.toppos)
            self.toppos += disk.dheight
            self.stack.append(disk)
            disk.showdisk()
        else:
            print("Invalid Move. Cannot place a larger disk on top of a smaller one.")
    
    def popdisk(self):
        if self.stack:
            disk = self.stack.pop()
            disk.cleardisk()
            if self.stack:
                self.toppos = self.stack[-1].dypos + self.stack[-1].dheight
            else:
                self.toppos = 0
            return disk
        else:
            print("No disk to pop.")
            return None