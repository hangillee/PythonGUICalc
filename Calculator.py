from tkinter import *
from tkinter.font import *
from math import *
from decimal import Decimal
import UnitChanger as uc

# Tkinter 객체 생성
window = Tk()
window.title("종합 계산기")
window.resizable(0, 0)

# 폰트 변경을 위한 폰트 객체
font = Font(family="맑은 고딕", size=15)

# 모든 위젯 리스트에 저장 (새 화면 출력을 위함)
def allChildren(window):
    widgetList = window.winfo_children()
    for item in widgetList:
        if item.winfo_children():
            widgetList.extend(item.winfo_children())
        return widgetList

#단위 변환 객체
unitChanger = uc.UnitChanger(window, allChildren)

class Calculator:
    # 결과 출력 여부 체크
    printResult = 0

    # ZeroDivision 예외 처리를 위한 변수
    # 연산자 버튼 객체 리스트
    expButtonList = []
    # 연산자 버튼 텍스트 리스트
    expButtonText = []
    isZeroDivision = 0

    # 양수 음수 전환을 위한 변수
    isPlusMinus = 0

    # 진수 변환을 위한 변수들
    radioValue = IntVar()
    alphaButtonList = []
    octButtonList = []
    binButtonList = []

    # 프로그래머용 계산기 변수
    isComputerCalc = 0
    pastValue = 0

    # 연산자 키 이벤트 처리용 변수
    specialChars = [
        'quoteleft', 'exclam', 'at', 'numbersign', 'asciitilde',
        'dollar', 'percent', 'asciicircum', 'ampersand'
    ]

    # 소수점 반복 출력 방지용 변수
    isPointPrint = 0

    # 버튼 키보드 입력 이벤트
    def pressButtonKey(self, event):
        print(event)
        if event.keycode == 13 or event.char == "=": # Return (결과 반환)
            # 버튼 상에서의 연산자를 eval 가능한 연산자로 치환
            expression = inputNum.get("1.0", END)
            expression = expression.strip("\n")
            if self.isComputerCalc == 1:
                if "/" in expression:
                    expression = expression.replace("/", "//")
            if expression.find(" Mod "):
                expression = expression.replace(" Mod ", "%")
            if expression.find(" OR "):
                if "NOR" in expression:
                    expression = "~(" + expression + ")"
                    expression = expression.replace(" NOR ", "|")
                expression = expression.replace(" OR ", "|")
            if expression.find(" XOR "):
                expression = expression.replace(" XOR ", "^")
            if expression.find(" AND "):
                if "NAND" in expression:
                    expression = "~(" + expression + ")"
                    expression = expression.replace(" NAND ", "&")
                expression = expression.replace(" AND ", "&")
            if expression.find(" Lsh "):
                expression = expression.replace(" Lsh ", "<<")
            if expression.find(" Rsh "):
                expression = expression.replace(" Rsh ", ">>")
            numericType = self.radioValue.get()
            # 16진수
            if numericType == 1:
                # 16진수 계산식을 만들기 위한 변수들
                tempString = ""
                enterNumber = ""
                entryString = expression
                isBracket = 0

                if len(entryString) > 0:
                    index = 0
                    # 연산을 위해 0x를 붙힐 위치 선정
                    if entryString[0].isdigit() \
                            or ord(entryString[index]) in range(ord("A"), ord("G")) \
                            or entryString[0] == "~" and not self.printResult == 1:
                        while index < len(entryString):
                            # 숫자가 아니고, A~F 사이의 16진수 수가 아닐 때
                            if not entryString[index].isdigit() \
                                    and not ord(entryString[index]) in range(ord("A"), ord("G")):
                                if entryString[index] == "~" or entryString[index] == "(":
                                    tempString += entryString[index]
                                    index += 1
                                    continue
                                elif entryString[index] == ")":
                                    isBracket = 1
                                    tempString += "0x" + enterNumber + entryString[index]
                                    break
                                elif entryString[index] == "<":
                                    tempString += "0x" + enterNumber + entryString[index] + entryString[index+1]
                                    enterNumber = ""
                                    index += 2
                                elif entryString[index] == ">":
                                    tempString += "0x" + enterNumber + entryString[index] + entryString[index+1]
                                    enterNumber = ""
                                    index += 2
                                elif entryString[index] == "/":
                                    tempString += "0x" + enterNumber + entryString[index] + entryString[index+1]
                                    enterNumber = ""
                                    index += 2
                                else:
                                    tempString += "0x" + enterNumber + entryString[index]
                                    enterNumber = ""
                                    index += 1
                                    continue
                            enterNumber += str(entryString[index])
                            index += 1
                        if not isBracket == 1:
                            tempString += "0x" + enterNumber
                        expression = tempString
            # 8진수
            elif numericType == 3:
                # 8진수 계산식을 만들기 위한 변수들
                tempString = ""
                enterNumber = ""
                entryString = expression
                isBracket = 0

                if len(entryString) > 0:
                    index = 0
                    # 연산을 위해 0x를 붙힐 위치 선정
                    if entryString[0].isdigit() and not self.printResult == 1:
                        while index < len(entryString):
                            if not entryString[index].isdigit():
                                if entryString[index] == "~" or entryString[index] == "(":
                                    tempString += entryString[index]
                                    index += 1
                                    continue
                                elif entryString[index] == ")":
                                    isBracket = 1
                                    tempString += "0o" + enterNumber + entryString[index]
                                    break
                                elif entryString[index] == "<":
                                    tempString += "0o" + enterNumber + entryString[index] + entryString[index+1]
                                    enterNumber = ""
                                    index += 2
                                elif entryString[index] == ">":
                                    tempString += "0o" + enterNumber + entryString[index] + entryString[index+1]
                                    enterNumber = ""
                                    index += 2
                                elif entryString[index] == "/":
                                    tempString += "0o" + enterNumber + entryString[index] + entryString[index+1]
                                    enterNumber = ""
                                    index += 2
                                else:
                                    tempString += "0o" + enterNumber + entryString[index]
                                    enterNumber = ""
                                    index += 1
                                    continue
                            enterNumber += str(entryString[index])
                            index += 1
                        if not isBracket == 1:
                            tempString += "0o" + enterNumber
                        expression = tempString
            # 2진수
            elif numericType == 4:
                # 2진수 계산식을 만들기 위한 변수들
                tempString = ""
                enterNumber = ""
                entryString = expression
                isBracket = 0

                if len(entryString) > 0:
                    index = 0
                    # 연산을 위해 0x를 붙힐 위치 선정
                    if entryString[0].isdigit() and not self.printResult == 1:
                        while index < len(entryString):
                            if not entryString[index].isdigit():
                                if entryString[index] == "~" or entryString[index] == "(":
                                    tempString += entryString[index]
                                    index += 1
                                    continue
                                elif entryString[index] == ")":
                                    isBracket = 1
                                    tempString += "0b" + enterNumber + entryString[index]
                                    break
                                elif entryString[index] == "<":
                                    tempString += "0b" + enterNumber + entryString[index] + entryString[index+1]
                                    enterNumber = ""
                                    index += 2
                                elif entryString[index] == ">":
                                    tempString += "0b" + enterNumber + entryString[index] + entryString[index+1]
                                    enterNumber = ""
                                    index += 2
                                elif entryString[index] == "/":
                                    tempString += "0b" + enterNumber + entryString[index] + entryString[index+1]
                                    enterNumber = ""
                                    index += 2
                                else:
                                    tempString += "0b" + enterNumber + entryString[index]
                                    enterNumber = ""
                                    index += 1
                                    continue
                            enterNumber += str(entryString[index])
                            index += 1
                        if not isBracket == 1:
                            tempString += "0b" + enterNumber
                        expression = tempString
            # ZeroDivisionError 예외처리
            try:
                result = eval(expression)
                result = round(result, 12)
                strResult = str(result)
                if numericType == 1:
                    strResult = f'{int(hex(result), 16):01X}'
                elif numericType == 3:
                    strResult = f'{int(oct(result), 8):0o}'
                elif numericType == 4:
                    strResult = f'{int(bin(result), 2):0b}'
                inputNum.configure(state=NORMAL)
                inputNum.insert(END, "\n", "tag-right")
                inputNum.insert("2.0", "= " + strResult, "tag-right")
                # eval()메소드의 취약점 해결을 위해 버튼을 제외한 임의의 입력 제한
                inputNum.configure(state="disabled")
                self.printResult = 1
            except ZeroDivisionError:
                self.isZeroDivision = 1
                for expButton in self.expButtonList:
                    expButton.config(state="disabled")
                inputNum.configure(state=NORMAL)
                inputNum.insert(END, "\n", "tag-right")
                inputNum.insert("2.0", "0으로 나눌 수 없습니다.", "tag-right")
                inputNum.configure(state="disabled")
                self.printResult = 1
        # 전체 삭제
        elif event.keycode == 27:
            self.printResult = 1
            self.isZeroDivision = 0
            self.isPlusMinus = 0
            self.isPointPrint = 0
            # 버튼 활성화 비활성화 여부 결정
            for expButton in self.expButtonList:
                expButton.config(state=NORMAL)
            inputNum.configure(state=NORMAL)
            inputNum.delete("1.0", END)
            inputNum.insert(END, "0", "tag-right")
            self.printResult = 0
            inputNum.configure(state="disabled")
        # Backspace 기능
        elif event.keycode == 8 and not self.isZeroDivision:
            if len(inputNum.get("1.0", END)) == 2:
                inputNum.configure(state=NORMAL)
                inputNum.insert("1.0", "0", "tag-right")
                inputNum.configure(state="disabled")
            else:
                pass
            if not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                inputNum.delete("%s-1c" % INSERT, INSERT)
                inputNum.configure(state="disabled")
            else:
                pass
        else:
            # 초기 화면 0표기와 연산 결과를 활용해 연계 계산을 위한 조건
            if self.printResult == 1:
                if event.char.isdigit():
                    self.isZeroDivision = 0
                    inputNum.configure(state=NORMAL)
                    inputNum.delete("1.0", END)
                    inputNum.configure(state="disabled")
                    self.printResult = 0
                else:
                    if self.isZeroDivision:
                        inputNum.configure(state="disabled")
                    else:
                        # 초기 화면 숫자 0으로 연산 하기 위한 로직
                        if inputNum.get("1.0", END) == "0\n":
                            pass
                        else:
                            inputNum.configure(state=NORMAL)
                            pastResult = inputNum.get("2.2", "%s" % INSERT)
                            inputNum.delete("1.0", END)
                            inputNum.insert("1.0", pastResult, "tag-right")
                            inputNum.configure(state="disabled")
            # ZeroDivisionError가 일어나지 않았을 때만
            if not self.isZeroDivision and not event.keysym in self.specialChars or event.keycode == 16:
                self.printResult = 0
                inputNum.configure(state=NORMAL)
                # 프로그래머용 계산기일 경우 입력 제한
                if self.isComputerCalc == 1:
                    numericValue = self.radioValue.get()
                    # 10진수 입력
                    if numericValue == 2:
                        # 16진수 수 입력 금지 (모든 알파벳 포함)
                        if ord(event.char.upper()) in range(ord("A"), ord("Z")+1) or event.char == ".":
                            pass
                        else:
                            inputNum.insert(INSERT, event.char, "tag-right")
                            inputNum.configure(state="disabled")
                    # 8진수 입력
                    elif numericValue == 3:
                        # 16진수 수와 8, 9 입력 금지
                        if ord(event.char.upper()) in range(ord("A"), ord("Z")+1)\
                                or ord(event.char) in range(ord("8"), ord("9")+1)\
                                or event.char == ".":
                            pass
                        else:
                            inputNum.insert(INSERT, event.char, "tag-right")
                            inputNum.configure(state="disabled")
                    # 2진수 입력
                    elif numericValue == 4:
                        # 16진수 수와 2~9까지 입력 금지
                        if ord(event.char.upper()) in range(ord("A"), ord("Z")+1)\
                                or ord(event.char) in range(ord("2"), ord("9")+1)\
                                or event.char == ".":
                            pass
                        else:
                            inputNum.insert(INSERT, event.char, "tag-right")
                            inputNum.configure(state="disabled")
                    # 16진수 모든 입력 가능 (16진수 수 이외의 알파벳 제외)
                    else:
                        if ord(event.char.upper()) in range(ord("G"), ord("Z") + 1)\
                                or event.char == ".":
                            pass
                        else:
                            inputNum.insert(INSERT, event.char, "tag-right")
                            inputNum.configure(state="disabled")
                else:
                    if not event.char.isdigit():
                        #컴퓨터용 계산기 외의 계산기에서도 알파벳 입력 제한
                        if ord(event.char.upper()) in range(ord("A"), ord("Z") + 1):
                            pass
                        else:
                            inputNum.insert(INSERT, event.char, "tag-right")
                            inputNum.configure(state="disabled")
                    else:
                        inputNum.insert(INSERT, event.char, "tag-right")
                        inputNum.configure(state="disabled")
                    # 소수점이 출력되었음을 알림
                    if event.char == "." and self.isPointPrint == 0:
                        print("enter")
                        self.isPointPrint = 1
                        inputNum.insert(INSERT, event.char, "tag-right")
                        inputNum.configure(state="disabled")
                    elif self.isPointPrint == 1:
                        if event.char == ".":
                            inputNum.configure(state=NORMAL)
                            inputNum.delete("%s-1c" % INSERT, INSERT)
                            inputNum.configure(state="disabled")
                        elif not event.char.isdigit():
                            print("enter3")
                            inputNum.insert(INSERT, event.char, "tag-right")
                            inputNum.configure(state="disabled")
                            self.isPointPrint = 0
                entryString = inputNum.get("1.0", INSERT)
                # 괄호 갯수 입력 제한
                if event.char == ")":
                    if not entryString[-2].isdigit():
                        inputNum.delete("%s-1c" % INSERT, INSERT)
                    openBracket = entryString.count("(")
                    closeBracket = entryString.count(")")
                    if openBracket < closeBracket:
                        inputNum.delete("%s-1c" % INSERT, INSERT)
                if len(entryString) > 1:
                    if event.char == "(" and not entryString[0] == "0":
                        if entryString[-2].isdigit():
                            inputNum.delete("%s-1c" % INSERT, INSERT)
                # 버튼 활성화 비활성화 여부 결정
                for expButton in self.expButtonList:
                    expButton.config(state=NORMAL)
                inputNum.configure(state="disabled")
                if len(entryString) > 1:
                    # 수식의 맨 앞에 불필요한 0이 오지 않도록 자동 제거
                    if entryString[0] == "0":
                        # 연산자 앞 0은 제거하지 않음
                        if not entryString[1].isdigit():
                            # 괄호 입력 시에는 제거
                            if entryString[1] == "(":
                                inputNum.configure(state=NORMAL)
                                inputNum.delete("1.0", "1.1")
                                inputNum.configure(state="disabled")
                            if ord(entryString[1]) in range(ord("A"), ord("G")):
                                inputNum.configure(state=NORMAL)
                                inputNum.delete("1.0", "1.1")
                                inputNum.configure(state="disabled")
                            pass
                        else:
                            inputNum.configure(state=NORMAL)
                            inputNum.delete("1.0", "1.1")
                            inputNum.configure(state="disabled")
                    # 식을 완성하지 않고 다른 연산자를 입력 시 자동 변환
                    if not self.isZeroDivision:
                        if not entryString[-1].isdigit():
                            if not entryString[-2].isdigit():
                                if entryString[-2] == ")" or entryString[-2] == "(" or entryString[-1] == "(":
                                    pass
                                elif ord(entryString[-2]) in range(ord("A"), ord("G")) or ord(entryString[-1]) in range(ord("A"), ord("G")):
                                    pass
                                elif entryString[-1] == ".":
                                    if entryString[-2] == ".":
                                        inputNum.configure(state=NORMAL)
                                        inputNum.delete("%s-2c" % INSERT, INSERT)
                                        inputNum.insert(INSERT, event.char, "tag-right")
                                        inputNum.configure(state="disabled")
                                    else:
                                        inputNum.configure(state=NORMAL)
                                        inputNum.delete("%s-1c" % INSERT, INSERT)
                                        inputNum.insert(INSERT, "0" + event.char, "tag-right")
                                        inputNum.configure(state="disabled")
                                else:
                                    inputNum.configure(state=NORMAL)
                                    inputNum.delete("%s-2c" % INSERT, INSERT)
                                    inputNum.insert(INSERT, event.char, "tag-right")
                                    inputNum.configure(state="disabled")
                    # 연산자 뒤에 0이 나와 연산할 수 없는 경우 (소수점 제외)
                    if len(entryString) > 2:
                        if entryString[-1].isdigit():
                            if entryString[-2] == "0":
                                if not entryString[-3].isdigit() and not entryString[-3] == ".":
                                    entryString = entryString[:-2] + entryString[-1:]
                                    inputNum.configure(state=NORMAL)
                                    inputNum.delete("1.0", END)
                                    inputNum.insert(END, entryString, "tag-right")
                                    inputNum.configure(state="disabled")
    
    # 버튼 클릭 이벤트
    def pressButton(self, value):
        numericType = self.radioValue.get()
        if value == "=":
            # 버튼 상에서의 연산자를 eval 가능한 연산자로 치환
            expression = inputNum.get("1.0", END)
            expression = expression.strip("\n")
            if self.isComputerCalc == 1:
                if "/" in expression:
                    expression = expression.replace("/", "//")
            if expression.find(" Mod "):
                expression = expression.replace(" Mod ", "%")
            if expression.find(" OR "):
                if "NOR" in expression:
                    expression = "~(" + expression + ")"
                    expression = expression.replace(" NOR ", "|")
                expression = expression.replace(" OR ", "|")
            if expression.find(" XOR "):
                expression = expression.replace(" XOR ", "^")
            if expression.find(" AND "):
                if "NAND" in expression:
                    expression = "~(" + expression + ")"
                    expression = expression.replace(" NAND ", "&")
                expression = expression.replace(" AND ", "&")
            if expression.find(" Lsh "):
                expression = expression.replace(" Lsh ", "<<")
            if expression.find(" Rsh "):
                expression = expression.replace(" Rsh ", ">>")
            # 16진수
            if numericType == 1:
                # 16진수 계산식을 만들기 위한 변수들
                tempString = ""
                enterNumber = ""
                entryString = expression
                isBracket = 0

                if len(entryString) > 0:
                    index = 0
                    # 연산을 위해 0x를 붙힐 위치 선정
                    if entryString[0].isdigit()\
                            or ord(entryString[index]) in range(ord("A"), ord("G"))\
                            or entryString[0] == "~" and not self.printResult == 1:
                        while index < len(entryString):
                            # 숫자가 아니고, A~F 사이의 16진수 수가 아닐 때
                            if not entryString[index].isdigit()\
                                    and not ord(entryString[index]) in range(ord("A"), ord("G")):
                                if entryString[index] == "~" or entryString[index] == "(":
                                    tempString += entryString[index]
                                    index += 1
                                    continue
                                elif entryString[index] == ")":
                                    isBracket = 1
                                    tempString += "0x" + enterNumber + entryString[index]
                                    break
                                elif entryString[index] == "<":
                                    tempString += "0x" + enterNumber + entryString[index] + entryString[index+1]
                                    enterNumber = ""
                                    index += 2
                                elif entryString[index] == ">":
                                    tempString += "0x" + enterNumber + entryString[index] + entryString[index+1]
                                    enterNumber = ""
                                    index += 2
                                elif entryString[index] == "/":
                                    tempString += "0x" + enterNumber + entryString[index] + entryString[index + 1]
                                    enterNumber = ""
                                    index += 2
                                else:
                                    tempString += "0x" + enterNumber + entryString[index]
                                    enterNumber = ""
                                    index += 1
                                    continue
                            enterNumber += str(entryString[index])
                            index += 1
                        if not isBracket == 1:
                            tempString += "0x" + enterNumber
                        expression = tempString
            # 8진수
            elif numericType == 3:
                # 8진수 계산식을 만들기 위한 변수들
                tempString = ""
                enterNumber = ""
                entryString = expression
                isBracket = 0

                if len(entryString) > 0:
                    index = 0
                    # 연산을 위해 0x를 붙힐 위치 선정
                    if entryString[0].isdigit() and not self.printResult == 1:
                        while index < len(entryString):
                            if not entryString[index].isdigit():
                                if entryString[index] == "~" or entryString[index] == "(":
                                    tempString += entryString[index]
                                    index += 1
                                    continue
                                elif entryString[index] == ")":
                                    isBracket = 1
                                    tempString += "0o" + enterNumber + entryString[index]
                                    break
                                elif entryString[index] == "<":
                                    tempString += "0o" + enterNumber + entryString[index] + entryString[index+1]
                                    enterNumber = ""
                                    index += 2
                                elif entryString[index] == ">":
                                    tempString += "0o" + enterNumber + entryString[index] + entryString[index+1]
                                    enterNumber = ""
                                    index += 2
                                elif entryString[index] == "/":
                                    tempString += "0o" + enterNumber + entryString[index] + entryString[index+1]
                                    enterNumber = ""
                                    index += 2
                                else:
                                    tempString += "0o" + enterNumber + entryString[index]
                                    enterNumber = ""
                                    index += 1
                                    continue
                            enterNumber += str(entryString[index])
                            index += 1
                        if not isBracket == 1:
                            tempString += "0o" + enterNumber
                        expression = tempString
            # 2진수
            elif numericType == 4:
                # 2진수 계산식을 만들기 위한 변수들
                tempString = ""
                enterNumber = ""
                entryString = expression
                isBracket = 0

                if len(entryString) > 0:
                    index = 0
                    # 연산을 위해 0x를 붙힐 위치 선정
                    if entryString[0].isdigit() and not self.printResult == 1:
                        while index < len(entryString):
                            if not entryString[index].isdigit():
                                if entryString[index] == "~" or entryString[index] == "(":
                                    tempString += entryString[index]
                                    index += 1
                                    continue
                                elif entryString[index] == ")":
                                    isBracket = 1
                                    tempString += "0b" + enterNumber + entryString[index]
                                    break
                                elif entryString[index] == "<":
                                    tempString += "0b" + enterNumber + entryString[index] + entryString[index+1]
                                    enterNumber = ""
                                    index += 2
                                elif entryString[index] == ">":
                                    tempString += "0b" + enterNumber + entryString[index] + entryString[index+1]
                                    enterNumber = ""
                                    index += 2
                                elif entryString[index] == "/":
                                    tempString += "0b" + enterNumber + entryString[index] + entryString[index+1]
                                    enterNumber = ""
                                    index += 2
                                else:
                                    tempString += "0b" + enterNumber + entryString[index]
                                    enterNumber = ""
                                    index += 1
                                    continue
                            enterNumber += str(entryString[index])
                            index += 1
                        if not isBracket == 1:
                            tempString += "0b" + enterNumber
                        expression = tempString
            # ZeroDivisionError 예외처리
            try:
                result = eval(expression)
                result = round(result, 12)
                strResult = str(result)
                if numericType == 1:
                    strResult = f'{int(hex(result), 16):01X}'
                elif numericType == 3:
                    strResult = f'{int(oct(result), 8):0o}'
                elif numericType == 4:
                    strResult = f'{int(bin(result), 2):0b}'
                inputNum.configure(state=NORMAL)
                inputNum.insert(END, "\n", "tag-right")
                inputNum.insert("2.0", "= " + strResult, "tag-right")
                # eval()메소드의 취약점 해결을 위해 버튼을 제외한 임의의 입력 제한
                inputNum.configure(state="disabled")
                self.printResult = 1
            except ZeroDivisionError:
                self.isZeroDivision = 1
                for expButton in self.expButtonList:
                    expButton.config(state="disabled")
                inputNum.configure(state=NORMAL)
                inputNum.insert(END, "\n", "tag-right")
                inputNum.insert("2.0", "0으로 나눌 수 없습니다.", "tag-right")
                inputNum.configure(state="disabled")
                self.printResult = 1
        # 전체 삭제
        elif value == "AC":
            self.printResult = 1
            self.isZeroDivision = 0
            self.isPlusMinus = 0
            self.isPointPrint = 0
            # 버튼 활성화 비활성화 여부 결정
            for expButton in self.expButtonList:
                expButton.config(state=NORMAL)
            inputNum.configure(state=NORMAL)
            inputNum.delete("1.0", END)
            inputNum.insert(END, "0", "tag-right")
            self.printResult = 0
            inputNum.configure(state="disabled")
        # 현재 입력했던 것 삭제 (숫자, 연산자 단위)
        elif value == "CE":
            # 현재 수식 저장
            entryString = inputNum.get("1.0", INSERT)
            # 현재 수식이 0밖에 없을 경우, 즉 초기화면과 같을 경우 AC와 같은 동작
            if entryString == "0" or self.printResult == 1:
                self.printResult = 1
                self.isZeroDivision = 0
                self.isPlusMinus = 0
                self.isPointPrint = 0
                # 버튼 활성화 비활성화 여부 결정
                for expButton in self.expButtonList:
                    expButton.config(state=NORMAL)
                inputNum.configure(state=NORMAL)
                inputNum.delete("1.0", END)
                inputNum.insert(END, "0", "tag-right")
                self.printResult = 1
                inputNum.configure(state="disabled")
            # 0외의 수식이 존재할 경우, 즉 길이가 0보다 클 경우
            elif len(entryString) > 0:
                # 숫자일 경우
                if entryString[-1].isdigit():
                    while entryString[len(entryString)-1].isdigit():
                        entryString = entryString[0:len(entryString)-1]
                        inputNum.configure(state=NORMAL)
                        inputNum.delete("1.0", END)
                        inputNum.insert(END, entryString, "tag-right")
                        inputNum.configure(state="disabled")
                        if len(entryString)-1 < 0:
                            inputNum.configure(state=NORMAL)
                            inputNum.delete("1.0", END)
                            inputNum.insert(END, "0", "tag-right")
                            self.printResult = 1
                            inputNum.configure(state="disabled")
                            break
                # 연산자일 경우
                else:
                    while not entryString[len(entryString)-1].isdigit():
                        entryString = entryString[0:len(entryString) - 1]
                        inputNum.configure(state=NORMAL)
                        inputNum.delete("1.0", END)
                        inputNum.insert(END, entryString, "tag-right")
                        inputNum.configure(state="disabled")
                        if len(entryString)-1 < 0:
                            inputNum.configure(state=NORMAL)
                            inputNum.delete("1.0", END)
                            inputNum.insert(END, "0", "tag-right")
                            self.printResult = 1
                            inputNum.configure(state="disabled")
                            break
        # Backspace 기능
        elif value == "←":
            if len(inputNum.get("1.0", END)) == 2:
                inputNum.configure(state=NORMAL)
                inputNum.insert("1.0", "0", "tag-right")
                inputNum.configure(state="disabled")
            else:
                pass
            if not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                inputNum.delete("%s-1c" % INSERT, INSERT)
                inputNum.configure(state="disabled")
            else:
                pass
        # 양수 음수 전환
        elif value == "±":
            entryString = inputNum.get("1.0", INSERT)
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
                        inputNum.configure(state=NORMAL)
                        inputNum.delete("1.0", END)
                        if entryString == enterNumber:
                            inputNum.insert(END, "-" + enterNumber, "tag-right")
                        else:
                            inputNum.insert(END, entryString[0:index+1] + "-" + enterNumber, "tag-right")
                        inputNum.configure(state="disabled")
                        self.isPlusMinus = 1
                    else:
                        inputNum.configure(state=NORMAL)
                        inputNum.delete("1.0", END)
                        inputNum.insert(END, entryString[0:index] + enterNumber, "tag-right")
                        inputNum.configure(state="disabled")
                        self.isPlusMinus = 0
        # 연산 버튼
        elif value == "%":
            # 연산 결과를 활용해 연계 계산을 위한 조건
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            number = float(inputNum.get("1.0", END))
            result = str(number/100.0)
            inputNum.configure(state=NORMAL)
            # 연산 기호를 포함한 출력
            inputNum.insert(END, value + "\n", "tag-right")
            inputNum.insert("2.0", "= " + result, "tag-right")
            inputNum.configure(state="disabled")
            self.printResult = 1
        elif value == "sin":
            # 연산 결과를 활용해 연계 계산을 위한 조건
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            number = float(inputNum.get("1.0", END))
            radian = radians(number)
            result = str(round(sin(radian), 4))
            inputNum.configure(state=NORMAL)
            # 연산 기호를 포함한 출력
            inputNum.delete("1.0", END)
            inputNum.insert("1.0", value+"("+str(number)+")"+"\n", "tag-right")
            inputNum.insert("2.0", "= "+result, "tag-right")
            inputNum.configure(state="disabled")
            self.printResult = 1
        elif value == "cos":
            # 연산 결과를 활용해 연계 계산을 위한 조건
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
            # 연산 기호를 포함한 출력
            inputNum.delete("1.0", END)
            inputNum.insert("1.0", value+"("+str(number)+")"+"\n", "tag-right")
            inputNum.insert("2.0", "= "+result, "tag-right")
            inputNum.configure(state="disabled")
            self.printResult = 1
        elif value == "tan":
            # 연산 결과를 활용해 연계 계산을 위한 조건
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            number = float(inputNum.get("1.0", END))
            radian = radians(number)
            result = str(round(tan(radian), 4))
            inputNum.configure(state=NORMAL)
            # 연산 기호를 포함한 출력
            inputNum.delete("1.0", END)
            inputNum.insert("1.0", value+"("+str(number)+")"+"\n", "tag-right")
            inputNum.insert("2.0", "= "+result, "tag-right")
            inputNum.configure(state="disabled")
            self.printResult = 1
        elif value == "π":
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            number = float(inputNum.get("1.0", END))
            result = str(pi * number)
            inputNum.configure(state=NORMAL)
            # 연산 기호를 포함한 출력
            inputNum.delete("1.0", END)
            inputNum.insert("1.0", str(number)+ "π"+"\n", "tag-right")
            inputNum.insert("2.0", "= "+result, "tag-right")
            inputNum.configure(state="disabled")
            self.printResult = 1
        elif value == "x²":
            # 연산 결과를 활용해 연계 계산을 위한 조건
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            number = float(inputNum.get("1.0", END))
            result = str(round(pow(number, 2), 1))
            inputNum.configure(state=NORMAL)
            # 연산 기호를 포함한 출력
            inputNum.insert(END, "²" + "\n", "tag-right")
            inputNum.insert("2.0", "= " + result, "tag-right")
            inputNum.configure(state="disabled")
            self.printResult = 1
        elif value == "xʸ":
            # 연산 결과를 활용해 연계 계산을 위한 조건
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            self.printResult = 0
            inputNum.configure(state=NORMAL)
            inputNum.insert(INSERT, "**", "tag-right")
            inputNum.configure(state="disabled")
        elif value == "10ˣ":
            # 연산 결과를 활용해 연계 계산을 위한 조건
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
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
            # 연산 기호를 포함한 출력
            inputNum.delete("1.0", END)
            inputNum.insert("1.0","10^"+numberStr, "tag-right")
            inputNum.insert(END, "\n", "tag-right")
            inputNum.insert("2.0", "= " + result, "tag-right")
            inputNum.configure(state="disabled")
            self.printResult = 1
        elif value == "√x":
            # 연산 결과를 활용해 연계 계산을 위한 조건
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            number = float(inputNum.get("1.0", END))
            result = str(sqrt(number))
            inputNum.configure(state=NORMAL)
            # 연산 기호를 포함한 출력
            inputNum.insert("1.0","√", "tag-right")
            inputNum.insert(END, "\n", "tag-right")
            inputNum.insert("2.0", "= " + result, "tag-right")
            inputNum.configure(state="disabled")
            self.printResult = 1
        elif value == "1/x":
            # 연산 결과를 활용해 연계 계산을 위한 조건
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
                self.isZeroDivision = 1
                for expButton in self.expButtonList:
                    expButton.config(state="disabled")
                inputNum.configure(state=NORMAL)
                inputNum.insert("1.0", "1/", "tag-right")
                inputNum.insert(END, "\n", "tag-right")
                inputNum.insert("2.0", "0으로 나눌 수 없습니다.", "tag-right")
                inputNum.configure(state="disabled")
                self.printResult = 1
        # Factorial 연산
        elif value == "n!":
            # 연산 결과를 활용해 연계 계산을 위한 조건
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
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
        # Log 연산
        elif value == "log":
            # 연산 결과를 활용해 연계 계산을 위한 조건
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            number = float(inputNum.get("1.0", END))
            result = log(number, 10)
            inputNum.configure(state=NORMAL)
            inputNum.insert("1.0", "log(", "tag-right")
            inputNum.insert(END, ")\n", "tag-right")
            inputNum.insert("2.0", "= " + str(result), "tag-right")
            inputNum.configure(state="disabled")
            self.printResult = 1
        # Mod 연산
        elif value == "Mod":
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
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
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            self.printResult = 0
            inputNum.configure(state=NORMAL)
            inputNum.insert(INSERT, " OR ", "tag-right")
            inputNum.configure(state="disabled")
        elif value == "NOR":
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            self.printResult = 0
            inputNum.configure(state=NORMAL)
            inputNum.insert(INSERT, " NOR ", "tag-right")
            inputNum.configure(state="disabled")
        elif value == "XOR":
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
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
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            self.printResult = 0
            inputNum.configure(state=NORMAL)
            inputNum.insert(INSERT, " AND ", "tag-right")
            inputNum.configure(state="disabled")
        elif value == "NAND":
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            self.printResult = 0
            inputNum.configure(state=NORMAL)
            inputNum.insert(INSERT, " NAND ", "tag-right")
            inputNum.configure(state="disabled")
        elif value == "Lsh":
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            self.printResult = 0
            inputNum.configure(state=NORMAL)
            inputNum.insert(INSERT, " Lsh ", "tag-right")
            inputNum.configure(state="disabled")
        elif value == "Rsh":
            if self.printResult == 1 and not inputNum.get("1.0", END) == "0\n":
                inputNum.configure(state=NORMAL)
                pastResult = inputNum.get("2.2", "%s" % INSERT)
                inputNum.delete("1.0", END)
                inputNum.insert("1.0", pastResult, "tag-right")
                inputNum.configure(state="disabled")
            self.printResult = 0
            inputNum.configure(state=NORMAL)
            inputNum.insert(INSERT, " Rsh ", "tag-right")
            inputNum.configure(state="disabled")
        # 위의 특수 입력을 제외한 입력 처리
        else:
            # 초기 화면 0표기와 연산 결과를 활용해 연계 계산을 위한 조건
            if self.printResult == 1:
                if value.isdigit():
                    self.isZeroDivision = 0
                    inputNum.configure(state=NORMAL)
                    inputNum.delete("1.0", END)
                    inputNum.configure(state="disabled")
                    self.printResult = 0
                else:
                    # 0으로 나눴을 때는 연계 계산을 하지않아야 함.
                    if self.isZeroDivision:
                        inputNum.configure(state="disabled")
                    else:
                        # 초기 화면 숫자 0으로 연산 하기 위한 로직
                        if inputNum.get("1.0", END) == "0\n":
                            pass
                        else:
                            inputNum.configure(state=NORMAL)
                            pastResult = inputNum.get("2.2", "%s" % INSERT)
                            inputNum.delete("1.0", END)
                            inputNum.insert("1.0", pastResult, "tag-right")
                            inputNum.configure(state="disabled")
            # ZeroDivisionError가 일어나지 않았을 때만
            if not self.isZeroDivision:
                self.printResult = 0
                inputNum.configure(state=NORMAL)
                inputNum.insert(INSERT, value, "tag-right")
                inputNum.configure(state="disabled")
                # 소수점이 출력되었음을 알림
                if value == "." and self.isPointPrint == 0:
                    print("enter")
                    self.isPointPrint = 1
                    inputNum.configure(state=NORMAL)
                    inputNum.insert(INSERT, value, "tag-right")
                    inputNum.configure(state="disabled")
                elif self.isPointPrint == 1:
                    if value == ".":
                        inputNum.configure(state=NORMAL)
                        inputNum.delete("%s-1c" % INSERT, INSERT)
                        inputNum.configure(state="disabled")
                    elif not value.isdigit():
                        inputNum.configure(state=NORMAL)
                        inputNum.insert(INSERT, value, "tag-right")
                        inputNum.configure(state="disabled")
                        self.isPointPrint = 0
                entryString = inputNum.get("1.0", INSERT)
                print(entryString)
                # 괄호 갯수 입력 제한
                if value == ")":
                    if not entryString[-2].isdigit():
                        inputNum.delete("%s-1c" % INSERT, INSERT)
                    openBracket = entryString.count("(")
                    closeBracket = entryString.count(")")
                    if openBracket < closeBracket:
                        inputNum.delete("%s-1c" % INSERT, INSERT)
                if len(entryString) > 1:
                    if value == "(" and not entryString[0] == "0":
                        if entryString[-2].isdigit():
                            inputNum.delete("%s-1c" % INSERT, INSERT)
                # 버튼 활성화 비활성화 여부 결정
                for expButton in self.expButtonList:
                    expButton.config(state=NORMAL)
                inputNum.configure(state="disabled")
                if len(entryString) > 1:
                    # 수식의 맨 앞에 불필요한 0이 오지 않도록 자동 제거
                    if entryString[0] == "0":
                        # 연산자 앞 0은 제거하지 않음
                        if not entryString[1].isdigit():
                            # 괄호 입력 시에는 제거
                            if entryString[1] == "(":
                                inputNum.configure(state=NORMAL)
                                inputNum.delete("1.0", "1.1")
                                inputNum.configure(state="disabled")
                            elif ord(entryString[1]) in range(ord("A"), ord("G")):
                                inputNum.configure(state=NORMAL)
                                inputNum.delete("1.0", "1.1")
                                inputNum.configure(state="disabled")
                            pass
                        else:
                            inputNum.configure(state=NORMAL)
                            inputNum.delete("1.0", "1.1")
                            inputNum.configure(state="disabled")
                    # 식을 완성하지 않고 다른 연산자를 입력 시 자동 변환
                    if not entryString[-1].isdigit():
                        if not entryString[-2].isdigit():
                            if entryString[-2] == ")" or entryString[-2] == "(" or entryString[-1] == "(":
                                pass
                            elif ord(entryString[-2]) in range(ord("A"), ord("G")) or ord(entryString[-1]) in range(ord("A"), ord("G")):
                                pass
                            elif entryString[-1] == ".":
                                if entryString[-2] == ".":
                                    inputNum.configure(state=NORMAL)
                                    inputNum.delete("%s-2c" % INSERT, INSERT)
                                    inputNum.insert(INSERT, value, "tag-right")
                                    inputNum.configure(state="disabled")
                                else:
                                    inputNum.configure(state=NORMAL)
                                    inputNum.delete("%s-1c" % INSERT, INSERT)
                                    inputNum.insert(INSERT, "0" + value, "tag-right")
                                    inputNum.configure(state="disabled")
                            else:
                                inputNum.configure(state=NORMAL)
                                inputNum.delete("%s-2c" % INSERT, INSERT)
                                inputNum.insert(INSERT, value, "tag-right")
                                inputNum.configure(state="disabled")
                    # 연산자 뒤의 수가 0이 먼저 나와 연산할 수 없는 경우 (소수점 제외)
                    if len(entryString) > 2:
                        if entryString[-1].isdigit():
                            if entryString[-2] == "0":
                                if not entryString[-3].isdigit() and not entryString[-3] == ".":
                                    entryString = entryString[:-2] + entryString[-1:]
                                    inputNum.configure(state=NORMAL)
                                    inputNum.delete("1.0", END)
                                    inputNum.insert(END, entryString, "tag-right")
                                    inputNum.configure(state="disabled")
    # 산술 계산기 화면 출력 함수
    def printNormalCalc(self):
        self.isComputerCalc = 0
        # 화면 전환 할 때마다 위젯을 전부 삭제하고 재출력
        widgetList = allChildren(window)
        for item in widgetList:
            item.grid_forget()
        # 버튼 그리드 변수
        rowIndex = 1
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

        # 결과 표시창
        global inputNum
        inputNum = Text(window, width=30, height=3, relief="groove", \
                        font=font, background="gray95", pady=5, padx=10)
        inputNum.tag_configure('tag-right', justify="right")
        inputNum.grid(row=0, column=0, columnspan=4, pady=5, padx=5, ipady=20, ipadx=5)
        inputNum.insert(END, "0", "tag-right")
        inputNum.configure(state="disabled")
        self.printResult = 1

        buttonList = []
        index = 0
        # 버튼 표시
        for button in buttonText:
            def click(t=button):
                self.pressButton(t)

            buttonObject = Button(window, text=button, width=7, height=2, \
                                    relief="groove", command=click, font=font, padx=0, pady=0)
            buttonObject.grid(row=rowIndex, column=colIndex, sticky="nesw")
            buttonList.append(buttonObject)
            if not button.isdigit():
                if button == "AC":
                    pass
                else:
                    self.expButtonList.append(buttonObject)
            # 결과 출력 버튼 색 변경
            if button == "=":
                buttonObject.configure(bg="skyblue")
            index += 1
            colIndex += 1
            if colIndex > 3:
                rowIndex += 1
                colIndex = 0
        window.bind("<Key>", self.pressButtonKey)
    # 공학용 계산기 화면 출력 함수
    def printScientificCalc(self):
        self.isComputerCalc = 0
        # 화면 전환 할 때마다 위젯을 전부 삭제하고 재출력
        widgetList = allChildren(window)
        for item in widgetList:
            item.grid_forget()
        rowIndex = 1
        colIndex = 0
        buttonText = [
            'sin', 'cos', 'tan', 'π', '←',
            'x²', 'xʸ', '√x', '10ˣ', 'n!',
            '7', '8', '9', '/', 'log',
            '4', '5', '6', '*', 'AC',
            '1', '2', '3', '-', 'CE',
            '.', '0', '±', '+', '=',
        ]

        # 결과 표시창
        global inputNum
        inputNum = Text(window, width=30, height=3, relief="groove", \
                        font=font, background="gray95", pady=5, padx=10)
        inputNum.tag_configure('tag-right', justify="right")
        inputNum.grid(row=0, column=0, columnspan=5, pady=5, padx=5, ipady=20, ipadx=5)
        inputNum.insert(END, "0", "tag-right")
        inputNum.configure(state="disabled")
        self.printResult = 1

        buttonList = []
        index = 0
        # 버튼 표시
        for button in buttonText:
            def click(t=button):
                self.pressButton(t)

            buttonObject = Button(window, text=button, width=6, height=2, \
                                    relief="groove", command=click, font=font, padx=0, pady=0)
            buttonObject.grid(row=rowIndex, column=colIndex, sticky="nesw")
            buttonList.append(buttonObject)
            if not button.isdigit():
                if button == "AC":
                    pass
                else:
                    self.expButtonList.append(buttonObject)
            # 결과 출력 버튼 색 변경
            if button == "=":
                buttonObject.configure(bg="skyblue")
            index += 1
            colIndex += 1
            if colIndex > 4:
                rowIndex += 1
                colIndex = 0
        window.bind("<Key>", self.pressButtonKey)
    # 프로그래머용 계산기 화면 출력 함수
    def printComputerCalc(self):
        self.isComputerCalc = 1
        self.printResult = 0

        # 화면 전환 할 때마다 위젯을 전부 삭제하고 재출력
        font = Font(family="맑은 고딕", size=15)
        radioFont = Font(family="맑은 고딕", size=10, weight="bold")
        widgetList = allChildren(window)
        for item in widgetList:
            item.grid_forget()
        rowIndex = 2
        colIndex = 0

        buttonText = [
            'NAND', 'NOR', 'OR', 'XOR', 'NOT', 'AND',
            'Lsh', 'Rsh', 'Mod', 'AC', '←', '/',
            'A', 'B', '7', '8', '9', '*',
            'C', 'D', '4', '5', '6', '-',
            'E', 'F', '1', '2', '3', '+',
            '(', ')', '±', '0', '.', '='
        ]

        # 결과 표시창
        global inputNum
        inputNum = Text(window, width=30, height=3, relief="groove", \
                        font=font, background="gray95", pady=5, padx=10)
        inputNum.tag_configure('tag-right', justify="right")
        inputNum.grid(row=0, column=0, columnspan=6, pady=5, ipady=20, ipadx=5)
        inputNum.insert(END, "0", "tag-right")
        inputNum.configure(state="disabled")

        # 첫 화면은 10진수
        for binButton in self.binButtonList:
            binButton.configure(state=NORMAL)
        for octButton in self.octButtonList:
            octButton.configure(state=NORMAL)
        for alphaButton in self.alphaButtonList:
            alphaButton.configure(state="disabled")
        self.pastValue = 2

        # 라디오 버튼 이벤트 처리 (진수 변환)
        def selectRadio():
            value = self.radioValue.get()
            if value == 1:
                for octButton in self.octButtonList:
                    octButton.configure(state=NORMAL)
                for binButton in self.binButtonList:
                    binButton.configure(state=NORMAL)
                for alphaButton in self.alphaButtonList:
                    alphaButton.configure(state=NORMAL)
                if self.printResult == 1:
                    number = inputNum.get("2.2", INSERT)
                    if self.pastValue == 2:
                        number = int(number)
                        number = f'{number:01X}'
                    elif self.pastValue == 3:
                        number = int(number, 8)
                        number = f'{number:01X}'
                    elif self.pastValue == 4:
                        number = int(number, 2)
                        number = f'{number:01X}'
                    self.printResult = 0
                else:
                    number = inputNum.get("1.0", INSERT)
                    if self.pastValue == 2:
                        number = int(number)
                        number = f'{number:01X}'
                    elif self.pastValue == 3:
                        number = int(number, 8)
                        number = f'{number:01X}'
                    elif self.pastValue == 4:
                        number = int(number, 2)
                        number = f'{number:01X}'
                inputNum.configure(state=NORMAL)
                inputNum.delete("1.0", END)
                inputNum.insert(END, number, "tag-right")
                inputNum.configure(state="disabled")
                self.pastValue = 1
            elif value == 2:
                for binButton in self.binButtonList:
                    binButton.configure(state=NORMAL)
                for octButton in self.octButtonList:
                    octButton.configure(state=NORMAL)
                for alphaButton in self.alphaButtonList:
                    alphaButton.configure(state="disabled")
                if self.printResult == 1:
                    number = inputNum.get("2.2", INSERT)
                    if self.pastValue == 1:
                        number = int(number, 16)
                        number = f'{number}'
                    elif self.pastValue == 3:
                        number = int(number, 8)
                        number = f'{number}'
                    elif self.pastValue == 4:
                        number = int(number, 2)
                        number = f'{number}'
                    self.printResult = 0
                else:
                    number = inputNum.get("1.0", INSERT)
                    if self.pastValue == 1:
                        number = int(number, 16)
                        number = f'{number}'
                    elif self.pastValue == 3:
                        number = int(number, 8)
                        number = f'{number}'
                    elif self.pastValue == 4:
                        number = int(number, 2)
                        number = f'{number}'
                inputNum.configure(state=NORMAL)
                inputNum.delete("1.0", END)
                inputNum.insert(END, number, "tag-right")
                inputNum.configure(state="disabled")
                self.pastValue = 2
            elif value == 3:
                for binButton in self.binButtonList:
                    binButton.configure(state=NORMAL)
                for octButton in self.octButtonList:
                    octButton.configure(state="disabled")
                for alphaButton in self.alphaButtonList:
                    alphaButton.configure(state="disabled")
                if self.printResult == 1:
                    number = inputNum.get("2.2", INSERT)
                    if self.pastValue == 1:
                        number = int(number, 16)
                        number = f'{number:0o}'
                    elif self.pastValue == 2:
                        number = int(number)
                        number = f'{number:0o}'
                    elif self.pastValue == 4:
                        number = int(number, 2)
                        number = f'{number:0o}'
                    self.printResult = 0
                else:
                    number = inputNum.get("1.0", INSERT)
                    if self.pastValue == 1:
                        number = int(number, 16)
                        number = f'{number:0o}'
                    elif self.pastValue == 2:
                        number = int(number)
                        number = f'{number:0o}'
                    elif self.pastValue == 4:
                        number = int(number, 2)
                        number = f'{number:0o}'
                inputNum.configure(state=NORMAL)
                inputNum.delete("1.0", END)
                inputNum.insert(END, number, "tag-right")
                inputNum.configure(state="disabled")
                self.pastValue = 3
            elif value == 4:
                for binButton in self.binButtonList:
                    binButton.configure(state="disabled")
                for alphaButton in self.alphaButtonList:
                    alphaButton.configure(state="disabled")
                if self.printResult == 1:
                    number = inputNum.get("2.2", INSERT)
                    if self.pastValue == 1:
                        number = int(number, 16)
                        number = f'{number:0b}'
                    elif self.pastValue == 2:
                        number = int(number)
                        number = f'{number:0b}'
                    elif self.pastValue == 3:
                        number = int(number, 8)
                        number = f'{number:0b}'
                    self.printResult = 0
                else:
                    number = inputNum.get("1.0", INSERT)
                    if self.pastValue == 1:
                        number = int(number, 16)
                        number = f'{number:0b}'
                    elif self.pastValue == 2:
                        number = int(number)
                        number = f'{number:0b}'
                    elif self.pastValue == 3:
                        number = int(number, 8)
                        number = f'{number:0b}'
                inputNum.configure(state=NORMAL)
                inputNum.delete("1.0", END)
                inputNum.insert(END, number, "tag-right")
                inputNum.configure(state="disabled")
                self.pastValue = 4
        # 라디오 버튼 목록
        hexNumeral = Radiobutton(window, text="HEX", value=1, variable=self.radioValue, font=radioFont, command=selectRadio)
        hexNumeral.grid(row=1, column=1, sticky="nesw")
        dexNumeral = Radiobutton(window, text="DEX", value=2, variable=self.radioValue, font=radioFont, command=selectRadio)
        dexNumeral.select()
        self.radioValue.set(2)
        dexNumeral.grid(row=1, column=2, sticky="nesw")
        octNumeral = Radiobutton(window, text="OCT", value=3, variable=self.radioValue, font=radioFont, command=selectRadio)
        octNumeral.grid(row=1, column=3, sticky="nesw")
        binNumeral = Radiobutton(window, text="BIN", value=4, variable=self.radioValue, font=radioFont, command=selectRadio)
        binNumeral.grid(row=1, column=4, sticky="nesw")

        buttonList = []
        index = 0
        # 버튼 표시
        for button in buttonText:
            def click(t=button):
                self.pressButton(t)
            buttonObject = Button(window, text=button, width=5, height=2,\
                                  relief="groove", command=click, font=font, padx=0, pady=0)
            buttonObject.grid(row=rowIndex, column=colIndex, sticky="nesw")
            buttonList.append(buttonObject)
            # 컴퓨터 계산기 소수점 사용 금지
            if button == ".":
                pointButton = buttonList[index]
                pointButton.configure(state="disabled")
            # 연산자 버튼 리스트
            if not button.isdigit():
                if button == "AC" or button == ".":
                    pass
                # 프로그래머용 계산기에서 16진수 수들은 연산자가 아님
                elif len(button) == 1:
                    if ord(button) in range(ord("A"), ord("G")):
                        pass
                else:
                    self.expButtonText.append(button)
                    self.expButtonList.append(buttonObject)
            # 결과 출력 버튼 색 변경
            if button == "=":
                buttonObject.configure(bg="skyblue")
            # 진수 변경을 위한 각 진수 별 버튼 리스트
            if len(button) == 1:
                if ord(button) in range(ord("A"), ord("G")):
                    self.alphaButtonList.append(buttonObject)
                elif button == "8" or button == "9":
                    self.octButtonList.append(buttonObject)
                    self.binButtonList.append(buttonObject)
                elif ord(button) in range(ord("2"), ord("9")):
                    self.binButtonList.append(buttonObject)
            index += 1
            colIndex += 1
            if colIndex > 5:
                rowIndex += 1
                colIndex = 0
        # 화면 첫 출력 시 자동으로 10진수로 설정 (16진수 수 입력 불가)
        for alphaButton in self.alphaButtonList:
            alphaButton.configure(state="disabled")

    def printWindow(self):
        # 메뉴 변수
        menubar = Menu(window)
        calcMenu = Menu(menubar, tearoff=0)
        calcMenu.add_command(label="산술", command=self.printNormalCalc)
        calcMenu.add_command(label="공학", command=self.printScientificCalc)
        calcMenu.add_command(label="프로그래머", command=self.printComputerCalc)
        menubar.add_cascade(label="계산기", menu=calcMenu)
        unitMenu = Menu(menubar, tearoff=0)
        unitMenu.add_command(label="온도", command=unitChanger.temperature)
        unitMenu.add_command(label="길이", command=unitChanger.length)
        unitMenu.add_command(label="데이터", command=self.printScientificCalc)
        unitMenu.add_command(label="무게 및 질량", command=self.printComputerCalc)
        menubar.add_cascade(label="단위 변환", menu=unitMenu)
        window.config(menu=menubar)
        self.printNormalCalc()

        window.mainloop()

if __name__ == "__main__":
    mainCalc = Calculator()
    mainCalc.printWindow()
