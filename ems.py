from customtkinter import *
from PIL import Image
from tkinter import ttk

app = CTk()

app.title('Employee Management systen')
app.configure(fg_color='#161C30')
app. geometry('900x900')
app.resizable(False,False)


#Loading and displaying the first image
logo = CTkImage(Image.open('first.jpeg'), size=(330,158))
logoLable = CTkLabel(app,image=logo, text='')
logoLable.grid(row=0,column=0)


#Loading and displaying second image
second= CTkImage(Image.open('second.png'), size =(270,158))
secondLable = CTkLabel(app, image=second, text='')
secondLable.grid(row =0, column=1)

#loading and displaying third imgae
third = CTkImage(Image.open('third.jpg'), size = (300,158))
thirdLable = CTkLabel(app, image=third, text='')
thirdLable.grid(row =0, column=2)


#creating Data Frame
dataFrame = CTkFrame(app)
dataFrame.grid(row =1, column=0, columnspan = 2)

#creating left and right frame inside the data frame
leftFrame = CTkFrame(dataFrame, fg_color='#161C30')
leftFrame.grid(row =0, column=0)

rightFrame = CTkFrame(dataFrame, fg_color='#161C30')
rightFrame.grid(row=0, column=1)

#adding entry and combobox to the left frame

#------------------- ID Row-----------------------
id_label = CTkLabel(leftFrame, text= "ID:", font = ('arial', 18, 'bold'), text_color = 'white')
id_label.grid(row =0, column=0, sticky = 'w')

id = CTkEntry(leftFrame, width = 180)
id.grid(row =0, column=1, padx=10, pady =10, sticky = 'ew')

#------------------ Name Row-------------------------
name_label = CTkLabel(leftFrame, text="Name:", font = ('arial', 18, 'bold'), text_color = 'white')
name_label.grid(row=1, column=0, sticky = 'w')

name = CTkEntry(leftFrame, width = 180)
name.grid(row = 1, column=1, padx=10, pady =10, sticky = 'ew')

#------------------ Phone Row--------------------------

phone_label = CTkLabel(leftFrame, text="Phone:", font = ('arial', 18, 'bold'), text_color = 'white')
phone_label.grid(row=2, column=0, sticky = 'w')

phone = CTkEntry(leftFrame, width = 180)
phone.grid(row = 2, column=1, padx=10, pady =10, sticky = 'ew')

#----------------- Role Row--------------------

role_label = CTkLabel(leftFrame, text= "Role:", font = ('arial', 18, 'bold'), text_color = 'white')
role_label.grid(row =3, column=0, sticky = 'w')

role = CTkComboBox(leftFrame, values= ["Administrator", "Manager", "HR", "Team Lead", "Finance Officer", "IT Support"], width = 180, state='readonly')
role.grid(row =3, column=1, padx=10, pady =10, sticky = 'ew')

#-------------------------Gender Row-------------------
gender_label = CTkLabel(leftFrame, text="Gender:", font = ('arial', 18, 'bold'), text_color = 'white')
gender_label.grid(row =4, column=0, sticky = 'w')

gender = CTkComboBox(leftFrame, values=["Male", "Female", "Others"], width = 180, state='readonly')
gender.grid(row=4, column=1, padx=10, pady =10, sticky = 'ew')

#---------------------------Salary Row-----------------------

salary_label = CTkLabel(leftFrame, text = "Salary:", font = ('arial', 18, 'bold'), text_color = 'white')
salary_label.grid(row =5, column=0, sticky = 'w')

salary = CTkEntry(leftFrame, width=180)
salary.grid(row=5, column=1, padx=10, pady =10, sticky = 'ew')

#-------------------------------------------------------------------

#Adding button in right data frame

search_options = ['Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary']
searchbox = CTkComboBox(rightFrame, values= search_options, state = 'readonly')
searchbox.grid(row=0, column=0, padx = 10, pady=10)
searchbox.set('Search By')


searchEntry = CTkEntry(rightFrame)
searchEntry.grid(row = 0, column=1, padx = 10, pady=10)

#=========buttons===============================================
searchButton = CTkButton(rightFrame, text= 'Search', width=100)
searchButton.grid(row=0, column=2)

showallButton = CTkButton(rightFrame, text = 'Show All', width=100)
showallButton.grid(row=0, column=3)

tree = ttk.Treeview(rightFrame)
tree.grid(row=1, column=0)



app.mainloop()