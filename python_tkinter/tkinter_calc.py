# ！/user/bin/evn python 
# -*- conding: utf-8 -*-
# author: xingzhaonian
import tkinter
import tkinter.font
import math
import tkinter.scrolledtext
import simpleeval


class Calc():
    def __init__(self, window) -> None:
        self.window = window
        self.show_text = ''
        self.result = None
        self.spot_isclick = True
        self.plus_minusisclick = True
        self.plus_isclick = True
        self.reduce_isclick = True
        self.multiply_isclick = True
        self.divide_click = True
        self.percentage_click = True




    def set_init_but(self) -> None:

        self.window.title('计算器')
        self.window.geometry('685x500+1050+400')
        self.font = tkinter.font.Font(family="Helvetica", size=20, weight="bold")

        self.label_text = tkinter.StringVar()
        self.label_text.set('计 算 器')

        self.label = tkinter.Label(self.window, textvariable=self.label_text, font=self.font)
        self.label.place(x=280, y=5)

        self.but_text_1 = tkinter.StringVar()
        self.but_text_1.set('1')
        self.but_1 = tkinter.Button(self.window, textvariable=self.but_text_1, font=('SimHei', 15), width=8, height=2, command=self.but_1)
        self.but_1.place(x=5, y=381)


        self.but_text_2 = tkinter.StringVar()
        self.but_text_2.set('2')
        self.but_2 = tkinter.Button(self.window, textvariable=self.but_text_2, font=('SimHei', 15), width=8, height=2, command=self.but_2)
        self.but_2.place(x=110, y=381)
                    
        self.but_text_3 = tkinter.StringVar()
        self.but_text_3.set('3')
        self.but_3 = tkinter.Button(self.window, textvariable=self.but_text_3, font=('SimHei', 15), width=8, height=2, command=self.but_3)
        self.but_3.place(x=215, y=381)

        self.but_text_4 = tkinter.StringVar()
        self.but_text_4.set('4')
        self.but_4 = tkinter.Button(self.window, textvariable=self.but_text_4, font=('SimHei', 15), width=8, height=2, command=self.but_4)
        self.but_4.place(x=5, y=322)

        self.but_text_5 = tkinter.StringVar()
        self.but_text_5.set('5')
        self.but_5 = tkinter.Button(self.window, textvariable=self.but_text_5, font=('SimHei', 15), width=8, height=2, command=self.but_5)
        self.but_5.place(x=110, y=322)

        self.but_text_6 = tkinter.StringVar()
        self.but_text_6.set('6')
        self.but_6 = tkinter.Button(self.window, textvariable=self.but_text_6, font=('SimHei', 15), width=8, height=2, command=self.but_6)
        self.but_6.place(x=215, y=322)

        self.but_text_7 = tkinter.StringVar()
        self.but_text_7.set('7')
        self.but_7 = tkinter.Button(self.window, textvariable=self.but_text_7, font=('SimHei', 15), width=8, height=2, command=self.but_7)
        self.but_7.place(x=5, y=263)

        self.but_text_8 = tkinter.StringVar()
        self.but_text_8.set('8')
        self.but_8 = tkinter.Button(self.window, textvariable=self.but_text_8, font=('SimHei', 15), width=8, height=2, command=self.but_8)
        self.but_8.place(x=110, y=263)

        self.but_text_9 = tkinter.StringVar()
        self.but_text_9.set('9')
        self.but_9 = tkinter.Button(self.window, textvariable=self.but_text_9, font=('SimHei', 15), width=8, height=2, command=self.but_9)
        self.but_9.place(x=215, y=263)



        self.but_text_0 = tkinter.StringVar()
        self.but_text_0.set('0')
        self.but_text_0 = tkinter.Button(self.window, textvariable=self.but_text_0, font=('SimHei', 15), width=8, height=2, command=self.but_0)
        self.but_text_0.place(x=110, y=440)


        self.but_text_plus_minus = tkinter.StringVar()
        self.but_text_plus_minus.set('±')
        self.but_square = tkinter.Button(self.window, textvariable=self.but_text_plus_minus, font=('SimHei', 15), width=8, height=2, command=self.but_plus_minus)
        self.but_square.place(x=5, y=440)



        self.but_text_spot = tkinter.StringVar()
        self.but_text_spot.set('.')
        self.but_spot = tkinter.Button(self.window, textvariable=self.but_text_spot, font=('SimHei', 15), width=8, height=2, command=self.but_spot)
        self.but_spot.place(x=215, y=440)


        self.but_text_plus = tkinter.StringVar()
        self.but_text_plus.set('+')
        self.but_plus = tkinter.Button(self.window, textvariable=self.but_text_plus, font=('SimHei', 15), width=8, height=2, command=self.but_plus)
        self.but_plus.place(x=320, y=381)


        self.but_text_reduce = tkinter.StringVar()
        self.but_text_reduce.set('-')
        self.but_reduce = tkinter.Button(self.window, textvariable=self.but_text_reduce, font=('SimHei', 15), width=8, height=2,command=self.but_reduce)
        self.but_reduce.place(x=320, y=322)


        self.but_text_multiply = tkinter.StringVar()
        self.but_text_multiply.set('x')
        self.but_multiply = tkinter.Button(self.window, textvariable=self.but_text_multiply, font=('SimHei', 15), width=8, height=2, command=self.but_multiply)
        self.but_multiply.place(x=320, y=263)


        self.but_text_divide = tkinter.StringVar()
        self.but_text_divide.set('÷')
        self.but_divide = tkinter.Button(self.window, textvariable=self.but_text_divide, font=('SimHei', 15), width=8, height=2, command=self.but_divide)
        self.but_divide.place(x=320, y=204)
        

        self.but_text_equal = tkinter.StringVar()
        self.but_text_equal.set('=')
        self.but_equal = tkinter.Button(self.window, textvariable=self.but_text_equal, font=('SimHei', 15), width=8, height=2, command=self.but_equal)
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
        self.but_percentage = tkinter.Button(self.window, textvariable=self.but_text_percentage, font=('SimHei', 15), width=8, height=2, command=self.but_percentage)
        self.but_percentage.place(x=5, y=145)



        self.but_text_clearEntry = tkinter.StringVar()
        self.but_text_clearEntry.set('CE')
        self.but_clearEntry = tkinter.Button(self.window, textvariable=self.but_text_clearEntry, font=('SimHei', 15), width=8, height=2)
        self.but_clearEntry.place(x=110, y=145)



        self.but_text_clear = tkinter.StringVar()
        self.but_text_clear.set('C')
        self.but_clear = tkinter.Button(self.window, textvariable=self.but_text_clear, font=('SimHei', 15), width=8, height=2, command=self.but_clearShow_text)
        self.but_clear.place(x=215, y=145)



        self.but_text_delSingle = tkinter.StringVar()
        self.but_text_delSingle.set('✘')
        self.but_delSingle = tkinter.Button(self.window, textvariable=self.but_text_delSingle, font=('SimHei', 15), width=8, height=2, command=self.but_delSingle_num)
        self.but_delSingle.place(x=320, y=145)


        self.show_region_text = tkinter.StringVar()
        self.show_region = tkinter.Text(self.window, wrap=tkinter.WORD, width=40, height=3, font=('SimHei', 15))
        self.show_region.insert(tkinter.END, '\n'+'0', 'right')
        self.show_region.config(state=tkinter.DISABLED)
        self.show_region.tag_configure('right', justify='right')
        self.show_region.place(x=5, y=70)


        # 历史记录
        self.history_text = tkinter.scrolledtext.ScrolledText(self.window, wrap=tkinter.WORD,  width=22, height=17, font=('SimHei', 15))
        self.history_text.place(x=430, y=140)
        self.history_label = tkinter.Label(self.window, text='历史记录',  font=('SimHei', 15), width=30, height=3)
        self.history_label.place(x=410, y=80)


    def can_click(self):
        self.plus_minusisclick = True
        self.plus_isclick = True
        self.reduce_isclick = True
        self.multiply_isclick = True
        self.divide_click = True
        self.percentage_click = True


    def nocan_click(self):
        self.plus_minusisclick = False
        self.plus_isclick = False
        self.reduce_isclick = False
        self.multiply_isclick = False
        self.divide_click = False    





    def but_1(self):
        self.but_1_text = '1'
        self.show_text += self.but_1_text
        self.show_region.config(state=tkinter.NORMAL)   # 启用编辑模式
        self.show_region.delete(1.0, tkinter.END)
        self.show_region.insert(tkinter.END, '\n' + self.show_text, 'right')
        self.show_region.config(state=tkinter.DISABLED)    # 禁用编辑模式
        self.can_click()

    def but_2(self):
        self.but_2_text = '2'
        self.show_text += self.but_2_text
        self.show_region.config(state=tkinter.NORMAL)   # 启用编辑模式
        self.show_region.delete(1.0, tkinter.END)
        self.show_region.insert(tkinter.END, '\n' + self.show_text, 'right')
        self.show_region.config(state=tkinter.DISABLED)    # 禁用编辑模式
        self.can_click()


    def but_3(self):
        self.but_3_text = '3'
        self.show_text += self.but_3_text
        self.show_region.config(state=tkinter.NORMAL)   # 启用编辑模式
        self.show_region.delete(1.0, tkinter.END)
        self.show_region.insert(tkinter.END, '\n' + self.show_text, 'right')
        self.show_region.config(state=tkinter.DISABLED)    # 禁用编辑模式
        self.can_click()

    def but_4(self):
        self.but_4_text = '4'
        self.show_text += self.but_4_text
        self.show_region.config(state=tkinter.NORMAL)   # 启用编辑模式
        self.show_region.delete(1.0, tkinter.END)
        self.show_region.insert(tkinter.END, '\n' + self.show_text, 'right')
        self.show_region.config(state=tkinter.DISABLED)    # 禁用编辑模式
        self.can_click()


    def but_5(self):
        self.but_5_text = '5'
        self.show_text += self.but_5_text
        self.show_region.config(state=tkinter.NORMAL)   # 启用编辑模式
        self.show_region.delete(1.0, tkinter.END)
        self.show_region.insert(tkinter.END, '\n' + self.show_text, 'right')
        self.show_region.config(state=tkinter.DISABLED)    # 禁用编辑模式
        self.can_click()


    def but_6(self):
        self.but_6_text = '6'
        self.show_text += self.but_6_text
        self.show_region.config(state=tkinter.NORMAL)   # 启用编辑模式
        self.show_region.delete(1.0, tkinter.END)
        self.show_region.insert(tkinter.END, '\n' + self.show_text, 'right')
        self.show_region.config(state=tkinter.DISABLED)    # 禁用编辑模式
        self.can_click()


    def but_7(self):
        self.but_7_text = '7'
        self.show_text += self.but_7_text
        self.show_region.config(state=tkinter.NORMAL)   # 启用编辑模式
        self.show_region.delete(1.0, tkinter.END)
        self.show_region.insert(tkinter.END, '\n' + self.show_text, 'right')
        self.show_region.config(state=tkinter.DISABLED)    # 禁用编辑模式
        self.can_click()


    def but_8(self):
        self.but_8_text = '8'
        self.show_text += self.but_8_text
        self.show_region.config(state=tkinter.NORMAL)   # 启用编辑模式
        self.show_region.delete(1.0, tkinter.END)
        self.show_region.insert(tkinter.END, '\n' + self.show_text, 'right')
        self.show_region.config(state=tkinter.DISABLED)    # 禁用编辑模式
        self.can_click()



    def but_9(self):
        self.but_9_text = '9'
        self.show_text += self.but_9_text
        self.show_region.config(state=tkinter.NORMAL)   # 启用编辑模式
        self.show_region.delete(1.0, tkinter.END)
        self.show_region.insert(tkinter.END, '\n' + self.show_text, 'right')
        self.show_region.config(state=tkinter.DISABLED)    # 禁用编辑模式
        self.can_click()


    def but_0(self):
        self.but_0_text = '0'
        self.show_text += self.but_0_text
        self.show_region.config(state=tkinter.NORMAL)   # 启用编辑模式
        self.show_region.delete(1.0, tkinter.END)
        self.show_region.insert(tkinter.END, '\n' + self.show_text, 'right')
        self.show_region.config(state=tkinter.DISABLED)    # 禁用编辑模式
        self.can_click()



    def but_spot(self):
        self.but_spot_text = '.'
        if self.spot_isclick:
            #if '+' not in self.show_text and '-' not in self.show_text and '*' not in self.show_text and '/' not in self.show_text:
             #   pass
            #else:
            self.show_text += self.but_spot_text
            self.show_region.config(state=tkinter.NORMAL)   # 启用编辑模式
            self.show_region.delete(1.0, tkinter.END)
            self.show_region.insert(tkinter.END, '\n' + self.show_text, 'right')
            self.show_region.config(state=tkinter.DISABLED)    # 禁用编辑模式
            self.spot_isclick = False
            self.percentage_click = True

                
        

    def but_equal(self):
        try:
            self.result = eval(self.show_text)
        except ZeroDivisionError:
            self.history_text.config(state=tkinter.NORMAL)  # 历史记录启用编辑模式
            self.history_text.insert(tkinter.END, '\n' + self.show_text + '=' + str(self.result) + '除数不能为0' + '\n')
            self.history_text.config(state=tkinter.DISABLED)   # 历史记录启用禁用模式

            self.show_region.config(state=tkinter.NORMAL)   # 启用编辑模式
            self.show_region.delete(1.0, tkinter.END)
            self.show_region.insert(tkinter.END, '\n' +'除数不能为0', 'right')
            self.show_region.config(state=tkinter.DISABLED)    # 禁用编辑模式
            self.show_text = ''
        else:
            self.show_region.config(state=tkinter.NORMAL)   # 启用编辑模式
            self.show_region.delete(1.0, tkinter.END)
            self.show_region.insert(tkinter.END, '\n' + str(self.result), 'right')
            self.show_region.config(state=tkinter.DISABLED)    # 禁用编辑模式       
            self.history_text.config(state=tkinter.NORMAL)  # 历史记录启用编辑模式
            self.history_text.insert(tkinter.END, '\n' + self.show_text + '=' + str(self.result) + '\n')
            self.history_text.config(state=tkinter.DISABLED)   # 历史记录启用禁用模式
            self.show_text = str(self.result)


    def but_plus(self):
        if self.plus_isclick:
            self.but_plus_text = '+'
            self.show_text += self.but_plus_text
            self.show_region.config(state=tkinter.NORMAL)   # 启用编辑模式
            self.show_region.delete(1.0, tkinter.END)
            self.show_region.insert(tkinter.END, '\n' + self.show_text, 'right')
            self.show_region.config(state=tkinter.DISABLED)    # 禁用编辑模式
            self.nocan_click()
            self.spot_isclick = True
            self.percentage_click = True



    def but_reduce(self):
        if self.reduce_isclick:
            self.but_reduce_text = '-'
            self.show_text += self.but_reduce_text
            self.show_region.config(state=tkinter.NORMAL)   # 启用编辑模式
            self.show_region.delete(1.0, tkinter.END)
            self.show_region.insert(tkinter.END, '\n' + self.show_text, 'right')
            self.show_region.config(state=tkinter.DISABLED)    # 禁用编辑模式
            self.nocan_click()
            self.spot_isclick = True
            self.percentage_click = True



    def but_multiply(self):
        if self.multiply_isclick:
            self.but_multiply_text = '*'
            self.show_text += self.but_multiply_text
            self.show_region.config(state=tkinter.NORMAL)   # 启用编辑模式
            self.show_region.delete(1.0, tkinter.END)
            self.show_region.insert(tkinter.END, '\n' + self.show_text, 'right')
            self.show_region.config(state=tkinter.DISABLED)    # 禁用编辑模式
            self.nocan_click()
            self.spot_isclick = True
            self.percentage_click = True


    def but_divide(self):
        if self.divide_click:
            self.but_divide_text = '/'
            self.show_text += self.but_divide_text
            self.show_region.config(state=tkinter.NORMAL)   # 启用编辑模式
            self.show_region.delete(1.0, tkinter.END)
            self.show_region.insert(tkinter.END, '\n' + self.show_text, 'right')
            self.show_region.config(state=tkinter.DISABLED)    # 禁用编辑模式
            self.nocan_click()
            self.spot_isclick = True
            self.percentage_click = True
        
    def but_clearShow_text(self):
        self.show_text = ''
        self.show_region.config(state=tkinter.NORMAL)    # 启用编辑模式

        self.show_region.delete(1.0, tkinter.END)
        self.show_region.insert(tkinter.END, '\n'+'0', 'right')

        self.show_region.config(state=tkinter.DISABLED)# 禁用编辑模式
        self.can_click()

    def but_delSingle_num(self):
        self.can_click()
        if self.show_text:
            self.show_text = self.show_text[:-1]
            self.show_region.config(state=tkinter.NORMAL)# 启用编辑模式
            self.show_region.delete(1.0, tkinter.END)
            self.show_region.insert(tkinter.END, '\n' + self.show_text, 'right')
            self.show_region.config(state=tkinter.DISABLED)# 禁用编辑模式
            if not self.show_text:
                self.show_region.config(state=tkinter.NORMAL) # 启用编辑模式
                self.show_region.delete(1.0, tkinter.END)
                self.show_region.insert(tkinter.END, '\n' + '0', 'right')
                self.show_region.config(state=tkinter.DISABLED)    # 禁用编辑模式    


    def but_plus_minus(self):
        self.plus_minus = '-'
        if self.plus_minusisclick:
            if self.show_text:
                if '+' not in self.show_text and '-' not in self.show_text and '*' not in self.show_text and '/' not in self.show_text:
                    self.show_text = self.plus_minus + self.show_text
                    self.show_region.config(state=tkinter.NORMAL)# 启用编辑模式
                    self.show_region.delete(1.0, tkinter.END)
                    self.show_region.insert(tkinter.END, '\n' + self.show_text, 'right')
                    self.show_region.config(state=tkinter.DISABLED)    # 禁用编辑模式  
                else: 
                    self.show_text = self.show_text + self.plus_minus
                    self.show_region.config(state=tkinter.NORMAL)# 启用编辑模式
                    self.show_region.delete(1.0, tkinter.END)
                    self.show_region.insert(tkinter.END, '\n' + self.show_text, 'right')
                    self.show_region.config(state=tkinter.DISABLED)    # 禁用编辑模式   



    def but_percentage(self):   # 百分比
        self.percentage_text = '%'
        if self.percentage_click:
            if self.show_text:
                self.show_text += self.percentage_text
                self.show_region.config(state=tkinter.NORMAL)# 启用编辑模式
                self.show_region.delete(1.0, tkinter.END)
                self.show_region.insert(tkinter.END, '\n' + self.show_text, 'right')
                self.show_region.config(state=tkinter.DISABLED)    # 禁用编辑模式   
                self.percentage_click = False






def start_calc():
    window = tkinter.Tk()
    ZMJ_CALA = Calc(window)
    ZMJ_CALA.set_init_but()
    window.mainloop()

start_calc()
