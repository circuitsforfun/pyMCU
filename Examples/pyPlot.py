
import os,sys, subprocess, time, shutil, glob
import pymcu
import  numpy  as  np
import  matplotlib
matplotlib.use('GTKAgg')  # do this before importing pylab
 
import  matplotlib.pyplot  as  plt
 
mb = pymcu.mcuModule()
 
fig  =  plt.figure()
 
ax  =  fig.add_subplot(111)
ax.set_ylim(-1.1, 1.1)
ax.set_xlim(0, 5)
ax.grid()
 
def  animate():
    tstart  =  time.time() # for profiling
    data = [0]*100
    background = fig.canvas.copy_from_bbox(ax.bbox)
 
    for  i  in  np.arange(1,1000):
        ax.clear()
        ax.grid()
        dt = float(mb.analogRead(4)) / 1024.0
        data.append(dt)
        if len(data) > 100:
            data.pop(0)
 
        ax.plot(data)
        fig.canvas.draw() # redraw the canvas
 
    raise  SystemExit
 
import  gobject
print  'adding idle'
gobject.idle_add(animate)
print  'showing'
plt.show()
