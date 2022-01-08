import copy

class BigBangPrototype:
    def __init__(self,attrs):
        self.attrs=attrs
    
    def clone(self):
        return BigBangPrototype(copy.deepcopy(self.attrs))
        
    def __str__(self):
        return 'attrs: '+str(self.attrs)


# original prototype that is the source of all objects
selobj='O'
symtab={
    'O':BigBangPrototype({})
}

while True:
    print('1. show objects')
    print('2. create object')
    print('3. customize object')
    print('q. quit')
    ch=input()
    if ch=='1':
        print('-----')
        for k in symtab.keys():
            print(k,symtab[k])
        print('-----')
    elif ch=='2':
        print('[mkobj] select prototyping source: ',end='')
        src=input().strip()
        print('[mkobj] object name: ',end='')
        onm=input().strip()
        symtab[onm]=symtab[src].clone()
    elif ch=='3':
        print('[custom] object name: ',end='')
        selobj=input().strip()
        custobj=symtab[selobj]
        while True:
            print('[customizer] > ',end='')
            inarr=input().strip().split(' ')
            if inarr[0]=='_q':
                break
            custobj.attrs[inarr[0]]=inarr[1]
        symtab[selobj]=custobj
    elif ch=='q':
        break
    else:
        print('unknown option: '+ch)

