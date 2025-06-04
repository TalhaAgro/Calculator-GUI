import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

import logging

logging.basicConfig(format="%(levelname)s: %(message)s", level=logging.DEBUG)
logging.disable(logging.CRITICAL)


def main():
    root = Calculator()
    root.mainloop()


class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator App")
        self.geometry("455x480")
        self.configure(bg="#222244")

        # self.rowconfigure(0, weight = 1)
        self.page_style = ttk.Style()
        self.page_style.configure(
            "styling.TButton",
            foreground="black",
            font=("Yu Gothic UI Semibold", 12, "bold"),
            background="#333333",
        )

        self.page = Page(self, style="styling.TButton")
        self.page.grid(row=0, column=0, sticky="nsew", padx=5, pady=5)
        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)
        self.bindings()

    def bindings(self):
        self.bind("<Return>", self.page.equal)
        self.bind("<BackSpace>", self.page.delete)
        self.bind("<Key>", self.check_key)

    def check_key(self, event):
        if event.char.isdigit() and 0 <= int(event.char) <= 9:
            self.page.number(int(event.char))
        if event.char == "/":
            self.page.division()
        elif event.char == "*":
            self.page.multiplication()
        elif event.char == "+":
            self.page.addition()
        elif event.char == "-":
            self.page.subtraction()
        elif event.char == ".":
            self.page.decimal()
        elif event.char == "(":
            self.page.parenthesis_open()
        elif event.char == ")":
            self.page.parenthesis_close()


class Page(ttk.Frame):
    def __init__(self, parent_calculator, style=None):
        frame_style = ttk.Style()
        frame_style.configure("Calc.TFrame", background="#222244")  #

        super().__init__(parent_calculator, style="Calc.TFrame")

        self.rowconfigure(0, weight=3)
        for i in range(1, 7):
            self.rowconfigure(i, weight=1)
        for i in range(4):
            self.columnconfigure(i, weight=1)

        """Add calculator main area"""
        self.entry = tk.Label(
            self,
            text="",
            width=20,
            height=3,
            anchor="e",
            borderwidth=1,
            relief="solid",
            bg="#222222",
            fg="white",
            font=("Yu Gothic UI Semibold", 30, "bold"),
        )
        self.entry.grid(row=0, column=0, columnspan=4, sticky="new")

        button_style = ttk.Style()
        button_style.theme_use("clam")
        button_style.configure(
            "btn.TButton",
            foreground="white",
            font=("Yu Gothic UI Semibold", 14, "bold"),
            background="#333333",
            borderwidth=1,
            focusthickness=3,
            focuscolor="none",
        )
        button_style.map("btn.TButton", background=[("active", "#444444")])

        enter_button_style = ttk.Style()
        enter_button_style.theme_use("clam")
        enter_button_style.configure(
            "enter_btn.TButton",
            foreground="black",
            font=("Yu Gothic UI Semibold", 14, "bold"),
            background="#00B4D8",
            borderwidth=1,
            focusthickness=3,
            focuscolor="none",
        )
        enter_button_style.map("enter_btn.TButton", background=[("active", "#4ACEE9")])

        pil_img = (
            Image.open("delete-315.png").resize((24, 24), Image.LANCZOS).convert("RGBA")
        )
        datas = pil_img.getdata()
        newData = []
        for item in datas:
            if item[3] > 0:
                newData.append((255, 255, 255, item[3]))
            else:
                newData.append(item)
        pil_img.putdata(newData)
        self.delete_image = ImageTk.PhotoImage(pil_img)

        # 1st row
        # ttk.Style().theme_use('xpnative')
        self.parenthesis_open_button = my_button(
            self,
            text="(",
            command=self.parenthesis_open,
            style="btn.TButton",
            row=1,
            column=0,
        )
        self.parenthesis_close_button = my_button(
            self,
            text=")",
            command=self.parenthesis_close,
            style="btn.TButton",
            row=1,
            column=1,
        )
        self.C_button = my_button(
            self, text="C", command=self.clear, style="btn.TButton", row=1, column=2
        )
        self.delete_button = my_button(
            self,
            image=self.delete_image,
            command=self.delete,
            style="btn.TButton",
            row=1,
            column=3,
            text=" ",
        )
        # 2nd row
        self.reciprocal_button = my_button(
            self,
            text="1/x",
            command=self.reciprocal,
            style="btn.TButton",
            row=2,
            column=0,
        )
        self.squared_button = my_button(
            self, text="x^", command=self.squared, style="btn.TButton", row=2, column=1
        )
        self.square_root_button = my_button(
            self,
            text="sqrt(x)",
            command=self.square_root,
            style="btn.TButton",
            row=2,
            column=2,
        )
        self.divide_button = my_button(
            self, text="/", command=self.division, style="btn.TButton", row=2, column=3
        )
        # 3rd row
        self.seven_button = my_button(
            self,
            text="7",
            command=lambda: self.number(7),
            style="btn.TButton",
            row=3,
            column=0,
        )
        self.eight_button = my_button(
            self,
            text="8",
            command=lambda: self.number(8),
            style="btn.TButton",
            row=3,
            column=1,
        )
        self.nine_button = my_button(
            self,
            text="9",
            command=lambda: self.number(9),
            style="btn.TButton",
            row=3,
            column=2,
        )
        self.multiply_button = my_button(
            self,
            text="x",
            command=self.multiplication,
            style="btn.TButton",
            row=3,
            column=3,
        )
        # 4th row
        self.four_button = my_button(
            self,
            text="4",
            command=lambda: self.number(4),
            style="btn.TButton",
            row=4,
            column=0,
        )
        self.five_button = my_button(
            self,
            text="5",
            command=lambda: self.number(5),
            style="btn.TButton",
            row=4,
            column=1,
        )
        self.six_button = my_button(
            self,
            text="6",
            command=lambda: self.number(6),
            style="btn.TButton",
            row=4,
            column=2,
        )
        self.subtract_button = my_button(
            self,
            text="-",
            command=self.subtraction,
            style="btn.TButton",
            row=4,
            column=3,
        )
        # 5th row
        self.one_button = my_button(
            self,
            text="1",
            command=lambda: self.number(1),
            style="btn.TButton",
            row=5,
            column=0,
        )
        self.two_button = my_button(
            self,
            text="2",
            command=lambda: self.number(2),
            style="btn.TButton",
            row=5,
            column=1,
        )
        self.three_button = my_button(
            self,
            text="3",
            command=lambda: self.number(3),
            style="btn.TButton",
            row=5,
            column=2,
        )
        self.plus_button = my_button(
            self, text="+", command=self.addition, style="btn.TButton", row=5, column=3
        )
        # 6th row
        self.negate_button = my_button(
            self,
            text="+/-",
            command=self.negation,
            style="btn.TButton",
            row=6,
            column=0,
        )
        self.zero_button = my_button(
            self,
            text="0",
            command=lambda: self.number(0),
            style="btn.TButton",
            row=6,
            column=1,
        )
        self.dot_button = my_button(
            self, text=".", command=self.decimal, style="btn.TButton", row=6, column=2
        )
        self.equals_button = my_button(
            self,
            text="=",
            command=self.equal,
            style="enter_btn.TButton",
            row=6,
            column=3,
        )

    def get_text(self, _=None):
        current_text = self.entry.cget("text")
        return current_text

    def append_value(self, new_value, _=None):
        try:
            current_text = self.get_text()
            if (
                current_text == "Invalid Expression"
                or current_text == "Append Value Error"
            ):
                self.clear()
                current_text = ""
            # logging.debug(f"Current text type: {type(current_text)}, New value: {new_value}")
            if type(current_text) is int or type(current_text) is float:
                self.clear()
                current_text = ""

            updated_text = str(current_text) + str(new_value)
            self.entry.config(text=updated_text)
        except Exception:
            # logging.debug(f"Error appending value: {e}")
            self.entry.config(text="Append Value Error")

    def number(self, number, _=None):
        self.append_value((number))

    def parenthesis_open(self, _=None):
        self.append_value("(")

    def parenthesis_close(self, _=None):
        self.append_value(")")

    def addition(self, _=None):
        self.append_value("+")

    def subtraction(self, _=None):
        self.append_value("-")

    def multiplication(self, _=None):
        self.append_value("*")

    def division(self, _=None):
        self.append_value("/")

    def squared(self, _=None):
        self.append_value("**")

    def square_root(self, _=None):
        self.append_value("**0.5")

    def delete(self, _=None):
        try:
            current_text = self.entry.cget("text")
            if current_text == "Invalid Expression" or current_text == "Delete Error":
                self.clear()
                current_text = ""
            updated_text = current_text[:-1]
            self.entry.config(text=updated_text)
        except Exception:
            # logging.debug(f"Error deleting last character: {e}")
            self.entry.config(text="Delete Error")

    def equal(self, _=None):
        current_text = self.entry.cget("text")
        try:
            updated_text = eval(current_text)
            self.entry.config(text=updated_text)
        except ZeroDivisionError:
            self.entry.config(text="Cannot divide by zero")
            # logging.debug("ZeroDivisionError: Cannot divide by zero")
        except Exception:
            self.entry.config(text="Invalid Expression")
            # logging.debug(f"Error evaluating expression: {e}")

    def clear(self, _=None):
        self.entry.config(text="")

    def reciprocal(self, _=None):
        current_text = self.entry.cget("text")
        try:
            updated_text = f"1/{eval(current_text)}" if current_text else "1/"
        except Exception:
            updated_text = "Invalid Expression"
        # updated_text=eval(updated_text)
        self.entry.config(text=updated_text)

    def decimal(self, _=None):
        self.append_value(".")

    def negation(self, _=None):
        current_text = self.entry.cget("text")
        if current_text.startswith("-"):
            updated_text = current_text[1:]
        else:
            updated_text = "-" + current_text
        self.entry.config(text=updated_text)


class my_button(ttk.Button):
    def __init__(
        self, parent_frame, command, row, column, text=None, image=None, style=None
    ):
        super().__init__(
            parent_frame, text=text, command=command, image=image, style=style, width=4
        )
        self.grid(row=row, column=column, ipady=8, sticky="ew", padx=0, pady=0)


if __name__ == "__main__":
    main()
