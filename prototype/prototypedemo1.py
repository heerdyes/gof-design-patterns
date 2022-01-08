class SoftSynth:
    def __init__(self,polyphony,channels,latency):
        self.polyphony=polyphony
        self.channels=channels
        self.latency=latency
        
    def __str__(self):
        return 'SoftSynth[poly=%d,ch=%d,lat=%d]'%(self.polyphony,self.channels,self.latency)


class AnalogSynth:
    def __init__(self,polyphony):
        self.polyphony=polyphony
    
    def __str__(self):
        return 'AnalogSynth[poly=%d]'%self.polyphony
        

class SynthWorkstation:
    def __init__(self,polyphony,channels):
        self.polyphony=polyphony
        self.channels=channels
        
    def __str__(self):
        return 'SynthWorkstation[poly=%d,ch=%d]'%(self.polyphony,self.channels)


instmenu={
    'sw': (SynthWorkstation, 128, 16),
    'as': (AnalogSynth, 4),
    'ss': (SoftSynth, 256, 256, 50)
}

print('enter inst code [sw,as,ss]: ')
inst=input()
syn=instmenu[inst]
# reminiscent of lisp's car and cdr
i0=syn[0](*syn[1:])
print(i0)

