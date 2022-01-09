class IntLiteral:
    def __init__(self,strval,intparser=None):
        self.strval=strval
        self.intparser=intparser or int
        
    def value(self):
        return self.intparser(self.strval)


# arbitrary custom integer parser
def custint(x):
    if '.' in x:
        return int(x.split('.')[0])
    return int(x)

sn1=IntLiteral('3')
pn1=sn1.value()
print(pn1,type(pn1)) # 3 <class 'int'>

sn2=IntLiteral('42.5',custint)
pn2=sn2.value()
print(pn2,type(pn2)) # 42 <class 'int'>

