class Ab:
    def reset(self):
        self.count=0
    def increment(self):
        self.count+=1
    def get(self):
        return self.count
    
a=Ab()

a.reset()
a.increment()
print('a 값',a.get())