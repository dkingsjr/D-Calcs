from tkinter import*

app_width = 500
app_height = 500

screen_width = splash_root.winfo_screenwidth()
screen_height = splash_root.winfo_screenheight()

x = (screen_width / 2) - (app_width / 2)
y = (screen_height / 2) - (app_height / 2)



splash_root = Tk()
splash_root.title("Splash Screen!")
splash_root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')
#hide title bar
splash_root.overrideredirect(True)
splash_label = Label(splash_root, text="splash screen!", font=("helvetica", 18))
splash_label.pack(pady=20)



def main_window():
    splash_root.destroy()
    root = Tk()
    root.title('Codemy.com - Tab Order')
    root.iconbitmap('c:/gui/codemy.ico')
    root.geometry=(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    main_label = Label(root, text="main screen", font=("helvetica", 18))
    main_label.pack(pady=20)



    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()

    x = (screen_width / 2) - (app_width / 2)
    y = (screen_height / 2) - (app_height / 2)

    root.geometry(f'{app_width}x{app_height}+{int(x)}+{int(y)}')

    my_label = Label(root, text=f'Width:{screen_width} Height:{screen_height}')
    my_label.pack(pady=20)


#splash screen timer
splash_root.after(3000, main_window)
app_width = 500
app_height = 500

mainloop()

#designate height and width of our app



