from turtle import *
import time

def triangle(l, alfa):    
    left(alfa)
    down()

    left(90)    
    circle(4)
    right(90)

    forward(l)    
    backward(l)
    
    up()
    right(alfa)
    
def kallantyu(r, alfa): 
    left(alfa+19)
    down()
    #begin_fill()
    forward(r*0.2)
    
    right(45)
    circle(r, 90)    
    circle(-4, 150)
    circle(-r*0.85, 152)
    right(-45+90-152-150)

    #end_fill()
    right(alfa+19)
    up()    


# main --------------------------------------------------------------------------------
def main() :
    #speed(0)

    (w,h) = screensize()
    #n = int(input("Irj be, hogy mennyi kallantyut akarsz:"))
    n = 6
    #alfa = 10
    r = min(w,h)*0.9
    l = r*1.3

    up()
    for alfa in range (0, 90-round(180/n)):
        tracer(0, 0)
        clear() 
        for i in range(n):    
            forward(r)
            left(90+180/n)
            triangle(l, alfa)
            #kallantyu(r, alfa)
            right(90+180/n)
            backward(r)
            right(360/n)
        tracer(1, 0)
        down()
        up()
        time.sleep(0.1)
        
    time.sleep(3)

main()    