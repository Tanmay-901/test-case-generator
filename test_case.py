from tkinter import *
from random import randint
import webbrowser

gui = Tk()
gui.title('Test Case generator')


class Case:

    def __init__(self, master):
        gen_frame = Frame(master)
        gen_frame.grid()
        self.test_case_counter = None
        # self.button1 = None
        # self.button2 = None
        # self.button3 = None
        # self.button4 = None

    def home(self):
        self.test_case_counter = Label(gui, text='T: ', font=('calibre', 10, 'bold'))
        self.button1 = Button(gui, justify=LEFT, text='T\nn1   \nA1 A2 A3...\nn2   \nA1 A2 A3... ', fg='black',
                         command=lambda: Type1(gui))  # , height=1, width=7)
        self.button1.grid(row=1, column=0, ipady=10, pady=10, padx=5)
        self.button2 = Button(gui, justify=LEFT, text='T\nm1 n1  \nA1 A2 A3...\nm2 n2\nA1 A2 A3... ', fg='black',
                         command=lambda: Type2(gui))  # , height=1, width=7)
        self.button2.grid(row=1, column=1, ipady=10, pady=10, padx=5)

        self.button3 = Button(gui, justify=LEFT, text='T\nA1 B1\nA2 B2\nA3 B3\n.    .', fg='black',
                         command=lambda: Type3(gui), width=7)
        self.button3.grid(row=1, column=2, ipady=10, pady=10, padx=5)

        self.button4 = Button(gui, text=' Another type ', fg='black',
                         command=lambda: self.NewFormat(self))  # , height=1, width=7)
        self.button4.grid(row=2, column=1, ipady=10, pady=10, padx=5)

    def NewFormat(self):
        url = "https://forms.gle/UVdo6QMAwBNxa9Ln7"
        webbrowser.open_new_tab(url)

    def forget_home(self):
        self.button1.grid_forget()
        self.button2.grid_forget()
        self.button3.grid_forget()
        self.button4.grid_forget()

    # def submit(self):
    #     self.retrieve_home()

    def cpy(self):
        txt = self.output.get('1.0', END)
        # print(txt)
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
        self.button1.grid(row=2, column=1, ipady=10, pady=10, padx=5)
        self.button2.grid(row=2, column=2, ipady=10, pady=10, padx=5)
        self.button3.grid(row=2, column=3, ipady=10, pady=10, padx=5)
        self.button4.grid(row=3, column=2, ipady=10, pady=10, padx=5)


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
        self.test_case_count_label = Label(gui, text='T: ', font=('calibre', 10, 'bold'))
        self.test_case_count = Entry(gui, textvariable=t, font=('calibre', 10, 'normal'))
        self.minimum_value_of_n = Entry(gui, textvariable=n_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_n_label = Label(gui, text='<= n <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_n = Entry(gui, textvariable=n_max, font=('calibre', 10, 'normal'))
        self.minimum_value_of_ai = Entry(gui, textvariable=a_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_ai_label = Label(gui, text='<= Ai <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_ai = Entry(gui, textvariable=a_max, font=('calibre', 10, 'normal'))
        self.sub_btn = Button(gui, text='Submit', command=self.submit)

        self.test_case_count_label.grid(row=0, column=0)
        self.test_case_count.grid(row=0, column=1)
        self.minimum_value_of_n.grid(row=1, column=0)
        self.min_max_values_of_n_label.grid(row=1, column=1)
        self.maximum_value_of_n.grid(row=1, column=2)
        self.minimum_value_of_ai.grid(row=2, column=0)
        self.min_max_values_of_ai_label.grid(row=2, column=1)
        self.maximum_value_of_ai.grid(row=2, column=2)
        self.sub_btn.grid(row=3, column=1)

    def display(self):
        self.output = Text(gui, height=5, bg="light cyan")
        self.output.grid(row=0, column=0, columnspan=10, sticky='n', ipady=10, pady=10, padx=5, )
        self.copy_button = Button(gui, text='copy', fg='black',
                                  command=self.cpy)  # , height=1, width=7)
        self.copy_button.grid(row=1, column=2, sticky='SW', ipady=10, pady=10, padx=5)
        self.generate_button = Button(gui, text='Re-generate', fg='black',
                                        command=lambda: self.generate())  # , height=1, width=7)
        self.generate_button.grid(row=1, column=4, sticky='S', ipady=10, pady=10, padx=5)
        self.change_values_button = Button(gui, text='Change Constraints', fg='black',
                                           command=lambda: self.take_input())  # , height=1, width=7)
        self.change_values_button.grid(row=1, column=5, sticky='S', ipady=10, pady=10, padx=5)
        self.done_button = Button(gui, text='done', fg='black',
                                  command=lambda: self.done(self.output))  # , height=1, width=7)
        self.done_button.grid(row=1, column=7, sticky='SE', ipady=10, pady=10, padx=5)

    def generate(self):
        # print('generated new')
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

    def change_values(self):
        pass

    def forget_type1(self):
        self.test_case_count_label.grid_forget()
        self.test_case_count.grid_forget()
        self.minimum_value_of_n.grid_forget()
        self.min_max_values_of_n_label.grid_forget()
        self.maximum_value_of_n.grid_forget()
        self.minimum_value_of_ai.grid_forget()
        self.min_max_values_of_ai_label.grid_forget()
        self.maximum_value_of_ai.grid_forget()
        self.sub_btn.grid_forget()

    def submit(self):
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
        self.test_case_count_label = Label(master, text='T: ', font=('calibre', 10, 'bold'))
        self.test_case_count = Entry(master, textvariable=t, font=('calibre', 10, 'normal'))
        self.minimum_value_of_n = Entry(master, textvariable=n_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_n_label = Label(master, text='<= n <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_n = Entry(master, textvariable=n_max, font=('calibre', 10, 'normal'))
        self.minimum_value_of_ai = Entry(master, textvariable=a_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_ai_label = Label(master, text='<= Ai <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_ai = Entry(master, textvariable=a_max, font=('calibre', 10, 'normal'))
        self.sub_btn = Button(master, text='Submit', command=self.submit)
        self.test_case_count_label.grid(row=0, column=0)

        self.test_case_count.grid(row=0, column=1)
        self.minimum_value_of_n.grid(row=1, column=0)
        self.min_max_values_of_n_label.grid(row=1, column=1)
        self.maximum_value_of_n.grid(row=1, column=2)
        self.minimum_value_of_ai.grid(row=2, column=0)
        self.min_max_values_of_ai_label.grid(row=2, column=1)
        self.maximum_value_of_ai.grid(row=2, column=2)
        self.sub_btn.grid(row=3, column=1)


class Type3(Case):

    def __init__(self, master):
        super(Type3, self).__init__(master)
        self.test_case_count_label = Label(master, text='T: ', font=('calibre', 10, 'bold'))
        self.test_case_count = Entry(master, textvariable=t, font=('calibre', 10, 'normal'))
        self.minimum_value_of_n = Entry(master, textvariable=n_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_n_label = Label(master, text='<= n <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_n = Entry(master, textvariable=n_max, font=('calibre', 10, 'normal'))
        self.minimum_value_of_ai = Entry(master, textvariable=a_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_ai_label = Label(master, text='<= Ai <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_ai = Entry(master, textvariable=a_max, font=('calibre', 10, 'normal'))
        self.sub_btn = Button(master, text='Submit', command=self.submit)
        self.test_case_count_label.grid(row=0, column=0)

        self.test_case_count.grid(row=0, column=1)
        self.minimum_value_of_n.grid(row=1, column=0)
        self.min_max_values_of_n_label.grid(row=1, column=1)
        self.maximum_value_of_n.grid(row=1, column=2)
        self.minimum_value_of_ai.grid(row=2, column=0)
        self.min_max_values_of_ai_label.grid(row=2, column=1)
        self.maximum_value_of_ai.grid(row=2, column=2)
        self.sub_btn.grid(row=3, column=1)


# class NewFormat(Case):
#     def __init__(self, master):
#         super(NewFormat, self).__init__(master)
#         self.test_case_count_label = Label(master, text='T: ', font=('calibre', 10, 'bold'))
#         self.test_case_count = Entry(master, textvariable=t, font=('calibre', 10, 'normal'))
#         self.minimum_value_of_n = Entry(master, textvariable=n_min, font=('calibre', 10, 'normal'))
#         self.min_max_values_of_n_label = Label(master, text='<= n <=', font=('calibre', 10, 'bold'))
#         self.maximum_value_of_n = Entry(master, textvariable=n_max, font=('calibre', 10, 'normal'))
#         self.minimum_value_of_ai = Entry(master, textvariable=a_min, font=('calibre', 10, 'normal'))
#         self.min_max_values_of_ai_label = Label(master, text='<= Ai <=', font=('calibre', 10, 'bold'))
#         self.maximum_value_of_ai = Entry(master, textvariable=a_max, font=('calibre', 10, 'normal'))
#         self.sub_btn = Button(master, text='Submit', command=self.submit)
#         self.test_case_count_label.grid(row=0, column=0)
#
#         self.test_case_count.grid(row=0, column=1)
#         self.minimum_value_of_n.grid(row=1, column=0)
#         self.min_max_values_of_n_label.grid(row=1, column=1)
#         self.maximum_value_of_n.grid(row=1, column=2)
#         self.minimum_value_of_ai.grid(row=2, column=0)
#         self.min_max_values_of_ai_label.grid(row=2, column=1)
#         self.maximum_value_of_ai.grid(row=2, column=2)
#         self.sub_btn.grid(row=3, column=1)


t = IntVar()
n_min = IntVar()
n_max = IntVar()
a_min = IntVar()
a_max = IntVar()
Case.home(self=Case)

gui.mainloop()
# e = Case(gui)
gui.mainloop()
