from tkinter import *
 
root = Tk()
root.title('New Project 1.0')
#root.iconbitmap('insert path')
root.geometry("500x300")
root.configure(bg='#384048')
#Removes frame from the window. Commented out for now due to development.
#root.overrideredirect(True)
 
#window dimensions(auto size)
#RWidth=root.winfo_screenwidth()
#RHeight=root.winfo_screenheight()
#root.geometry(("%dx%d")%(RWidth,RHeight))
 
#img = ImageTK.PhotoImage(image.open(path))
#panel = tk.Label(mainframe, image = img)
#panel.pack(side = "bottom", fill = "both", expand = "yes")
 
 
#Frame containing the app within the window.
mainframe = LabelFrame(root, bg='#384048', padx=15, pady=15, relief=SUNKEN)
mainframe.pack(fill="both", expand=True, padx=15, pady=15)
mainframe.columnconfigure(0, weight=2)
mainframe.columnconfigure(1, weight=2)
mainframe.columnconfigure(2, weight=2)
 
 
#Current o2% after air fill
def o2():
     fo2=int(Fo2_entry.get())
     ctp=int(Ctp_entry.get())
     dp=int(Dp_entry.get())
     
     r1= float(dp) - float(ctp)
     r2= float(r1) * 0.21
     r3= (float(fo2) / 100)
     r4=((float(ctp) * float(r3)) + (float(r2))) / float(dp)
     result = (float(r4) * 100)
     out_put.insert(0, f"{result:.0f}")
    
def clear():
    Fo2_entry.delete(0, END)
    Ctp_entry.delete(0, END)
    Dp_entry.delete(0, END)
    out_put.delete(0, END)
    
 
""" 
Fo2 = input("Enter Current o2:")
Ctp = input("Enter Current Tank Pressure:")
Dp = input("Enter Desired Tank Pressure:")
r1= float(Dp) - float(Ctp)
r2= float(r1) * 0.21
r3=(float(Fo2) / 100)
r4=((float(Ctp) * float(r3)) + (float(r2))) / float(Dp)
result = (float(r4) * 100)
print("New o2 Percentage:", f"{result:.0f}")
exit()
#original formula
#(500*0.36 + 2500*0.21)/3000 = 0.235 (23.5% O2)
"""
 
 
#labels
lbl1 = Label(mainframe, text="New o2% After Air Fill", bg='#384048', fg="white")
lbl1.grid(row=0, pady=100, columnspan=3)
 
lbl2 = Label(mainframe, text="Current o2 %", bg='#384048', fg="white")
lbl2.grid(row=1, pady=15, columnspan=3)
 
lbl3 = Label(mainframe, text="Current Tank Pressure", bg='#384048', fg="white")
lbl3.grid(row=3, pady=15, columnspan=3)
 
lbl4 = Label(mainframe, text="Desired Pressure", bg='#384048', fg="white")
lbl4.grid(row=5, pady=15, columnspan=3)
 
lbl5 = Label(mainframe, text="New o2 %", bg='#384048', fg="white")
lbl5.grid(row=7, pady=15, columnspan=3)
 
Fo2 = StringVar()
Ctp = StringVar()
Dp = StringVar()
 
Fo2_entry = Entry(mainframe, textvariable=Fo2)
Fo2_entry.grid(row=2, pady=15, columnspan=3) 
 
Ctp_entry = Entry(mainframe, textvariable=Ctp)
Ctp_entry.grid(row=4, pady=15, columnspan=3)
 
Dp_entry = Entry(mainframe, textvariable=Dp)
Dp_entry.grid(row=6, pady=15, columnspan=3)
 
out_put = Entry(mainframe)
out_put.grid(row=8, pady=15, columnspan=3)
 
calc = Button(mainframe, text="Calculate", command=o2)
calc.grid(row=9, pady=15, columnspan=3)
 
clear = Button(mainframe, text="Reset", bg="red", fg="white", command=clear)
clear.grid(row=10, pady=15, columnspan=3)
 
 
 
root.mainloop()
