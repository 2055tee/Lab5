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
