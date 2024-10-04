from customtkinter import *
from PIL import Image
from tkinter import messagebox    

def login():
    if userEntry.get() == '' or passwordEntry.get() == '':
        messagebox.showerror('Error', 'All fields are required')
    
    elif userEntry.get()=='Pratham' and passwordEntry.get() == '1234':
        messagebox.showinfo('Successful', "You are logged In")
        root.destroy()
        import ems
    
    else:
        messagebox.showerror('Error', "input contains wrong credentials") 


root = CTk()
root.geometry("800x400")
root.resizable(0,0)
root.title("Login Page")

#putting image in the window using CTkImage with pillow library
image = CTkImage(Image.open('login image.png'), size=(492,395))
imageLabel = CTkLabel(root, image=image, text='')
imageLabel.place(x=350,y=0)


#Creating heading frame
headingFrame = CTkFrame(root, width=350, height =60, corner_radius=5, fg_color='#E75480')
headingFrame.place(x= 0, y= 5)

#creating lable(or title) inside the heading frame
headingLabel = CTkLabel(headingFrame, text="Employee Mangament System", bg_color='#E75480', font=('Goudy Old Style', 26, 'bold'))
headingLabel.place(relx=0.06, rely= 0.25)

#creating loginframe where username and password entry box is place
contentFrame = CTkFrame(root, width= 350, height = 340, corner_radius= 5, fg_color='#ADD8E6')
contentFrame.place(x =0, y = 65)

#creating Username label and Password Lable
userLabel = CTkLabel(contentFrame, text="UserName: ", font=('Ariel',14, 'bold' ) )
userLabel.place(x=5, y = 70)

passwordLabel = CTkLabel(contentFrame, text="Password: ", font=('Ariel',14, 'bold' ) )
passwordLabel.place(x=5, y = 140)


#creating user and password entry boxes
userEntry = CTkEntry(contentFrame, width = 250, height = 60, placeholder_text="Enter your username")
userEntry.place(x = 90, y = 60)

passwordEntry = CTkEntry(contentFrame, width = 250, height = 60, placeholder_text="Enter your Password", show = '*')
passwordEntry.place(x = 90, y = 130)


#creating Login button
loginbutn = CTkButton(contentFrame, text='LOGIN', width = 50, height = 20, font=('Ariel', 15, 'bold'), cursor = 'hand2', command = login)
loginbutn.place(x =100, y = 200)

root.mainloop()