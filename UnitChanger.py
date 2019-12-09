import tkinter as tk
import tkinter.font as tf

class UnitChanger:
    window = None
    font = None
    menuFont = None
    allChildren = None

    def __init__(self, window, func):
        self.window = window
        self.allChildren = func

    def temperature(self):
        self.menuFont = tf.Font(family="맑은 고딕", size=12, weight="bold")
        self.font = tf.Font(family="맑은 고딕", size=15)
        widgetList = self.allChildren(self.window)
        for item in widgetList:
            item.grid_forget()

        global inputNum
        inputNum = tk.Text(self.window, width=30, height=1, relief="groove", \
                        font=self.font, background="gray95", padx=10)
        inputNum.tag_configure('tag-right', justify="right")
        inputNum.grid(row=0, column=0, columnspan=4, ipadx=5)
        inputNum.insert(tk.END, "0")
        inputNum.configure(state="disabled")

        variable = tk.StringVar(self.window)
        variable.set("섭씨")
        optionMenu = tk.OptionMenu(self.window, variable, "화씨", "섭씨", "절대 온도")
        optionMenu.grid(row=1, column=0, sticky="nesw")
        optionMenu.config(font=self.menuFont, relief=tk.GROOVE, width=10)

        global inputNum02
        inputNum02 = tk.Text(self.window, width=30, height=1, relief="groove", \
                           font=self.font, background="gray95", padx=10)
        inputNum02.tag_configure('tag-right', justify="right")
        inputNum02.grid(row=2, column=0, columnspan=4, ipadx=5)
        inputNum02.insert(tk.END, "0")
        inputNum02.configure(state="disabled")

        variable = tk.StringVar(self.window)
        variable.set("화씨")
        optionMenu02 = tk.OptionMenu(self.window, variable, "화씨", "섭씨", "절대 온도")
        optionMenu02.grid(row=3, column=0, sticky="nesw")
        optionMenu02.config(font=self.menuFont, relief=tk.GROOVE, width=10)

        # 버튼 그리드 변수
        rowIndex = 4
        colIndex = 0

        # 버튼 텍스트 변수
        buttonText = [
            '%', '√x', 'x²', '1/x',
            'CE', 'AC', '←', '/',
            '7', '8', '9', '*',
            '4', '5', '6', '-',
            '1', '2', '3', '+',
            '.', '0', '±', '='
        ]

        # 버튼 표시
        for button in buttonText:
            def click(t=button):
                self.pressButton(t)

            buttonObject = tk.Button(self.window, text=button, width=6, height=2, \
                                    relief="groove", command=click, font=self.font, padx=0, pady=0)
            buttonObject.grid(row=rowIndex, column=colIndex, sticky="nesw")
            # 결과 출력 버튼 색 변경
            if button == "=":
                buttonObject.configure(bg="skyblue")
            colIndex += 1
            if colIndex > 3:
                rowIndex += 1
                colIndex = 0
        self.window.bind("<Key>", self.pressButtonKey)