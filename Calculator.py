from tkinter import *
from tkinter.font import *
from math import *
from decimal import Decimal

window = Tk()
window.title("종합 계산기")
window.resizable(0, 0)
font = Font(family="맑은 고딕", size=15)
screenObject = None

def all_children(window):
    widget_list = window.winfo_children()

    for item in widget_list :
        if item.winfo_children():
            widget_list.extend(item.winfo_children())
        return widget_list

class Calculator:
    #결과 출력 여부 체크
    printResult = 0

    #생성자
    def __init__(self, screen):
        self.setScreenValue(screen)

    #화면 구성 변수 설정 (산술, 공학, 단위 등)
    def setScreenValue(self, buttonValue):
        self.printWindow(buttonValue)

    #버튼 키보드 입력 이벤트
    def pressButtonKey(self, event):
        if event.keycode == 13 or event.char == "=": #Return (결과 반환)
            result = eval(inputNum.get("1.0", END))
            strResult = str(result)
            inputNum.configure(state=NORMAL)
            inputNum.insert(END, "\n", "tag-right")
            inputNum.insert("2.0", "= " + strResult, "tag-right")
            #eval()메소드의 취약점 해결을 위해 버튼을 제외한 임의의 입력 제한
            inputNum.configure(state="disabled")
            self.printResult = 1
        elif event.keycode == 27 : #Escape (결과창 초기화)
            inputNum.configure(state=NORMAL)
            inputNum.delete("1.0", END)
            inputNum.insert(END, "0", "tag-right")
            self.printResult = 1
            inputNum.configure(state="disabled")
        elif event.keycode == 8: #Backspace (지우기)
            inputNum.configure(state=NORMAL)
            inputNum.delete("%s-1c" % INSERT, INSERT)
            inputNum.configure(state="disabled")
        else :
            #연산 결과를 활용해 연계 계산을 위한 조건
            if self.printResult == 1:
                if event.char.isdigit():
                    inputNum.configure(state=NORMAL)
                    inputNum.delete("1.0", END)
                    inputNum.configure(state="disabled")
                    self.printResult = 0
                else :
                    inputNum.configure(state=NORMAL)
                    pastResult = inputNum.get("2.2", "%s" % INSERT)
                    inputNum.delete("1.0", END)
                    inputNum.insert("1.0", pastResult, "tag-right")
                    inputNum.configure(state="disabled")
            self.printResult = 0
            inputNum.configure(state=NORMAL)
            inputNum.insert(INSERT, event.char, "tag-right")
            inputNum.configure(state="disabled")
            entryString = str(inputNum.get("1.0", INSERT))
            if len(entryString) > 1:
                # 수식의 맨 앞에 불필요한 0이 오지 않도록 자동 제거
                if entryString[0] == "0":
                    #소수점 앞 0은 제거하지 않음
                    if entryString[1] == ".":
                        pass
                    else:
                        inputNum.configure(state=NORMAL)
                        inputNum.delete("1.0", "1.1")
                        inputNum.configure(state="disabled")
                # 식을 완성하지 않고 다른 연산자를 입력 시 자동 변환
                if not entryString[-1].isdigit():
                    if not entryString[-2].isdigit():
                        if entryString[-2] == ")" or entryString[-2] == "(":
                            pass
                        else:
                            inputNum.configure(state=NORMAL)
                            inputNum.delete("%s-2c" % INSERT, INSERT)
                            inputNum.insert(INSERT, event.char, "tag-right")
                            inputNum.configure(state="disabled")
    
    #버튼 클릭 이벤트
    def pressButton(self, value):
        if value == "=":
            #버튼 상에서의 연산자를 eval 가능한 연산자로 치환
            expression = inputNum.get("1.0", END)
            if expression.find("Mod"):
                expression = expression.replace("Mod", "%")
            if expression.find("OR"):
                expression = expression.replace("OR", "|")
            if expression.find("XOR"):
                expression = expression.replace("XOR", "^")
            if expression.find("AND"):
                expression = expression.replace("AND", "&")
            if expression.find("Lsh"):
                expression = expression.replace("Lsh", "<<")
            if expression.find("Rsh"):
                expression = expression.replace("Rsh", ">>")
            try:
                result = eval(expression)
                strResult = str(result)
                inputNum.configure(state=NORMAL)
                inputNum.insert(END, "\n", "tag-right")
                inputNum.insert("2.0", "= " + strResult, "tag-right")
                # eval()메소드의 취약점 해결을 위해 버튼을 제외한 임의의 입력 제한
                inputNum.configure(state="disabled")
                self.printResult = 1
            except ZeroDivisionError:
                inputNum.configure(state=NORMAL)
                inputNum.insert(END, "\n", "tag-right")
                inputNum.insert("2.0", "0으로 나눌 수 없습니다.", "tag-right")
                inputNum.configure(state="disabled")
                self.printResult = 1
        elif value == "종료" :
            window.destroy()
        elif value == "C" :
            inputNum.configure(state=NORMAL)
            inputNum.delete("1.0", END)
            inputNum.insert(END, "0", "tag-right")
            self.printResult = 1
            inputNum.configure(state="disabled")
        elif value == "←":
            if not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                inputNum.delete("%s-1c" % INSERT, INSERT)
                inputNum.configure(state="disabled")
            else:
                pass
        #계산기 변경 버튼
        elif value == "공학":
            widget_list = all_children(window)
            for item in widget_list:
                item.grid_forget()
            self.setScreenValue(value)
        elif value == "산술":
            widget_list = all_children(window)
            for item in widget_list:
                item.grid_forget()
            self.setScreenValue(value)
        elif value == "컴퓨터":
            widget_list = all_children(window)
            for item in widget_list:
                item.grid_forget()
            self.setScreenValue(value)
        #연산 버튼
        elif value == "%":
            #연산 결과를 활용해 연계 계산을 위한 조건
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                print(pastResult)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            print(inputNum.get("1.0", END))
            number = float(inputNum.get("1.0", END))
            result = str(number/100.0)
            inputNum.configure(state=NORMAL)
            #연산 기호를 포함한 출력
            inputNum.insert(END, value + "\n", "tag-right")
            inputNum.insert("2.0", "= " + result, "tag-right")
            inputNum.configure(state="disabled")
            self.printResult = 1
        elif value == "sin":
            #연산 결과를 활용해 연계 계산을 위한 조건
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                print(pastResult)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            number = float(inputNum.get("1.0", END))
            radian = radians(number)
            result = str(round(sin(radian), 4))
            inputNum.configure(state=NORMAL)
            #연산 기호를 포함한 출력
            inputNum.delete("1.0", END)
            inputNum.insert("1.0", value+"("+str(number)+")"+"\n", "tag-right")
            inputNum.insert("2.0", "= "+result, "tag-right")
            inputNum.configure(state="disabled")
            self.printResult = 1
        elif value == "cos":
            #연산 결과를 활용해 연계 계산을 위한 조건
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                print(pastResult)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            number = float(inputNum.get("1.0", END))
            radian = radians(number)
            result = str(round(cos(radian), 4))
            inputNum.configure(state=NORMAL)
            #연산 기호를 포함한 출력
            inputNum.delete("1.0", END)
            inputNum.insert("1.0", value+"("+str(number)+")"+"\n", "tag-right")
            inputNum.insert("2.0", "= "+result, "tag-right")
            inputNum.configure(state="disabled")
            self.printResult = 1
        elif value == "tan":
            #연산 결과를 활용해 연계 계산을 위한 조건
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                print(pastResult)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            number = float(inputNum.get("1.0", END))
            radian = radians(number)
            result = str(round(tan(radian), 4))
            inputNum.configure(state=NORMAL)
            #연산 기호를 포함한 출력
            inputNum.delete("1.0", END)
            inputNum.insert("1.0", value+"("+str(number)+")"+"\n", "tag-right")
            inputNum.insert("2.0", "= "+result, "tag-right")
            inputNum.configure(state="disabled")
            self.printResult = 1
        elif value == "π":
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                print(pastResult)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            number = float(inputNum.get("1.0", END))
            result = str(pi * number)
            inputNum.configure(state=NORMAL)
            #연산 기호를 포함한 출력
            inputNum.delete("1.0", END)
            inputNum.insert("1.0", str(number)+ "π"+"\n", "tag-right")
            inputNum.insert("2.0", "= "+result, "tag-right")
            inputNum.configure(state="disabled")
            self.printResult = 1
        elif value == "x²":
            #연산 결과를 활용해 연계 계산을 위한 조건
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                print(pastResult)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            number = float(inputNum.get("1.0", END))
            result = str(pow(number, 2))
            inputNum.configure(state=NORMAL)
            #연산 기호를 포함한 출력
            inputNum.insert(END, "²" + "\n", "tag-right")
            inputNum.insert("2.0", "= " + result, "tag-right")
            inputNum.configure(state="disabled")
            self.printResult = 1
        elif value == "xʸ":
            #연산 결과를 활용해 연계 계산을 위한 조건
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                print(pastResult)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            self.printResult = 0
            inputNum.configure(state=NORMAL)
            inputNum.insert(INSERT, "**", "tag-right")
            inputNum.configure(state="disabled")
        elif value == "10ˣ":
            #연산 결과를 활용해 연계 계산을 위한 조건
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                print(pastResult)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            number = int(inputNum.get("1.0", END))
            numberStr = str(number)
            if number > 31:
                result = f"{Decimal(10 ** number):.2e}"
            else:
                result = str(10 ** number)
            inputNum.configure(state=NORMAL)
            #연산 기호를 포함한 출력
            inputNum.delete("1.0", END)
            inputNum.insert("1.0","10^"+numberStr, "tag-right")
            inputNum.insert(END, "\n", "tag-right")
            inputNum.insert("2.0", "= " + result, "tag-right")
            inputNum.configure(state="disabled")
            self.printResult = 1
        elif value == "√x":
            #연산 결과를 활용해 연계 계산을 위한 조건
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                print(pastResult)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            number = float(inputNum.get("1.0", END))
            result = str(sqrt(number))
            inputNum.configure(state=NORMAL)
            #연산 기호를 포함한 출력
            inputNum.insert("1.0","√", "tag-right")
            inputNum.insert(END, "\n", "tag-right")
            inputNum.insert("2.0", "= " + result, "tag-right")
            inputNum.configure(state="disabled")
            self.printResult = 1
        elif value == "x²":
            #연산 결과를 활용해 연계 계산을 위한 조건
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                print(pastResult)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            number = float(inputNum.get("1.0", END))
            result = str(pow(number, 2))
            inputNum.configure(state=NORMAL)
            #연산 기호를 포함한 출력
            inputNum.insert(END, "²" + "\n", "tag-right")
            inputNum.insert("2.0", "= " + result, "tag-right")
            inputNum.configure(state="disabled")
            self.printResult = 1
        elif value == "1/x":
            #연산 결과를 활용해 연계 계산을 위한 조건
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                print(pastResult)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            try:
                number = float(inputNum.get("1.0", END))
                result = str(1/number)
                inputNum.configure(state=NORMAL)
                inputNum.insert("1.0", "1/", "tag-right")
                inputNum.insert(END, "\n", "tag-right")
                inputNum.insert("2.0", "= " + result, "tag-right")
                inputNum.configure(state="disabled")
                self.printResult = 1
            except ZeroDivisionError:
                inputNum.configure(state=NORMAL)
                inputNum.insert("1.0", "1/", "tag-right")
                inputNum.insert(END, "\n", "tag-right")
                inputNum.insert("2.0", "0으로 나눌 수 없습니다.", "tag-right")
                inputNum.configure(state="disabled")
                self.printResult = 1
        #Factorial 연산
        elif value == "n!":
            #연산 결과를 활용해 연계 계산을 위한 조건
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                print(pastResult)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            number = int(inputNum.get("1.0", END))
            result = factorial(number)
            inputNum.configure(state=NORMAL)
            inputNum.insert(END, "!\n", "tag-right")
            inputNum.insert("2.0", "= " + str(result), "tag-right")
            inputNum.configure(state="disabled")
            self.printResult = 1
        #Mod 연산
        elif value == "Mod":
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                print(pastResult)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            self.printResult = 0
            inputNum.configure(state=NORMAL)
            inputNum.insert(INSERT, " Mod ", "tag-right")
            inputNum.configure(state="disabled")
        elif value == "OR":
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                print(pastResult)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            self.printResult = 0
            inputNum.configure(state=NORMAL)
            inputNum.insert(INSERT, " OR ", "tag-right")
            inputNum.configure(state="disabled")
        elif value == "XOR":
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                print(pastResult)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            self.printResult = 0
            inputNum.configure(state=NORMAL)
            inputNum.insert(INSERT, " XOR ", "tag-right")
            inputNum.configure(state="disabled")
        elif value == "NOT":
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                print(pastResult)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            number = int(inputNum.get("1.0", END))
            xorresult = ~number
            result = str(xorresult)
            self.printResult = 0
            inputNum.configure(state=NORMAL)
            inputNum.insert("1.0", "~", "tag-right")
            inputNum.insert(END, "\n", "tag-right")
            inputNum.insert("2.0", "= " + result, "tag-right")
            inputNum.configure(state="disabled")
            self.printResult = 1
        elif value == "AND":
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                print(pastResult)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            self.printResult = 0
            inputNum.configure(state=NORMAL)
            inputNum.insert(INSERT, " AND ", "tag-right")
            inputNum.configure(state="disabled")
        elif value == "LShift":
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                print(pastResult)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            self.printResult = 0
            inputNum.configure(state=NORMAL)
            inputNum.insert(INSERT, " Lsh ", "tag-right")
            inputNum.configure(state="disabled")
        elif value == "RShift":
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                print(pastResult)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            self.printResult = 0
            inputNum.configure(state=NORMAL)
            inputNum.insert(INSERT, " Rsh ", "tag-right")
            inputNum.configure(state="disabled")
        else :
            #초기 화면 숫자 0표기와 다른 숫자 입력시 0을 지우기 위한 로직
            if self.printResult == 1:
                if value.isdigit():
                    inputNum.configure(state=NORMAL)
                    inputNum.delete("1.0", END)
                    inputNum.configure(state="disabled")
                    self.printResult = 0
                else :
                    #초기 화면 숫자 0으로 연산 하기 위한 조건
                    if inputNum.get("1.0", END) == "0\n":
                        pass
                    else:
                        inputNum.configure(state=NORMAL)
                        pastResult = inputNum.get("2.2", "%s" % INSERT)
                        inputNum.delete("1.0", END)
                        inputNum.insert("1.0", pastResult, "tag-right")
                        inputNum.configure(state="disabled")
            #일반적인 입력
            self.printResult = 0
            inputNum.configure(state=NORMAL)
            inputNum.insert(INSERT, value, "tag-right")
            inputNum.configure(state="disabled")
            entryString = inputNum.get("1.0", INSERT)
            if len(entryString) > 1:
                # 수식의 맨 앞에 불필요한 0이 오지 않도록 자동 제거
                if entryString[0] == "0":
                    #소수점 앞 0은 제거하지 않음
                    if entryString[1] == ".":
                        pass
                    else:
                        inputNum.configure(state=NORMAL)
                        inputNum.delete("1.0", "1.1")
                        inputNum.configure(state="disabled")
                # 식을 완성하지 않고 다른 연산자를 입력 시 자동 변환
                if not entryString[-1].isdigit():
                    if not entryString[-2].isdigit():
                        if entryString[-2] == ")" or entryString[-2] == "(":
                            pass
                        else:
                            inputNum.configure(state=NORMAL)
                            inputNum.delete("%s-2c" % INSERT, INSERT)
                            inputNum.insert(INSERT, value, "tag-right")
                            inputNum.configure(state="disabled")

    def printWindow(self, screenValue):
        #버튼 그리드 변수
        rowIndex = 1
        colIndex = 0
        
        #버튼 텍스트 변수
        if screenValue == "산술":
            buttonText = [
                '%', '√x', 'x²', '1/x','←',
                '7', '8', '9', '/', 'C',
                '4', '5', '6', '*', '공학',
                '1', '2', '3', '-', '컴퓨터',
                '.', '0', '=', '+', '종료' ]
        elif screenValue == "공학":
            buttonText = [
                'sin', 'cos', 'tan', 'π','←',
                'x²', 'xʸ', '√x', '10ˣ', 'n!',
                '7', '8', '9', '/', 'C',
                '4', '5', '6', '*', '산술',
                '1', '2', '3', '-', '컴퓨터',
                '.', '0', '=', '+', '종료' ]
        elif screenValue == "컴퓨터":
            buttonText = [
                'Mod', 'OR', 'XOR', 'NOT', 'AND',
                'LShift', 'RShift', '(', ')', '←',
                '7', '8', '9', '/', 'C',
                '4', '5', '6', '*', '산술',
                '1', '2', '3', '-', '공학',
                '.', '0', '=', '+', '종료',
                ]
        
        
        #결과 표시창
        global inputNum
        inputNum = Text(window, width=30, height=3, relief="groove",\
                        font=font, background="gray95", pady=5, padx=10)
        inputNum.tag_configure('tag-right', justify="right")
        inputNum.grid(row=0, column=0, columnspan=5, pady=5,ipady=20, ipadx=5)
        inputNum.insert(END, "0", "tag-right")
        inputNum.configure(state="disabled")
        self.printResult = 1
        buttonList = []
        index = 0
        #버튼 표시
        for button in buttonText :
            def click(t = button):
                self.pressButton(t)
            buttonObject = Button(window, text=button, width=6, height=2,\
                                  relief="groove", command=click, font=font, padx=0, pady=0)
            buttonObject.grid(row=rowIndex, column=colIndex)
            buttonList.append(buttonObject)
            if screenValue == "컴퓨터" and button == ".":
                pointButton = buttonList[index]
                pointButton.configure(state="disabled")
            index += 1
            colIndex += 1
            if colIndex > 4 :
                rowIndex += 1
                colIndex = 0
        print(buttonList)
        window.bind("<Key>", self.pressButtonKey)
        window.mainloop()

if __name__ == "__main__":
    mainCalc = Calculator("산술")
