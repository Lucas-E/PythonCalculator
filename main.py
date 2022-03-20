import tkinter as tk
from tkinter import *

LARGE_FONT_STYLE = ('Arial', 40, "bold")
SMALL_FONT_STYLE = ('Arial', 16)
DIGIT_FONT_STYLE = ('Arial', 16, "bold")
DEFAULT_FONT_STYLE = ('Arial', 20)

OFF_WHITE = "#F8FAFF"
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"
LIGHT_BLUE = "#CCEDFF"
WHITE = "#FFFFFF"
DEEP_BLUE = "#00008b"

class Calculator:
    
    
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator")
        
        self.total_expression = ""
        self.current_expression = ""
        self.result = ""
        self.display_frame = self.create_display_frame()
        
        self.total_label, self.label = self.create_display_labels()
        
        self.digits = {
            7:(1,1), 8:(1,2), 9:(1,3),
            4:(2,1), 5:(2,2), 6:(2,3),
            1:(3,1), 2:(3,2), 3:(3,3),
            ".":(4,1), 0:(4,2)
            }
        self.brackets = {"(":"(", ")":")"}
        self.operations = {"/":"\u00F7", "*":"\u00D7","-":"-", "+":"+"}
        self.buttons_frame = self.create_buttons_frame()
        
        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1,5):
            self.buttons_frame.rowconfigure(index=x, weight = 1)
            self.buttons_frame.columnconfigure(index=x, weight = 1)
        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_clear_button()
        self.create_equals_button()
        self.create_delete_button()
        self.create_brackets()
        
    def run(self):
        self.window.mainloop()
    
    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame
    
    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame
    
    def create_display_labels(self):
        total_labels = tk.Label(self.display_frame, text=self.total_expression, anchor = tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_labels.pack(expand=True, fill="both")
        
        label = tk.Label(self.display_frame, text=self.current_expression, anchor = tk.E, bg=LIGHT_GRAY, fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill="both")
        
        return total_labels, label
    
    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGIT_FONT_STYLE, borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def create_operator_buttons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text = symbol, bg=OFF_WHITE, fg = LABEL_COLOR, font = DEFAULT_FONT_STYLE, borderwidth=0, command = lambda x = operator: self.append_operator(x))
            button.grid(row=i, column=4, sticky = tk.NSEW)
            i+=1
            
    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text = "C", bg=OFF_WHITE, fg = LABEL_COLOR, font = DEFAULT_FONT_STYLE, borderwidth=0, command = lambda: self.clear())
        button.grid(row=0, column=1, sticky = tk.NSEW)
        
    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text = "=", bg=LIGHT_BLUE, fg = LABEL_COLOR, font = DEFAULT_FONT_STYLE, borderwidth=0, command = lambda: self.evaluate())
        button.grid(row=4, column=4, sticky = tk.NSEW)
    
    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f'{symbol}')
        self.total_label.config(text=expression)
    
    def update_label(self):
        self.label.config(text=self.current_expression[:11])
    
    def add_to_expression(self, value):
        self.current_expression+= str(value)
        self.update_label()
    
    def append_operator(self, operator):
        self.current_expression+=operator
        self.update_label()
        
    def clear(self):
        self.current_expression = ""
        self.total_expression = ""
        self.update_total_label()
        self.update_label()
        
    def evaluate(self):
        expression = self.current_expression
        try:
            value = eval(expression)
            self.total_expression = expression
            self.current_expression = str(value)
        except Exception as e:
            self.current_expression = "Error"
        self.update_label()
        self.update_total_label()
        
    def create_delete_button(self):
        button = tk.Button(self.buttons_frame, text = "E", bg=LIGHT_BLUE, fg = LABEL_COLOR, font = DEFAULT_FONT_STYLE, borderwidth = 0, command=lambda: self.delete())
        button.grid(row=4, column=3, sticky = tk.NSEW)
        
    def delete(self):
        correction = self.current_expression[:-1]
        self.current_expression = correction
        self.update_label()
    def create_brackets(self):
        i = 2
        for operator, symbol in self.brackets.items():
            button = tk.Button(self.buttons_frame, text = symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font = DEFAULT_FONT_STYLE, borderwidth = 0, command = lambda x = operator: self.insert_bracket(x))
            button.grid(row=0, column=i, sticky=tk.NSEW)
            i+=1
            
    def insert_bracket(self, bracket):
        self.current_expression+=bracket
        self.update_label()
        
if __name__ == "__main__":
    
    calc = Calculator()
    calc.run()