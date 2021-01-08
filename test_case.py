#  ------------------------------------------------- ###
#  ------------------------------------------------- ###
#  ### Developed by TANMAY KHANDELWAL (aka Dude901). ###
#  _________________________________________________ ###
#  _________________________________________________ ###

from tkinter import *
from random import randint, choices
import webbrowser

mycolor = '#262626'
gui = Tk()
gui.title('TEST CASE GENERATOR')
gui.configure(bg=mycolor)  # , image = home_back)


class Case:

    def __init__(self, master):
        gen_frame = Frame(master)
        gen_frame.grid()
        self.test_case_counter = None

    def home(self):
        self.test_case_counter = Label(gui, text='T: ', font=('calibre', 10, 'bold'))
        self.button1 = Button(gui, justify=LEFT, text='T\nn   \nA1 A2 A3...An\nn   \nA1 A2 A3...An',
                              fg='white', command=lambda: Type1(gui))  # , height=1, width=7)
        self.button1.grid(row=0, column=0, ipady=10, pady=10, padx=10)
        self.button1.configure(background='grey20')
        self.button2 = Button(gui, justify=LEFT, text='T\nn  m  \nA1 A2 A3...An\nn  m\nA1 A2 A3...An', fg='white'
                         , command=lambda: Type2(gui), width=10)
        self.button2.grid(row=0, column=1, ipady=10, pady=10, padx=10)
        self.button2.configure(background='grey20')
        self.button3 = Button(gui, justify=LEFT, text='T\nA1  B1\nA2  B2\n(t rows of)\n(A, B pair)', fg='white'
                         , command=lambda: Type3(gui), width=10)
        self.button3.grid(row=0, column=2, ipady=10, pady=10, padx=10)
        self.button3.configure(background='grey20')
        self.button4 = Button(gui, justify=LEFT, text='T\nn  m  \nA1 A2...An\nB1 B2...Bm\n...  ...', fg='white'
                              , command=lambda: Type4(gui), width=10)  # , height=1, width=7)
        self.button4.grid(row=0, column=3, ipady=10, pady=10, padx=10)
        self.button4.configure(background='grey20')
        self.button5 = Button(gui, justify=LEFT, text='T\nn  m  k\nn  m  k\n(t rows of)\n(n m k  pair)', fg='white'
                              , command=lambda: Type5(gui), width=10)  # , height=1, width=7)
        self.button5.grid(row=0, column=4, ipady=10, pady=10, padx=10)
        self.button5.configure(background='grey20')
        self.button6 = Button(gui, justify=LEFT, text='n * m (matrix)\nA1  A2...Am\nA1  A2...Am\n__   __ ... __\n'
                              'A1  A2...Am', fg='white', command=lambda: Type6(gui), width=11)
        self.button6.grid(row=1, column=0, ipady=10, pady=10, padx=10)
        self.button6.configure(background='grey20')
        self.button7 = Button(gui, justify=LEFT, text='T\nn\nCustom string\n(ex: 0 1)\n(ex: + / -)'
                              , fg='white', command=lambda: Type7(gui), width=11)
        self.button7.grid(row=1, column=1, ipady=10, pady=10, padx=10)
        self.button7.configure(background='grey20')
        self.button8 = Button(gui, justify=LEFT, text='T\nn  m\nA1  B1\n...   ...\nAm  Bm'
                              , fg='white', command=lambda: Type7(gui), width=11)
        self.button8.grid(row=1, column=2, ipady=10, pady=10, padx=10)
        self.button8.configure(background='grey20')
        self.button9 = Button(gui, justify=LEFT, text='T\nCustom string\n(without "n")\n(ex: 0 1)\n(ex: + / -)'
                              , fg='white', command=lambda: Type9(gui), width=11)
        self.button9.grid(row=1, column=3, ipady=10, pady=10, padx=10)
        self.button9.configure(background='grey20')
        self.button10 = Button(gui, justify=LEFT, text='T\nn  k  m\nA1 A2...An\nn  k  m\nA1 A2...An'
                              , fg='white', command=lambda: Type10(gui), width=11)
        self.button10.grid(row=1, column=4, ipady=10, pady=10, padx=10)
        self.button10.configure(background='grey20')
        self.button_new = Button(gui, text=' Another type ', fg='black'
                             , command=lambda: self.newformat(self=Case))
        self.button_new.grid(row=2, column=2, ipady=10, pady=10, padx=10)

    def newformat(self):
        url = "https://forms.gle/UVdo6QMAwBNxa9Ln7"
        webbrowser.open_new_tab(url)

    def forget_home(self):
        self.button1.grid_forget()
        self.button2.grid_forget()
        self.button3.grid_forget()
        self.button4.grid_forget()
        self.button5.grid_forget()
        self.button6.grid_forget()
        self.button7.grid_forget()
        self.button8.grid_forget()
        self.button9.grid_forget()
        self.button10.grid_forget()
        self.button_new.grid_forget()

    def cpy(self):
        txt = self.output.get('1.0', END)
        gui.clipboard_clear()
        gui.clipboard_append(txt.strip())

    def done(self, output):
        self.output.grid_forget()
        self.copy_button.grid_forget()
        self.generate_button.grid_forget()
        self.change_values_button.grid_forget()
        self.done_button.grid_forget()
        self.retrieve_home()
        pass

    def retrieve_home(self):
        self.button1.grid(row=0, column=0, ipady=10, pady=10, padx=10)
        self.button2.grid(row=0, column=1, ipady=10, pady=10, padx=10)
        self.button3.grid(row=0, column=2, ipady=10, pady=10, padx=10)
        self.button4.grid(row=0, column=3, ipady=10, pady=10, padx=10)
        self.button5.grid(row=0, column=4, ipady=10, pady=10, padx=10)
        self.button6.grid(row=1, column=0, ipady=10, pady=10, padx=10)
        self.button7.grid(row=1, column=1, ipady=10, pady=10, padx=10)
        self.button8.grid(row=1, column=2, ipady=10, pady=10, padx=10)
        self.button9.grid(row=1, column=3, ipady=10, pady=10, padx=10)
        self.button10.grid(row=1, column=4, ipady=10, pady=10, padx=10)
        self.button_new.grid(row=2, column=2, ipady=10, pady=10, padx=10)


class Type1(Case):

    def __init__(self, master):
        super(Type1, self).__init__(master)
        Case.forget_home(self=Case)
        self.take_input()

    def take_input(self):
        try:
            self.output.grid_forget()
            self.copy_button.grid_forget()
            self.generate_button.grid_forget()
            self.change_values_button.grid_forget()
            self.done_button.grid_forget()
        except AttributeError:
            pass
        self.test_case_count_label = Label(gui, text='  T  =   ', font=('calibre', 10, 'bold'))  # Type 1
        self.test_case_count = Entry(gui, textvariable=t, font=('calibre', 10, 'normal'))
        self.minimum_value_of_n = Entry(gui, textvariable=n_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_n_label = Label(gui, text='<= n <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_n = Entry(gui, textvariable=n_max, font=('calibre', 10, 'normal'))
        self.minimum_value_of_ai = Entry(gui, textvariable=a_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_ai_label = Label(gui, text='<= Ai <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_ai = Entry(gui, textvariable=a_max, font=('calibre', 10, 'normal'))
        self.sub_btn = Button(gui, text='GENERATE', command=self.submit)

        self.test_case_count_label.grid(row=0, column=0, padx=10, pady=10, ipady=1)             # Type 1
        self.test_case_count.grid(row=0, column=1)
        self.minimum_value_of_n.grid(row=1, column=0, padx=10, pady=10)
        self.min_max_values_of_n_label.grid(row=1, column=1, ipadx=5, ipady=1)
        self.maximum_value_of_n.grid(row=1, column=2, padx=(10, 10))
        self.minimum_value_of_ai.grid(row=2, column=0, padx=10)
        self.min_max_values_of_ai_label.grid(row=2, column=1, ipadx=2, ipady=1)
        self.maximum_value_of_ai.grid(row=2, column=2)
        self.sub_btn.grid(row=3, column=1, pady=20)

    def display(self):
        self.output = Text(gui, height=12, bg="light cyan", width=82)
        self.output.grid(row=0, column=0, columnspan=10, sticky='n', ipady=10, pady=(15, 25), padx=7)
        self.copy_button = Button(gui, text='COPY', fg='black', command=self.cpy)
        self.copy_button.grid(row=1, column=2, sticky='SW', ipady=10, pady=10, padx=5)
        self.generate_button = Button(gui, text='RE-GENERATE', fg='black', command=lambda: self.generate())
        self.generate_button.grid(row=1, column=4, sticky='S', ipady=10, pady=10, padx=5)
        self.change_values_button = Button(gui, text='CHANGE CONSTRAINT', fg='black'
                                           , command=lambda: self.take_input())
        self.change_values_button.grid(row=1, column=5, sticky='S', ipady=10, pady=10, padx=5)
        self.done_button = Button(gui, text='DONE', fg='black', command=lambda: self.done(self.output))
        self.done_button.grid(row=1, column=7, sticky='SE', ipady=10, pady=(10,18), padx=5)

    def generate(self):                                         # Type 1
        self.output.delete('1.0', END)
        self.output.insert(END, self.t)
        self.output.insert(END, '\n')
        for i in range(self.t):
            self.n = randint(self.n_min, self.n_max)
            self.output.insert(END, self.n)
            self.output.insert(END, '\n')
            self.a = [0] * self.n
            for j in range(self.n):
                self.a[j] = randint(self.a_min, self.a_max)
            self.output.insert(END, self.a)
            self.output.insert(END, '\n')

    def forget_type1(self):                                     # Type 1
        self.test_case_count_label.grid_forget()
        self.test_case_count.grid_forget()
        self.minimum_value_of_n.grid_forget()
        self.min_max_values_of_n_label.grid_forget()
        self.maximum_value_of_n.grid_forget()
        self.minimum_value_of_ai.grid_forget()
        self.min_max_values_of_ai_label.grid_forget()
        self.maximum_value_of_ai.grid_forget()
        self.sub_btn.grid_forget()

    def submit(self):                                          # Type 1
        self.t = int(self.test_case_count.get())
        self.n_min = int(self.minimum_value_of_n.get())
        self.n_max = int(self.maximum_value_of_n.get())
        self.a_min = int(self.minimum_value_of_ai.get())
        self.a_max = int(self.maximum_value_of_ai.get())

        self.forget_type1()
        self.display()
        self.generate()


class Type2(Case):

    def __init__(self, master):
        super(Type2, self).__init__(master)
        Case.forget_home(self=Case)
        self.take_input()

    def take_input(self):              # Type 2
        try:
            self.output.grid_forget()
            self.copy_button.grid_forget()
            self.generate_button.grid_forget()
            self.change_values_button.grid_forget()
            self.done_button.grid_forget()
        except AttributeError:
            pass
        self.test_case_count_label = Label(gui, text='  T  =   ', font=('calibre', 10, 'bold'))  # Type 2
        self.test_case_count = Entry(gui, textvariable=t, font=('calibre', 10, 'normal'))
        self.minimum_value_of_n = Entry(gui, textvariable=n_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_n_label = Label(gui, text='<= n <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_n = Entry(gui, textvariable=n_max, font=('calibre', 10, 'normal'))
        self.minimum_value_of_m = Entry(gui, textvariable=m_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_m_label = Label(gui, text='<= m <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_m = Entry(gui, textvariable=m_max, font=('calibre', 10, 'normal'))
        self.minimum_value_of_ai = Entry(gui, textvariable=a_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_ai_label = Label(gui, text='<= Ai <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_ai = Entry(gui, textvariable=a_max, font=('calibre', 10, 'normal'))
        self.sub_btn = Button(gui, text='GENERATE', command=self.submit)

        self.test_case_count_label.grid(row=0, column=0, padx=10, pady=10, ipady=1)  # Type2
        self.test_case_count.grid(row=0, column=1)
        self.minimum_value_of_n.grid(row=1, column=0, padx=10, pady=10)
        self.min_max_values_of_n_label.grid(row=1, column=1, ipadx=7, ipady=1)
        self.maximum_value_of_n.grid(row=1, column=2, padx=(10, 10))
        self.minimum_value_of_m.grid(row=2, column=0, padx=10, pady=10)
        self.min_max_values_of_m_label.grid(row=2, column=1, padx=10, ipadx=5, ipady=1)
        self.maximum_value_of_m.grid(row=2, column=2, padx=10)
        self.minimum_value_of_ai.grid(row=3, column=0, padx=10, pady=10)
        self.min_max_values_of_ai_label.grid(row=3, column=1, ipadx=5, ipady=1)
        self.maximum_value_of_ai.grid(row=3, column=2, padx=(10, 10))
        self.sub_btn.grid(row=4, column=1, pady=10)

    def display(self):
        self.output = Text(gui, height=12, bg="light cyan", width=82)  # Type 2
        self.output.grid(row=0, column=0, columnspan=10, sticky='n', ipady=10, pady=(15, 25), padx=7)
        self.copy_button = Button(gui, text='COPY', fg='black', command=self.cpy)
        self.copy_button.grid(row=1, column=2, sticky='SW', ipady=10, pady=10, padx=5)
        self.generate_button = Button(gui, text='RE-GENERATE', fg='black', command=lambda: self.generate())
        self.generate_button.grid(row=1, column=4, sticky='S', ipady=10, pady=10, padx=5)
        self.change_values_button = Button(gui, text='CHANGE CONSTRAINT', fg='black'
                                           , command=lambda: self.take_input())
        self.change_values_button.grid(row=1, column=5, sticky='S', ipady=10, pady=10, padx=5)
        self.done_button = Button(gui, text='DONE', fg='black', command=lambda: self.done(self.output))
        self.done_button.grid(row=1, column=7, sticky='SE', ipady=10, pady=(10, 18), padx=5)

    def generate(self):                                # Type 2
        self.output.delete('1.0', END)
        self.output.insert(END, self.t)
        self.output.insert(END, '\n')
        for i in range(self.t):
            self.n = randint(self.n_min, self.n_max)
            self.m = randint(self.m_min, self.m_max)
            self.output.insert(END, self.n)
            self.output.insert(END, ' ')
            self.output.insert(END, self.m)
            self.output.insert(END, '\n')
            self.a = [0] * self.n
            for j in range(self.n):
                self.a[j] = randint(self.a_min, self.a_max)
            self.output.insert(END, self.a)
            self.output.insert(END, '\n')

    def forget_type2(self):                             # Type 2
        self.test_case_count_label.grid_forget()
        self.test_case_count.grid_forget()
        self.minimum_value_of_n.grid_forget()
        self.min_max_values_of_n_label.grid_forget()
        self.maximum_value_of_n.grid_forget()
        self.minimum_value_of_m.grid_forget()
        self.min_max_values_of_m_label.grid_forget()
        self.maximum_value_of_m.grid_forget()
        self.minimum_value_of_ai.grid_forget()
        self.min_max_values_of_ai_label.grid_forget()
        self.maximum_value_of_ai.grid_forget()
        self.sub_btn.grid_forget()

    def submit(self):                                 # Type 2
        self.t = int(self.test_case_count.get())
        self.n_min = int(self.minimum_value_of_n.get())
        self.n_max = int(self.maximum_value_of_n.get())
        self.m_min = int(self.minimum_value_of_m.get())
        self.m_max = int(self.maximum_value_of_m.get())
        self.a_min = int(self.minimum_value_of_ai.get())
        self.a_max = int(self.maximum_value_of_ai.get())

        self.forget_type2()
        self.display()
        self.generate()


class Type3(Case):
    def __init__(self, master):
        super(Type3, self).__init__(master)
        Case.forget_home(self=Case)
        self.take_input()

    def take_input(self):
        try:
            self.output.grid_forget()
            self.copy_button.grid_forget()
            self.generate_button.grid_forget()
            self.change_values_button.grid_forget()
            self.done_button.grid_forget()
        except AttributeError:
            pass
        self.test_case_count_label = Label(gui, text='  T  =   ', font=('calibre', 10, 'bold'))    # Type 3
        self.test_case_count = Entry(gui, textvariable=t, font=('calibre', 10, 'normal'))
        self.minimum_value_of_ai = Entry(gui, textvariable=a_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_ai_label = Label(gui, text='<= Ai <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_ai = Entry(gui, textvariable=a_max, font=('calibre', 10, 'normal'))
        self.minimum_value_of_bi = Entry(gui, textvariable=b_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_bi_label = Label(gui, text='<= Bi <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_bi = Entry(gui, textvariable=b_max, font=('calibre', 10, 'normal'))
        self.sub_btn = Button(gui, text='GENERATE', command=self.submit)

        self.test_case_count_label.grid(row=0, column=0, pady=10, padx=10, ipadx=5, ipady=1)    # Type 3
        self.test_case_count.grid(row=0, column=1, padx=10)
        self.minimum_value_of_ai.grid(row=1, column=0, padx=10, pady=10)
        self.min_max_values_of_ai_label.grid(row=1, column=1)
        self.maximum_value_of_ai.grid(row=1, column=2)
        self.minimum_value_of_bi.grid(row=2, column=0, pady=10)
        self.min_max_values_of_bi_label.grid(row=2, column=1, padx=10)
        self.maximum_value_of_bi.grid(row=2, column=2, padx=10)
        self.sub_btn.grid(row=3, column=1, pady=(10, 20))

    def display(self):                                                # Type 3
        self.output = Text(gui, height=12, bg="light cyan", width=82)
        self.output.grid(row=0, column=0, columnspan=10, sticky='n', ipady=10, pady=(15, 25), padx=7)
        self.copy_button = Button(gui, text='COPY', fg='black', command=self.cpy)
        self.copy_button.grid(row=1, column=2, sticky='SW', ipady=10, pady=10, padx=5)
        self.generate_button = Button(gui, text='RE-GENERATE', fg='black', command=lambda: self.generate())
        self.generate_button.grid(row=1, column=4, sticky='S', ipady=10, pady=10, padx=5)
        self.change_values_button = Button(gui, text='CHANGE CONSTRAINT', fg='black'
                                           , command=lambda: self.take_input())
        self.change_values_button.grid(row=1, column=5, sticky='S', ipady=10, pady=10, padx=5)
        self.done_button = Button(gui, text='DONE', fg='black', command=lambda: self.done(self.output))
        self.done_button.grid(row=1, column=7, sticky='SE', ipady=10, pady=(10, 18), padx=5)

    def generate(self):                                              # Type 3
        self.output.delete('1.0', END)
        self.output.insert(END, self.t)
        self.output.insert(END, '\n')
        for i in range(self.t):
            self.a = randint(self.a_min, self.a_max)
            self.b = randint(self.b_min, self.b_max)
            self.output.insert(END, self.a)
            self.output.insert(END, ' ')
            self.output.insert(END, self.b)
            self.output.insert(END, '\n')

    def forget_type3(self):                                         # Type 3
        self.test_case_count_label.grid_forget()
        self.test_case_count.grid_forget()
        self.minimum_value_of_ai.grid_forget()
        self.min_max_values_of_ai_label.grid_forget()
        self.maximum_value_of_ai.grid_forget()
        self.minimum_value_of_bi.grid_forget()
        self.min_max_values_of_bi_label.grid_forget()
        self.maximum_value_of_bi.grid_forget()
        self.sub_btn.grid_forget()

    def submit(self):                                              # Type 3
        self.t = int(self.test_case_count.get())
        self.a_min = int(self.minimum_value_of_ai.get())
        self.a_max = int(self.maximum_value_of_ai.get())
        self.b_min = int(self.minimum_value_of_bi.get())
        self.b_max = int(self.maximum_value_of_bi.get())

        self.forget_type3()
        self.display()
        self.generate()


class Type4(Case):

    def __init__(self, master):
        super(Type4, self).__init__(master)
        Case.forget_home(self=Case)
        self.take_input()

    def take_input(self):                                   # Type 4
        try:
            self.output.grid_forget()
            self.copy_button.grid_forget()
            self.generate_button.grid_forget()
            self.change_values_button.grid_forget()
            self.done_button.grid_forget()
        except AttributeError:
            pass
        self.test_case_count_label = Label(gui, text='  T  =   ', font=('calibre', 10, 'bold'))     # Type 4
        self.test_case_count = Entry(gui, textvariable=t, font=('calibre', 10, 'normal'))
        self.minimum_value_of_n = Entry(gui, textvariable=n_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_n_label = Label(gui, text='<= n <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_n = Entry(gui, textvariable=n_max, font=('calibre', 10, 'normal'))
        self.minimum_value_of_m = Entry(gui, textvariable=m_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_m_label = Label(gui, text='<= m <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_m = Entry(gui, textvariable=m_max, font=('calibre', 10, 'normal'))
        self.minimum_value_of_ai = Entry(gui, textvariable=a_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_ai_label = Label(gui, text='<= Ai <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_ai = Entry(gui, textvariable=a_max, font=('calibre', 10, 'normal'))
        self.minimum_value_of_bi = Entry(gui, textvariable=b_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_bi_label = Label(gui, text='<= Bi <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_bi = Entry(gui, textvariable=b_max, font=('calibre', 10, 'normal'))
        self.sub_btn = Button(gui, text='GENERATE', command=self.submit)

        self.test_case_count_label.grid(row=0, column=0, padx=10, ipady=1, pady=10)          # Type 4
        self.test_case_count.grid(row=0, column=1, padx=10)
        self.minimum_value_of_n.grid(row=1, column=0, pady=10, padx=10)
        self.min_max_values_of_n_label.grid(row=1, column=1)
        self.maximum_value_of_n.grid(row=1, column=2, padx=(10, 10))
        self.minimum_value_of_m.grid(row=2, column=0, pady=10)
        self.min_max_values_of_m_label.grid(row=2, column=1)
        self.maximum_value_of_m.grid(row=2, column=2)
        self.minimum_value_of_ai.grid(row=3, column=0, pady=10)
        self.min_max_values_of_ai_label.grid(row=3, column=1)
        self.maximum_value_of_ai.grid(row=3, column=2)
        self.minimum_value_of_bi.grid(row=4, column=0, pady=10)
        self.min_max_values_of_bi_label.grid(row=4, column=1)
        self.maximum_value_of_bi.grid(row=4, column=2)
        self.sub_btn.grid(row=5, column=1, pady=(10, 20))

    def display(self):                                                     # Type 4
        self.output = Text(gui, height=12, bg="light cyan", width=82)
        self.output.grid(row=0, column=0, columnspan=10, sticky='n', ipady=10, pady=(15, 25), padx=7)
        self.copy_button = Button(gui, text='COPY', fg='black', command=self.cpy)
        self.copy_button.grid(row=1, column=2, sticky='SW', ipady=10, pady=10, padx=5)
        self.generate_button = Button(gui, text='RE-GENERATE', fg='black', command=lambda: self.generate())
        self.generate_button.grid(row=1, column=4, sticky='S', ipady=10, pady=10, padx=5)
        self.change_values_button = Button(gui, text='CHANGE CONSTRAINT', fg='black'
                                           , command=lambda: self.take_input())
        self.change_values_button.grid(row=1, column=5, sticky='S', ipady=10, pady=10, padx=5)
        self.done_button = Button(gui, text='DONE', fg='black', command=lambda: self.done(self.output))
        self.done_button.grid(row=1, column=7, sticky='SE', ipady=10, pady=(10, 18), padx=5)

    def generate(self):                                     # Type 4
        self.output.delete('1.0', END)
        self.output.insert(END, self.t)
        self.output.insert(END, '\n')
        for i in range(self.t):
            self.n = randint(self.n_min, self.n_max)
            self.m = randint(self.m_min, self.m_max)
            self.output.insert(END, self.n)
            self.output.insert(END, ' ')
            self.output.insert(END, self.m)
            self.output.insert(END, '\n')
            self.a = [0] * self.n
            self.b = [0] * self.m
            for j in range(self.n):
                self.a[j] = randint(self.a_min, self.a_max)
            self.output.insert(END, self.a)
            self.output.insert(END, '\n')
            for j in range(self.m):
                self.b[j] = randint(self.b_min, self.b_max)
            self.output.insert(END, self.b)
            self.output.insert(END, '\n')

    def forget_type4(self):                                 # Type 4
        self.test_case_count_label.grid_forget()
        self.test_case_count.grid_forget()
        self.minimum_value_of_n.grid_forget()
        self.min_max_values_of_n_label.grid_forget()
        self.maximum_value_of_n.grid_forget()
        self.minimum_value_of_m.grid_forget()
        self.min_max_values_of_m_label.grid_forget()
        self.maximum_value_of_m.grid_forget()
        self.minimum_value_of_ai.grid_forget()
        self.min_max_values_of_ai_label.grid_forget()
        self.maximum_value_of_ai.grid_forget()
        self.minimum_value_of_bi.grid_forget()
        self.min_max_values_of_bi_label.grid_forget()
        self.maximum_value_of_bi.grid_forget()
        self.sub_btn.grid_forget()

    def submit(self):                                           # Type 4
        self.t = int(self.test_case_count.get())
        self.n_min = int(self.minimum_value_of_n.get())
        self.n_max = int(self.maximum_value_of_n.get())
        self.m_min = int(self.minimum_value_of_m.get())
        self.m_max = int(self.maximum_value_of_m.get())
        self.a_min = int(self.minimum_value_of_ai.get())
        self.a_max = int(self.maximum_value_of_ai.get())
        self.b_min = int(self.minimum_value_of_bi.get())
        self.b_max = int(self.maximum_value_of_bi.get())

        self.forget_type4()
        self.display()
        self.generate()


#  ------------------------------------------------- ###
#  ------------------------------------------------- ###
#  ### Developed by TANMAY KHANDELWAL (aka Dude901). ###
#  _________________________________________________ ###
#  _________________________________________________ ###


class Type5(Case):

    def __init__(self, master):
        super(Type5, self).__init__(master)
        Case.forget_home(self=Case)
        self.take_input()

    def take_input(self):                       # Type 5
        try:
            self.output.grid_forget()
            self.copy_button.grid_forget()
            self.generate_button.grid_forget()
            self.change_values_button.grid_forget()
            self.done_button.grid_forget()
        except AttributeError:
            pass
        self.test_case_count_label = Label(gui, text='  T  =   ', font=('calibre', 10, 'bold'))       # Type 5
        self.test_case_count = Entry(gui, textvariable=t, font=('calibre', 10, 'normal'))
        self.minimum_value_of_n = Entry(gui, textvariable=n_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_n_label = Label(gui, text='<= n <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_n = Entry(gui, textvariable=n_max, font=('calibre', 10, 'normal'))
        self.minimum_value_of_m = Entry(gui, textvariable=m_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_m_label = Label(gui, text='<= m <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_m = Entry(gui, textvariable=m_max, font=('calibre', 10, 'normal'))
        self.minimum_value_of_k = Entry(gui, textvariable=k_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_k_label = Label(gui, text='<= k <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_k = Entry(gui, textvariable=k_max, font=('calibre', 10, 'normal'))
        self.sub_btn = Button(gui, text='GENERATE', command=self.submit)

        self.test_case_count_label.grid(row=0, column=0, padx=10, pady=10, ipady=1)         # Type 5
        self.test_case_count.grid(row=0, column=1, padx=10)
        self.minimum_value_of_n.grid(row=1, column=0, padx=10, pady=10)
        self.min_max_values_of_n_label.grid(row=1, column=1, ipady=1, padx=10)
        self.maximum_value_of_n.grid(row=1, column=2, padx=(10, 10))
        self.minimum_value_of_m.grid(row=2, column=0, pady=10)
        self.min_max_values_of_m_label.grid(row=2, column=1)
        self.maximum_value_of_m.grid(row=2, column=2)
        self.minimum_value_of_k.grid(row=3, column=0, pady=10)
        self.min_max_values_of_k_label.grid(row=3, column=1)
        self.maximum_value_of_k.grid(row=3, column=2)
        self.sub_btn.grid(row=4, column=1, pady=(10, 20))

    def display(self):                                                       # Type 5
        self.output = Text(gui, height=12, bg="light cyan", width=82)
        self.output.grid(row=0, column=0, columnspan=10, sticky='n', ipady=10, pady=(15, 25), padx=7)
        self.copy_button = Button(gui, text='COPY', fg='black', command=self.cpy)
        self.copy_button.grid(row=1, column=2, sticky='SW', ipady=10, pady=10, padx=5)
        self.generate_button = Button(gui, text='RE-GENERATE', fg='black', command=lambda: self.generate())
        self.generate_button.grid(row=1, column=4, sticky='S', ipady=10, pady=10, padx=5)
        self.change_values_button = Button(gui, text='CHANGE CONSTRAINT', fg='black'
                                           , command=lambda: self.take_input())
        self.change_values_button.grid(row=1, column=5, sticky='S', ipady=10, pady=10, padx=5)
        self.done_button = Button(gui, text='DONE', fg='black', command=lambda: self.done(self.output))
        self.done_button.grid(row=1, column=7, sticky='SE', ipady=10, pady=(10, 18), padx=5)

    def generate(self):                             # Type 5
        self.output.delete('1.0', END)
        self.output.insert(END, self.t)
        self.output.insert(END, '\n')
        for i in range(self.t):
            self.n = randint(self.n_min, self.n_max)
            self.m = randint(self.m_min, self.m_max)
            self.k = randint(self.k_min, self.k_max)
            self.output.insert(END, self.n)
            self.output.insert(END, ' ')
            self.output.insert(END, self.m)
            self.output.insert(END, ' ')
            self.output.insert(END, self.k)
            self.output.insert(END, '\n')

    def forget_type5(self):                                 # Type 5
        self.test_case_count_label.grid_forget()
        self.test_case_count.grid_forget()
        self.minimum_value_of_n.grid_forget()
        self.min_max_values_of_n_label.grid_forget()
        self.maximum_value_of_n.grid_forget()
        self.minimum_value_of_m.grid_forget()
        self.min_max_values_of_m_label.grid_forget()
        self.maximum_value_of_m.grid_forget()
        self.minimum_value_of_k.grid_forget()
        self.min_max_values_of_k_label.grid_forget()
        self.maximum_value_of_k.grid_forget()
        self.sub_btn.grid_forget()

    def submit(self):                                       # Type 5
        self.t = int(self.test_case_count.get())
        self.n_min = int(self.minimum_value_of_n.get())
        self.n_max = int(self.maximum_value_of_n.get())
        self.m_min = int(self.minimum_value_of_m.get())
        self.m_max = int(self.maximum_value_of_m.get())
        self.k_min = int(self.minimum_value_of_k.get())
        self.k_max = int(self.maximum_value_of_k.get())

        self.forget_type5()
        self.display()
        self.generate()


class Type6(Case):

    def __init__(self, master):                     # Type 6
        super(Type6, self).__init__(master)
        Case.forget_home(self=Case)
        self.take_input()

    def take_input(self):                           # Type 6
        try:
            self.output.grid_forget()
            self.copy_button.grid_forget()
            self.generate_button.grid_forget()
            self.change_values_button.grid_forget()
            self.done_button.grid_forget()
        except AttributeError:
            pass                                # Type 6
        self.minimum_value_of_n = Entry(gui, textvariable=n_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_n_label = Label(gui, text='   <= No. of rows <=  ', font=('calibre', 10, 'bold'))
        self.maximum_value_of_n = Entry(gui, textvariable=n_max, font=('calibre', 10, 'normal'))
        self.minimum_value_of_m = Entry(gui, textvariable=m_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_m_label = Label(gui, text='<= No. of columns <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_m = Entry(gui, textvariable=m_max, font=('calibre', 10, 'normal'))
        self.minimum_value_of_ai = Entry(gui, textvariable=a_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_ai_label = Label(gui, text='  <= Ai <=  ', font=('calibre', 10, 'bold'))
        self.maximum_value_of_ai = Entry(gui, textvariable=a_max, font=('calibre', 10, 'normal'))
        self.sub_btn = Button(gui, text='GENERATE', command=self.submit)

        self.minimum_value_of_n.grid(row=0, column=0, padx=10, pady=20, ipady=1)               # Type 6
        self.min_max_values_of_n_label.grid(row=0, column=1)
        self.maximum_value_of_n.grid(row=0, column=2)
        self.minimum_value_of_m.grid(row=1, column=0, pady=10)
        self.min_max_values_of_m_label.grid(row=1, column=1, padx=10, ipady=1)
        self.maximum_value_of_m.grid(row=1, column=2, padx=(10, 10))
        self.minimum_value_of_ai.grid(row=2, column=0, pady=10)
        self.min_max_values_of_ai_label.grid(row=2, column=1)
        self.maximum_value_of_ai.grid(row=2, column=2)
        self.sub_btn.grid(row=3, column=1, pady=(10, 20))

    def display(self):                                                      # Type 6
        self.output = Text(gui, height=12, bg="light cyan", width=82)
        self.output.grid(row=0, column=0, columnspan=10, sticky='n', ipady=10, pady=(15, 25), padx=7)
        self.copy_button = Button(gui, text='COPY', fg='black', command=self.cpy)
        self.copy_button.grid(row=1, column=2, sticky='SW', ipady=10, pady=10, padx=5)
        self.generate_button = Button(gui, text='RE-GENERATE', fg='black', command=lambda: self.generate())
        self.generate_button.grid(row=1, column=4, sticky='S', ipady=10, pady=10, padx=5)
        self.change_values_button = Button(gui, text='CHANGE CONSTRAINT', fg='black'
                                           , command=lambda: self.take_input())
        self.change_values_button.grid(row=1, column=5, sticky='S', ipady=10, pady=10, padx=5)
        self.done_button = Button(gui, text='DONE', fg='black', command=lambda: self.done(self.output))
        self.done_button.grid(row=1, column=7, sticky='SE', ipady=10, pady=(10, 18), padx=5)

    def generate(self):                                         # Type 6
        self.output.delete('1.0', END)
        self.n = randint(self.n_min, self.n_max)
        self.m = randint(self.m_min, self.m_max)
        self.output.insert(END, self.n)
        self.output.insert(END, ' ')
        self.output.insert(END, self.m)
        self.output.insert(END, '\n')
        for i in range(self.n):
            self.a = [0] * self.m
            for j in range(self.m):
                self.a[j] = randint(self.a_min, self.a_max)
            self.output.insert(END, self.a)
            self.output.insert(END, '\n')

    def forget_type6(self):                                     # Type 6
        self.minimum_value_of_n.grid_forget()
        self.min_max_values_of_n_label.grid_forget()
        self.maximum_value_of_n.grid_forget()
        self.minimum_value_of_m.grid_forget()
        self.min_max_values_of_m_label.grid_forget()
        self.maximum_value_of_m.grid_forget()
        self.minimum_value_of_ai.grid_forget()
        self.min_max_values_of_ai_label.grid_forget()
        self.maximum_value_of_ai.grid_forget()
        self.sub_btn.grid_forget()

    def submit(self):                                          # Type 6
        self.n_min = int(self.minimum_value_of_n.get())
        self.n_max = int(self.maximum_value_of_n.get())
        self.m_min = int(self.minimum_value_of_m.get())
        self.m_max = int(self.maximum_value_of_m.get())
        self.a_min = int(self.minimum_value_of_ai.get())
        self.a_max = int(self.maximum_value_of_ai.get())

        self.forget_type6()
        self.display()
        self.generate()


class Type7(Case):

    def __init__(self, master):                               # Type 7
        super(Type7, self).__init__(master)
        Case.forget_home(self=Case)
        self.take_input()

    def take_input(self):                                     # Type 7
        try:
            self.output.grid_forget()
            self.copy_button.grid_forget()
            self.generate_button.grid_forget()
            self.change_values_button.grid_forget()
            self.done_button.grid_forget()
            self.char_list.delete(0, 'end')
        except AttributeError:
            pass
        self.test_case_count_label = Label(gui, text='  T  =   ', font=('calibre', 10, 'bold'))      # Type 7
        self.test_case_count = Entry(gui, textvariable=t, font=('calibre', 10, 'normal'))
        self.char_list_label = Label(gui, text=' Characters: ', font=('calibre', 10, 'bold'))
        self.char_list = Entry(gui, textvariable=char_lis, font=('calibre', 10, 'normal'), width=43)
        self.minimum_value_of_n = Entry(gui, textvariable=n_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_n_label = Label(gui, text='<=Length of string<=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_n = Entry(gui, textvariable=n_max, font=('calibre', 10, 'normal'))
        self.char_list.insert(END, '(Space separated characters)')
        self.char_list.bind("<FocusIn>", lambda args: self.char_list.delete('0', 'end'))
        self.sub_btn = Button(gui, text='Submit', command=self.submit)

        self.test_case_count_label.grid(row=0, column=0, pady=10)               # Type 7
        self.test_case_count.grid(row=0, column=1, padx=10)
        self.char_list_label.grid(row=1, column=0, pady=10)
        self.char_list.grid(row=1, column=1, columnspan=2, padx=10)
        self.minimum_value_of_n.grid(row=2, column=0, pady=10, padx=10)
        self.min_max_values_of_n_label.grid(row=2, column=1)
        self.maximum_value_of_n.grid(row=2, column=2, padx=(10, 10))
        self.sub_btn.grid(row=3, column=1, pady=(10, 20))

    def display(self):                                                      # Type 7
        self.output = Text(gui, height=12, bg="light cyan", width=82)
        self.output.grid(row=0, column=0, columnspan=10, sticky='n', ipady=10, pady=(15, 25), padx=7)
        self.copy_button = Button(gui, text='COPY', fg='black', command=self.cpy)
        self.copy_button.grid(row=1, column=2, sticky='SW', ipady=10, pady=10, padx=5)
        self.generate_button = Button(gui, text='RE-GENERATE', fg='black', command=lambda: self.generate())
        self.generate_button.grid(row=1, column=4, sticky='S', ipady=10, pady=10, padx=5)
        self.change_values_button = Button(gui, text='CHANGE CONSTRAINT', fg='black'
                                           , command=lambda: self.take_input())
        self.change_values_button.grid(row=1, column=5, sticky='S', ipady=10, pady=10, padx=5)
        self.done_button = Button(gui, text='DONE', fg='black', command=lambda: self.done(self.output))
        self.done_button.grid(row=1, column=7, sticky='SE', ipady=10, pady=(10, 18), padx=5)

    def generate(self):                                 # Type 7
        self.output.delete('1.0', END)
        self.output.insert(END, self.t)
        self.output.insert(END, '\n')
        for i in range(self.t):
            self.n = randint(self.n_min, self.n_max)
            self.output.insert(END, self.n)
            self.output.insert(END, '\n')
            # self.a = list(input().split())
            self.a = choices(self.char_lis, k=self.n)
            self.output.insert(END, ''.join(self.a))
            self.output.insert(END, '\n')

    def forget_type7(self):                                 # Type 7
        self.test_case_count_label.grid_forget()
        self.test_case_count.grid_forget()
        self.char_list_label.grid_forget()
        self.char_list.grid_forget()
        self.minimum_value_of_n.grid_forget()
        self.min_max_values_of_n_label.grid_forget()
        self.maximum_value_of_n.grid_forget()
        self.sub_btn.grid_forget()

    def submit(self):                                       # Type 7
        self.t = int(self.test_case_count.get())
        self.n_min = int(self.minimum_value_of_n.get())
        self.n_max = int(self.maximum_value_of_n.get())
        self.char_lis = list(self.char_list.get().split())

        self.forget_type7()
        self.display()
        self.generate()


class Type8(Case):

    def __init__(self, master):                             # Type 8
        super(Type8, self).__init__(master)
        Case.forget_home(self=Case)
        self.take_input()

    def take_input(self):
        try:
            self.output.grid_forget()
            self.copy_button.grid_forget()
            self.generate_button.grid_forget()
            self.change_values_button.grid_forget()
            self.done_button.grid_forget()
        except AttributeError:
            pass
        self.test_case_count_label = Label(gui, text='T: ', font=('calibre', 10, 'bold'))
        self.test_case_count = Entry(gui, textvariable=t, font=('calibre', 10, 'normal'))
        self.minimum_value_of_n = Entry(gui, textvariable=n_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_n_label = Label(gui, text='<= n <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_n = Entry(gui, textvariable=n_max, font=('calibre', 10, 'normal'))
        self.minimum_value_of_m = Entry(gui, textvariable=m_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_m_label = Label(gui, text='<= m <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_m = Entry(gui, textvariable=m_max, font=('calibre', 10, 'normal'))
        self.minimum_value_of_ai = Entry(gui, textvariable=a_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_ai_label = Label(gui, text='<= Ai <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_ai = Entry(gui, textvariable=a_max, font=('calibre', 10, 'normal'))
        self.minimum_value_of_bi = Entry(gui, textvariable=b_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_bi_label = Label(gui, text='<= Bi <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_bi = Entry(gui, textvariable=b_max, font=('calibre', 10, 'normal'))
        self.sub_btn = Button(gui, text='Submit', command=self.submit)

        self.test_case_count_label.grid(row=0, column=0)
        self.test_case_count.grid(row=0, column=1)
        self.minimum_value_of_n.grid(row=1, column=0)
        self.min_max_values_of_n_label.grid(row=1, column=1)
        self.maximum_value_of_n.grid(row=1, column=2)
        self.minimum_value_of_m.grid(row=2, column=0)
        self.min_max_values_of_m_label.grid(row=2, column=1)
        self.maximum_value_of_m.grid(row=2, column=2)
        self.minimum_value_of_ai.grid(row=3, column=0)
        self.min_max_values_of_ai_label.grid(row=3, column=1)
        self.maximum_value_of_ai.grid(row=3, column=2)
        self.minimum_value_of_bi.grid(row=4, column=0)
        self.min_max_values_of_bi_label.grid(row=4, column=1)
        self.maximum_value_of_bi.grid(row=4, column=2)
        self.sub_btn.grid(row=5, column=1)

    def display(self):
        self.output = Text(gui, height=12, bg="light cyan", width=82)
        self.output.grid(row=0, column=0, columnspan=10, sticky='n', ipady=10, pady=(15, 25), padx=7)
        self.copy_button = Button(gui, text='COPY', fg='black', command=self.cpy)
        self.copy_button.grid(row=1, column=2, sticky='SW', ipady=10, pady=10, padx=5)
        self.generate_button = Button(gui, text='RE-GENERATE', fg='black', command=lambda: self.generate())
        self.generate_button.grid(row=1, column=4, sticky='S', ipady=10, pady=10, padx=5)
        self.change_values_button = Button(gui, text='CHANGE CONSTRAINT', fg='black'
                                           , command=lambda: self.take_input())
        self.change_values_button.grid(row=1, column=5, sticky='S', ipady=10, pady=10, padx=5)
        self.done_button = Button(gui, text='DONE', fg='black', command=lambda: self.done(self.output))
        self.done_button.grid(row=1, column=7, sticky='SE', ipady=10, pady=(10, 18), padx=5)

    def generate(self):
        # print('generated new')
        self.output.delete('1.0', END)
        self.output.insert(END, self.t)
        self.output.insert(END, '\n')

        for i in range(self.t):
            self.n = randint(self.n_min, self.n_max)
            self.m = randint(self.m_min, self.m_max)
            self.output.insert(END, self.n)
            self.output.insert(END, ' ')
            self.output.insert(END, self.m)
            self.output.insert(END, '\n')
            for j in range(self.m):
                self.a = randint(self.a_min, self.a_max)
                self.b = randint(self.b_min, self.b_max)
                self.output.insert(END, self.a)
                self.output.insert(END, ' ')
                self.output.insert(END, self.b)
                self.output.insert(END, '\n')

    def forget_type8(self):
        self.test_case_count_label.grid_forget()
        self.test_case_count.grid_forget()
        self.minimum_value_of_n.grid_forget()
        self.min_max_values_of_n_label.grid_forget()
        self.maximum_value_of_n.grid_forget()
        self.minimum_value_of_m.grid_forget()
        self.min_max_values_of_m_label.grid_forget()
        self.maximum_value_of_m.grid_forget()
        self.minimum_value_of_ai.grid_forget()
        self.min_max_values_of_ai_label.grid_forget()
        self.maximum_value_of_ai.grid_forget()
        self.minimum_value_of_bi.grid_forget()
        self.min_max_values_of_bi_label.grid_forget()
        self.maximum_value_of_bi.grid_forget()
        self.sub_btn.grid_forget()

    def submit(self):
        self.t = int(self.test_case_count.get())
        self.n_min = int(self.minimum_value_of_n.get())
        self.n_max = int(self.maximum_value_of_n.get())
        self.m_min = int(self.minimum_value_of_m.get())
        self.m_max = int(self.maximum_value_of_m.get())
        self.a_min = int(self.minimum_value_of_ai.get())
        self.a_max = int(self.maximum_value_of_ai.get())
        self.b_min = int(self.minimum_value_of_bi.get())
        self.b_max = int(self.maximum_value_of_bi.get())

        self.forget_type8()
        self.display()
        self.generate()


class Type9(Case):

    def __init__(self, master):
        super(Type9, self).__init__(master)
        Case.forget_home(self=Case)
        self.take_input()

    def take_input(self):
        try:
            self.output.grid_forget()
            self.copy_button.grid_forget()
            self.generate_button.grid_forget()
            self.change_values_button.grid_forget()
            self.done_button.grid_forget()
        except AttributeError:
            pass
        self.test_case_count_label = Label(gui, text='T: ', font=('calibre', 10, 'bold'))
        self.test_case_count = Entry(gui, textvariable=t, font=('calibre', 10, 'normal'))
        self.minimum_value_of_n = Entry(gui, textvariable=n_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_n_label = Label(gui, text='<= n <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_n = Entry(gui, textvariable=n_max, font=('calibre', 10, 'normal'))
        self.char_list_label = Label(gui, text='Space separated Characters: ', font=('calibre', 10, 'bold'))
        self.char_list = Entry(gui, textvariable=char_lis, font=('calibre', 10, 'normal'))
        self.sub_btn = Button(gui, text='Submit', command=self.submit)

        self.test_case_count_label.grid(row=0, column=0)
        self.test_case_count.grid(row=0, column=1)
        self.minimum_value_of_n.grid(row=1, column=0)
        self.min_max_values_of_n_label.grid(row=1, column=1)
        self.maximum_value_of_n.grid(row=1, column=2)
        self.char_list_label.grid(row=2, column=0)
        self.char_list.grid(row=2, column=1)
        self.sub_btn.grid(row=3, column=1)

    def display(self):
        self.output = Text(gui, height=12, bg="light cyan", width=82)
        self.output.grid(row=0, column=0, columnspan=10, sticky='n', ipady=10, pady=(15, 25), padx=7)
        self.copy_button = Button(gui, text='COPY', fg='black', command=self.cpy)
        self.copy_button.grid(row=1, column=2, sticky='SW', ipady=10, pady=10, padx=5)
        self.generate_button = Button(gui, text='RE-GENERATE', fg='black', command=lambda: self.generate())
        self.generate_button.grid(row=1, column=4, sticky='S', ipady=10, pady=10, padx=5)
        self.change_values_button = Button(gui, text='CHANGE CONSTRAINT', fg='black'
                                           , command=lambda: self.take_input())
        self.change_values_button.grid(row=1, column=5, sticky='S', ipady=10, pady=10, padx=5)
        self.done_button = Button(gui, text='DONE', fg='black', command=lambda: self.done(self.output))
        self.done_button.grid(row=1, column=7, sticky='SE', ipady=10, pady=(10, 18), padx=5)

    def generate(self):
        # print('generated new')
        self.output.delete('1.0', END)
        self.output.insert(END, self.t)
        self.output.insert(END, '\n')
        for i in range(self.t):
            self.n = randint(self.n_min, self.n_max)
            self.a = choices(self.char_lis, k=self.n)
            self.output.insert(END, ''.join(self.a))
            self.output.insert(END, '\n')

    def forget_type9(self):
        self.test_case_count_label.grid_forget()
        self.test_case_count.grid_forget()
        self.char_list_label.grid_forget()
        self.char_list.grid_forget()
        self.minimum_value_of_n.grid_forget()
        self.min_max_values_of_n_label.grid_forget()
        self.maximum_value_of_n.grid_forget()
        self.sub_btn.grid_forget()

    def submit(self):    # Read Inputs from entry widgets
        self.t = int(self.test_case_count.get())
        self.n_min = int(self.minimum_value_of_n.get())
        self.n_max = int(self.maximum_value_of_n.get())
        self.char_lis = list(self.char_list.get().split())

        self.forget_type9()
        self.display()
        self.generate()


class Type10(Case):

    def __init__(self, master):
        super(Type10, self).__init__(master)
        Case.forget_home(self=Case)
        self.take_input()

    def take_input(self):
        try:
            self.output.grid_forget()
            self.copy_button.grid_forget()
            self.generate_button.grid_forget()
            self.change_values_button.grid_forget()
            self.done_button.grid_forget()
        except AttributeError:
            pass
        self.test_case_count_label = Label(gui, text='T:    ', font=('calibre', 10, 'bold'))
        self.test_case_count = Entry(gui, textvariable=t, font=('calibre', 10, 'normal'))
        self.minimum_value_of_n = Entry(gui, textvariable=n_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_n_label = Label(gui, text='<= n <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_n = Entry(gui, textvariable=n_max, font=('calibre', 10, 'normal'))
        self.minimum_value_of_k = Entry(gui, textvariable=k_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_k_label = Label(gui, text='<= k <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_k = Entry(gui, textvariable=k_max, font=('calibre', 10, 'normal'))
        self.minimum_value_of_m = Entry(gui, textvariable=m_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_m_label = Label(gui, text='<= m <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_m = Entry(gui, textvariable=m_max, font=('calibre', 10, 'normal'))
        self.minimum_value_of_ai = Entry(gui, textvariable=a_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_ai_label = Label(gui, text='<= Ai <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_ai = Entry(gui, textvariable=a_max, font=('calibre', 10, 'normal'))
        self.sub_btn = Button(gui, text='Submit', command=self.submit)

        self.test_case_count_label.grid(row=0, column=0, padx=10, pady=10)
        self.test_case_count.grid(row=0, column=1)
        self.minimum_value_of_n.grid(row=1, column=0, padx=10, pady=10)
        self.min_max_values_of_n_label.grid(row=1, column=1, ipadx=5, ipady=1)
        self.maximum_value_of_n.grid(row=1, column=2, padx=(10, 10))
        self.minimum_value_of_k.grid(row=2, column=0, padx=10, pady=10)
        self.min_max_values_of_k_label.grid(row=2, column=1, ipadx=5, ipady=1)
        self.maximum_value_of_k.grid(row=2, column=2, padx=(10, 10))
        self.minimum_value_of_m.grid(row=3, column=0, padx=10, pady=10)
        self.min_max_values_of_m_label.grid(row=3, column=1, padx=10, ipadx=4)
        self.maximum_value_of_m.grid(row=3, column=2, padx=10)
        self.minimum_value_of_ai.grid(row=4, column=0, padx=10, pady=10)
        self.min_max_values_of_ai_label.grid(row=4, column=1, ipadx=5)
        self.maximum_value_of_ai.grid(row=4, column=2, padx=(10, 10))
        self.sub_btn.grid(row=5, column=1, pady=10)

    def display(self):
        self.output = Text(gui, height=12, bg="light cyan", width=82)
        self.output.grid(row=0, column=0, columnspan=10, sticky='n', ipady=10, pady=(15, 25), padx=7)
        self.copy_button = Button(gui, text='COPY', fg='black', command=self.cpy)
        self.copy_button.grid(row=1, column=2, sticky='SW', ipady=10, pady=10, padx=5)
        self.generate_button = Button(gui, text='RE-GENERATE', fg='black', command=lambda: self.generate())
        self.generate_button.grid(row=1, column=4, sticky='S', ipady=10, pady=10, padx=5)
        self.change_values_button = Button(gui, text='CHANGE CONSTRAINT', fg='black'
                                           , command=lambda: self.take_input())
        self.change_values_button.grid(row=1, column=5, sticky='S', ipady=10, pady=10, padx=5)
        self.done_button = Button(gui, text='DONE', fg='black', command=lambda: self.done(self.output))
        self.done_button.grid(row=1, column=7, sticky='SE', ipady=10, pady=(10, 18), padx=5)

    def generate(self):
        # print('generated new')
        self.output.delete('1.0', END)
        self.output.insert(END, self.t)
        self.output.insert(END, '\n')
        for i in range(self.t):
            self.n = randint(self.n_min, self.n_max)
            self.k = randint(self.k_min, self.k_max)
            self.m = randint(self.m_min, self.m_max)
            self.output.insert(END, self.n)
            self.output.insert(END, ' ')
            self.output.insert(END, self.k)
            self.output.insert(END, ' ')
            self.output.insert(END, self.m)
            self.output.insert(END, '\n')
            self.a = [0] * self.n
            for j in range(self.n):
                self.a[j] = randint(self.a_min, self.a_max)
            self.output.insert(END, self.a)
            self.output.insert(END, '\n')

    def forget_type10(self):
        self.test_case_count_label.grid_forget()
        self.test_case_count.grid_forget()
        self.minimum_value_of_n.grid_forget()
        self.min_max_values_of_n_label.grid_forget()
        self.maximum_value_of_n.grid_forget()
        self.minimum_value_of_k.grid_forget()
        self.min_max_values_of_k_label.grid_forget()
        self.maximum_value_of_k.grid_forget()
        self.minimum_value_of_m.grid_forget()
        self.min_max_values_of_m_label.grid_forget()
        self.maximum_value_of_m.grid_forget()
        self.minimum_value_of_ai.grid_forget()
        self.min_max_values_of_ai_label.grid_forget()
        self.maximum_value_of_ai.grid_forget()
        self.sub_btn.grid_forget()

    def submit(self):
        self.t = int(self.test_case_count.get())
        self.n_min = int(self.minimum_value_of_n.get())
        self.n_max = int(self.maximum_value_of_n.get())
        self.k_min = int(self.minimum_value_of_k.get())
        self.k_max = int(self.maximum_value_of_k.get())
        self.m_min = int(self.minimum_value_of_m.get())
        self.m_max = int(self.maximum_value_of_m.get())
        self.a_min = int(self.minimum_value_of_ai.get())
        self.a_max = int(self.maximum_value_of_ai.get())

        self.forget_type10()
        self.display()
        self.generate()


t = IntVar()
n_min = IntVar()
n_max = IntVar()
m_min = IntVar()
m_max = IntVar()
k_min = IntVar()
k_max = IntVar()
a_min = IntVar()
a_max = IntVar()
b_min = IntVar()
b_max = IntVar()
char_lis = StringVar()

Case.home(self=Case)

gui.mainloop()
# e = Case(gui)
gui.mainloop()

#  ------------------------------------------------- ###
#  ------------------------------------------------- ###
#  ### Developed by TANMAY KHANDELWAL (aka Dude901). ###
#  _________________________________________________ ###
#  _________________________________________________ ###
