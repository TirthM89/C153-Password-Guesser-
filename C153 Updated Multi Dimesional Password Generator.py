from tkinter import *
import random

root = Tk()
root.title("Multi Dimensional Array - Password Generator")
root.geometry("400x400")

label = Label(root)
array_3d = [[["1","2","3","4","5","6"],["Head","Tail"],["A","B","C","D","E","F","G","H"]]]
entry1 = Entry(root)
label1 = Label(root)
def new_password():
    label["text"] = ""
    random_1 = random.randint(0,5)
    random_2 = random.randint(0,1)
    random_3 = random.randint(0,7)
    
    letter1 = str(array_3d[0][0][random_1])
    letter2 = str(array_3d[0][1][random_2])
    letter3 = str(array_3d[0][2][random_3])
    label1["text"] = "Guess Password: "+ entry1.get()
    label["text"] = letter1+letter2+letter3
    
btn = Button(root, text  = "New Password", command = new_password)
btn.place(relx = 0.5, rely = 0.5, anchor = CENTER)
label.place(relx = 0.5, rely = 0.64, anchor = CENTER)
label1.place(relx = 0.5, rely = 0.24, anchor = CENTER)
entry1.place(relx = 0.5, rely = 0.4, anchor = CENTER)

root.mainloop()