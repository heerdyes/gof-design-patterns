class RsrcPool:
    def __init__(self, sz):
        self._pool=[Rsrc(i) for i in range(sz)]

    def acquire(self):
        if len(self._pool)<=0:
            raise Exception('no more objects in pool!')
        return self._pool.pop()

    def release(self, r):
        print('releasing %s'%str(r))
        self._pool.append(r)


class Rsrc:
    def __init__(self,_id):
        self.pid=_id
        
    def __str__(self):
        return 'R[%d]'%self.pid


opool=RsrcPool(10)
r1=opool.acquire()
print(r1)
r2=opool.acquire()
print(r2)
opool.release(r1)
opool.release(r2)
