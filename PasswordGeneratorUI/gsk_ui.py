# from generate_safe_pass import generate_password
# <-- START generate_safe_pass -->
import random
import string

ran = random.SystemRandom()
words = open('words.txt').read().splitlines()
chars = list(string.printable[:-17])

def generate_password(word_amount, char_amount, all_start_uppercase, random_start_uppercase):
    password = ""
    amount = word_amount if int(word_amount) > 0 else char_amount

    for i in [""] * int(amount):
        wc_list = words if int(word_amount) > 0 else chars

        element = ran.choice(wc_list)

        if int(word_amount) > 0:
            if all_start_uppercase:
                element = element.title()
            elif random_start_uppercase:
                if ran.choice([1, 0]):
                    element = element.title()

        password += element
    
    return password

# <-- END generate_safe_pass -->

# <-- START ui -->

import Tkinter

top = Tkinter.Tk()
top.title("Random Password generator")

L1 = Tkinter.Label(text="Lenght (int)")
L1.pack()

E1 = Tkinter.Entry(top)
E1.pack()

Lb1 = Tkinter.Listbox(top, height = 2)
Lb1.insert(1, "Words")
Lb1.insert(2, "Chars")
Lb1.pack()

CheckVar1 = Tkinter.IntVar()
CheckVar2 = Tkinter.IntVar()
C1 = Tkinter.Checkbutton(top, text = "Random uppercasing", variable = CheckVar1, onvalue = 1, offvalue = 0, height=5, width = 20)
C2 = Tkinter.Checkbutton(top, text = "All uppercase", variable = CheckVar2, onvalue = 1, offvalue = 0, height=5, width = 20)
C1.pack()
C2.pack()

def generate():
   amount = E1.get()
   type_of_pass = Lb1.get(Tkinter.ACTIVE)
   random_start_upper = CheckVar1.get()
   all_start_upper = CheckVar2.get()

   if type_of_pass == "Words":
       word_amount = int(amount)
       char_amount = 0
   else:
       word_amount = 0
       char_amount = int(amount)
   
   print(amount, type_of_pass)
   global text
   text = Tkinter.Text(top, width = 20, height = 5)
   text.insert(Tkinter.INSERT, generate_password(word_amount, char_amount, all_start_upper, random_start_upper))
   text.pack()

B = Tkinter.Button(top, text ="Generate", command = generate)
B.pack()

# <-- END ui -->


# start program
top.mainloop()
