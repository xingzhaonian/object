# ！/user/bin/evn python 
# -*- conding: utf-8 -*-
# author: xingzhaonian
import tkinter
import tkinter.font
import math


class Calc():
    def __init__(self, window) -> None:
        self.window = window


    def set_init_but(self):

        self.window.title('计算器')
        self.window.geometry('685x500+1050+400')
        self.font = tkinter.font.Font(family="Helvetica", size=20, weight="bold")

        self.label_text = tkinter.StringVar()
        self.label_text.set('计 算 器')

        self.label = tkinter.Label(self.window, textvariable=self.label_text, font=self.font)
        self.label.place(x=280, y=5)

        self.but_text_1 = tkinter.StringVar()
        self.but_text_1.set('1')
        self.but_1 = tkinter.Button(self.window, textvariable=self.but_text_1, font=('SimHei', 15), width=8, height=2)
        self.but_1.place(x=5, y=381)


        self.but_text_2 = tkinter.StringVar()
        self.but_text_2.set('2')
        self.but_2 = tkinter.Button(self.window, textvariable=self.but_text_2, font=('SimHei', 15), width=8, height=2)
        self.but_2.place(x=110, y=381)
                    
        self.but_text_3 = tkinter.StringVar()
        self.but_text_3.set('3')
        self.but_3 = tkinter.Button(self.window, textvariable=self.but_text_3, font=('SimHei', 15), width=8, height=2)
        self.but_3.place(x=215, y=381)

        self.but_text_4 = tkinter.StringVar()
        self.but_text_4.set('4')
        self.but_4 = tkinter.Button(self.window, textvariable=self.but_text_4, font=('SimHei', 15), width=8, height=2)
        self.but_4.place(x=5, y=322)

        self.but_text_5 = tkinter.StringVar()
        self.but_text_5.set('5')
        self.but_5 = tkinter.Button(self.window, textvariable=self.but_text_5, font=('SimHei', 15), width=8, height=2)
        self.but_5.place(x=110, y=322)

        self.but_text_6 = tkinter.StringVar()
        self.but_text_6.set('6')
        self.but_6 = tkinter.Button(self.window, textvariable=self.but_text_6, font=('SimHei', 15), width=8, height=2)
        self.but_6.place(x=215, y=322)

        self.but_text_7 = tkinter.StringVar()
        self.but_text_7.set('7')
        self.but_7 = tkinter.Button(self.window, textvariable=self.but_text_7, font=('SimHei', 15), width=8, height=2)
        self.but_7.place(x=5, y=263)

        self.but_text_8 = tkinter.StringVar()
        self.but_text_8.set('8')
        self.but_8 = tkinter.Button(self.window, textvariable=self.but_text_8, font=('SimHei', 15), width=8, height=2)
        self.but_8.place(x=110, y=263)

        self.but_text_9 = tkinter.StringVar()
        self.but_text_9.set('9')
        self.but_9 = tkinter.Button(self.window, textvariable=self.but_text_9, font=('SimHei', 15), width=8, height=2)
        self.but_9.place(x=215, y=263)



        self.but_text_0 = tkinter.StringVar()
        self.but_text_0.set('0')
        self.but_text_0 = tkinter.Button(self.window, textvariable=self.but_text_0, font=('SimHei', 15), width=8, height=2)
        self.but_text_0.place(x=110, y=440)


        self.but_text_plus_minus = tkinter.StringVar()
        self.but_text_plus_minus.set('±')
        self.but_square = tkinter.Button(self.window, textvariable=self.but_text_plus_minus, font=('SimHei', 15), width=8, height=2)
        self.but_square.place(x=5, y=440)



        self.but_text_spot = tkinter.StringVar()
        self.but_text_spot.set('.')
        self.but_spot = tkinter.Button(self.window, textvariable=self.but_text_spot, font=('SimHei', 15), width=8, height=2)
        self.but_spot.place(x=215, y=440)


        self.but_text_plus = tkinter.StringVar()
        self.but_text_plus.set('+')
        self.but_plus = tkinter.Button(self.window, textvariable=self.but_text_plus, font=('SimHei', 15), width=8, height=2)
        self.but_plus.place(x=320, y=381)


        self.but_text_reduce = tkinter.StringVar()
        self.but_text_reduce.set('-')
        self.but_reduce = tkinter.Button(self.window, textvariable=self.but_text_reduce, font=('SimHei', 15), width=8, height=2)
        self.but_reduce.place(x=320, y=322)


        self.but_text_multiply = tkinter.StringVar()
        self.but_text_multiply.set('x')
        self.but_multiply = tkinter.Button(self.window, textvariable=self.but_text_multiply, font=('SimHei', 15), width=8, height=2)
        self.but_multiply.place(x=320, y=263)


        self.but_text_divide = tkinter.StringVar()
        self.but_text_divide.set('÷')
        self.but_divide = tkinter.Button(self.window, textvariable=self.but_text_divide, font=('SimHei', 15), width=8, height=2)
        self.but_divide.place(x=320, y=204)
        

        self.but_text_equal = tkinter.StringVar()
        self.but_text_equal.set('=')
        self.but_equal = tkinter.Button(self.window, textvariable=self.but_text_equal, font=('SimHei', 15), width=8, height=2)
        self.but_equal.place(x=320, y=440)


        self.but_text_reciprocal = tkinter.StringVar()
        self.but_text_reciprocal.set('1/x')
        self.but_reciprocal = tkinter.Button(self.window, textvariable=self.but_text_reciprocal, font=('SimHei', 15), width=8, height=2)
        self.but_reciprocal.place(x=5, y=204)



        self.but_text_square = tkinter.StringVar()
        self.but_text_square.set('x²')
        self.but_square = tkinter.Button(self.window, textvariable=self.but_text_square, font=('SimHei', 15), width=8, height=2)
        self.but_square.place(x=110, y=204)



        self.but_text_squareRoot = tkinter.StringVar()
        self.but_text_squareRoot.set('2√x')
        self.but_squareRoot = tkinter.Button(self.window, textvariable=self.but_text_squareRoot, font=('SimHei', 15), width=8, height=2)
        self.but_squareRoot.place(x=215, y=204)



        self.but_text_percentage = tkinter.StringVar()
        self.but_text_percentage.set('%')
        self.but_percentage = tkinter.Button(self.window, textvariable=self.but_text_percentage, font=('SimHei', 15), width=8, height=2)
        self.but_percentage.place(x=5, y=145)



        self.but_text_clearEntry = tkinter.StringVar()
        self.but_text_clearEntry.set('CE')
        self.but_clearEntry = tkinter.Button(self.window, textvariable=self.but_text_clearEntry, font=('SimHei', 15), width=8, height=2)
        self.but_clearEntry.place(x=110, y=145)



        self.but_text_clear = tkinter.StringVar()
        self.but_text_clear.set('C')
        self.but_clear = tkinter.Button(self.window, textvariable=self.but_text_clear, font=('SimHei', 15), width=8, height=2)
        self.but_clear.place(x=215, y=145)



        self.but_text_delSingle = tkinter.StringVar()
        self.but_text_delSingle.set('✘')
        self.but_delSingle = tkinter.Button(self.window, textvariable=self.but_text_delSingle, font=('SimHei', 15), width=8, height=2)
        self.but_delSingle.place(x=320, y=145)



def start_calc():
    window = tkinter.Tk()
    ZMJ_CALA = Calc(window)
    ZMJ_CALA.set_init_but()
    window.mainloop()

start_calc()
