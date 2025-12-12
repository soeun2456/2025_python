from tkinter import *
import random
import time

tk = Tk()
tk.title("Game 02: Score")
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
        self.score = 0 # 점수 변수 추가
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.reset()

    def reset(self):
        self.canvas.coords(self.id, 10, 10, 25, 25)
        self.canvas.move(self.id, 245, 100)
        starts = [-3, -2, -1, 1, 2, 3]
        random.shuffle(starts)
        self.x = starts[0]
        self.y = -3
        self.score = 0 # 재시작 시 점수 초기화
        self.hit_bottom = False
        canvas.itemconfigure(score_label, text=f"Score: {self.score}") # 점수판 업데이트

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
            self.y = 3
        if pos[3] >= self.canvas_height:
            self.hit_bottom = True
        
        if self.hit_paddle(pos) == True:
            self.y = -3
            self.score += 1 # 패들에 닿으면 점수 증가
            canvas.itemconfigure(score_label, text=f"Score: {self.score}") # 화면 점수 업데이트
        
        if pos[0] <= 0:
            self.x = 3
        if pos[2] >= self.canvas_width:
            self.x = -3

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

# 점수 표시용 텍스트


game_over_text = canvas.create_text(250, 150, text="GAME OVER", state='hidden', font=('Helvetica', 30), fill='red')
restart_text = canvas.create_text(250, 200, text="Click to Restart", state='hidden', font=('Helvetica', 15))

def restart_game(event):
    if ball.hit_bottom:
        ball.reset()
        canvas.itemconfigure(game_over_text, state='hidden')
        canvas.itemconfigure(restart_text, state='hidden')

canvas.bind("<Button-1>", restart_game)

while True:
    try:
        # 1. 게임이 진행 중일 때
        if not ball.hit_bottom:
            ball.draw()    # 에러 발생 지점! (창이 없는데 그리려고 해서)
            paddle.draw()  # 에러 발생 지점!
        
        # 2. 게임 오버일 때 (텍스트 띄우기)
        else:
            canvas.itemconfigure(game_over_text, state='normal')
            canvas.itemconfigure(restart_text, state='normal')
            
        # 3. 화면 업데이트
        tk.update_idletasks()
        tk.update()
        time.sleep(0.01)

    except TclError:
        # 창이 닫혀서 에러가 나면 반복문을 조용히 종료
        break
    except:
        # 그 외 오류도 종료
        break