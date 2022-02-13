from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import Image, ImageTk
import pymysql


class Register:
    def __init__(self, root):
        # initlaizing root title and geometry
        self.root = root
        self.root.title("Registration window")
        self.root.geometry("1350x700+0+0")  # x axis = 0  and y axis = 0

        # ----background image
        # --Alternate--------------------
        # self.bg = Image.open("C:\\python\\registration_form\\images\\background.jpg")
        # bg = ImageTk.PhotoImage(self.bg)
        # label = Label(root, image = bg)
        # label.place(x=0,y=0)
        self.bg = ImageTk.PhotoImage(file="E:\\python codes\\REGISTRATION_USING_TKINTER\\background.jpg")
        bg = Label(self.root, image=self.bg).place(
            x=0, y=0, relwidth=1, relheight=1)

        # --Registration Frame--
        frame1 = Frame(self.root, bg="white")
        frame1.place(x=400, y=100, width=500, height=500)

        title = Label(frame1, text="REGISTER HERE", font=(
            "times new roman bold", 20), bg="white", fg="Green").place(x=130, y=30)

        # ------Row 1------
        # self.var_fname = StringVar()  first way to get property of variable using textvariable and StringVar()
        # f_name = Label(frame1,text="First Name",font=("times new roman",15),bg="white",fg="black").place(x=40,y=100)
        # txt_fname = Entry(frame1, font =("times new roman",15),bg="#EBECF0",textvariable=self.var_fname).place(x=40,y=130,width=170)

        f_name = Label(frame1, text="First Name", font=(
            "times new roman", 15), bg="white", fg="black").place(x=40, y=100)
        self.txt_fname = Entry(frame1, font=(
            "times new roman", 15), bg="#EBECF0")
        self.txt_fname.place(x=40, y=130, width=170)

        l_name = Label(frame1, text="Last Name", font=(
            "times new roman", 15), bg="white", fg="black").place(x=260, y=100)
        self.txt_lname = Entry(frame1, font=(
            "times new roman", 15), bg="#EBECF0")
        self.txt_lname.place(x=260, y=130, width=170)

        # -----Row 2-------
        contact_no = Label(frame1, text="Contact no", font=(
            "times new roman", 15), bg="white", fg="black").place(x=40, y=180)
        self.txt_cno = Entry(frame1, font=(
            "times new roman", 15), bg="#EBECF0")
        self.txt_cno.place(x=40, y=210, width=170)

        email = Label(frame1, text="Email", font=(
            "times new roman", 15), bg="white", fg="black").place(x=260, y=180)
        self.txt_email = Entry(frame1, font=(
            "times new roman", 15), bg="#EBECF0")
        self.txt_email.place(x=260, y=210, width=170)

        # ------Row 3--------
        security = Label(frame1, text="Security Question", font=(
            "times new roman", 15), bg="white", fg="black").place(x=40, y=260)

        self.cmb_quest = ttk.Combobox(frame1, font=(
            "times new roman", 13), state='readonly', justify=LEFT)
        self.cmb_quest['values'] = (
            'select', 'First name', "Best friend", 'Birth place', 'School')
        self.cmb_quest.place(x=40, y=290, width=170)
        self.cmb_quest.current(0)

        Answer = Label(frame1, text="Answer", font=(
            "times new roman", 15), bg="white", fg="black").place(x=260, y=260)
        self.txt_ans = Entry(frame1, font=(
            "times new roman", 15), bg="#EBECF0")
        self.txt_ans.place(x=260, y=290, width=170)

        # ------Row4-----------
        password = Label(frame1, text="Password", font=(
            "times new roman", 15), bg="white", fg="black").place(x=40, y=340)
        self.txt_pass = Entry(frame1, font=(
            "times new roman", 15), bg="#EBECF0")
        self.txt_pass.place(x=40, y=370, width=170)

        c_password = Label(frame1, text="Confirm Password", font=(
            "times new roman", 15), bg="white", fg="black").place(x=260, y=340)
        self.txt_cpass = Entry(frame1, font=(
            "times new roman", 15), bg="#EBECF0")
        self.txt_cpass.place(x=260, y=370, width=170)

        # -----Terms and conditions---------
        self.var_chk = IntVar()
        check = Checkbutton(frame1, text="I Agree The Terms And Conditions",
                            variable=self.var_chk, onvalue=1, offvalue=0, bg="white").place(x=35, y=410)
        btn = Button(frame1, text="Register", font=("times new roman bold", 15),
                     command=self.register_data, bg="green", fg="white").place(x=100, y=450)
        btn_login = Button(frame1, text="Log In", font=(
            "times new roman bold", 15), bg="dark red", fg="white").place(x=270, y=450)

    def register_data(self):
        if self.txt_fname.get() == "" or self.txt_lname.get() == "" or self.txt_cno.get() == "" or self.txt_email.get() == "" or self.txt_pass.get() == "" or self.txt_cpass.get() == "" or self.txt_ans.get() == "" or self.cmb_quest.get() == "select":
            messagebox.showerror(
                "Error", "All Fields Are Required ", parent=self.root)

        elif self.txt_pass.get() != self.txt_cpass.get():
            messagebox.showerror(
                "Error", "Password and confirm password does not match", parent=self.root)
        elif self.var_chk.get() == 0:
            messagebox.showerror(
                "Error", "Please Agree Our Terms & Conditions", parent=self.root)

        else:
            try:
                con = pymysql.connect(host="localhost", user="root", password="", database="register details")
                cus = con.cursor() 
                cus.execute("select * from people where email=%s",self.txt_email.get())
                row = cus.fetchone()
                # if the record found it will give you the whole row as a output
                if row!=None:
                    messagebox.showinfo("Success","user already exist!",parent=self.root)


                # A cursor is an object which helps to execute the query and fetch the records from the database.

                cus.execute("insert into people (f_name,l_name,contact,email,question,answer,password) values(%s,%s,%s,%s,%s,%s,%s)",
                            (self.txt_fname.get(),
                             self.txt_lname.get(),
                             self.txt_cno.get(),
                             self.txt_email.get(),
                             self.cmb_quest.get(),
                             self.txt_ans.get(),
                             self.txt_pass.get()
                             ))
                con.commit()  #used to commit or insert changes 
                con.close()
                messagebox.showinfo("Success","Register Successfully",parent=self.root)

            except Exception as es:
                messagebox.showerror("Error", f"Error due to: {str(es)}", parent=self.root)



root = Tk()
obj = Register(root)
root.mainloop()


# references
# image tk is used to deal with jpg files that
