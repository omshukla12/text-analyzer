''' Root of the application '''

import tkinter as tk
from tkinter import *
from tkinter import messagebox
from mydb import Database as db
from myapi import MyAPI as api


class NLPApp:

    def __init__(self):
        self.apio = api()
        self.root = tk.Tk()
        self.root.title('NLP App')
        self.root.geometry('350x550')
        self.root.configure(bg='white')
        self.root.iconbitmap('resources/favicon.ico')

        # Login page loads on startup ...
        self.login_gui()

        # Calling the event loop of Tk ...
        self.root.mainloop()

    def login_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP App', bg='white', fg='blue')
        heading.pack(pady=(30, 20))
        heading.configure(font=('Lucida Sans', 24, 'bold'))

        label1 = Label(self.root, text='Enter Email')
        label1.pack(pady=(50, 10))
        label1.configure(bg='white', font=('Arial', 9))

        self.email_input = Entry(self.root, width=30)
        self.email_input.pack(pady=(5, 10), ipady=3)

        label2 = Label(self.root, text='Enter Password')
        label2.pack(pady=(10, 10))
        label2.configure(bg='white', font=('Arial', 9))

        self.pwd_input = Entry(self.root, width=30, show='*')
        self.pwd_input.pack(pady=(5, 10), ipady=3)

        login_btn = Button(self.root, text='Log In', width=15,
                           height=2, command=self.login)
        login_btn.pack(pady=(20, 10))
        login_btn.configure(bg='blue', fg='white', font=('Arial', 10, 'bold'))

        label3 = Label(self.root, text='Not a member?')
        label3.pack(pady=(70, 10))
        label3.configure(bg='white', font=('Arial', 9))

        redirect_btn = Button(self.root, text='Register Now',
                              width=15, height=1, command=self.register_gui)
        redirect_btn.pack(pady=(0, 10))
        redirect_btn.configure(bg='green', fg='white',
                               font=('Arial', 9))

    def register_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP App', bg='white', fg='blue')
        heading.pack(pady=(30, 20))
        heading.configure(font=('Lucida Sans', 24, 'bold'))

        label0 = Label(self.root, text='Enter Name')
        label0.pack(pady=(10, 10))
        label0.configure(bg='white', font=('Arial', 9))

        self.name_input = Entry(self.root, width=30)
        self.name_input.pack(pady=(5, 10), ipady=3)

        label1 = Label(self.root, text='Enter Email')
        label1.pack(pady=(10, 10))
        label1.configure(bg='white', font=('Arial', 9))

        self.email_input = Entry(self.root, width=30)
        self.email_input.pack(pady=(5, 10), ipady=3)

        label2 = Label(self.root, text='Enter Password')
        label2.pack(pady=(10, 10))
        label2.configure(bg='white', font=('Arial', 9))

        self.pwd_input = Entry(self.root, width=30, show='*')
        self.pwd_input.pack(pady=(5, 10), ipady=3)

        register_btn = Button(self.root, text='Register',
                              width=15, height=2, command=self.registration)
        register_btn.pack(pady=(20, 10))
        register_btn.configure(bg='blue', fg='white',
                               font=('Arial', 10, 'bold'))

        label3 = Label(self.root, text='Already a member?')
        label3.pack(pady=(30, 10))
        label3.configure(bg='white', font=('Arial', 9))

        login_btn = Button(self.root, text='Log In',
                           width=15, height=1, command=self.login_gui)
        login_btn.pack(pady=(0, 10))
        login_btn.configure(bg='green', fg='white',
                            font=('Arial', 9))

    # Logic for L O G G I N G  I N ...

    def login(self):
        email = self.email_input.get()
        pwd = self.pwd_input.get()

        loggedin = db()
        response = loggedin.search(email=email, pwd=pwd)
        if response:
            self.home_gui()
        else:
            messagebox.showerror('Error', 'Incorrect email or password.')

    # Logic for R E G I S T R A T I O N ...

    def registration(self):
        name = self.name_input.get()
        email = self.email_input.get()
        pwd = self.pwd_input.get()

        register = db()
        response = register.add_data(name=name, email=email, pwd=pwd)
        if response[0] == 0:
            match response[1]:
                case True:
                    messagebox.showerror('Error', 'Email already exists.')
                case False:
                    messagebox.showerror('Error', 'Password already in use.')
        else:
            messagebox.showinfo('Sucess', 'Registration successful!')

    def home_gui(self):
        self.clear()

        btn_bg_col = '#4681f4'

        heading = Label(self.root, text='NLP App', bg='white', fg='blue')
        heading.pack(pady=(30, 30))
        heading.configure(font=('Lucida Sans', 24, 'bold'))

        label0 = Label(self.root, text='Choose an analysis option.')
        label0.pack(pady=(10, 10))
        label0.configure(bg='white', font=('Arial', 10))

        sentiment_btn = Button(self.root, text='Sentiment Analysis', width=25,
                               height=2, command=self.sentiment_gui)
        sentiment_btn.pack(pady=(20, 10))
        sentiment_btn.configure(bg=btn_bg_col, fg='white',
                                font=('Arial', 10, 'bold'))

        ner_btn = Button(self.root, text='Named Entity Recognition', width=25,
                         height=2, command=self.ner_gui)
        ner_btn.pack(pady=(20, 10))
        ner_btn.configure(bg=btn_bg_col, fg='white',
                          font=('Arial', 10, 'bold'))

        emotion_btn = Button(self.root, text='Emotion Prediction', width=25,
                             height=2, command=self.emo_gui)
        emotion_btn.pack(pady=(20, 10))
        emotion_btn.configure(bg=btn_bg_col, fg='white',
                              font=('Arial', 10, 'bold'))

        logout_btn = Button(self.root, text='Logout',
                            width=15, command=self.login_gui)
        logout_btn.pack(pady=(104, 10))
        logout_btn.configure(bg='red', fg='white', font=('Arial', 9, 'bold'))

    # A N A L Y S I S  O P T I O N S ...

    def sentiment_gui(self):
        self.clear()

        heading = Label(self.root, text='NLP App', bg='white', fg='blue')
        heading.pack(pady=(30, 30))
        heading.configure(font=('Lucida Sans', 24, 'bold'))

        heading2 = Label(self.root, text='Sentiment Analysis',
                         bg='white', fg='black')
        heading2.pack(pady=(0, 30))
        heading2.configure(font=('Lucida Sans', 16, 'bold'))

        label1 = Label(self.root, text='Enter the text for analysis.')
        label1.pack(pady=(10, 10), padx=(0, 130))
        label1.configure(bg='white', font=('Arial', 10))

        self.sentiment_input = Text(
            self.root, height=5, width=35, highlightthickness=1, wrap='word')
        self.sentiment_input.pack(pady=(0, 15), expand=False)

        sentiment_btn = Button(
            self.root, text='Analyze Sentiment', width=30, command=self.senti_analysis)
        sentiment_btn.pack(pady=(10, 0))
        sentiment_btn.configure(bg='blue', fg='white',
                                font=('Arial', 9, 'bold'))

        self.sentiment_result = Label(
            self.root, text='', fg='blue', bg='white')
        self.sentiment_result.pack(pady=(40, 13))
        self.sentiment_result.configure(
            font=('Arial', 11, 'bold'), height=4, justify='left', anchor='w')

        back_btn = Button(self.root, text='Go Back',
                          width=15, command=self.home_gui)
        back_btn.pack(pady=(0, 10))
        back_btn.configure(bg='lightblue', fg='black',
                           font=('Arial', 9, 'bold'))

    def senti_analysis(self):
        self.sentiment_result['text'] = ''

        text = self.sentiment_input.get('1.0', tk.END)
        req = self.apio.sentiment(text=text)

        res = ''
        for i in req['sentiment']:
            if i == 'negative':
                res += i.title() + '  :\t' + \
                    f"{round(req['sentiment'][i]*100,2)} %\n"
            else:
                res += i.title() + '\t  :\t' + \
                    f"{round(req['sentiment'][i]*100,2)} %\n"

        self.sentiment_result['text'] = res

    def ner_gui(self):
        self.clear()
        pass

    def emo_gui(self):
        self.clear()
        pass

    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()


# Creating the instance of the GUI class ...
nlp = NLPApp()
