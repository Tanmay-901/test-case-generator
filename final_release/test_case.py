#  ------------------------------------------------- ###
#  ------------------------------------------------- ###
#  ### Developed by TANMAY KHANDELWAL (aka Dude901). ###
#                github.com/Tanmay-901               ###
#  _________________________________________________ ###
#  _________________________________________________ ###

from tkinter import *
from random import randint, choices
import webbrowser

mycolor = '#262626'
gui = Tk()
gui.title('TEST CASE GENERATOR')
gui.configure(bg=mycolor)


class Case:

    def __init__(self, master):
        '''
        This constructor is used to initialize the GUI.
        '''
        gen_frame = Frame(
            master)  # Tkinter frame in which the GUI will be presented
        gen_frame.grid()
        self.test_case_counter = None
        # title
        self.statement = Label(gui, text='Select Test Case Type',
                               fg='white', height=1, font=('calibre', 12, 'normal'))

        # TestCase Buttons
        self.button1 = Button(gui, justify=LEFT, text='T\nn   \n[A1 A2 A3...An]\nn   \n[A1 A2 A3...An]', width=13,
                              fg='white', bd=3, command=lambda: changeButton(1), bg='red', font='calibre')
        self.button2 = Button(gui, justify=LEFT, text='T\nn  m  \n[A1 A2 A3...An]\nn  m\n[A1 A2 A3...An]', fg='white', command=lambda: changeButton(2
                                                                                                                                                    ), width=13, font='calibre', bd=3)
        self.button3 = Button(gui, justify=LEFT, text='T\n[A1  B1]\n[A2  B2]\n(t rows of)\n(A, B pair)', fg='white', command=lambda: changeButton(3
                                                                                                                                                  ), width=13, font='calibre', bd=3)
        self.button4 = Button(gui, justify=LEFT, text='T\nn  m  \n[A1 A2...An]\n[B1 B2...Bm]\n...  ...', fg='white', command=lambda: changeButton(4
                                                                                                                                                  ), width=13, font='calibre', bd=3)
        self.button5 = Button(gui, justify=LEFT, text='T\n[n  m  k]\n[n  m  k]\n(t rows of)\n(n m k  pair)', fg='white', command=lambda: changeButton(5
                                                                                                                                                      ), width=13, font='calibre', bd=3)
        self.button6 = Button(gui, justify=LEFT, text='n * m (matrix)\n[A1  A2...Am]\n[A1  A2...Am]\n__   __ ... __\n'
                              'A1  A2...Am', fg='white', command=lambda: changeButton(6), width=13, font='calibre', bd=3)
        self.button7 = Button(gui, justify=LEFT, text='T\nn\nCustom string\n(ex: 0 1)\n(ex: + / -)',
                              fg='white', command=lambda: changeButton(7), width=13, font='calibre', bd=3)
        self.button8 = Button(gui, justify=LEFT, text='T\nn  m\n[A1  B1]\n...   ...\n[Am  Bm]', fg='white', command=lambda: changeButton(8
                                                                                                                                         ), width=13, font='calibre', bd=3)
        self.button9 = Button(gui, justify=LEFT, text='T\nCustom string\n(without "n")\n(ex: 0 1)\n(ex: + / -)',
                              fg='white', command=lambda: changeButton(9), width=13, font='calibre', bd=3)
        self.button10 = Button(gui, justify=LEFT, text='T\nn  k  m\n[A1 A2...An]\nn  k  m\n[A1 A2...An]', fg='white', command=lambda: changeButton(
            10), width=13, font='calibre', bd=3)

        # Submit Button
        self.button_new_test_case = Button(gui, text=' ANOTHER TYPE ', fg='black',
                                           width=13, font='calibre', bd=3, command=lambda: self.newformat())
        self.button_feedback = Button(gui, text='FEEDBACK', fg='black', width=13,
                                      font='calibre', bd=3, command=lambda: self.feedback())
        self.button_exit = Button(gui, text=' EXIT ', fg='black', width=11, font='calibre',
                                  bd=3, command=lambda: gui.destroy())
        self.copyright_label = Button(gui, text='© Dude901', fg='white', width=7, height=1, bd=3, command=lambda:
                                      webbrowser.open_new_tab("https://github.com/Tanmay-901"), font=('calibre', 6, 'normal'))

        # scrollbar
        self.y_scroll = Scrollbar(gui)
        self.x_scroll = Scrollbar(gui, orient=HORIZONTAL)
        self.output = Text(gui, height=12, bg="light cyan", width=82, yscrollcommand=self.y_scroll.set,
                           xscrollcommand=self.x_scroll.set, wrap='none')
        self.copy_button = Button(
            gui, text='COPY', fg='black', width=18, command=self.cpy, font='calibre', bd=3)
        self.generate_button = Button(gui, text='RE-GENERATE', width=23, fg='black', command=lambda: whichGenerate(),
                                      font='calibre', bd=3)
        self.change_values_button = Button(
            gui, text='CHANGE CONSTRAINT', fg='black', command=lambda: whichInput(), width=20, font='calibre', bd=3)
        self.done_button = Button(gui, text='HOME', fg='black', command=lambda: self.done(self.output), width=20,
                                  font='calibre', bd=3)
        self.button_exit_output = Button(gui, text=' EXIT ', fg='black', width=20, font='calibre', bd=3,
                                         command=lambda: gui.destroy())

        # get_t
        self.test_case_count_label = Label(gui, text='T  = ', font=(
            'calibre', 10, 'bold'), width=17)  # Type 1
        self.test_case_count = Entry(
            gui, text=t, textvariable=t, font=('calibre', 10, 'normal'))

        # get_n
        self.minimum_value_of_n = Entry(
            gui, text=n_min, textvariable=n_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_n_label = Label(
            gui, text=' <= n <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_n = Entry(
            gui, text=n_max, textvariable=n_max, font=('calibre', 10, 'normal'))

        # get_m
        self.minimum_value_of_m = Entry(
            gui, text=m_min, textvariable=m_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_m_label = Label(
            gui, text='<= m <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_m = Entry(
            gui, text=m_max, textvariable=m_max, font=('calibre', 10, 'normal'))

        # get_k
        self.minimum_value_of_k = Entry(
            gui, text=k_min, textvariable=k_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_k_label = Label(
            gui, text=' <= k <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_k = Entry(
            gui, text=k_max, textvariable=k_max, font=('calibre', 10, 'normal'))

        # get_a
        self.minimum_value_of_ai = Entry(
            gui, text=a_min, textvariable=a_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_ai_label = Label(
            gui, text=' <= Ai <=', font=('calibre', 10, 'bold'))
        self.maximum_value_of_ai = Entry(
            gui, text=a_max, textvariable=a_max, font=('calibre', 10, 'normal'))

        # get_b
        self.minimum_value_of_bi = Entry(
            gui, text=b_min, textvariable=b_min, font=('calibre', 10, 'normal'))
        self.min_max_values_of_bi_label = Label(
            gui, text=' <= Bi <= ', font=('calibre', 10, 'bold'))
        self.maximum_value_of_bi = Entry(
            gui, text=b_max, textvariable=b_max, font=('calibre', 10, 'normal'))

        # get_char_list
        self.char_list_label = Label(
            gui, text='  Characters :  ', font=('calibre', 10, 'bold'), width=17)
        self.char_list = Entry(gui, textvariable=char_lis, font=(
            'calibre', 10, 'normal'), width=43)

        # show_button
        self.radio_type_space_separated = Radiobutton(gui, text='1 2 3 ... N', variable=radio_input, value=0,
                                                      font='calibre', bd=3)
        self.radio_type_comma_separated = Radiobutton(gui, text='[1,2,3,...,N]', variable=radio_input, value=1,
                                                      font='calibre', bd=3)
        self.back_btn = Button(gui, text=' HOME ', command=lambda: case.forget_testcase_take_input_screen(1),
                               font='calibre', bd=3)
        self.sub_btn = Button(gui, text=' GENERATE ',
                              command=self.submit, font='calibre', bd=3)
        self.exit_btn = Button(
            gui, text=' EXIT ', command=lambda: gui.destroy(), font='calibre', bd=3)

    def home(self):
        self.statement.configure(bg=mycolor)
        self.button1.configure(background='grey20')
        self.button2.configure(background='grey20')
        self.button3.configure(background='grey20')
        self.button4.configure(background='grey20')
        self.button5.configure(background='grey20')
        self.button6.configure(background='grey20')
        self.button7.configure(background='grey20')
        self.button8.configure(background='grey20')
        self.button9.configure(background='grey20')
        self.button10.configure(background='grey20')
        self.copyright_label.configure(bg=mycolor)
        self.retrieve_home()

    def newformat(self):
        url = "https://github.com/Tanmay-901/test-case-generator/issues/new?assignees=&labels=&" \
              "template=suggest-test-case.md&title=Suggest+Test+Case"
        webbrowser.open_new_tab(url)

    def feedback(self):
        url = "https://github.com/Tanmay-901/test-case-generator/issues/new/choose"
        webbrowser.open_new_tab(url)

    def forget_home(self):
        self.statement.place_forget()
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
        self.button_new_test_case.grid_forget()
        self.button_feedback.grid_forget()
        self.button_exit.grid_forget()

    def retrieve_home(self):
        self.statement.place(relx=0.39, rely=0.005)
        self.button1.grid(row=1, column=0, ipady=10, pady=27, padx=10)
        self.button2.grid(row=1, column=1, ipady=10, pady=27, padx=10)
        self.button3.grid(row=1, column=2, ipady=10, pady=27, padx=10)
        self.button4.grid(row=1, column=3, ipady=10, pady=27, padx=10)
        self.button5.grid(row=1, column=4, ipady=10, pady=27, padx=10)
        self.button6.grid(row=2, column=0, ipady=10, pady=13, padx=10)
        self.button7.grid(row=2, column=1, ipady=10, pady=13, padx=10)
        self.button8.grid(row=2, column=2, ipady=10, pady=13, padx=10)
        self.button9.grid(row=2, column=3, ipady=10, pady=13, padx=10)
        self.button10.grid(row=2, column=4, ipady=10, pady=13, padx=10)
        self.button_new_test_case.grid(
            row=3, column=1, ipady=10, pady=13, padx=10)
        self.button_feedback.grid(row=3, column=2, ipady=10, pady=13, padx=10)
        self.button_exit.grid(row=3, column=3, ipady=10, pady=13, padx=10)
        self.copyright_label.place(relx=0.92, rely=0.005)

    def cpy(self):
        txt = self.output.get('1.0', END)
        gui.clipboard_clear()
        gui.clipboard_append(txt.strip())

    def done(self, output):
        self.a = [0]
        case.try_forget()
        self.retrieve_home()
        pass

    def display(self):
        self.y_scroll.grid(row=0, column=11, sticky='NS',
                           pady=(22, 0), padx=(0, 20))
        self.x_scroll.grid(row=1, sticky='EW', columnspan=10,
                           padx=(20, 0), pady=(0, 30))
        self.output.grid(row=0, column=0, columnspan=10,
                         sticky='n', ipady=10, padx=(20, 0), pady=(22, 0))
        self.y_scroll.config(command=self.output.yview)
        self.x_scroll.config(command=self.output.xview)
        self.copy_button.grid(row=2, column=3, sticky='SW',
                              ipady=10, pady=(10, 18), padx=15)
        self.generate_button.grid(
            row=2, column=4, ipady=10, pady=(10, 18), padx=15)

        self.change_values_button.grid(
            row=2, column=5, ipady=10, pady=(10, 18), padx=5)
        self.done_button.grid(row=3, column=3, columnspan=2,
                              ipady=10, pady=(10, 20), padx=5)
        self.button_exit_output.grid(
            row=3, column=4, columnspan=2, ipady=10, pady=(10, 20), padx=5)

    def try_forget(self):
        self.output.grid_forget()
        self.copy_button.grid_forget()
        self.generate_button.grid_forget()
        self.change_values_button.grid_forget()
        self.done_button.grid_forget()
        self.y_scroll.grid_forget()
        self.x_scroll.grid_forget()
        self.button_exit_output.grid_forget()
        try:
            self.constraints.grid_forget()
        except AttributeError:
            pass

    def get_t(self, r):
        self.test_case_count_label.grid(
            row=r, column=0, pady=20, ipady=1)  # Type 1
        self.test_case_count.grid(row=r, column=1)

    def get_n(self, r):
        self.minimum_value_of_n.grid(row=r, column=0, padx=10, pady=10)
        self.min_max_values_of_n_label.grid(row=r, column=1, ipadx=5, ipady=1)
        self.maximum_value_of_n.grid(row=r, column=2, padx=(10, 10))

    def get_m(self, r):
        self.minimum_value_of_m.grid(row=r, column=0, padx=10, pady=10)
        self.min_max_values_of_m_label.grid(
            row=r, column=1, padx=10, ipadx=5, ipady=1)
        self.maximum_value_of_m.grid(row=r, column=2, padx=10)

    def get_k(self, r):
        self.minimum_value_of_k.grid(row=r, column=0, pady=10)
        self.min_max_values_of_k_label.grid(row=r, column=1)
        self.maximum_value_of_k.grid(row=r, column=2)

    def get_a(self, r):
        self.minimum_value_of_ai.grid(row=r, column=0, padx=10, pady=10)
        self.min_max_values_of_ai_label.grid(row=r, column=1, ipadx=2, ipady=1)
        self.maximum_value_of_ai.grid(row=r, column=2)

    def get_b(self, r):
        self.minimum_value_of_bi.grid(row=r, column=0, pady=10)
        self.min_max_values_of_bi_label.grid(row=r, column=1, padx=10)
        self.maximum_value_of_bi.grid(row=r, column=2, padx=10)

    def get_char_list(self, r):
        self.char_list.insert(END, '(Space separated characters)')
        self.char_list.bind(
            "<FocusIn>", lambda args: self.char_list.delete('0', 'end'))
        self.char_list_label.grid(row=r, column=0, pady=10)
        self.char_list.grid(row=r, column=1, columnspan=2, padx=10)

    def show_button(self, r):
        self.radio_type_space_separated.grid(row=r, column=0, pady=1, ipady=1)
        self.radio_type_comma_separated.grid(row=r, column=2, pady=1, ipady=1)
        self.back_btn.grid(row=r+1, column=0, pady=(20, 20), ipady=1)
        self.sub_btn.grid(row=r+1, column=1, pady=(20, 20), ipady=1)
        self.exit_btn.grid(row=r+1, column=2, pady=(20, 20), ipady=1)
        self.copyright_label.place(relx=0.9, y=0)

    def submit(self):
        try:
            self.t = min(int(self.test_case_count.get()), 1000)
            if self.t == 0:
                print("self.t == 0")
                return
        except ValueError:
            return
        except AttributeError:
            pass
        try:
            self.n_min = min(int(self.minimum_value_of_n.get()),
                             int(self.maximum_value_of_n.get()), 1000)
            self.n_max = min(max(int(self.minimum_value_of_n.get()), int(
                self.maximum_value_of_n.get())), 1000)
            if self.n_max == 0:
                print("self.n_max == 0")
                return
        except ValueError:
            return
        except AttributeError:
            pass
        try:
            self.m_min = min(int(self.minimum_value_of_m.get()),
                             int(self.maximum_value_of_m.get()), 1000)
            self.m_max = min(max(int(self.minimum_value_of_m.get()), int(
                self.maximum_value_of_m.get())), 1000)
            if self.m_max == 0:
                print("self.m_max == 0")
                return
        except ValueError:
            return
        except AttributeError:
            pass
        try:
            self.k_min = min(int(self.minimum_value_of_k.get()),
                             int(self.maximum_value_of_k.get()), 1000)
            self.k_max = min(max(int(self.minimum_value_of_k.get()), int(
                self.maximum_value_of_k.get())), 1000)
            if self.k_max == 0:
                print("self.k_max == 0")
                return
        except ValueError:
            return
        except AttributeError:
            pass
        try:
            self.a_min = min(int(self.minimum_value_of_ai.get()), int(
                self.maximum_value_of_ai.get()), 10000)
            self.a_max = min(max(int(self.minimum_value_of_ai.get()), int(
                self.maximum_value_of_ai.get())), 10000)
            if self.a_max == 0:
                print("self.a_max == 0")
                return
        except ValueError:
            return
        except AttributeError:
            pass
        try:
            self.b_min = min(int(self.minimum_value_of_bi.get()), int(
                self.maximum_value_of_bi.get()), 10000)
            self.b_max = min(max(int(self.minimum_value_of_bi.get()), int(
                self.maximum_value_of_bi.get())), 10000)
            if self.b_max == 0:
                print("self.b_max == 0")
                return
        except ValueError:
            return
        except AttributeError:
            pass
        try:
            self.char_lis = list(self.char_list.get().split())
            if self.char_lis[0] == '(Space':
                print("self.char_lis[0] == '(Space'")
                return
        except IndexError:
            return
        except ValueError:
            return
        except AttributeError:
            pass
        finally:
            case.forget_testcase_take_input_screen()
            self.display()
            whichGenerate()

    def forget_testcase_take_input_screen(self, check=0):
        try:
            self.test_case_count_label.grid_forget()
            self.test_case_count.grid_forget()
        except AttributeError:
            pass
        try:
            self.minimum_value_of_n.grid_forget()
            self.min_max_values_of_n_label.grid_forget()
            self.maximum_value_of_n.grid_forget()
        except AttributeError:
            pass
        try:
            self.minimum_value_of_ai.grid_forget()
            self.min_max_values_of_ai_label.grid_forget()
            self.maximum_value_of_ai.grid_forget()
        except AttributeError:
            pass
        try:
            self.minimum_value_of_bi.grid_forget()
            self.min_max_values_of_bi_label.grid_forget()
            self.maximum_value_of_bi.grid_forget()
        except AttributeError:
            pass
        try:
            self.minimum_value_of_m.grid_forget()
            self.min_max_values_of_m_label.grid_forget()
            self.maximum_value_of_m.grid_forget()
        except AttributeError:
            pass
        try:
            self.minimum_value_of_k.grid_forget()
            self.min_max_values_of_k_label.grid_forget()
            self.maximum_value_of_k.grid_forget()
        except AttributeError:
            pass
        try:
            self.char_list_label.grid_forget()
            self.char_list.delete('0', 'end')
            self.char_list.grid_forget()
        except AttributeError:
            pass
        try:
            self.constraints.grid_forget()
        except AttributeError:
            pass
        try:
            self.radio_type_space_separated.grid_forget()
            self.radio_type_comma_separated.grid_forget()
        except AttributeError:
            pass
        finally:
            self.sub_btn.grid_forget()
            self.back_btn.grid_forget()
            self.exit_btn.grid_forget()

        if check:
            self.retrieve_home()


class Type1():
    def __init__(self):
        butNum = 1
        # super(Type1, self).__init__(master)             # Type 1
        case.forget_home()
        self.take_input()

    def take_input(self):
        try:
            case.try_forget()                           # Type 1
        except AttributeError:
            pass
        case.get_t(0)
        case.get_n(1)
        case.get_a(2)
        case.show_button(3)

    def generate(self):                                         # Type 1
        case.forget_testcase_take_input_screen()
        self.output.delete('1.0', END)
        self.output.insert(END, self.t)
        self.output.insert(END, '\n')
        for i in range(self.t):
            self.n = randint(self.n_min, self.n_max)
            self.output.insert(END, self.n)
            self.output.insert(END, '\n')
            self.a = [0] * self.n
            for j in range(self.n):
                self.a[j] = str(randint(self.a_min, self.a_max))
            if radio_input.get() == 0:
                self.output.insert(END, self.a)
            elif radio_input.get() == 1:
                self.output.insert(END, "[")
                self.a = ", ".join(self.a)
                self.output.insert(END, self.a)
                self.output.insert(END, "]")
            self.output.insert(END, '\n')


class Type2():                                      # Type 2

    def __init__(self):
        butNum = 2
        # super(Type2, self).__init__(master)
        case.forget_home()
        self.take_input()

    def take_input(self):                              # Type 2
        try:
            case.try_forget()
        except AttributeError:
            pass
        case.get_t(0)
        case.get_n(1)
        case.get_m(2)
        case.get_a(3)
        case.show_button(4)

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
                self.a[j] = str(randint(self.a_min, self.a_max))     # Type 2
            if radio_input.get() == 0:
                self.output.insert(END, self.a)
            elif radio_input.get() == 1:
                self.output.insert(END, "[")
                self.a = ", ".join(self.a)
                self.output.insert(END, self.a)
                self.output.insert(END, "]")
            self.output.insert(END, '\n')


class Type3():                    # Type 3
    def __init__(self):
        butNum = 3
        # super(Type3, self).__init__(master)
        case.forget_home()
        self.take_input()

    def take_input(self):                   # Type 3
        try:
            case.try_forget()
        except AttributeError:
            pass
        case.get_t(0)
        case.get_a(1)
        case.get_b(2)
        case.show_button(3)

    def generate(self):                                              # Type 3
        self.output.delete('1.0', END)
        self.output.insert(END, self.t)
        self.output.insert(END, '\n')
        for i in range(self.t):
            self.a = str(randint(self.a_min, self.a_max))
            self.b = str(randint(self.b_min, self.b_max))
            if radio_input.get() == 0:
                self.output.insert(END, self.a)
                self.output.insert(END, ' ')
                self.output.insert(END, self.b)
            elif radio_input.get() == 1:
                self.output.insert(END, "[")
                self.output.insert(END, self.a)
                self.output.insert(END, ', ')
                self.output.insert(END, self.b)
                self.output.insert(END, "]")
            self.output.insert(END, '\n')


class Type4():                          # Type 4
    def __init__(self):
        butNum = 4
        # super(Type4, self).__init__(master)
        case.forget_home()
        self.take_input()

    def take_input(self):                                   # Type 4
        try:
            case.try_forget()
        except AttributeError:
            pass
        case.get_t(0)
        case.get_n(1)
        case.get_m(2)
        case.get_a(3)
        case.get_b(4)
        case.show_button(5)

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
            self.a = [0] * self.n                           # Type 4
            self.b = [0] * self.m

            for j in range(self.n):
                self.a[j] = str(randint(self.a_min, self.a_max))
            for j in range(self.m):
                self.b[j] = str(randint(self.b_min, self.b_max))
            if radio_input.get() == 0:
                self.output.insert(END, self.a)
                self.output.insert(END, '\n')
                self.output.insert(END, self.b)
                self.output.insert(END, '\n')
            elif radio_input.get() == 1:
                self.output.insert(END, "[")                   # Type 4
                self.a = ", ".join(self.a)
                self.output.insert(END, self.a)
                self.output.insert(END, "]")
                self.output.insert(END, '\n')
                self.output.insert(END, "[")
                self.b = ", ".join(self.b)
                self.output.insert(END, self.b)
                self.output.insert(END, "]")
                self.output.insert(END, '\n')


class Type5():

    def __init__(self):
        butNum = 5
        # super(Type5, self).__init__(master)
        case.forget_home()
        self.take_input()

    def take_input(self):                       # Type 5
        try:
            case.try_forget()
        except AttributeError:
            pass
        case.get_t(0)
        case.get_n(1)
        case.get_m(2)
        case.get_k(3)
        case.show_button(4)

    def generate(self):                             # Type 5
        self.output.delete('1.0', END)
        self.output.insert(END, self.t)
        self.output.insert(END, '\n')
        for i in range(self.t):
            self.n = randint(self.n_min, self.n_max)
            self.m = randint(self.m_min, self.m_max)
            self.k = randint(self.k_min, self.k_max)
            if radio_input.get() == 0:
                self.output.insert(END, self.n)
                self.output.insert(END, ' ')
                self.output.insert(END, self.m)
                self.output.insert(END, ' ')
                self.output.insert(END, self.k)
                self.output.insert(END, '\n')
            elif radio_input.get() == 1:              # Type 5
                self.output.insert(END, "[")
                self.output.insert(END, self.n)
                self.output.insert(END, ', ')
                self.output.insert(END, self.m)
                self.output.insert(END, ', ')
                self.output.insert(END, self.k)
                self.output.insert(END, "]")
                self.output.insert(END, '\n')


class Type6():

    def __init__(self):                     # Type 6
        butNum = 6
        # super(Type6, self).__init__(master)
        case.forget_home()
        self.take_input()

    def take_input(self):                           # Type 6
        try:
            case.try_forget()
        except AttributeError:
            pass                                # Type 6
        self.constraints = Label(gui, text='Enter Constraints',
                                 fg='white', height=1, font=('calibre', 12, 'normal'))
        self.constraints.configure(bg=mycolor)
        self.constraints.grid(row=0, column=1)
        case.get_n(1)
        case.get_m(2)
        case.get_a(3)
        case.show_button(4)

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
                self.a[j] = str(randint(self.a_min, self.a_max))
            if radio_input.get() == 0:                   # Type 6
                self.output.insert(END, self.a)
            elif radio_input.get() == 1:
                self.output.insert(END, "[")
                self.a = ", ".join(self.a)
                self.output.insert(END, self.a)
                self.output.insert(END, "]")
            self.output.insert(END, '\n')


class Type7():

    def __init__(self):                               # Type 7
        butNum = 7
        # super(Type7, self).__init__(master)
        case.forget_home()
        self.take_input()

    def take_input(self):                                     # Type 7
        try:
            case.try_forget()
        except AttributeError:
            pass
        case.get_t(0)
        case.get_char_list(1)
        case.get_n(2)
        case.show_button(3)
        case.radio_type_comma_separated.grid_forget()
        case.radio_type_space_separated.grid_forget()

    def generate(self):                                 # Type 7
        self.output.delete('1.0', END)
        self.output.insert(END, self.t)
        self.output.insert(END, '\n')
        for i in range(self.t):
            self.n = randint(self.n_min, self.n_max)
            self.output.insert(END, self.n)
            self.output.insert(END, '\n')
            self.a = choices(self.char_lis, k=self.n)
            self.a = ''.join(self.a)
            self.output.insert(END, self.a)
            self.output.insert(END, '\n')


class Type8(Case):

    def __init__(self):                             # Type 8
        butNum = 8
        # super(Type8, self).__init__(master)
        case.forget_home()
        self.take_input()

    def take_input(self):
        try:                                                # Type 8
            case.try_forget()
        except AttributeError:
            pass
        case.get_t(0)
        case.get_n(1)
        case.get_m(2)
        case.get_a(3)
        case.get_b(4)
        case.show_button(5)

    def generate(self):                                 # Type 8
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
                self.b = randint(self.b_min, self.b_max)     # Type 8
                if radio_input.get() == 0:
                    self.output.insert(END, self.a)
                    self.output.insert(END, ' ')
                    self.output.insert(END, self.b)
                    self.output.insert(END, '\n')
                elif radio_input.get() == 1:
                    self.output.insert(END, '[')
                    self.output.insert(END, self.a)
                    self.output.insert(END, ', ')
                    self.output.insert(END, self.b)
                    self.output.insert(END, ']')
                    self.output.insert(END, '\n')


class Type9(Case):
    def __init__(self):
        # super(Type9, self).__init__(master)
        butNum = 9
        case.forget_home()
        self.take_input()

    def take_input(self):                       # Type 9
        try:
            case.try_forget()
        except AttributeError:
            pass
        case.get_t(0)
        case.get_char_list(1)
        case.get_n(2)
        case.show_button(3)
        case.radio_type_comma_separated.grid_forget()
        case.radio_type_space_separated.grid_forget()

    def generate(self):                                         # Type 9
        self.output.delete('1.0', END)
        self.output.insert(END, self.t)
        self.output.insert(END, '\n')
        for i in range(self.t):
            self.n = randint(self.n_min, self.n_max)
            self.a = choices(self.char_lis, k=self.n)
            self.output.insert(END, ''.join(self.a))
            self.output.insert(END, '\n')


class Type10():

    def __init__(self):
        butNum = 10
        # super(Type10, self).__init__(master)
        case.forget_home()
        self.take_input()

    def take_input(self):                               # Type 10
        try:
            case.try_forget()
        except AttributeError:
            pass
        case.get_n(1)
        case.get_t(0)
        case.get_k(2)
        case.get_m(3)
        case.get_a(4)
        case.show_button(5)

    def generate(self):                             # Type 10
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
            self.output.insert(END, ' ')            # Type 10
            self.output.insert(END, self.m)
            self.output.insert(END, '\n')
            self.a = [0] * self.n
            for j in range(self.n):
                self.a[j] = str(randint(self.a_min, self.a_max))
            if radio_input.get() == 0:
                self.output.insert(END, self.a)
            if radio_input.get() == 1:
                self.a = ", ".join(self.a)
                self.output.insert(END, "[")
                self.output.insert(END, self.a)
                self.output.insert(END, "]")
            self.output.insert(END, '\n')


def whichInput():
    print(butNum)
    if(butNum == 1):
        Type1.take_input(case)
    elif(butNum == 2):
        Type2.take_input(case)
    elif(butNum == 3):
        Type3.take_input(case)
    elif(butNum == 4):
        Type4.take_input(case)
    elif(butNum == 5):
        Type5.take_input(case)
    elif(butNum == 6):
        Type6.take_input(case)
    elif(butNum == 7):
        Type7.take_input(case)
    elif(butNum == 8):
        Type8.take_input(case)
    elif(butNum == 9):
        Type9.take_input(case)
    elif(butNum == 10):
        Type10.take_input(case)
    return


def whichGenerate():
    print(butNum)
    if(butNum == 1):
        Type1.generate(case)
    elif(butNum == 2):
        Type2.generate(case)
    elif(butNum == 3):
        Type3.generate(case)
    elif(butNum == 4):
        Type4.generate(case)
    elif(butNum == 5):
        Type5.generate(case)
    elif(butNum == 6):
        Type6.generate(case)
    elif(butNum == 7):
        Type7.generate(case)
    elif(butNum == 8):
        Type8.generate(case)
    elif(butNum == 9):
        Type9.generate(case)
    elif(butNum == 10):
        Type10.generate(case)
    return


def changeButton(num):
    global butNum
    print(butNum)
    if(num == 1):
        butNum = 1
        Type1()
    elif(num == 2):
        butNum = 2
        Type2()
    elif(num == 3):
        butNum = 3
        Type3()
    elif(num == 4):
        butNum = 4
        Type4()
    elif(num == 5):
        butNum = 5
        Type5()
    elif(num == 6):
        butNum = 6
        Type6()
    elif(num == 7):
        butNum = 7
        Type7()
    elif(num == 8):
        butNum = 8
        Type8()
    elif(num == 9):
        butNum = 9
        Type9()
    elif(num == 10):
        butNum = 10
        Type10()
    return


# Buttons
butNum = 1  # default value

t = IntVar()
t.set(5)
n_min = IntVar()
n_min.set(1)
n_max = IntVar()
n_max.set(10)
m_min = IntVar()
m_min.set(1)
m_max = IntVar()
m_max.set(10)
k_min = IntVar()
k_min.set(1)
k_max = IntVar()
k_max.set(10)
a_min = IntVar()
a_min.set(0)
a_max = IntVar()
a_max.set(20)
b_min = IntVar()
b_min.set(0)
b_max = IntVar()
b_max.set(20)
char_lis = StringVar()
radio_input = IntVar()

case = Case(gui)
case.home()

gui.mainloop()

#  ------------------------------------------------- ###
#  ------------------------------------------------- ###
#  ### Developed by TANMAY KHANDELWAL (aka Dude901). ###
#                github.com/Tanmay-901               ###
#  _________________________________________________ ###
#  _________________________________________________ ###
