from tkinter import *

main_window = Tk()
main_window.title('Mocking Bird')
main_window.geometry("400x400+10+20")

Label(main_window, text= "To continue press a button...", font=("Arial Bold", 18), fg="white", bg="#34A2FE").pack()
Label(main_window, text= "1. Petrol", font=("Arial Bold", 12)).pack()
Label(main_window, text= "2. Kerosene", font=("Arial Bold", 12)).pack()
Label(main_window, text= "3. Diesel", font=("Arial Bold", 12)).pack()
Label(main_window, text= "4. LPG", font=("Arial Bold", 12)).pack()

main_window.mainloop()
