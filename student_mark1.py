from tkinter import *
t=Tk()
t.title("Student Marksheet")
t.geometry("500x600")
class Student():
    def show(self,master):
        self.intro=Label(master,text="Student Marksheet Details",font="arial 15 bold",fg="red",bg="Blue")
        self.intro.pack()
        self.rlno=Label(master,text="Enter Roll No:",font="arial 15 bold",fg="Red")
        self.rlno.place(x=0,y=60)
        self.e1=Entry(master,font="arial 15 bold")
        self.e1.place(x=210,y=65)
        self.name=Label(master,text="Enter Student Name:",font="arial 15 bold",fg="Green")
        self.name.place(x=0,y=100)
        self.e2=Entry(master,font="arial 15 bold")
        self.e2.place(x=210,y=105)

        self.m1=Label(master,text="Enter Marks 1:",font="arial 15 bold",fg="blue")
        self.m1.place(x=0,y=160)
        self.e3=Entry(master,font="arial 15 bold")
        self.e3.place(x=210,y=165)

        self.m2=Label(master,text="Enter Marks 2:",font="arial 15 bold",fg="blue")
        self.m2.place(x=0,y=200)
        self.e4=Entry(master,font="arial 15 bold")
        self.e4.place(x=210,y=205)

        self.m3=Label(master,text="Enter Marks 3:",font="arial 15 bold",fg="blue")
        self.m3.place(x=0,y=240)
        self.e5=Entry(master,font='arial 15 bold')
        self.e5.place(x=210,y=245)

        self.btn1=Button(master,text="View Result:",font="arial 12 bold",command=self.det)
        self.btn1.place(x=210,y=280)

        self.tMarks=Label(master,text="Total Marks:",font="arial 15 bold",fg="red")
        self.tMarks.place(x=0,y=350)
        self.e6=Entry(master,font="arial 15 bold")
        self.e6.place(x=210,y=355)
        self.per=Label(master,text="Percentage:",font="arial 15 bold ",fg="blue")
        self.per.place(x=0,y=400)
        self.e7=Entry(master,font="arial 15 bold")
        self.e7.place(x=210,y=405)

        self.res=Label(master,text="Result:",font="arial 15 bold",fg="Green")
        self.res.place(x=0,y=450)
        self.e8=Entry(master,font="arial 15 bold")
        self.e8.place(x=210,y=455)
        self.grade=Label(master,text="Grade:",font='arial 15 bold')
        self.grade.place(x=0,y=500)
        self.e9=Entry(master,font="arial 15 bold")
        self.e9.place(x=210,y=505)
    
    def det(self):
        self.e6.delete(0,'end')
        self.e7.delete(0,'end')
        self.e8.delete(0,'end')
        self.e9.delete(0,'end')
        self.mark1=int(self.e3.get())
        self.mark2=int(self.e4.get())
        self.mark3=int(self.e5.get())

        self.total=self.mark1+self.mark2+self.mark3
        self.percent=self.total//3.0
        self.e6.insert(END,str(self.total))
        self.e7.insert(END,str(self.percent))

        if self.mark1>=35 and self.mark2>=35 and self.mark3>=35:
            self.e8.insert(END,str("Pass"))
        else:
            self.e8.insert(END,str("Fail"))

        if self.percent>=90:
            self.e9.insert(END,str("A+"))
        if self.percent>=80 and self.percent<90:
            self.e9.insert(END,str("A"))
        if self.percent>=70 and self.percent<80:
            self.e9.insert(END,str("B"))
        if self.percent>=60 and self.percent<70:
            self.e9.insert(END,str("C"))
        if self.percent>=35 and self.percent<60:
            self.e9.insert(END,str("D"))
        else:
            self.e9.insert(END,str(""))

        

obj=Student()
obj.show(t)
t.mainloop()