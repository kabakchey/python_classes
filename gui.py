import tkinter as tk


# Design in QTCreator:
#   - video course: https://www.youtube.com/watch?v=53oeJPKRttY
#   - pyuic4 editorFrame.ui -o editorFrame.py


#-------------------------------------------------------------
class HelloWorld(tk.Frame):
    def __init__(self, parent):
        super(HelloWorld, self).__init__(parent)

        self.lbl_hello      = tk.Label(self, text="Hello, World!")
        self.btn_quit       = tk.Button(self, text="QUIT", fg="red", command=self.quit)
        self.btn_hi_there   = tk.Button(self, text="Hello", command=self.say_hi)

        self.lbl_hello.pack(padx=20, pady=20)
        self.btn_quit.pack(side=tk.LEFT)
        self.btn_hi_there.pack(side=tk.LEFT)

    def say_hi(self):
        print ("hi there, everyone!")


#-------------------------------------------------------------
def simple_window():
    root = tk.Tk()

    main = HelloWorld(root)
    main.pack(fill="both", expand=True)

    root.mainloop()

#-------------------------------------------------------------
def turtle_demo():
    import turtle

    spiral = turtle.Turtle()
    spiral.speed(100)
    spiral.color("#00ff00")

    for i in range(400):
        spiral.forward(i * 5)
        spiral.right(242)

    turtle.done()

#-------------------------------------------------------------
def turtle_demo_2():
    import turtle

    ninja = turtle.Turtle()

    ninja.speed(10)

    for i in range(180):
        ninja.forward(100)
        ninja.right(30)
        ninja.forward(20)
        ninja.left(60)
        ninja.forward(50)
        ninja.right(30)

        ninja.penup()
        ninja.setposition(0, 0)
        ninja.pendown()

        ninja.right(2)

    turtle.done()

#-------------------------------------------------------------
if __name__ == "__main__":

    simple_window()
    #turtle_demo()
    #turtle_demo_2()
