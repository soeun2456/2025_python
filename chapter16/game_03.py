from tkinter import *
import random
import time

tk = Tk()
tk.title("Game 03: Speed Up Feature")
tk.resizable(0, 0)
tk.wm_attributes("-topmost", 1)

canvas = Canvas(tk, width=500, height=400, bd=0, highlightthickness=0)
canvas.pack()
tk.update()

class Ball:
    def __init__(self, canvas, paddle, color):
        self.canvas = canvas
        self.paddle = paddle
        self.id = canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple'] # 공 색상 리스트
        self.reset()

    def reset(self):
        self.canvas.coords(self.id, 10, 10, 25, 25)
        self.canvas.move(self.id, 245, 100)
        
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        
        self.speed = 3  # [아이디어] 초기 속도 설정
        
        self.x = starts[0]
        self.y = -self.speed 
        self.score = 0
        self.hit_bottom = False
        canvas.itemconfigure(score_label, text=f"Score: {self.score}")
        self.canvas.itemconfig(self.id, fill='red') # 색상 초기화

    def hit_paddle(self, pos):
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]:
            if pos[3] >= paddle_pos[1] and pos[3] <= paddle_pos[3]:
                return True
        return False
    
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        
        if pos[1] <= 0:
            self.y = self.speed # 상단 벽 충돌 시 현재 스피드로 반사
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        
        if self.hit_paddle(pos) == True:
            self.score += 1
            
            # [아이디어] 패들에 닿으면 속도 증가 (최대 속도 제한 없음)
            self.speed += 0.5 
            self.y = -self.speed
            
            # x축 속도도 현재 방향에 맞춰 스피드 증가
            if self.x > 0:
                self.x = self.speed
            else:
                self.x = -self.speed
                
            # [아이디어] 패들에 닿으면 공 색상 랜덤 변경
            random_color = random.choice(self.colors)
            self.canvas.itemconfig(self.id, fill=random_color)
            
            canvas.itemconfigure(score_label, text=f"Score: {self.score}")
        
        if pos[0] <= 0:
            self.x = self.speed # 좌측 벽
        if pos[2] >= self.canvas_width:
            self.x = -self.speed # 우측 벽

class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = canvas.create_rectangle(0, 0, 100, 10, fill=color)
        self.canvas.move(self.id, 200, 300)
        self.x = 0
        self.canvas_width = self.canvas.winfo_width()
        self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        self.canvas.bind_all('<KeyPress-Right>', self.turn_right)

    def turn_left(self, evt):
        self.x = -2

    def turn_right(self, evt):
        self.x = 2

    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
        elif pos[2] >= self.canvas_width:
            self.x = 0

paddle = Paddle(canvas, 'blue')
score_label = canvas.create_text(50, 20, text="Score: 0", font=('Helvetica', 15), fill='black')
ball = Ball(canvas, paddle, 'red')


game_over_text = canvas.create_text(250, 150, text="GAME OVER", state='hidden', font=('Helvetica', 30), fill='red')
restart_text = canvas.create_text(250, 200, text="Click to Restart", state='hidden', font=('Helvetica', 15))

def restart_game(event):
    if ball.hit_bottom:
        ball.reset()
        canvas.itemconfigure(game_over_text, state='hidden')
        canvas.itemconfigure(restart_text, state='hidden')

canvas.bind("<Button-1>", restart_game)

while True:
    if not ball.hit_bottom:
        ball.draw()
        paddle.draw()
    else:
        canvas.itemconfigure(game_over_text, state='normal')
        canvas.itemconfigure(restart_text, state='normal')
        
    tk.update_idletasks()
    tk.update()
    time.sleep(0.01)