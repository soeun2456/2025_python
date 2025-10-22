class Ab:
    def reset(self):
        self.count=0
    def increment(self):
        self.count+=1
    def get(self):
        return self.count
    
a=Ab()
b=Ab()

a.reset()
b.reset()

a.increment()
a.increment()
a.increment()

b.increment()
print('카운트 a 값은?:',a.get())
print('카운트 b 값은?:',b.get())

