from tkinter import *

def submit():
    value = scale.get()
    label.config(text=f"The Temperature is: {value} degrees Celsius")

window = Tk()
window.title("Temperature scaling App")
window.geometry("300x200")
window.configure(bg="lightblue")
window.minsize(500, 500)
window.maxsize(800, 700)

image = PhotoImage(file="funky-monkey-with-gold-watch-cartoon_43623-1535.png")
window.iconphoto(True, image)

scale = Scale(window, 
              from_=0, to=100,
              orient=VERTICAL,
              length=400,
              font=("Arial", 10),
              bg="lightgreen",
              troughcolor="blue",
              tickinterval=10
              )
scale.pack()

label = Label(window, text="Slide to check the temperature",
              font=("Arial", 20, "bold"),
              bg="lightblue",
              fg="black",
              wraplength=300,
              justify=LEFT,
              )
label.pack()

button = Button(window, text="Submit", command=submit)
button.pack()

window.mainloop()
