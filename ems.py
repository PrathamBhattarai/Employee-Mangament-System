from customtkinter import *
from PIL import Image
from tkinter import ttk

app = CTk()

app.title('Employee Management system')
app.configure(fg_color='#161C30')
app. geometry('960x580')
#app.resizable(False,False)


#Loading and displaying the first image
logo = CTkImage(Image.open('first.jpeg'), size=(320,158))
logoLabel = CTkLabel(app,image=logo, text='')
logoLabel.grid(row=0,column=0, sticky='nsew')


#Loading and displaying second image
second= CTkImage(Image.open('second.png'), size =(320,158))
secondLabel = CTkLabel(app, image=second, text='')
secondLabel.grid(row =0, column=1, sticky='nsew')

#loading and displaying third imgae
third = CTkImage(Image.open('third.jpg'), size = (320,158))
thirdLabel = CTkLabel(app, image=third, text='')
thirdLabel.grid(row =0, column=2, sticky='nsew')


#configure the grid weights
app.grid_columnconfigure(0, weight=1)
app.grid_columnconfigure(1, weight=1)
app.grid_columnconfigure(2, weight=1)
app.grid_rowconfigure(0, weight=0)
app.grid_rowconfigure(1, weight = 1)


# Ensure there's no padding or margin around the images
logoLabel.grid_configure(padx=0, pady=0)
secondLabel.grid_configure(padx=0, pady=0)
thirdLabel.grid_configure(padx=0, pady=0)


#creating Data Frame
dataFrame = CTkFrame(app,fg_color='#161C30')
dataFrame.grid(row =1, column=0, columnspan = 3, padx=0, pady=0, sticky = 'nsew')

#Adjusting the weight of columns to distribute the space between left and right frame.
dataFrame.grid_columnconfigure(0, weight = 1) #left frame(less weight)
dataFrame.grid_columnconfigure(1, weight=2) #right frame(more weight)

#creating left and right frame inside the data frame
leftFrame = CTkFrame(dataFrame, fg_color='#161C30')
leftFrame.grid(row =0, column=0, padx=10, pady=1, sticky ='nsew')
dataFrame.grid_rowconfigure(0, weight=1) #ensures that dataframe takes the entire space where it is allocated

rightFrame = CTkFrame(dataFrame, fg_color='#161C30')
rightFrame.grid(row=0, column=1, padx=10, pady=1, sticky = 'nsew')


# Ensure both frames take up the height of the window
dataFrame.grid_rowconfigure(0, weight=1)




# Set row configurations to ensure left frame contents are displayed properly
leftFrame.grid_rowconfigure(0, weight=1) #ensures 1st row containing ID takes the entire row space without leaving spaces
leftFrame.grid_rowconfigure(1, weight=1)
leftFrame.grid_rowconfigure(2, weight=1)
leftFrame.grid_rowconfigure(3, weight=1)
leftFrame.grid_rowconfigure(4, weight=1)
leftFrame.grid_rowconfigure(5, weight=1)






#adding entry and combobox to the left frame

#------------------- ID Row-----------------------
id_label = CTkLabel(leftFrame, text= "ID:", font = ('arial', 18, 'bold'), text_color = 'white')
id_label.grid(row =0, column=0, sticky = 'w', padx=10)

id = CTkEntry(leftFrame, width = 180)
id.grid(row =0, column=1, padx=10, pady =10, sticky = 'ew')

#------------------ Name Row-------------------------
name_label = CTkLabel(leftFrame, text="Name:", font = ('arial', 18, 'bold'), text_color = 'white')
name_label.grid(row=1, column=0, sticky = 'w', padx=10)

name = CTkEntry(leftFrame, width = 180)
name.grid(row = 1, column=1, padx=10, pady =10, sticky = 'ew')

#------------------ Phone Row--------------------------

phone_label = CTkLabel(leftFrame, text="Phone:", font = ('arial', 18, 'bold'), text_color = 'white')
phone_label.grid(row=2, column=0, sticky = 'w', padx=10)

phone = CTkEntry(leftFrame, width = 180)
phone.grid(row = 2, column=1, padx=10, pady =10, sticky = 'ew')

#----------------- Role Row--------------------

role_label = CTkLabel(leftFrame, text= "Role:", font = ('arial', 18, 'bold'), text_color = 'white')
role_label.grid(row =3, column=0, sticky = 'w', padx=10)

role = CTkComboBox(leftFrame, values= ["Administrator", "Manager", "HR", "Team Lead", "Finance Officer", "IT Support"], width = 180, state='readonly')
role.grid(row =3, column=1, padx=10, pady =10, sticky = 'ew')

#-------------------------Gender Row-------------------
gender_label = CTkLabel(leftFrame, text="Gender:", font = ('arial', 18, 'bold'), text_color = 'white')
gender_label.grid(row =4, column=0, sticky = 'w', padx=10)

gender = CTkComboBox(leftFrame, values=["Male", "Female", "Others"], width = 180, state='readonly')
gender.grid(row=4, column=1, padx=10, pady =10, sticky = 'ew')

#---------------------------Salary Row-----------------------

salary_label = CTkLabel(leftFrame, text = "Salary:", font = ('arial', 18, 'bold'), text_color = 'white')
salary_label.grid(row =5, column=0, sticky = 'w', padx=10)

salary = CTkEntry(leftFrame, width=180)
salary.grid(row=5, column=1, padx=10, pady =10, sticky = 'ew')







#=================================================RIGHT FRAME================================================================================================================================
#configuring right frame
rightFrame.grid_columnconfigure(0, weight=1)
rightFrame.grid_columnconfigure(1, weight=1)
rightFrame.grid_columnconfigure(2, weight=1)
rightFrame.grid_columnconfigure(3, weight=1)

#-------------------------------------------------------------------

#Adding button in right data frame

search_options = ['Id', 'Name', 'Phone', 'Role', 'Gender', 'Salary']
searchbox = CTkComboBox(rightFrame, values= search_options, state = 'readonly')
searchbox.grid(row=0, column=0, padx = 1, pady=1)
searchbox.set('Search By')


searchEntry = CTkEntry(rightFrame)
searchEntry.grid(row = 0, column=1, padx = 1, pady=1)

#=========buttons===============================================
searchButton = CTkButton(rightFrame, text= 'Search', width=100)
searchButton.grid(row=0, column=2, padx=1)

showallButton = CTkButton(rightFrame, text = 'Show All', width=100)
showallButton.grid(row=0, column=3, padx=1)




tree = ttk.Treeview(rightFrame)
tree.grid(row=1, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')

#for making the tree view fill the right frame
rightFrame.grid_rowconfigure(0, weight=1)




app.mainloop()