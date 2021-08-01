# -*- coding: utf-8 -*-


from remi.gui import *
import threading
from remi import start, App
import time
import webbrowser
import shengcheng_biao
import os
from os import walk
import zhuan_pdf
import zhuan_tu_1
import remi.gui as gui

class untitled(App):
    def __init__(self, *args):
        super(untitled, self).__init__(*args)

    def idle(self):
        # idle function called every update cycle
        pass

    def main(self):
        return untitled.construct_ui(self)

    @staticmethod
    def construct_ui(self):
        # DON'T MAKE CHANGES HERE, THIS METHOD GETS OVERWRITTEN WHEN SAVING IN THE EDITOR
        container0 = Container()
        container0.attr_class = "Container"
        container0.attr_editor_newclass = False
        container0.css_height = "150%"
        container0.css_left = "0.0px"
        container0.css_position = "absolute"
        container0.css_top = "0%"
        container0.css_width = "100%"
        container0.variable_name = "container0"
        label0 = Label()
        label0.attr_class = "Label"
        label0.attr_editor_newclass = False
        label0.css_height = "30px"
        label0.css_left = "20px"
        label0.css_position = "absolute"
        label0.css_top = "20px"
        label0.css_width = "100px"
        label0.text = "50C="
        label0.variable_name = "label0"
        container0.append(label0, 'label0')
        label1 = Label()
        label1.attr_class = "Label"
        label1.attr_editor_newclass = False
        label1.css_height = "30px"
        label1.css_left = "435.0px"
        label1.css_position = "absolute"
        label1.css_top = "60.0px"
        label1.css_width = "100px"
        label1.text = "称重根数"
        label1.variable_name = "label1"
        container0.append(label1, 'label1')
        textinput0 = TextInput()
        textinput0.attr_class = "TextInput"
        textinput0.attr_editor_newclass = False
        textinput0.attr_maxlength = "100"
        textinput0.css_height = "30.0px"
        textinput0.css_left = "60.0px"
        textinput0.css_position = "absolute"
        textinput0.css_top = "15.0px"
        textinput0.css_width = "210.0px"
        textinput0.text = ""
        textinput0.variable_name = "textinput0"
        self.textinput0=textinput0
        container0.append(textinput0, 'textinput0')
        container0.children['textinput0'].onchange.do(self.onchange_textinput0)
        textinput27 = TextInput()
        textinput27.attr_class = "TextInput"
        textinput27.attr_editor_newclass = False
        textinput27.attr_maxlength = "100"
        textinput27.css_height = "30.0px"
        textinput27.css_left = "75.0px"
        textinput27.css_position = "absolute"
        textinput27.css_top = "60.0px"
        textinput27.css_width = "315.0px"
        textinput27.text = ""
        self.textinput27=textinput27
        textinput27.variable_name = "textinput27"
        container0.append(textinput27, 'textinput27')
        container0.children['textinput27'].onchange.do(self.onchange_textinput27)
        label2 = Label()
        label2.attr_class = "Label"
        label2.attr_editor_newclass = False
        label2.css_height = "30px"
        label2.css_left = "180.0px"
        label2.css_position = "absolute"
        label2.css_top = "150.0px"
        label2.css_width = "100px"
        label2.text = "纱支数"
        label2.variable_name = "label2"
        container0.append(label2, 'label2')
        label3 = Label()
        label3.attr_class = "Label"
        label3.attr_editor_newclass = False
        label3.css_height = "30px"
        label3.css_left = "15.0px"
        label3.css_position = "absolute"
        label3.css_top = "105.0px"
        label3.css_width = "100px"
        label3.text = "重量"
        label3.variable_name = "label3"
        container0.append(label3, 'label3')
        textinput2 = TextInput()
        textinput2.attr_class = "TextInput"
        textinput2.attr_editor_newclass = False
        textinput2.attr_maxlength = "100"
        textinput2.css_height = "30.0px"
        textinput2.css_left = "60.0px"
        textinput2.css_position = "absolute"
        textinput2.css_top = "105.0px"
        textinput2.css_width = "210.0px"
        textinput2.text = ""
        self.textinput2=textinput2
        textinput2.variable_name = "textinput2"
        container0.append(textinput2, 'textinput2')
        container0.children['textinput2'].onchange.do(self.onchange_textinput2)
        textinput3 = TextInput()
        textinput3.attr_class = "TextInput"
        textinput3.attr_editor_newclass = False
        textinput3.attr_maxlength = "100"
        textinput3.css_height = "30px"
        textinput3.css_left = "60.0px"
        textinput3.css_position = "absolute"
        textinput3.css_top = "150.0px"
        textinput3.css_width = "100px"
        textinput3.text = ""
        textinput3.variable_name = "textinput3"
        container0.append(textinput3, 'textinput3')
        label5 = Label()
        label5.attr_class = "Label"
        label5.attr_editor_newclass = False
        label5.css_height = "30px"
        label5.css_left = "315.0px"
        label5.css_position = "absolute"
        label5.css_top = "105.0px"
        label5.css_width = "100px"
        label5.text = ""
        label5.variable_name = "label5"
        container0.append(label5, 'label5')
        label7 = Label()
        label7.attr_class = "Label"
        label7.attr_editor_newclass = False
        label7.css_height = "30px"
        label7.css_left = "15.0px"
        label7.css_position = "absolute"
        label7.css_top = "60.0px"
        label7.css_width = "100px"
        label7.text = "对应长度"
        label7.variable_name = "label7"
        container0.append(label7, 'label7')
        textinput1 = TextInput()
        textinput1.attr_class = "TextInput"
        textinput1.attr_editor_newclass = False
        textinput1.attr_maxlength = "100"
        textinput1.css_height = "30.0px"
        textinput1.css_left = "75.0px"
        textinput1.css_position = "absolute"
        textinput1.css_top = "195.0px"
        textinput1.css_width = "90.0px"
        textinput1.text = ""
        textinput1.variable_name = "textinput1"
        container0.append(textinput1, 'textinput1')
        label8 = Label()
        label8.attr_class = "Label"
        label8.attr_editor_newclass = False
        label8.css_height = "30px"
        label8.css_left = "405.0px"
        label8.css_position = "absolute"
        label8.css_top = "60.0px"
        label8.css_width = "100px"
        label8.text = "CM"
        label8.variable_name = "label8"
        container0.append(label8, 'label8')
        label14 = Label()
        label14.attr_class = "Label"
        label14.attr_editor_newclass = False
        label14.css_height = "30.0px"
        label14.css_left = "15.0px"
        label14.css_position = "absolute"
        label14.css_top = "150.0px"
        label14.css_width = "75.0px"
        label14.text = "WPI"
        label14.variable_name = "label14"
        container0.append(label14, 'label14')
        label15 = Label()
        label15.attr_class = "Label"
        label15.attr_editor_newclass = False
        label15.css_height = "30.0px"
        label15.css_left = "390.0px"
        label15.css_position = "absolute"
        label15.css_top = "150.0px"
        label15.css_width = "30.0px"
        label15.text = "机号"
        label15.variable_name = "label15"
        container0.append(label15, 'label15')
        textinput9 = TextInput()
        textinput9.attr_class = "TextInput"
        textinput9.attr_editor_newclass = False
        textinput9.attr_maxlength = "100"
        textinput9.css_height = "30px"
        textinput9.css_left = "435.0px"
        textinput9.css_position = "absolute"
        textinput9.css_top = "150.0px"
        textinput9.css_width = "100px"
        textinput9.text = ""
        textinput9.variable_name = "textinput9"
        self.textinput9=textinput9
        container0.append(textinput9, 'textinput9')
        container0.children['textinput9'].onchange.do(self.onchange_textinput9)
        label16 = Label()
        label16.attr_class = "Label"
        label16.attr_editor_newclass = False
        label16.css_height = "30.0px"
        label16.css_left = "15.0px"
        label16.css_position = "absolute"
        label16.css_top = "195.0px"
        label16.css_width = "60.0px"
        label16.text = "半径"
        label16.variable_name = "label16"
        container0.append(label16, 'label16')
        textinput4 = TextInput()
        textinput4.attr_class = "TextInput"
        textinput4.attr_editor_newclass = False
        textinput4.attr_maxlength = "100"
        textinput4.css_height = "30px"
        textinput4.css_left = "495.0px"
        textinput4.css_position = "absolute"
        textinput4.css_top = "60.0px"
        textinput4.css_width = "100px"
        textinput4.text = "10"
        textinput4.variable_name = "textinput4"
        self.textinput4=textinput4
        container0.append(textinput4, 'textinput4')
        container0.children['textinput4'].onchange.do(self.onchange_textinput4)
        label9 = Label()
        label9.attr_class = "Label"
        label9.attr_editor_newclass = False
        label9.css_height = "30px"
        label9.css_left = "270.0px"
        label9.css_position = "absolute"
        label9.css_top = "105.0px"
        label9.css_width = "100px"
        label9.text = "gm"
        label9.variable_name = "label9"
        container0.append(label9, 'label9')
        label10 = Label()
        label10.attr_class = "Label"
        label10.attr_editor_newclass = False
        label10.css_height = "30px"
        label10.css_left = "300.0px"
        label10.css_position = "absolute"
        label10.css_top = "105.0px"
        label10.css_width = "100px"
        label10.text = "公式"
        label10.variable_name = "label10"
        container0.append(label10, 'label10')
        textinput5 = TextInput()
        textinput5.attr_class = "TextInput"
        textinput5.attr_editor_newclass = False
        textinput5.attr_maxlength = "100"
        textinput5.css_height = "45.0px"
        textinput5.css_left = "90.0px"
        textinput5.css_position = "absolute"
        textinput5.css_top = "240.0px"
        textinput5.css_width = "165.0px"
        textinput5.text = "机号*半径*3.14159"
        textinput5.variable_name = "textinput5"
        container0.append(textinput5, 'textinput5')
        label11 = Label()
        label11.attr_class = "Label"
        label11.attr_editor_newclass = False
        label11.css_height = "30px"
        label11.css_left = "15.0px"
        label11.css_position = "absolute"
        label11.css_top = "240.0px"
        label11.css_width = "100px"
        label11.text = "公式"
        label11.variable_name = "label11"
        container0.append(label11, 'label11')
        label12 = Label()
        label12.attr_class = "Label"
        label12.attr_editor_newclass = False
        label12.css_height = "30px"
        label12.css_left = "270.0px"
        label12.css_position = "absolute"
        label12.css_top = "240.0px"
        label12.css_width = "100px"
        label12.text = "总针数"
        label12.variable_name = "label12"
        container0.append(label12, 'label12')
        textinput7 = TextInput()
        textinput7.attr_class = "TextInput"
        textinput7.attr_editor_newclass = False
        textinput7.attr_maxlength = "100"
        textinput7.css_height = "30px"
        textinput7.css_left = "360.0px"
        textinput7.css_position = "absolute"
        textinput7.css_top = "240.0px"
        textinput7.css_width = "100px"
        textinput7.text = ""
        textinput7.variable_name = "textinput7"
        container0.append(textinput7, 'textinput7')
        textinput11 = TextInput()
        textinput11.attr_class = "TextInput"
        textinput11.attr_editor_newclass = False
        textinput11.attr_maxlength = "100"
        textinput11.css_height = "30px"
        textinput11.css_left = "540.0px"
        textinput11.css_position = "absolute"
        textinput11.css_top = "240.0px"
        textinput11.css_width = "100px"
        textinput11.text = ""
        textinput11.variable_name = "textinput11"
        container0.append(textinput11, 'textinput11')
        label13 = Label()
        label13.attr_class = "Label"
        label13.attr_editor_newclass = False
        label13.css_height = "30px"
        label13.css_left = "495.0px"
        label13.css_position = "absolute"
        label13.css_top = "240.0px"
        label13.css_width = "100px"
        label13.text = "12倍"
        label13.variable_name = "label13"
        container0.append(label13, 'label13')
        label17 = Label()
        label17.attr_class = "Label"
        label17.attr_editor_newclass = False
        label17.css_height = "30px"
        label17.css_left = "15.0px"
        label17.css_position = "absolute"
        label17.css_top = "300.0px"
        label17.css_width = "100px"
        label17.text = "门幅"
        label17.variable_name = "label17"
        container0.append(label17, 'label17')
        textinput12 = TextInput()
        textinput12.attr_class = "TextInput"
        textinput12.attr_editor_newclass = False
        textinput12.attr_maxlength = "100"
        textinput12.css_height = "30px"
        textinput12.css_left = "75.0px"
        textinput12.css_position = "absolute"
        textinput12.css_top = "300.0px"
        textinput12.css_width = "100px"
        textinput12.text = "总针数/wpi"
        textinput12.variable_name = "textinput12"
        container0.append(textinput12, 'textinput12')
        textinput13 = TextInput()
        textinput13.attr_class = "TextInput"
        textinput13.attr_editor_newclass = False
        textinput13.attr_maxlength = "100"
        textinput13.css_height = "30px"
        textinput13.css_left = "180.0px"
        textinput13.css_position = "absolute"
        textinput13.css_top = "300.0px"
        textinput13.css_width = "100px"
        textinput13.text = ""
        textinput13.variable_name = "textinput13"
        container0.append(textinput13, 'textinput13')
        label18 = Label()
        label18.attr_class = "Label"
        label18.attr_editor_newclass = False
        label18.css_height = "30px"
        label18.css_left = "285.0px"
        label18.css_position = "absolute"
        label18.css_top = "300.0px"
        label18.css_width = "100px"
        label18.text = "取整"
        label18.variable_name = "label18"
        container0.append(label18, 'label18')
        textinput14 = TextInput()
        textinput14.attr_class = "TextInput"
        textinput14.attr_editor_newclass = False
        textinput14.attr_maxlength = "100"
        textinput14.css_height = "30px"
        textinput14.css_left = "345.0px"
        textinput14.css_position = "absolute"
        textinput14.css_top = "300.0px"
        textinput14.css_width = "100px"
        textinput14.text = ""
        textinput14.variable_name = "textinput14"
        self.textinput14=textinput14
        container0.append(textinput14, 'textinput14')
        container0.children['textinput14'].onchange.do(self.onchange_textinput14)
        container1 = Container()
        container1.attr_class = "Container"
        container1.attr_editor_newclass = False
        container1.css_height = "225.0px"
        container1.css_left = "45.0px"
        container1.css_position = "absolute"
        container1.css_top = "330.0px"
        container1.css_width = "555.0px"
        container1.variable_name = "container1"
        label19 = Label()
        label19.attr_class = "Label"
        label19.attr_editor_newclass = False
        label19.css_height = "30px"
        label19.css_left = "20px"
        label19.css_position = "absolute"
        label19.css_top = "20px"
        label19.css_width = "100px"
        label19.text = "长"
        label19.variable_name = "label19"
        container1.append(label19, 'label19')
        textinput15 = TextInput()
        textinput15.attr_class = "TextInput"
        textinput15.attr_editor_newclass = False
        textinput15.attr_maxlength = "100"
        textinput15.css_height = "30px"
        textinput15.css_left = "75.0px"
        textinput15.css_position = "absolute"
        textinput15.css_top = "15.0px"
        textinput15.css_width = "100px"
        textinput15.text = ""
        textinput15.variable_name = "textinput15"
        self.textinput15=textinput15
        container1.append(textinput15, 'textinput15')
        container1.children['textinput15'].onchange.do(self.onchange_textinput15)
        label20 = Label()
        label20.attr_class = "Label"
        label20.attr_editor_newclass = False
        label20.css_height = "30px"
        label20.css_left = "15.0px"
        label20.css_position = "absolute"
        label20.css_top = "60.0px"
        label20.css_width = "100px"
        label20.text = "宽"
        label20.variable_name = "label20"
        container1.append(label20, 'label20')
        textinput16 = TextInput()
        textinput16.attr_class = "TextInput"
        textinput16.attr_editor_newclass = False
        textinput16.attr_maxlength = "100"
        textinput16.css_height = "30px"
        textinput16.css_left = "75.0px"
        textinput16.css_position = "absolute"
        textinput16.css_top = "60.0px"
        textinput16.css_width = "100px"
        textinput16.text = ""
        textinput16.variable_name = "textinput16"
        self.textinput16=textinput16
        container1.append(textinput16, 'textinput16')
        container1.children['textinput16'].onchange.do(self.onchange_textinput16)
        label21 = Label()
        label21.attr_class = "Label"
        label21.attr_editor_newclass = False
        label21.css_height = "30px"
        label21.css_left = "15.0px"
        label21.css_position = "absolute"
        label21.css_top = "105.0px"
        label21.css_width = "100px"
        label21.text = "重量"
        label21.variable_name = "label21"
        container1.append(label21, 'label21')
        textinput17 = TextInput()
        textinput17.attr_class = "TextInput"
        textinput17.attr_editor_newclass = False
        textinput17.attr_maxlength = "100"
        textinput17.css_height = "30px"
        textinput17.css_left = "90.0px"
        textinput17.css_position = "absolute"
        textinput17.css_top = "105.0px"
        textinput17.css_width = "100px"
        textinput17.text = ""
        self.textinput17=textinput17
        textinput17.variable_name = "textinput17"
        container1.append(textinput17, 'textinput17')
        container1.children['textinput17'].onchange.do(self.onchange_textinput17)
        label22 = Label()
        label22.attr_class = "Label"
        label22.attr_editor_newclass = False
        label22.css_height = "30px"
        label22.css_left = "195.0px"
        label22.css_position = "absolute"
        label22.css_top = "105.0px"
        label22.css_width = "100px"
        label22.text = "gm"
        label22.variable_name = "label22"
        container1.append(label22, 'label22')
        label23 = Label()
        label23.attr_class = "Label"
        label23.attr_editor_newclass = False
        label23.css_height = "30px"
        label23.css_left = "240.0px"
        label23.css_position = "absolute"
        label23.css_top = "15.0px"
        label23.css_width = "100px"
        label23.text = "面积"
        label23.variable_name = "label23"
        container1.append(label23, 'label23')
        textinput18 = TextInput()
        textinput18.attr_class = "TextInput"
        textinput18.attr_editor_newclass = False
        textinput18.attr_maxlength = "100"
        textinput18.css_height = "30px"
        textinput18.css_left = "300.0px"
        textinput18.css_position = "absolute"
        textinput18.css_top = "15.0px"
        textinput18.css_width = "100px"
        textinput18.text = ""
        textinput18.variable_name = "textinput18"
        self.textinput18=textinput18
        container1.append(textinput18, 'textinput18')
        label24 = Label()
        label24.attr_class = "Label"
        label24.attr_editor_newclass = False
        label24.css_height = "30px"
        label24.css_left = "240.0px"
        label24.css_position = "absolute"
        label24.css_top = "60.0px"
        label24.css_width = "100px"
        label24.text = "克重"
        label24.variable_name = "label24"
        container1.append(label24, 'label24')
        textinput19 = TextInput()
        textinput19.attr_class = "TextInput"
        textinput19.attr_editor_newclass = False
        textinput19.attr_maxlength = "100"
        textinput19.css_height = "30px"
        textinput19.css_left = "300.0px"
        textinput19.css_position = "absolute"
        textinput19.css_top = "60.0px"
        textinput19.css_width = "100px"
        textinput19.text = ""
        textinput19.variable_name = "textinput19"
        self.textinput19=textinput19
        self.textinput19=textinput19
        container1.append(textinput19, 'textinput19')
        container1.children['textinput19'].onchange.do(self.onchange_textinput19)
        label25 = Label()
        label25.attr_class = "Label"
        label25.attr_editor_newclass = False
        label25.css_height = "30px"
        label25.css_left = "405.0px"
        label25.css_position = "absolute"
        label25.css_top = "60.0px"
        label25.css_width = "100px"
        label25.text = "gsm"
        label25.variable_name = "label25"
        container1.append(label25, 'label25')
        container0.append(container1, 'container1')
        textinput6 = TextInput()
        textinput6.attr_class = "TextInput"
        textinput6.attr_editor_newclass = False
        textinput6.attr_maxlength = "100"
        textinput6.css_height = "50px"
        textinput6.css_left = "255.0px"
        textinput6.css_position = "absolute"
        textinput6.css_top = "150.0px"
        textinput6.css_width = "100px"
        textinput6.text = ""
        textinput6.variable_name = "textinput6"
        self.textinput6=textinput6
        container0.append(textinput6, 'textinput6')
        container0.children['textinput6'].onchange.do(self.onchange_textinput6)
        textinput8 = TextInput()
        textinput8.attr_class = "TextInput"
        textinput8.attr_editor_newclass = False
        textinput8.attr_maxlength = "100"
        textinput8.css_height = "30.0px"
        textinput8.css_left = "360.0px"
        textinput8.css_position = "absolute"
        textinput8.css_top = "105.0px"
        textinput8.css_width = "300.0px"
        textinput8.text = "0.00059*10*chang*zhong"
        textinput8.variable_name = "textinput8"
        self.textinput8=textinput8
        container0.append(textinput8, 'textinput8')
        #container0.children['textinput17'].onchange.do(self.onchange_textinput17)
        button0 = Button()
        button0.attr_class = "Button"
        button0.attr_editor_newclass = False
        button0.css_background_color = "rgb(115,200,171)"
        button0.css_height = "30px"
        button0.css_left = "495.0px"
        button0.css_position = "absolute"
        button0.css_top = "315.0px"
        button0.css_width = "100px"
        button0.text = "生成分析登记表"
        button0.variable_name = "button0"
        container0.append(button0, 'button0')
        progress0 = Progress()
        progress0.attr_class = "Progress"
        progress0.attr_editor_newclass = False
        progress0.attr_max = "140"
        progress0.attr_value = "20"
        progress0.css_height = "90.0px"
        progress0.css_left = "180.0px"
        progress0.css_position = "absolute"
        progress0.css_visibility = "hidden"
        progress0.css_top = "165.0px"
        progress0.css_width = "435.0px"
        progress0.variable_name = "progress0"
        container0.append(progress0, 'progress0')
        container0.children['button0'].onclick.do(self.onclick_button0)
        dropdown0 = gui.DropDown.new_from_list(('2×2氨罗纹（一单一双）', 'CVC（DTY）','CVC'),)
        dropdown0.attr_class = "DropDown"
        dropdown0.attr_editor_newclass = False
        dropdown0.css_height = "30.0px"
        dropdown0.css_left = "435.0px"
        dropdown0.css_position = "absolute"
        dropdown0.css_top = "15.0px"
        dropdown0.css_width = "250.0px"
        dropdown0.variable_name = "dropdown0"
        container0.append(dropdown0, 'dropdown0')
        label6 = Label()
        label6.attr_class = "Label"
        label6.attr_editor_newclass = False
        label6.css_height = "30px"
        label6.css_left = "375.0px"
        label6.css_position = "absolute"
        label6.css_top = "15.0px"
        label6.css_width = "100px"
        label6.text = "纱比计算"
        label6.variable_name = "label6"
        container0.append(label6, 'label6')
        button1 = Button()
        button1.attr_class = "Button"
        button1.attr_editor_newclass = False
        button1.css_background_color = "rgb(162,221,129)"
        button1.css_height = "30px"
        button1.css_left = "750.0px"
        button1.css_position = "absolute"
        button1.css_top = "15.0px"
        button1.css_width = "100px"
        button1.text = "知识"
        button1.variable_name = "button1"
        container0.append(button1, 'button1')
        container0.children['dropdown0'].onchange.do(self.onchange_dropdown0)
        container0.children['button1'].onclick.do(self.onclick_button1)



        self.container0 = container0
        return self.container0
    def onclick_button1(self, emitter):
        self.dialog = GenericDialog(title='欢迎学习新知识', message='',
                                    width='1000px')
        mingcheng=['织物简称','纺纱方式','圆机机号对应尺寸','织物分类','织造机种类','织物鉴别','长短丝分类']
        dizhi=[r'D:\Study\pythonProject\remi_design\jisuan_shabu_canshu\来样分析表.png',r'D:\Study\pythonProject\remi_design\jisuan_shabu_canshu\额XX清单.png','','','','','']
        self.dialog.add_field_with_xuexi('image',mingcheng,dizhi)
        self.dialog.show(self)

    def onchange_dropdown0(self,emitter,new_value):
        if new_value =='2×2氨罗纹（一单一双）':
            self.dialog = GenericDialog(title=new_value, message='',
                                      width='1224px')
            self.dialog.show(self)

        elif new_value =='CVC（DTY）':
            self.dialog = GenericDialog(title=new_value, message='',
                                        width='1224px')
            self.dialog.show(self)
        elif new_value =='CVC':
            self.dialog = GenericDialog(title=new_value, message='',
                                        width='1224px')
            self.dialog.show(self)
    def yincang(self,d):
        self.container0.children['button0'].css_visibility = "hidden"

    def xin_chuan(self,d):
        self.dialog = GenericDialog(title='欢迎观看', message='',
                                    width='1224px')

        with open(r'D:\Study\pythonProject\remi_design\jisuan_shabu_canshu\ceshi\1.txt', 'w+',
                  encoding='utf-8') as f:  # 接口写入
            f.write(self.textinput19.text)
            f.write('\n')
            f.write(self.textinput9.text)
            f.write('\n')
            f.write(self.textinput14.text)
            f.write('\n')
            f.write(self.textinput6.text)
            f.write('\n')
            f.write(self.textinput0.text)
            f.write('\n')

        shengcheng_biao.yun_xing(d)
        zhuan_pdf.zhi("{}".format(d))
        zhuan_tu_1.run(d)
        # os.system("shengcheng_biao.py")
        # os.system("zhuan_pdf.py")
        # os.system("zhuan_tu_1.py")
        directory = d
        t = -1
        for root, dirs, filenames in walk(directory):
            for file in filenames:
                if file.endswith(".doc") or file.endswith(".docx"):
                    t = t + 1
        bianma = t + 1
        ri_qi = str(time.strftime("%Y%m%d", time.localtime()))
        deng_ji_hao = ri_qi[2:] + '-%s' % bianma

        fengmian = r'{}\{}来样分析表.png'.format(d,deng_ji_hao)
        self.dialog.add_field_with_image('image', fengmian)
        self.dialog.show(self)
        self.container0.children['button0'].css_visibility = "visible"
    def dengdai(self,d):
        self.container0.children['progress0'].css_visibility = "visible"
        t=0
        for i in range(14):
            t=t+10
            self.container0.children['progress0'].attr_value = t
            time.sleep(1)
        self.container0.children['progress0'].css_visibility = "hidden"

    def mkdir(self,path):

        folder = os.path.exists(path)

        if not folder:  # 判断是否存在文件夹如果不存在则创建为文件夹
            os.makedirs(path)  # makedirs 创建文件时如果路径不存在会创建这个路径
        else:
            pass

    def onclick_button0(self, emitter):
        ri_qi = str(time.strftime("%Y%m%d", time.localtime()))
        xu_hao= ri_qi[2:]
        file = r"D:\Study\pythonProject\remi_design\jisuan_shabu_canshu\{}".format(xu_hao)
        t4 = threading.Thread(target=self.mkdir, args=(file,))
        t1 = threading.Thread(target=self.yincang, args=("t1",))
        t2 = threading.Thread(target=self.xin_chuan, args=(file,))
        t3 = threading.Thread(target=self.dengdai, args=("t2",))
        t4.start()
        t1.start()
        t2.start()
        t3.start()

        #self.container0.children['button0'].css_visibility = "hidden"
        # self.dialog = GenericDialog(title='欢迎观看', message='',
        #                             width='1224px')
        #
        #
        # with open(r'D:\Study\pythonProject\remi_design\jisuan_shabu_canshu\ceshi\1.txt', 'w+', encoding='utf-8') as f:  # 接口写入
        #     f.write(self.textinput19.text)
        #     f.write('\n')
        #     f.write(self.textinput9.text)
        #     f.write('\n')
        #     f.write(self.textinput14.text)
        #     f.write('\n')
        #     f.write(self.textinput6.text)
        #     f.write('\n')
        #     f.write(self.textinput0.text)
        #     f.write('\n')
        #
        # shengcheng_biao.yun_xing()
        # zhuan_pdf.zhi(r"D:\Study\pythonProject\remi_design\jisuan_shabu_canshu\ceshi")
        # zhuan_tu_1.run()
        # #os.system("shengcheng_biao.py")
        # #os.system("zhuan_pdf.py")
        # #os.system("zhuan_tu_1.py")
        # directory = r"D:\Study\pythonProject\remi_design\jisuan_shabu_canshu\ceshi"
        # t = -1
        # for root, dirs, filenames in walk(directory):
        #     for file in filenames:
        #         if file.endswith(".doc") or file.endswith(".docx"):
        #             t = t + 1
        # bianma = t + 1
        # ri_qi = str(time.strftime("%Y%m%d", time.localtime()))
        # deng_ji_hao = ri_qi[2:] + '-%s' % bianma
        #
        # fengmian = r'D:\Study\pythonProject\remi_design\jisuan_shabu_canshu\ceshi\{}来样分析表.png'.format(deng_ji_hao)
        # self.dialog.add_field_with_image('image', fengmian)
        # self.dialog.show(self)
        # self.button0.css_visibility = "visible"

   #自身变化
    def onchange_textinput19(self, emitter, new_value):
        self.textinput19.text=self.textinput19.text
    def onchange_textinput9(self, emitter, new_value):
        self.textinput9.text=self.textinput9.text
    def onchange_textinput14(self, emitter, new_value):
        self.textinput14.text=self.textinput14.text
    def onchange_textinput6(self, emitter, new_value):
        self.textinput6.text=self.textinput6.text
    def onchange_textinput0(self, emitter, new_value):
        self.textinput0.text=self.textinput0.text
    def onchange_textinput27(self, emitter, new_value):
        self.textinput8.text='0.00059×{}×{}×10÷{}'.format(self.textinput4.text,self.textinput27.text,self.textinput2.text)
        s = self.textinput27.text.split('/')
        e=  self.textinput2.text.split('/')
        if len(s) > 1:
            a = len(self.textinput27.text.split('/'))
            t = ''
            for i in range(a):
                t = t + str(format(0.00059 * float(self.textinput4.text) * float(s[i]) * 10.00 / float(e[i]), '.4f')) + '/'
            self.textinput6.text=t
        else:
            self.textinput6.text=str(format(0.00059 * float(self.textinput4.text) * float(self.textinput27.text) * 10.00 / float(self.textinput2.text),'4f'))
    def onchange_textinput2(self, emitter, new_value):
        self.textinput8.text='0.00059×{}×{}×10÷{}'.format(self.textinput4.text,self.textinput27.text,self.textinput2.text)
        s = self.textinput27.text.split('/')
        e = self.textinput2.text.split('/')
        if len(s) > 1:
            a = len(self.textinput27.text.split('/'))
            t = ''
            for i in range(a):
                t = t + str(
                    format(0.00059 * float(self.textinput4.text) * float(s[i]) * 10.00 / float(e[i]), '.4f')) + '/'
            self.textinput6.text = t
        else:
            self.textinput6.text = str(format(
                0.00059 * float(self.textinput4.text) * float(self.textinput27.text) * 10.00 / float(
                    self.textinput2.text), '4f'))
    def onchange_textinput4(self, emitter, new_value):
        self.textinput8.text='0.00059×{}×{}×10÷{}'.format(self.textinput4.text,self.textinput27.text,self.textinput2.text)
        s = self.textinput27.text.split('/')
        e = self.textinput2.text.split('/')
        if len(s) > 1:
            a = len(self.textinput27.text.split('/'))
            t = ''
            for i in range(a):
                t = t + str(
                    format(0.00059 * float(self.textinput4.text) * float(s[i]) * 10.00 / float(e[i]), '.4f')) + '/'
            self.textinput6.text = t
        else:
            self.textinput6.text = str(format(
                0.00059 * float(self.textinput4.text) * float(self.textinput27.text) * 10.00 / float(
                    self.textinput2.text), '4f'))

    def onchange_textinput15(self, emitter, new_value):
        self.textinput18.text=str(float(self.textinput15.text)*float(self.textinput16.text)*0.0001)
        self.textinput19.text=str(float(self.textinput17.text)/float(self.textinput18.text))
    def onchange_textinput16(self, emitter, new_value):
        self.textinput18.text=str(float(self.textinput15.text)*float(self.textinput16.text)*0.0001)
        self.textinput19.text=str(float(self.textinput17.text)/float(self.textinput18.text))
    def onchange_textinput17(self, emitter, new_value):
        self.textinput19.text=str(float(self.textinput17.text)/float(self.textinput18.text))



# processing_code



if __name__ == "__main__":
    start(untitled, debug=True, address='0.0.0.0', port=8081, start_browser=True, multiple_instance=True)
    #webbrowser.open("http://127.1.1.1:7373/")
    #start(untitled, standalone=True)


