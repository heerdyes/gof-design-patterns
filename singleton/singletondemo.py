class Turtlebot:
    _instance = None
    
    def __init__(self):
        raise RuntimeError('simulating a private constructor by blowing __init__ up!')
        
    @classmethod
    def instance(cls,x,y,a):
        if cls._instance is None:
            print('creating first instance...')
            cls._instance=cls.__new__(cls)
            cls._instance.x=x
            cls._instance.y=y
            cls._instance.a=a
        return cls._instance
        
    def __str__(self):
        return 'turtlebot: %d, %d, %d'%(self.x,self.y,self.a)


#t0=Turtlebot(3,4,0) # this is rendered impossible
t0=Turtlebot.instance(3,4,0)
print(t0)
t1=Turtlebot.instance(6,8,90) # parameters have no effect, simply returns the existing _instance
print(t1)

