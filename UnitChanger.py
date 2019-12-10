import tkinter as tk
import tkinter.font as tf

class UnitChanger:
    # 결과 출력 여부 체크
    printResult = 0

    # 윈도우 요소와 필수 함수를 넘겨받기 위한 변수
    window = None
    font = None
    menuFont = None
    allChildren = None

    # 옵션 메뉴 선택 값
    upperValue = None
    lowerValue = None

    def __init__(self, window, func):
        self.window = window
        self.allChildren = func

    def pressButtonKey(self, event):
        # 전체 삭제
        if event.keycode == 27:
            inputNum.configure(state=tk.NORMAL)
            inputNum02.configure(state=tk.NORMAL)
            inputNum.delete("1.0", tk.END)
            inputNum.insert(tk.END, "0")
            inputNum02.delete("1.0", tk.END)
            inputNum02.insert(tk.END, "0")
            self.printResult = 1
            inputNum.configure(state="disabled")
            inputNum02.configure(state="disabled")
        # Backspace 기능
        elif event.keycode == 8:
            if len(inputNum.get("1.0", tk.END)) == 2:
                inputNum.configure(state=tk.NORMAL)
                inputNum.insert("1.0", "0")
                self.printResult = 1
                inputNum.configure(state="disabled")
            else:
                pass
            if not inputNum.get("1.0", tk.END) == "0\n":
                inputNum.configure(state=tk.NORMAL)
                inputNum.delete("%s-1c" % tk.INSERT, tk.INSERT)
                inputNum.configure(state="disabled")
            else:
                pass
        else:
            # 초기 화면 0표기와 연산 결과를 활용해 연계 계산을 위한 조건
            if self.printResult == 1:
                inputNum.configure(state=tk.NORMAL)
                inputNum.delete("1.0", tk.END)
                inputNum.configure(state="disabled")
                self.printResult = 0
            self.printResult = 0
            inputNum.configure(state=tk.NORMAL)
            inputNum.insert(tk.INSERT, event.char)
            inputNum.configure(state="disabled")
            self.temperatureChanger()

    def setUpperOptionValue(self, upperValue):
        self.upperValue = upperValue

    def setLowerOptionValue(self, lowerValue):
        self.lowerValue = lowerValue

    def temperature(self):
        self.menuFont = tf.Font(family="맑은 고딕", size=12, weight="bold")
        self.font = tf.Font(family="맑은 고딕", size=15)
        widgetList = self.allChildren(self.window)
        for item in widgetList:
            item.grid_forget()

        global inputNum
        inputNum = tk.Text(self.window, width=30, height=1, relief="groove", \
                        font=self.font, background="gray95", padx=10)
        inputNum.grid(row=0, column=0, columnspan=4)
        inputNum.insert(tk.END, "0")
        self.printResult = 1
        inputNum.configure(state="disabled")

        variable = tk.StringVar(self.window)
        variable.set("섭씨")
        optionMenu = tk.OptionMenu(self.window, variable, "화씨", "섭씨", "절대 온도", command=self.setUpperOptionValue)
        self.upperValue = "섭씨"
        optionMenu.grid(row=1, column=0, columnspan=2, sticky="nesw")
        optionMenu.config(font=self.menuFont, relief=tk.GROOVE)

        global inputNum02
        inputNum02 = tk.Text(self.window, width=30, height=1, relief="groove", \
                           font=self.font, background="gray95", padx=10)
        inputNum02.grid(row=2, column=0, columnspan=4)
        inputNum02.insert(tk.END, "0")
        self.printResult = 1
        inputNum02.configure(state="disabled")

        variable = tk.StringVar(self.window)
        variable.set("화씨")
        optionMenu02 = tk.OptionMenu(self.window, variable, "화씨", "섭씨", "절대 온도", command=self.setLowerOptionValue)
        self.lowerValue = "화씨"
        optionMenu02.grid(row=3, column=0, columnspan=2, sticky="nesw")
        optionMenu02.config(font=self.menuFont, relief=tk.GROOVE)

        # 버튼 그리드 변수
        rowIndex = 4
        colIndex = 0

        # 버튼 텍스트 변수
        buttonText = [
            'CE', 'AC', '←',
            '7', '8', '9',
            '4', '5', '6',
            '1', '2', '3',
            '.', '0', '±'
        ]

        # 버튼 표시
        for button in buttonText:
            def click(t=button):
                self.pressButton(t)

            buttonObject = tk.Button(self.window, text=button, width=10, height=2, \
                                    relief="groove", command=click, font=self.font, padx=0, pady=0)
            buttonObject.grid(row=rowIndex, column=colIndex, sticky="nesw")
            # 결과 출력 버튼 색 변경
            if button == "=":
                buttonObject.configure(bg="skyblue")
            colIndex += 1
            if colIndex > 2:
                rowIndex += 1
                colIndex = 0
        self.window.bind("<Key>", self.pressButtonKey)

    def temperatureChanger(self):
        print("enter")
        inputNum02.configure(state=tk.NORMAL)
        inputNum02.delete("1.0", tk.END)
        inputNum02.configure(state="disabled")
        if self.upperValue == "섭씨":
            if self.lowerValue == "화씨":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str((number * 9 / 5) + 32)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")