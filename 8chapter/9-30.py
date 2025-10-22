class Tv:
    def __init__(self,channel,volume,on):
        self.channel=channel
        self.volume=volume
        self.on=on
    def show(self):
        print(self.channel,self.volume,self.on)
    def schannel(self,channel):
        self.channel=channel
    def a(self):
        return self.channel
    
t=Tv(9,10,True)
t.show()
t.schannel(11)
t.show()