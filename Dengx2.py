from tkinter import *
import random
import time

counter = 0
counter1 = 0

# หน้าจอ
tk = Tk()
tk.title('Dengx2')
tk.resizable(0,0)

canvas = Canvas(tk, width=500, height=400, bd = 0)
f = PhotoImage(file='pg.png')
f2 = PhotoImage(file='bg1.png')
home = canvas.create_image(0,400,anchor=SW,image=f)
canvas.pack()
tk.update()

class bg1:
    def __init__(self,canvas):
        self.canvas=canvas
        self.canvas.create_image(0,400,anchor=SW,image=f2)
        
class Ball:
    def __init__(self,canvas,color,paddle,paddle1):
        self.canvas = canvas
        self.paddle = paddle
        self.paddle1 = paddle1
        self.id = canvas.create_oval(10,10,25,25,fill=color)
        self.canvas.move(self.id,233,200)
        start = [-3,3]
        random.shuffle(start)
        self.x = start[0]
        self.y = -3
        self.canvas_height = self.canvas.winfo_height()#ไม่ทะลุขอบบน
        self.canvas_width = self.canvas.winfo_width()
        self.counter = 0
        self.counter1 = 0
        

    def hit_paddle(self,pos):#ไม่ทะลุไม้
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[0] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
                return True
            return False

    def hit_paddle1(self,pos):
        paddle_pos = self.canvas.coords(self.paddle1.id)
        if pos[1] >= paddle_pos[1] and pos[1] <= paddle_pos[3]:
            if pos[2] >= paddle_pos[0] and pos[2] <= paddle_pos[2]:
                return True
            return False
        
    def draw(self):
        self.canvas.move(self.id,self.x,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.y = -3
        if pos[0] <= 0:
            self.x = 3
            self.score(True)
        if pos[2] >= self.canvas_width:
            self.x = -3
            self.score(False)
        if self.hit_paddle(pos) == True:
            self.x = 3
        if self.hit_paddle1(pos) == True:
            self.x = -3

    def score(self,val):
        global counter
        global counter1

        if val == True:
            a = self.canvas.create_text(375,40,text = counter,font = ("Terminal",40),fill = 'white')
            canvas.itemconfig(a,fill = 'black')
            counter += 1
            a = self.canvas.create_text(375,40,text = counter,font = ("Terminal",40),fill = 'white')

        if val == False:
            a = self.canvas.create_text(125,40,text = counter1,font = ("Terminal",40),fill = 'white')
            canvas.itemconfig(a,fill = 'black')
            counter1 += 1
            a = self.canvas.create_text(125,40,text = counter1,font = ("Terminal",40),fill = 'white')

    
class Paddle:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0,150,30,250,fill=color)
        self.y = 0
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('w',self.turn_up)#ตั้งปุ่มบังคับ
        self.canvas.bind_all('s',self.turn_down)

    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= 400:
            self.y = 0

    def turn_up(self,evt):#ขยับ
        self.y = -3
    def turn_down(self,evt):
        self.y = 3

class Paddle1:
    def __init__(self,canvas,color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(470,150,500,250,fill=color)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.y = 0
        self.canvas.bind_all('<KeyPress-Up>',self.turn_up)#ตั้งปุ่มบังคับ
        self.canvas.bind_all('<KeyPress-Down>',self.turn_down)

    def draw(self):
        self.canvas.move(self.id,0,self.y)
        pos = self.canvas.coords(self.id)
        if pos[1] <= 0:
            self.y = 0
        if pos[3] >= 400:
            self.y = 0
        
    def turn_up(self,evt):#ขยับ
        self.y = -3
    def turn_down(self,evt):
        self.y = 3
    
    
            
        
def play(event): #เรียกใช้
    global paddle,paddle1,ball,start
    if event.keysym == 'space':
        bg1(canvas)
        paddle = Paddle(canvas,'white')
        paddle1 = Paddle1(canvas,'gray')
        ball = Ball(canvas,'orange',paddle,paddle1)
        start = 1
        canvas.delete(home)        
canvas.bind_all('<KeyPress-space>',play)
start = 0
while True:
    if start == 1:
        ball.draw()
        paddle.draw()
        paddle1.draw()
    if counter == 7:
        ball.x = 0
        ball.y = 0
        paddle.y = 0
        paddle1.y = 0
        canvas.create_text(365,200,text = 'Congrats Player 2! You Win!',font = ("Terminal",11),fill = 'white')
        canvas.create_text(365,215,text = 'Score: '+str(counter)+'-'+str(counter1),font = ("Terminal",11),fill = 'white')
    if counter1 == 7:
        ball.x = 0
        ball.y = 0
        paddle.y = 0
        paddle1.y = 0
        canvas.create_text(120,200,text = 'Congrats Player 1! You Win!',font = ("Terminal",11),fill = 'white')
        canvas.create_text(120,215,text = 'Score: '+str(counter1)+'-'+str(counter),font = ("Terminal",11),fill = 'white')
    
    #tk.update_idletask()
    tk.update()
    time.sleep(0.0003)

    if counter==7 or counter1 ==7:
        break
    
