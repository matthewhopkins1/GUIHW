import tkinter as t
import tkinter.messagebox

class myGUI:
    def __init__(self):
        self.main_window = t.Tk()

        self.main_window.geometry('500x300')
        self.main_window.title('Responsive Registration Form')

        self.top_frame = t.Frame(self.main_window)
        self.bottom_frame = t.Frame(self.main_window)
        

        self.top_frame.pack(side = 'top')
        self.bottom_frame.pack(side = 'bottom')

        self.fname_label = t.Label(self.top_frame, text = 'First Name')
        self.lname_label = t.Label(self.top_frame, text = 'Last Name')
        self.email_label = t.Label(self.top_frame, text = 'Email')
        self.pass_label = t.Label(self.top_frame, text = 'Password')
        self.pass2_label = t.Label(self.top_frame, text = 'Re-type Password')
        
        self.fname_entry = t.Entry(self.top_frame)
        self.lname_entry = t.Entry(self.top_frame)
        self.email_entry = t.Entry(self.top_frame)
        self.pass_entry = t.Entry(self.top_frame, show = '*')
        self.pass2_entry = t.Entry(self.top_frame, show = '*')
        

        self.fname_label.pack(side = 'left')
        self.fname_entry.pack(side = 'left')
        self.lname_label.pack(side = 'left')
        self.lname_entry.pack(side = 'left')
        self.email_label.pack(side = 'left')
        self.email_entry.pack(side = 'left')
        self.pass_label.pack(side = 'left')
        self.pass_entry.pack(side = 'left')
        self.pass2_label.pack(side = 'left')
        self.pass2_entry.pack(side = 'left')
        


        self.radio_var = t.IntVar()

        self.gender_rb1 = t.Radiobutton(self.top_frame, text = 'Male', variable = self.radio_var, value = 'Male')
        self.gender_rb2 = t.Radiobutton(self.top_frame, text = 'Female', variable = self.radio_var, value = 'Female')

        self.gender_rb1.pack(side = 'left')
        self.gender_rb2.pack(side = 'left')

        self.cb_var1 = t.IntVar()
        self.cb_var2 = t.IntVar()

        self.terms_cb = t.Checkbutton(self.bottom_frame, text = 'I agree with terms and conditions', variable = self.cb_var1)
        self.news_cb = t.Checkbutton(self.bottom_frame, text = 'I want to receive the newsletter', variable = self.cb_var2)

        self.terms_cb.pack()
        self.news_cb.pack()

        self.register_button = t.Button(self.bottom_frame, text = 'Register', command = self.show_choice, bg = 'green')

        self.register_button.pack()

        t.mainloop()
        
    def show_choice(self):
        if not self.radio_var.get():
            t.messagebox.showinfo('Error', 'Select a gender.')

        if not self.cb_var1.get() or self.cb_var2.get():
            t.messagebox.showinfo('Error', 'Check both boxes.')
            
        if self.pass_entry != self.pass2_entry:
            t.messagebox.showinfo('Error', 'Passwords do not match.')

        else:
            t.messagebox.showinfo('Registered', 'Success!')


myinstance = myGUI()

