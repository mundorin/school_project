import tkinter as tk
from tkinter import ttk


def translate_from_10(digit, step):
    minus = False
    digit = rounding(float(digit))
    step = int(step)
    if digit < 0:
        minus = True
        digit = abs(digit)
    degri = 0
    strok = ''
    integir = {
        0: '0',
        1: '1',
        2: '2',
        3: '3',
        4: '4',
        5: '5',
        6: '6',
        7: '7',
        8: '8',
        9: '9',
        10: 'A',
        11: 'B',
        12: 'C',
        13: 'D',
        14: 'E',
        15: 'F'
    }
    while digit / (step ** degri) >= 1:
        degri += 1
    degri -= 1
    if degri < 0:
        degri = 0
    while degri > -11:
        strok = strok + str(integir[int(digit // step ** degri)])
        digit = digit % (step ** degri)
        if degri == 0:
            strok = strok + '.'
        degri -= 1

    strok = str(strok)
    if minus:
        return [('-' + strok), step]
    else:
        return [strok, step]


def translate_to_10(digit, step):
    integir = {
        '0': 0,
        '1': 1,
        '2': 2,
        '3': 3,
        '4': 4,
        '5': 5,
        '6': 6,
        '7': 7,
        '8': 8,
        '9': 9,
        'A': 10,
        'B': 11,
        'C': 12,
        'D': 13,
        'E': 14,
        'F': 15
    }
    minus = ''
    digit = str(digit)
    step = int(step)
    if ('.' in digit) == False:
        digit = digit + '.0'
    if digit[0] == '-':
        ឦ = '-'
        digit = digit[1:]
    degri = 0
    out = 0
    degri = digit.index('.') - 1
    digit = digit[:(digit.index('.'))] + digit[(digit.index('.') + 1):]
    for i in range(len(digit)):
        out += float(integir[digit[i]]) * (step ** degri)
        degri -= 1
    if 'e' in str(out):
        return ['0.0', 10]
    out = str(rounding(float(out)))
    if ('.' in digit) == False:
        out = float(out)
    return [minus + str(out)[:(str(out).index('.') + 11)], 10]


def rounding(digit):
    if digit == 0:
        return digit
    tr = 1
    if digit < 0:
        tr = -1
    if abs(digit) < 10:
        if (abs(digit) // 1) / abs(digit) > 0.999:
            return tr * (abs(digit) // 1)
        elif (abs(digit) // 1 + 1) / abs(digit) < 1.001:
            return tr * (abs(digit) // 1 + 1)
    elif abs(digit) < 100:
        if (abs(digit) // 1) / abs(digit) > 0.9999:
            return tr * (abs(digit) // 1)
        elif (abs(digit) // 1 + 1) / abs(digit) < 1.0001:
            return tr * (abs(digit) // 1 + 1)
    elif abs(digit) < 1000:
        if (abs(digit) // 1) / abs(digit) > 0.99999:
            return tr * (abs(digit) // 1)
        elif (abs(digit) // 1 + 1) / abs(digit) < 1.000015:
            return tr * (abs(digit) // 1 + 1)
    elif abs(digit) < 10000:
        if (abs(digit) // 1) / abs(digit) > 0.999999:
            return tr * (abs(digit) // 1)
        elif (abs(digit) // 1 + 1) / abs(digit) < 1.000002:
            return tr * (abs(digit) // 1 + 1)
    elif abs(digit) < 100000:
        if (abs(digit) // 1) / abs(digit) > 0.9999999:
            return tr * (abs(digit) // 1)
        elif (abs(digit) // 1 + 1) / abs(digit) < 1.00000025:
            return tr * (abs(digit) // 1 + 1)
    elif abs(digit) < 1000000:
        if (abs(digit) // 1) / abs(digit) > 0.99999999:
            return tr * (abs(digit) // 1)
        elif (abs(digit) // 1 + 1) / abs(digit) < 1.00000003:
            return tr * (abs(digit) // 1 + 1)
    elif abs(digit) < 10000000:
        if (abs(digit) // 1) / abs(digit) > 0.999999999:
            return tr * (abs(digit) // 1)
        elif (abs(digit) // 1 + 1) / abs(digit) < 1.0000000035:
            return tr * (abs(digit) // 1 + 1)
    elif abs(digit) < 100000000:
        if (abs(digit) // 1) / abs(digit) > 0.9999999999:
            return tr * (abs(digit) // 1)
        elif (abs(digit) // 1 + 1) / abs(digit) < 1.0000000004:
            return tr * (abs(digit) // 1 + 1)
    elif abs(digit) < 1000000000:
        if (abs(digit) // 1) / abs(digit) > 0.99999999999:
            return tr * (abs(digit) // 1)
        elif (abs(digit) // 1 + 1) / abs(digit) < 1.000000000045:
            return tr * (abs(digit) // 1 + 1)
    return digit


def add_digit(digit):
    value = calc.get()
    if len(value) > 0:
        if value[0] == '0' and len(value) == 1 and digit != '.' and value[:2] != '0.':
            value = value[1:]
        if value[:2] == '-0' and digit != '.' and value[:3] != '-0.':
            value = '-' + value[3:]
    calc.delete(0, tk.END)
    calc.insert(0, value + digit)


def add_operation(operation):
    value = calc.get()
    tr = False
    if value[-1] in '-+*/' and (value[-1] != '*' and operation != '*'):
        value = value[:-1]
    if value[0] == '0' and len(value) == 1:
        value = value[1:]
    if '+' in value:
        tr = True
    elif '*' in value and (operation == '*' and value[-1] == '*' and value[-2:] != '**') != True:
        tr = True
    elif '/' in value:
        tr = True
    elif '-' in value[1:]:
        tr = True
    if tr:
        calculate()
        value = calc.get()
        calc.delete(0, tk.END)
        calc.insert(0, value + operation)
    else:
        calc.delete(0, tk.END)
        calc.insert(0, value + operation)


def make_digit_button(digit):
    return tk.Button(text=digit, bd=5, font=('Arial', 13), command=lambda: add_digit(digit))


def make_operation_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=lambda: add_operation(operation))


def translate():
    value = calc.get()
    tr = True
    yt = ''
    if value[0] == '-':
        yt = '-'
        value = value[1:]
    for i in value:
        if (i in free[combo.get()[21:]]) == False or i in '+-*/':
            calc.delete(0, tk.END)
            calc.insert(0, 'wrong evidence')
            tr = False
            break
    value = yt + value
    if tr:
        if combo2.get()[21:] != '10':
            out = translate_from_10(translate_to_10(calc.get(), combo.get()[21:])[0], combo2.get()[21:])[0]
        else:
            out = translate_to_10(calc.get(), combo.get()[21:])[0]
        while out[-1] == '0' or out[-1] == '.':
            if out[-1] == '0':
                out = out[:-1]
            else:
                out = out[:-1]
                break
        calc.delete(0, tk.END)
        calc.insert(0, out)
        combo.set(combo2.get())


def calculate():
    value = calc.get()
    tr = True
    if '/0' in value:
        calc.delete(0, tk.END)
        calc.insert(0, 'divided by zero')
    if value[-1] in '+-*/':
        calc.delete(0, tk.END)
        calc.insert(0, 'wrong evidence')
        tr = False
    for i in value:
        if (i in free[combo.get()[21:]]) == False:
            calc.delete(0, tk.END)
            calc.insert(0, 'wrong evidence')
            tr = False
            break
    if tr:
        yu = ''
        operation = ''
        if value[0] == '-':
            yu = '-'
            value = value[1:]
        if '+' in value:
            ind = value.index('+')
            operation = '+'
        elif '*' in value:
            ind = value.index('*')
            operation = '*'
        elif '/' in value:
            ind = value.index('/')
            operation = '/'
        elif '-' in value:
            ind = value.index('-')
            operation = '-'
        number1 = yu + translate_to_10(value[:(ind)], combo.get()[21:])[0]
        if '**' in value:
            ind += 1
            operation = '**'
        number2 = value[(ind + 1):]
        yu = ''
        if number2[0] == '-':
            yu = '-'
            number2 = number2[1:]
        number2 = yu + translate_to_10(number2, combo.get()[21:])[0]
        out10 = eval(number1 + operation + number2)
        out = translate_from_10(out10, combo.get()[21:])[0]
        while out[-1] == '0' or out[-1] == '.':
            if out[-1] == '0':
                out = out[:-1]
            else:
                out = out[:-1]
                break
        calc.delete(0, tk.END)
        calc.insert(0, out)


def clear():
    calc.delete(0, tk.END)
    calc.insert(0, 0)


def delit():
    value = calc.get()
    calc.delete(0, tk.END)
    calc.insert(0, value[:-1])


def make_calc_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=calculate)


def make_delit_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=delit)


def make_clear_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=clear)


def make_translate_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=translate)


def make_minusplus_button(operation):
    return tk.Button(text=operation, bd=5, font=('Arial', 13), fg='red', command=make_minusplus)


def press_key(event):
    if event.char.isdigit():
        add_digit(event.char)
    elif event.char in '+-/*':
        add_digit(event.char)
    elif event.char == '\r':
        calculate()


def whatsystem():
    return combo.get()[21:]


def make_minusplus():
    value = calc.get()
    tr = False
    if '+' in value:
        ind = value.index('+') - 1
        tr = True
    elif '*' in value:
        ind = value.index('*')
        tr = True
    elif '/' in value:
        ind = value.index('/')
        tr = True
    elif '-' in value[1:]:
        ind = value[1:].index('-')
        tr = True
    if '**' in value:
        ind += 1
    if tr:
        if value[ind] == value[-1]:
            value = value + '-'
        elif value[ind + 1] == '-':
            value = value[:(ind + 1)] + '+' + value[(ind + 2):]
        elif value[ind + 1] == '+':
            value = value[:(ind + 1)] + '-' + value[(ind + 2):]
        else:
            value = value[:(ind + 1)] + '-' + value[(ind + 1):]
        calc.delete(0, tk.END)
        calc.insert(0, value)
    else:
        if value[0] == '-':
            value = value[1:]
        else:
            value = '-' + value
        calc.delete(0, tk.END)
        calc.insert(0, value)


win = tk.Tk()
win.geometry(f'430x320+800+250')
win['bg'] = '#37afc6'
win.title('calculator')

systems = ['                     2', '                     3', '                     4', '                     5',
           '                     6', '                     7', '                     8', '                     9',
           '                     10', '                     11', '                     12', '                     13',
           '                     14', '                     15', '                     16']

free = {
    '2': '01.+-*/',
    '3': '012.+-*/',
    '4': '0123.+-*/',
    '5': '01234.+-*/',
    '6': '012345.+-*/',
    '7': '0123456.+-*/',
    '8': '01234567.+-*/',
    '9': '012345678.+-*/',
    '10': '0123456789.+-*/',
    '11': '0123456789A.+-*/',
    '12': '0123456789AB.+-*/',
    '13': '0123456789ABC.+-*/',
    '14': '0123456789ABCD.+-*/',
    '15': '0123456789ABCDE.+-*/',
    '16': '0123456789ABCDEF.+-*/',
}

combo = ttk.Combobox(win, values=systems)
combo.grid(row=5, column=0, columnspan=2, stick='wens', padx='1', pady='1')
combo.current(8)
combo2 = ttk.Combobox(win, values=systems)
combo2.grid(row=5, column=4, columnspan=2, stick='wens', padx='1', pady='1')
combo2.current(8)

calc = tk.Entry(win, justify=tk.RIGHT, font=('Arial', 15), width=25)

calc.grid(row=0, column=0, columnspan=7, stick='we')
calc.insert(0, '0')
make_digit_button('0').grid(row=1, column=0, stick='wens', padx='5', pady='5')
make_digit_button('1').grid(row=1, column=1, stick='wens', padx='5', pady='5')
make_digit_button('2').grid(row=1, column=2, stick='wens', padx='5', pady='5')
make_digit_button('3').grid(row=1, column=3, stick='wens', padx='5', pady='5')
make_digit_button('4').grid(row=2, column=0, stick='wens', padx='5', pady='5')
make_digit_button('5').grid(row=2, column=1, stick='wens', padx='5', pady='5')
make_digit_button('6').grid(row=2, column=2, stick='wens', padx='5', pady='5')
make_digit_button('7').grid(row=2, column=3, stick='wens', padx='5', pady='5')
make_digit_button('8').grid(row=3, column=0, stick='wens', padx='5', pady='5')
make_digit_button('9').grid(row=3, column=1, stick='wens', padx='5', pady='5')
make_digit_button('A').grid(row=3, column=2, stick='wens', padx='5', pady='5')
make_digit_button('B').grid(row=3, column=3, stick='wens', padx='5', pady='5')
make_digit_button('C').grid(row=4, column=0, stick='wens', padx='5', pady='5')
make_digit_button('D').grid(row=4, column=1, stick='wens', padx='5', pady='5')
make_digit_button('E').grid(row=4, column=2, stick='wens', padx='5', pady='5')
make_digit_button('F').grid(row=4, column=3, stick='wens', padx='5', pady='5')
make_digit_button('.').grid(row=5, column=2, stick='wens', padx='5', pady='5')

make_operation_button('+').grid(row=1, column=4, stick='wens', padx='5', pady='5')
make_operation_button('-').grid(row=2, column=4, stick='wens', padx='5', pady='5')
make_operation_button('/').grid(row=3, column=4, stick='wens', padx='5', pady='5')
make_operation_button('*').grid(row=4, column=5, stick='wens', padx='5', pady='5')

make_calc_button('=').grid(row=1, column=5, stick='wens', padx='5', pady='5')
make_clear_button('C').grid(row=2, column=5, stick='wens', padx='5', pady='5')
make_translate_button('T').grid(row=3, column=5, stick='wens', padx='5', pady='5')
make_delit_button('<').grid(row=4, column=4, stick='wens', padx='5', pady='5')
make_minusplus_button('+\-').grid(row=5, column=3, stick='wens', padx='5', pady='5')

win.grid_columnconfigure(0, minsize=60)
win.grid_columnconfigure(1, minsize=60)
win.grid_columnconfigure(2, minsize=70)
win.grid_columnconfigure(3, minsize=70)
win.grid_columnconfigure(4, minsize=60)
win.grid_columnconfigure(5, minsize=60)
win.grid_rowconfigure(1, minsize=60)
win.grid_rowconfigure(2, minsize=60)
win.grid_rowconfigure(3, minsize=60)
win.grid_rowconfigure(4, minsize=60)
win.mainloop()