
# coding: utf-8

# In[83]:

import sys
from tkinter import *
import tkinter.font
from PIL import Image, ImageTk

def clear():
    txtDisplay.delete(0,END);
    return;

#Parent Window.
root = Tk();
root.title('EOG Calculator');
root.geometry('900x830');

#Main entry.
number = StringVar();
txtDisplay = Entry(root, textvariable = number, relief=RIDGE, bd = 10, width=92,    insertwidth = 1, font = 40);
txtDisplay.place(x=25, y=25);
txtDisplay.focus();

plusActive = minusActive = multiplyActive =  divideActive = False;

def update(value):
    currentValue = number.get()
    number.set(currentValue + value)
    
def add():
    global plusActive, minusActive, multiplyActive, divideActive;
    plusActive = True; minusActive = multiplyActive = divideActive = False;
    currentValue = number.get()
    number.set(currentValue + '+')

def minus():
    global plusActive, minusActive, multiplyActive, divideActive;
    minusActive = True; plusActive = multiplyActive = divideActive = False;
    currentValue = number.get()
    number.set(currentValue + '-')
    
def multiply():
    global plusActive, minusActive, multiplyActive, divideActive;
    multiplyActive = True; minusActive = plusActive = divideActive = False;
    currentValue = number.get()
    number.set(currentValue + 'x')
    
def divide():
    global plusActive, minusActive, multiplyActive, divideActive;
    divideActive = True; minusActive = multiplyActive = plusActive = False;
    currentValue = number.get()
    number.set(currentValue + '/')
    
def equal():
    currentValue = number.get()
    if(plusActive==True):
        [x,y]=currentValue.split('+')
        x=float(x); y=float(y);
        number.set(x+y)
    if(minusActive==True):
        [x,y]=currentValue.split('-')
        x=float(x); y=float(y);
        number.set(x-y)
    if(multiplyActive==True):
        [x,y]=currentValue.split('x')
        x=float(x); y=float(y);
        number.set(x*y)
    if(divideActive==True):
        [x,y]=currentValue.split('/')
        x=float(x); y=float(y);
        number.set(x/y)

#Buttons:
zeroButton = Button(root, text='0', width=70, height=10, bg='white', fg='black', command = lambda: update('0')).place(x=25,y=645);
oneButton = Button(root, text='1', width=20, height=10, bg='white', fg='black', command = lambda: update('1')).place(x=25, y=460);
twoButton = Button(root, text='2', width=20, height=10, bg='white', fg='black', command = lambda: update('2')).place(x=200, y=460);
threeButton = Button(root, text='3', width=20, height=10, bg='white', fg='black', command = lambda: update('3')).place(x=375, y=460);
fourButton = Button(root, text='4', width=20, height=10, bg='white', fg='black', command = lambda: update('4')).place(x=25, y=275);
fiveButton = Button(root, text='5', width=20, height=10, bg='white', fg='black', command = lambda: update('5')).place(x=200, y=275);
sixButton = Button(root, text='6', width=20, height=10, bg='white', fg='black', command = lambda: update('6')).place(x=375, y=275);
sevenButton = Button(root, text='7', width=20, height=10, bg='white', fg='black', command = lambda: update('7')).place(x=25, y=90);
eightButton = Button(root, text='8', width=20, height=10, bg='white', fg='black', command = lambda: update('8')).place(x=200, y=90);
ninthButton = Button(root, text='9', width=20, height=10, bg='white', fg='black', command = lambda: update('9')).place(x=375, y=90);

plusButton = Button(root, text='+', width=20, height=10, bg='orange', fg='black', command = lambda: add() ).place(x=550, y=90);
minusButton = Button(root, text='-', width=20, height=10, bg='orange', fg='black', command = lambda: minus() ).place(x=725, y=90);
multiplyButton = Button(root, text='x',width=20, height=10, bg='orange', fg='black', command = lambda: multiply() ).place(x=550, y=275);
divideButton = Button(root, text='÷', width=20, height=10, bg='orange', fg='black', command = lambda: divide() ).place(x=725, y=275);
equalButton = Button(root, text='=', width=20, height=10, bg='Lightgreen', fg='black', command = lambda: equal() ).place(x=550, y=460);
clearButton = Button(root, text='Clear (CE)', width=20, height=10, bg='Lightgreen', fg='black', command = clear).place(x=725, y=460);

#Locks the parent windows size.
root.maxsize(900,830);
root.minsize(900,830);

#Parent window's background color:
root.configure(background = 'grey');
root.mainloop();


# In[ ]:



