from tkinter import *
from tkinter.font import *
from math import *

class GeneralCalc:
    #결과 출력 여부 체크
    printResult = 0

    #Entry에 있는 식 저장용 변수
    entryString = []

    #버튼 키보드 입력 이벤트
    def pressButtonKey(self, event):
        if event.keycode == 13: #Return (결과 반환)
            result = eval(inputNum.get("1.0", END))
            strResult = str(result)
            inputNum.configure(state=NORMAL)
            inputNum.insert(END, "\n", "tag-right")
            inputNum.insert("2.0", "= " + strResult, "tag-right")
            #eval()메소드의 취약점 해결을 위해 버튼을 제외한 임의의 입력 제한
            inputNum.configure(state="disabled")
            GeneralCalc.printResult = 1
        elif event.keysym == "<Escape>" : #Escape (결과창 초기화)
            inputNum.configure(state=NORMAL)
            inputNum.delete("1.0", END)
            inputNum.configure(state="disabled")
        elif event.keycode == 8: #Backspace (지우기)
            inputNum.configure(state=NORMAL)
            inputNum.delete("%s-1c" % INSERT, INSERT)
            inputNum.configure(state="disabled")
        else :
            #연산 결과를 활용해 연계 계산을 위한 조건
            if GeneralCalc.printResult == 1:
                if event.char.isdigit():
                    inputNum.configure(state=NORMAL)
                    inputNum.delete("1.0", END)
                    inputNum.configure(state="disabled")
                    GeneralCalc.printResult = 0
                else :
                    inputNum.configure(state=NORMAL)
                    pastResult = inputNum.get("2.2", "%s" % INSERT)
                    print(pastResult)
                    inputNum.delete("1.0", END)
                    inputNum.insert("1.0", pastResult, "tag-right")
                    inputNum.configure(state="disabled")
            GeneralCalc.printResult = 0
            inputNum.configure(state=NORMAL)
            inputNum.insert(INSERT, event.char, "tag-right")
            inputNum.configure(state="disabled")
            entryString = str(inputNum.get("1.0", INSERT))
            if len(entryString) > 1:
                if not entryString[-1].isdigit():
                    if not entryString[-2].isdigit():
                        print("enter")
                        print(entryString)
                        inputNum.configure(state=NORMAL)
                        inputNum.delete("%s-2c" % INSERT, INSERT)
                        print(entryString)
                        inputNum.insert(INSERT, event.char, "tag-right")
                        inputNum.configure(state="disabled")
    
    #버튼 클릭 이벤트
    def pressButton(self, value):
        if value == "=":
            result = eval(inputNum.get("1.0", END))
            strResult = str(result)
            inputNum.configure(state=NORMAL)
            inputNum.insert(END, "\n", "tag-right")
            inputNum.insert("2.0", "= " + strResult, "tag-right")
            #eval()메소드의 취약점 해결을 위해 버튼을 제외한 임의의 입력 제한
            inputNum.configure(state="disabled")
            GeneralCalc.printResult = 1
        elif value == "종료" :
            window.destroy()
        elif value == "C" :
            inputNum.configure(state=NORMAL)
            inputNum.delete("1.0", END)
            inputNum.configure(state="disabled")
        elif value == "←":
            inputNum.configure(state=NORMAL)
            inputNum.delete("%s-1c" % INSERT, INSERT)
            inputNum.configure(state="disabled")
        elif value == "%":
            #연산 결과를 활용해 연계 계산을 위한 조건
            if GeneralCalc.printResult == 1:
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                print(pastResult)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            number = float(inputNum.get("1.0", END))
            result = str(number/100.0)
            inputNum.configure(state=NORMAL)
            #연산 기호를 포함한 출력
            inputNum.insert(END, value + "\n", "tag-right")
            inputNum.insert("2.0", "= " + result, "tag-right")
            inputNum.configure(state="disabled")
            GeneralCalc.printResult = 1
        elif value == "√x":
            #연산 결과를 활용해 연계 계산을 위한 조건
            if GeneralCalc.printResult == 1:
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
            GeneralCalc.printResult = 1
        elif value == "x²":
            #연산 결과를 활용해 연계 계산을 위한 조건
            if GeneralCalc.printResult == 1:
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
            GeneralCalc.printResult = 1
        elif value == "1/x":
            #연산 결과를 활용해 연계 계산을 위한 조건
            if GeneralCalc.printResult == 1:
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                print(pastResult)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            number = float(inputNum.get("1.0", END))
            result = str(1/number)
            inputNum.configure(state=NORMAL)
            inputNum.insert("1.0", "1/", "tag-right")
            inputNum.insert(END, "\n", "tag-right")
            inputNum.insert("2.0", "= " + result, "tag-right")
            inputNum.configure(state="disabled")
            GeneralCalc.printResult = 1
        else :
            if GeneralCalc.printResult == 1:
                if value.isdigit():
                    inputNum.configure(state=NORMAL)
                    inputNum.delete("1.0", END)
                    inputNum.configure(state="disabled")
                    GeneralCalc.printResult = 0
                else :
                    inputNum.configure(state=NORMAL)
                    pastResult = inputNum.get("2.2", "%s" % INSERT)
                    inputNum.delete("1.0", END)
                    inputNum.insert("1.0", pastResult, "tag-right")
                    inputNum.configure(state="disabled")
            GeneralCalc.printResult = 0
            inputNum.configure(state=NORMAL)
            inputNum.insert(INSERT, value, "tag-right")
            inputNum.configure(state="disabled")
            entryString = str(inputNum.get("1.0", INSERT))
            #식을 완성하지 않고 다른 연산자를 입력 시 자동 변환
            if len(entryString) > 1:
                if not entryString[-1].isdigit():
                    if not entryString[-2].isdigit():
                        print("enter")
                        inputNum.configure(state=NORMAL)
                        inputNum.delete("%s-2c" % INSERT, INSERT)
                        inputNum.insert(INSERT, value, "tag-right")
                        inputNum.configure(state="disabled")

    def printWindow(self):
        #버튼 그리드 변수
        rowIndex = 1
        colIndex = 0
        
        #버튼 텍스트 변수
        buttonText = [
            '%', '√x', 'x²', '1/x','←',
            '7', '8', '9', '/', 'C',
            '4', '5', '6', '*', '공학',
            '1', '2', '3', '-', '단위',
            '.', '0', '=', '+', '종료' ]
        
        #기본 화면
        global window
        window = Tk()
        window.title("종합 계산기")
        window.resizable(0, 0)
        font = Font(family="맑은 고딕", size=15)
        
        #결과 표시창
        global inputNum
        inputNum = Text(window, width=30, height=3, relief="groove",\
                        font=font, background="gray95", pady=5, padx=10)
        inputNum.tag_configure('tag-right', justify="right")
        inputNum.configure(state="disabled")
        inputNum.grid(row=0, column=0, columnspan=5, pady=5,ipady=20, ipadx=5)

        for button in buttonText :
            def click(t = button):
                self.pressButton(t)
            Button(window, text=button, width=6, height=2,\
                relief="groove", command=click, font=font, padx=0, pady=0)\
                .grid(row=rowIndex, column=colIndex)
            colIndex += 1
            if colIndex > 4 :
                rowIndex += 1
                colIndex = 0
        window.bind("<Key>", self.pressButtonKey)
        window.mainloop()

if __name__ == "__main__":
    mainCalc = GeneralCalc()
    mainCalc.printWindow()
