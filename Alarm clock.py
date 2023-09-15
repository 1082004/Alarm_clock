

# Importing modules
import turtle
import time
import winsound

# Creating screen
wn = turtle.Screen()
wn.bgcolor("White") 
wn.setup(width=300,height=200)    
wn.title("Alarm")
wn.tracer(0)

# Creating pens
pen1 = turtle.Turtle()
pen1.speed(0)
pen1.penup()
pen1.hideturtle()

pen2 = turtle.Turtle()
pen2.speed(0)
pen2.penup()
pen2.hideturtle()

pen3 = turtle.Turtle()
pen3.speed(0)
pen3.penup()
pen3.hideturtle()

# Creating a time variable
Time = time.strftime("%H:%M:%S")

# Display the current time and wait for input
print("")
print("Now it's " + Time + ".")
Alarm = input("Enter the time in HH:MM:SS format: ")
print("")

# Creating the confirmation
print("You'll be notified at " + Alarm + ".")
yes_no = input("Would you like to set this alarm? [y/n] ").lower()
print("")

# Creating functions
def draw_clock():
    pen1.pencolor("black")
    pen1.pensize(5)
    X = pen1.xcor =-75
    Y = pen1.ycor =45
    pen1.goto(X,Y)
    pen1.pendown()
    for i in range(2) :
        pen1.fd(150)
        pen1.rt(90)
        pen1.fd(50)
        pen1.rt(90)
    pen1.penup()
    pen2.penup()
    pen2.goto(X-15,Y+15)
    pen2.pencolor("gray")
    pen2.pensize(25) 
    pen2.pendown()
    for i in range(2):
        pen2.fd(180)
        pen2.rt(90)
        pen2.fd(80)
        pen2.rt(90)
        
def clock_time():
    pen3.pencolor("green")
    pen3.goto(0,0)
    pen3.clear()
    pen3.write (h + ":" + m +":" + s, font =( "D" , 25 ,"normal" ), align = "center")
    pen3.penup()
    pen3.goto(0,-32)
    pen3.pendown()
    pen3.write( d , font = ( "D" , 15 , "normal"))               

# Main loops
while yes_no == "n" or yes_no == "no":
    print("")
    print("Now it's "+ Time +".")
    Alarm = input("Enter the time in HH:MM:SS format: ")
    print("")
    print("You'll be notified at " + Alarm +".")
    yes_no = input("Would you like to set this alarm? [y/n] ").lower()
    print("")
    
while yes_no == "y" or yes_no =="yes":
    try:
        while True:
            Time = time.strftime ("%H:%M:%S")
            h = time.strftime("%H")
            m = time.strftime("%M")
            s = time.strftime("%S")
            d = time.strftime("%D")
            clock_time()
            draw_clock()
            wn.update()
            if Time == Alarm:
                winsound.Beep(1000, 5000) # Beep sound with frequency 1000 Hz and duration 5000 ms
                break # Break the loop when the alarm goes off
            time.sleep(1) # Wait for one second before updating the time
    except ValueError: # Handle the invalid input
        print("Invalid time format. Please enter the time in HH:MM:SS format.")
        yes_no = "n" # Set yes_no to "n" to ask for a new input

wn.mainloop() # Keep the turtle window open until closed manually