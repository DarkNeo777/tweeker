from tkinter import *
import twt

people = {
    'joe rogan':'joerogan',
    'elon musk': 'elonmusk',
    'andrew scultz': 'andrewscultz',
}
    
test = 'readthis'
root = Tk()#creates the instance objects, root is the windows
root.geometry("600x600") 
frame = Frame(root, bd=4, bg="purple")#adds frame to instance, frame is a border
frame.pack()# pack i think finalilzes the object into the frame
 

rightframe = Frame(root)
rightframe.pack(side=RIGHT)

radio_value=0
class Window:
    def __init__(self, master):
        def retrieve():
            print(var2.get())
        label_frame = LabelFrame(master, text = "People:")
        label_frame.pack(padx = 5, pady = 5)

        var2 = IntVar()
 
        radio1 = Radiobutton(label_frame, text = people['joe rogan'],
                                variable = var2, value = 1,command=retrieve)
        radio1.pack(padx = 5, pady = 5)
 
        radio2 = Radiobutton(label_frame, text = people['elon musk'],
                                variable = var2, value = 2,command=retrieve)
        radio2.pack(padx = 5, pady = 5)
 
        radio3 = Radiobutton(label_frame, text = people['andrew scultz'],
                                variable = var2, value = 3,command=retrieve)
        radio3.pack(padx = 5, pady = 5)
       

def set():
    var.set("Goood by cruelworld")
def retrieve():
    if(user_name.get() != 'username'):
        twt.user_entered(user_name.get())
        window2 = Toplevel()
        window2.geometry('400x400')
        newlabel = Label(window2, text = "Info about person")
        newlabel.pack()
        info_laber =Label(window2,text=user_name.get())
        info_laber.pack()
    else: print("enter real")
 

var = StringVar()
var.set("Twitter users profiles")

image = PhotoImage(file="twt-bird.png")  
canvas = Canvas(width = 200, height = 200, bg='white')
canvas.create_image(100, 100, image = image)
canvas.pack(padx=10,pady=10)

label = Label(frame, textvariable=var)#not the variable frame is based not the root
label.pack()

leftframe = Frame(root)#creates another fram with instance
leftframe.pack(padx=10,pady=10)#finalizes the frame on the left side

label_user = Label(leftframe,text='Enter a user twitter \n handle:',bg='white',fg='blue')
label_user.pack()

user_name = Entry(leftframe,width=20,justify=CENTER)
user_name.insert(0,'username')
user_name.pack(padx = 5, pady=5)

Button = Button(leftframe,text="Submit",command=retrieve)
Button.pack(padx=5,pady=5)
 
window = Window(leftframe)

root.title("Twt Info")
root.mainloop()