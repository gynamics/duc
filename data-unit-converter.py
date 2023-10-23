#!/usr/bin/python
# -*- coding:utf-8 -*-
"""
  A unit converter between Y, Z, E, P, T, G, M, K, B, N, b
  considering sometimes 1K=1000 and otherwise it is 1024

  CopyRevolted 🍥 by gynamics
"""

import tkinter as tk
import tkinter.ttk as ttk
import string


def intpow(x, n):
    "Calculate integer power x**n but return 1 if n<=0."
    if n <= 0:
        return 1
    else:
        return x * pow(x, n - 1)


def int2base(x, base):
    "Convert an int value to string represention of base"
    if x == 0:
        return "0"  # annoying conner case

    digs = string.digits + string.ascii_letters
    sign = "-" if x < 0 else ""

    digits = []
    while x != 0:
        digits.append(digs[x % base])
        x = x // base

    digits.reverse()
    return sign.join(digits)


def main():
    win = tk.Tk()
    win.title("DUC")
    win.geometry("600x400")
    tk.Label(
        win, text="Data Unit Converter 🦊", font=("serif", 28), fg="red", anchor="c"
    ).pack()

    text_font = ("serif", 16)
    code_font = ("monospace", 12)

    win.option_add("*TCombobox*Listbox.font", ("monospace", 12))

    prefix_units = {
        " ": 0,
        "K": 1,
        "M": 2,
        "G": 3,
        "T": 4,
        "P": 5,
        "E": 6,
        "Z": 7,
        "Y": 8,
    }
    iprefixsel = ttk.Combobox(
        win, font=code_font, width=2, values=tuple(prefix_units.keys())
    )
    iprefixsel.hint = tk.Label(
        win,
        text="Unit",
        font=text_font,
    )
    iprefixsel.place(x=300, y=140)
    iprefixsel.hint.place(x=240, y=140)
    iprefixsel.set(list(prefix_units.keys())[0])

    oprefixsel = ttk.Combobox(
        win, font=code_font, width=2, values=tuple(prefix_units.keys())
    )
    oprefixsel.hint = tk.Label(
        win,
        text="Unit",
        font=text_font,
    )
    oprefixsel.place(x=300, y=260)
    oprefixsel.hint.place(x=240, y=260)
    oprefixsel.set(list(prefix_units.keys())[0])

    byte_units = {
        "(b) Bit": 1,
        "(N) Nibble": 4,
        "(B) Byte": 8,
    }
    ibytesel = ttk.Combobox(
        win, font=code_font, width=10, values=tuple(byte_units.keys())
    )
    ibytesel.hint = tk.Label(win, text="Byte/bit", font=text_font)
    ibytesel.place(x=460, y=140)
    ibytesel.hint.place(x=360, y=140)
    ibytesel.set(list(byte_units.keys())[0])

    obytesel = ttk.Combobox(
        win, font=code_font, width=10, values=tuple(byte_units.keys())
    )
    obytesel.hint = tk.Label(win, text="Byte/bit", font=text_font)
    obytesel.place(x=460, y=260)
    obytesel.hint.place(x=360, y=260)
    obytesel.set(list(byte_units.keys())[0])

    kilo_units = {
        "1000": 1000,
        "1024": 1024,
    }
    ikilosel = ttk.Combobox(
        win, font=code_font, width=4, values=tuple(kilo_units.keys())
    )
    ikilosel.hint = tk.Label(win, text="1k =", font=code_font)
    ikilosel.place(x=440, y=80)
    ikilosel.hint.place(x=400, y=80)
    ikilosel.set("1024")

    okilosel = ttk.Combobox(
        win, font=code_font, width=4, values=tuple(kilo_units.keys())
    )
    okilosel.hint = tk.Label(win, text="1k =", font=code_font)
    okilosel.place(x=440, y=200)
    okilosel.hint.place(x=400, y=200)
    okilosel.set("1024")

    base_units = {
        "Bin": 2,
        "Oct": 8,
        "Dec": 10,
        "Hex": 16,
    }
    ibasesel = ttk.Combobox(
        win, font=code_font, width=4, values=tuple(base_units.keys())
    )
    ibasesel.hint = tk.Label(win, text="Input Base", font=text_font)
    ibasesel.place(x=160, y=140)
    ibasesel.hint.place(x=20, y=140)
    ibasesel.set("Dec")

    obasesel = ttk.Combobox(
        win, font=code_font, width=4, values=tuple(base_units.keys())
    )
    obasesel.hint = tk.Label(win, text="Output Base", font=text_font)
    obasesel.place(x=160, y=260)
    obasesel.hint.place(x=20, y=260)
    obasesel.set("Dec")

    inputfld = tk.Text(win, font=code_font, height=1, width=32)
    inputfld.hint = tk.Label(win, text="Input", font=text_font)
    inputfld.place(x=100, y=80)
    inputfld.hint.place(x=20, y=80)
    inputfld.focused = False

    outputfld = tk.Text(win, font=code_font, height=1, width=32)
    outputfld.hint = tk.Label(win, text="Output", font=text_font)
    outputfld.place(x=100, y=200)
    outputfld.hint.place(x=20, y=200)

    def convert(event):
        outputfld.delete("1.0", tk.END)
        inputstr = inputfld.get("1.0", "end-1c")
        if inputstr == "":
            return

        try:
            num = int(inputstr, base_units[ibasesel.get()])
        except:
            outputfld.insert("1.0", "ERROR")
            outputfld.tag_add("errorstyle", "1.0", "end-1c")
            outputfld.tag_config("errorstyle", foreground="red")
            return

        num *= byte_units[ibytesel.get()] * intpow(
            kilo_units[ikilosel.get()], prefix_units[iprefixsel.get()]
        )
        num //= byte_units[obytesel.get()] * intpow(
            kilo_units[okilosel.get()], prefix_units[oprefixsel.get()]
        )
        outputfld.delete("1.0", tk.END)
        outputfld.insert("1.0", int2base(num, base_units[obasesel.get()]))

    def hit_return_handler(event):
        convert(event)
        return "break"

    ibasesel.bind("<<ComboboxSelected>>", convert)
    obasesel.bind("<<ComboboxSelected>>", convert)
    ikilosel.bind("<<ComboboxSelected>>", convert)
    okilosel.bind("<<ComboboxSelected>>", convert)
    iprefixsel.bind("<<ComboboxSelected>>", convert)
    oprefixsel.bind("<<ComboboxSelected>>", convert)
    inputfld.bind("<KeyRelease>", convert)
    inputfld.bind("<Return>", hit_return_handler)
    win.mainloop()


if __name__ == "__main__":
    main()
