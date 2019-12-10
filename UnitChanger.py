import tkinter as tk
import tkinter.font as tf

class UnitChanger:
    # 사용하지 않는 특수 문자 목록
    specialChars = [
        'quoteleft', 'exclam', 'at',
        'numbersign', 'dollar', 'percent',
        'asciicircum', 'ampersand', 'asterisk',
        'parenleft', 'parenright', 'minus',
        'equal', 'plus', 'slash'
    ]
    # 결과 출력 여부 체크
    printResult = 0
    isPlusMinus = 0

    # 윈도우 요소와 필수 함수를 넘겨받기 위한 변수
    window = None
    font = None
    menuFont = None
    allChildren = None

    # 옵션 메뉴 선택 값
    upperValue = None
    lowerValue = None

    # 선택된 단위 변환기 확인 변수
    isTemperature = 0
    isLength = 0
    isData = 0
    isWeight = 0

    def __init__(self, window, func):
        self.window = window
        self.allChildren = func

    def pressButtonKey(self, event):
        print(event)
        # 전체 삭제
        if event.keycode == 27:
            inputNum.configure(state=tk.NORMAL)
            inputNum02.configure(state=tk.NORMAL)
            inputNum.delete("1.0", tk.END)
            inputNum.insert(tk.END, "0")
            inputNum02.delete("1.0", tk.END)
            if self.isTemperature == 1:
                self.temperatureChanger()
            elif self.isLength == 1:
                self.lengthChanger()
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
                if self.isTemperature == 1:
                    self.temperatureChanger()
                elif self.isLength == 1:
                    self.lengthChanger()
                inputNum.configure(state="disabled")
            else:
                pass
        else:
            if event.keysym in self.specialChars or event.keycode == 16:
                pass
            # 초기 화면 0표기와 연산 결과를 활용해 연계 계산을 위한 조건
            else:
                if self.printResult == 1:
                    inputNum.configure(state=tk.NORMAL)
                    inputNum.delete("1.0", tk.END)
                    inputNum.configure(state="disabled")
                    self.printResult = 0
                self.printResult = 0
                inputNum.configure(state=tk.NORMAL)
                inputNum.insert(tk.INSERT, event.char)
                inputNum.configure(state="disabled")
                if self.isTemperature == 1:
                    self.temperatureChanger()
                elif self.isLength == 1:
                    self.lengthChanger()

    def pressButton(self, value):
        # 전체 삭제
        if value == "AC" or value == "CE":
            self.isPlusMinus = 0
            inputNum.configure(state=tk.NORMAL)
            inputNum02.configure(state=tk.NORMAL)
            inputNum.delete("1.0", tk.END)
            inputNum.insert(tk.END, "0")
            inputNum02.delete("1.0", tk.END)
            if self.isTemperature == 1:
                self.temperatureChanger()
            elif self.isLength == 1:
                self.lengthChanger()
            self.printResult = 1
            inputNum.configure(state="disabled")
            inputNum02.configure(state="disabled")
        # Backspace 기능
        elif value == "←":
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
                if self.isTemperature == 1:
                    self.temperatureChanger()
                elif self.isLength == 1:
                    self.lengthChanger()
                inputNum.configure(state="disabled")
            else:
                pass
        # 음수 양수 전환
        elif value == "±":
            entryString = inputNum.get("1.0", tk.INSERT)
            if len(entryString) > 0:
                index = len(entryString) - 1
                enterNumber = 0
                # 숫자일 경우나 소수점이 있을 경우에 부호를 입력할 위치 선정
                if entryString[-1].isdigit() or entryString[-1] == "." and not self.printResult == 1:
                    while entryString[index].isdigit() or entryString[index] == ".":
                        enterNumber = entryString[index:]
                        index -= 1
                        if index < 0:
                            index += 1
                            break
                    # 부호 변경
                    if self.isPlusMinus == 0:
                        inputNum.configure(state=tk.NORMAL)
                        inputNum.delete("1.0", tk.END)
                        if entryString == enterNumber:
                            inputNum.insert(tk.END, "-" + enterNumber, "tag-right")
                        else:
                            inputNum.insert(tk.END, entryString[0:index + 1] + "-" + enterNumber, "tag-right")
                        inputNum.configure(state="disabled")
                        self.isPlusMinus = 1
                    else:
                        inputNum.configure(state=tk.NORMAL)
                        inputNum.delete("1.0", tk.END)
                        inputNum.insert(tk.END, entryString[0:index] + enterNumber, "tag-right")
                        inputNum.configure(state="disabled")
                        self.isPlusMinus = 0
        else:
            # 초기 화면 0표기와 연산 결과를 활용해 연계 계산을 위한 조건
            if self.printResult == 1:
                inputNum.configure(state=tk.NORMAL)
                inputNum.delete("1.0", tk.END)
                inputNum.configure(state="disabled")
                self.printResult = 0
            self.printResult = 0
            inputNum.configure(state=tk.NORMAL)
            inputNum.insert(tk.INSERT, value)
            inputNum.configure(state="disabled")
            if self.isTemperature == 1:
                self.temperatureChanger()
            elif self.isLength == 1:
                self.lengthChanger()

    def setUpperOptionValue(self, upperValue):
        self.upperValue = upperValue
        if self.isTemperature == 1:
            self.temperatureChanger()
        elif self.isLength == 1:
            self.lengthChanger()

    def setLowerOptionValue(self, lowerValue):
        self.lowerValue = lowerValue
        if self.isTemperature == 1:
            self.temperatureChanger()
        elif self.isLength == 1:
            self.lengthChanger()

    def temperature(self):
        self.isTemperature = 1
        self.isLength = 0
        self.isData = 0
        self.isWeight = 0

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
        optionMenu.grid(row=1, column=0, columnspan=3, sticky="nesw")
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
        optionMenu02.grid(row=3, column=0, columnspan=3, sticky="nesw")
        optionMenu02.config(font=self.menuFont, relief=tk.GROOVE)
        self.temperatureChanger()

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
            elif self.lowerValue == "섭씨":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "절대 온도":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number + 273.15)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
        elif self.upperValue == "화씨":
            if self.lowerValue == "화씨":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "섭씨":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(round((number - 32) * 5/9, 4))
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "절대 온도":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(round((number - 32) * 5/9 + 273.15, 4))
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
        elif self.upperValue == "절대 온도":
            if self.lowerValue == "화씨":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(round((number-273.15)*9/5+32, 4))
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "섭씨":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number - 273.15)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "절대 온도":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")

    def length(self):
        self.isTemperature = 0
        self.isLength = 1
        self.isData = 0
        self.isWeight = 0

        self.menuFont = tf.Font(family="맑은 고딕", size=12, weight="bold")
        self.font = tf.Font(family="맑은 고딕", size=15)
        widgetList = self.allChildren(self.window)
        for item in widgetList:
            item.grid_forget()

        global inputNum
        inputNum = tk.Text(self.window, width=30, height=1, relief="groove",\
                           font=self.font, background="gray95", padx=10)
        inputNum.grid(row=0, column=0, columnspan=4)
        inputNum.insert(tk.END, "0")
        self.printResult = 1
        inputNum.configure(state="disabled")

        variable = tk.StringVar(self.window)
        variable.set("센티미터")
        optionMenu = tk.OptionMenu(self.window, variable,
                                   "밀리미터", "센티미터", "미터", "킬로미터",
                                   "인치", "피트", "야드", "마일",
                                   command=self.setUpperOptionValue)
        self.upperValue = "센티미터"
        optionMenu.grid(row=1, column=0, columnspan=3, sticky="nesw")
        optionMenu.config(font=self.menuFont, relief=tk.GROOVE)

        global inputNum02
        inputNum02 = tk.Text(self.window, width=30, height=1, relief="groove",\
                             font=self.font, background="gray95", padx=10)
        inputNum02.grid(row=2, column=0, columnspan=4)
        inputNum02.insert(tk.END, "0")
        self.printResult = 1
        inputNum02.configure(state="disabled")

        variable = tk.StringVar(self.window)
        variable.set("인치")
        optionMenu02 = tk.OptionMenu(self.window, variable,
                                     "밀리미터", "센티미터", "미터", "킬로미터",
                                     "인치", "피트", "야드", "마일",
                                     command=self.setLowerOptionValue)
        self.lowerValue = "인치"
        optionMenu02.grid(row=3, column=0, columnspan=3, sticky="nesw")
        optionMenu02.config(font=self.menuFont, relief=tk.GROOVE)
        self.lengthChanger()

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
            # 길이는 음수 전환 불가
            if button == "±":
                buttonObject.configure(state="disabled")
            # 결과 출력 버튼 색 변경
            if button == "←":
                buttonObject.configure(bg="skyblue")
            colIndex += 1
            if colIndex > 2:
                rowIndex += 1
                colIndex = 0
        self.window.bind("<Key>", self.pressButtonKey)

    def lengthChanger(self):
        inputNum02.configure(state=tk.NORMAL)
        inputNum02.delete("1.0", tk.END)
        inputNum02.configure(state="disabled")
        # 센티 미터를 기준으로 반환할 때
        if self.upperValue == "센티미터":
            if self.lowerValue == "밀리미터":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number * 10)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "센티미터":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "미터":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number / 100)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "킬로미터":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number / 100000)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "인치":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number / 2.54)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "피트":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number / 30.48)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "야드":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number / 91.44)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "마일":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number / 160934.4)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
        # 밀리미터를 기준으로 변환할 때
        elif self.upperValue == "밀리미터":
            if self.lowerValue == "밀리미터":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "센티미터":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number / 10)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "미터":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number / 1000)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "킬로미터":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number / 1000000)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "인치":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number / 25.4)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "피트":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number / 304.8)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "야드":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number / 914.4)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "마일":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number / 1609344)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
        # 미터를 기준으로 변환할 때
        elif self.upperValue == "미터":
            if self.lowerValue == "밀리미터":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number * 1000)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "센티미터":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number * 100)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "미터":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "킬로미터":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number / 1000)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "인치":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number * 39.37008)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "피트":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number * 3.28084)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "야드":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number * 1.093613)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "마일":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number / 1609.344)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
        # 킬로미터를 기준으로 변환할 때
        elif self.upperValue == "킬로미터":
            if self.lowerValue == "밀리미터":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number * 1000000)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "센티미터":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number * 100000)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "미터":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number * 1000)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "킬로미터":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "인치":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number * 39370.08)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "피트":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number * 3280.84)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "야드":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number * 1093.613)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "마일":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number / 1.609344)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
        # 인치를 기준으로 변환할 때
        elif self.upperValue == "인치":
            if self.lowerValue == "밀리미터":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number * 25.4)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "센티미터":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number * 2.54)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "미터":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(round(number / 39.370079, 10))
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "킬로미터":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(round(number / 39370.079, 10))
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "인치":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "피트":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(round(number / 12, 10))
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "야드":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(round(number / 36, 10))
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "마일":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(round(number / 63360, 10))
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
        # 피트를 기준으로 변환할 때
        elif self.upperValue == "피트":
            if self.lowerValue == "밀리미터":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number * 304.8)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "센티미터":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number * 30.48)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "미터":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(round(number / 3.2808398, 10))
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "킬로미터":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(round(number / 3280.8398, 10))
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "인치":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number * 12)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "피트":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "야드":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(round(number / 3, 10))
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "마일":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(round(number / 5280, 10))
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
        # 야드를 기준으로 변환할 때
        elif self.upperValue == "야드":
            if self.lowerValue == "밀리미터":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number * 914.4)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "센티미터":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number * 91.44)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "미터":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(round(number / 1.093613, 10))
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "킬로미터":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(round(number / 1093.613, 10))
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "인치":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number * 36)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "피트":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number * 3)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "야드":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "마일":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(round(number / 1760, 10))
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
        # 마일을 기준으로 변환할 때
        elif self.upperValue == "마일":
            if self.lowerValue == "밀리미터":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number * 1609344)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "센티미터":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number * 160934.4)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "미터":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number * 1609.344)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "킬로미터":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number * 1.609344)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "인치":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number * 63360)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "피트":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number * 5280)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "야드":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number * 1760)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")
            elif self.lowerValue == "마일":
                number = inputNum.get("1.0", tk.INSERT)
                number = float(number)
                result = str(number)
                inputNum02.configure(state=tk.NORMAL)
                inputNum02.insert("1.0", result)
                inputNum02.configure(state="disabled")