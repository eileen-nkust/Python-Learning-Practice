#基本資料型態 & 變數

#字串
"小林你好"

#數字
70
-87
163.4


#布林值
True
False


nane = "小鐘"
age = "25"
is_male = False
#1.變數名稱只能是英文、數字、_的組合
#2.變數開頭不可以是數字

#清除指令 windows cls、Mac clear
print("有一個人叫" + nane)
print(nane + "今年25歲")
print(nane + "身高163公分")
print(nane + "討厭自己身高只有163")

nane = "小黃"
print(nane)
nane = "小紅"
print(nane)
nane = 50
print(nane)
nane = False
print(nane)

# 如何使用字串、字串的用法

# 函式 function

phrase = "Hi Mr.Lin"
print(phrase.lower().islower())

#找0位 是哪個字母
print(phrase[0])

#找字母在第幾位 python第一位是0123456...
print(phrase.index("H"))
print(phrase.index("i"))

#替換字母
print(phrase.replace("H","h"))

# 如何使用數字、數字的用法
print(-77.2)
#整數除法// 小數點不省略/ 、取除法餘數%
print(8+5)
print(8/5)
print(8//5)
print(8+8*5)
print((8+8)*5)
number = -8
print(number*5)
print("會印出數字" + str(number))
#ABS=取絕對值
print(abs(number))
#pow=次方
print(pow(2,5))
print(pow(2,0))
print(max(2,6,58,99,458))
print(min(2,5,1,88,6))
#round=四捨五入
print(round(4.2))

#引入更多數學函數
from math import *
#無條件捨去函數
print(floor(4.6))
#無條件進位
print(ceil(2.6))
#開根號
print(sqrt(64))

#建立基本機算機
name = input("請輸入您的名字: ")
age = input("請輸入您的年紀: ")
print("您好" + name + "，您今年" + age + "歲")

number1 = input("請輸入第一個數字: ")
number2 = input("請輸入第二個數字: ")
#int 可以將字串轉換成整數
print(int(number1) + int(number2))
#float 可以將字串轉換成小數
print(float(number1) + float(number2))

#列表list、列表的用法
scores = [90,70,60,90,50,80]
print(scores)
friends = ["小林","小鐘","小黃"]
things = [90,"小林",True]
print(friends)
print(things)
print(scores[0])
print(scores[-2])
#0:2 = 從第0位開始取到第2位之前 = 0、1
print(scores[0:2])
print(scores[1:4])
#1: = 從第一位開始取到最後一個數字、:4 = 取第四位往前到第1個數字
print(scores[1:])
phrase = "Hello Ms,Lin"
print(phrase[4])
print(phrase[0:5])
print(phrase[6:])
scores[0] = 30
print(scores)
#extend = 延伸
scores.extend(friends)
print(scores)
#append = 加上值
scores.append(30)
print(scores)
#insert = 插入
scores.insert(2,30)
print(scores)
#remove = 刪除列表中的數字
scores.remove(90)
print(scores)
#clear = 清除
scores.clear()
print(scores)
#pop = 移除列表最後一位
scores.pop()
print(scores)
#sort = 由小到大做排列
scores.sort()
print(scores)
#reverse = 整組字串做反轉
scores.reverse()
print(scores)
#index()找值，只會回傳優先找到的第一位
print(scores.index(90))
#count()找一串數裡面有幾個指定數字
print(scores.count(90))

#元組tuple [] = 列表 () = 元組 
scores = (90,80,60,70,50)
# len = 知道這串列裡面有幾個值
print(scores[0])
print(len(scores))
#元組創建後不能透過函數 做新增、修改、刪除
#元組型態是為了防止被意外修改

#函式 function
#函式的定義 = 只能式大小寫英文、底線；數字的組合，但開頭不可以是數字
def hello(name,age):
    print("hello" + name + "你今年" + age + "歲")
#str = 把age函數轉成字串
def hello(name,age):
    print("hello" + name + "你今年" + str(age) + "歲")
hello("小林",25)
#練習函數相加
def add(num1,num2):
    print(num1+num2)
    return num1+num2
#回傳return

print(add(2,3))

def add(num1,num2):
    print(num1+num2)
    return 10

value=add(3,4)
print(value)
#if判斷式
#1.
#如果 我肚子餓
#    我就去吃飯
hungry = False
if hungry:
    print("我就去吃飯")

#2.
#如果 今天下雨
#    我就開車去上班
#否則=else
#    我就走路去

rainy = True
if rainy:
    print("我就開車去上班")
else:
    print("我就走路去上班")


rainy = False
if rainy:
    print("我就開車去上班")
else:
    print("我就走路去上班")

#3.
#如果 你考100分
#    我就給你1000元
#或是如果 你考80分以上
#    我給你500元
#或是如果 你考60分以上
#    我給你100元
#否則
#    你給我300元

# == 代表判斷左邊與右邊的質有沒有相等

#或是=elif
score=20
if score==100:
    print("我給你1000元")
elif score>=80:
    print("我給你500元")
elif score>=60:
    print("我給你100元")
else:
    print("你給我300元")

#4.
#如果 你考100分 且 今天下雨
#    我給你1000元
#否則
#    你給我100元

#且=and
score=1000
rainy=True
if score==100 and rainy:
    print("我給你1000元")
else:
    print("你給我100元")

#5.
#如果 你考100分 或今天下雨
#    我給你1000元
#否則
#    你給我100元

#或=or
score=100
rainy=True
if score==100 or rainy:
    print("我給你1000元")
else:
    print("你給我100元")

#6.
# 如果 你考100分 或 沒有下雨
#     我給你1000元
#否則
#     你給我100元

score=100
rainy=False
if score==100 or not(rainy):
    print("我給你1000元")
else:
    print("你給我100元")

#如果左邊不等於右邊 !=
score=100
rainy=False
if score!=100 or not(rainy):
    print("我給你1000元")
else:
    print("你給我100元")

#判斷3個數子哪個最大的函數寫法
def max_num(num1,num2,num3):
    if num1>=num2 and num1>=num3:
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3
print(max_num(-1,-9,3))

#建立進階計算機
num1 = float(input("請輸入第一個數:"))
op = input("請輸入運算符號:")
num2 = float(input("請輸入第二個數"))

if op=="+":
    print(num1+num2)
elif op=="-":
    print(num1-num2)
elif op=="*":
    print(num1*num2)
elif op=="/":
    print(num1/num2)
else:
    print("很抱歉您輸入的符號，不支援的運算")

#字典dictionary
# key value
# 鍵    值

dic = {"蘋果":"apple","香蕉":"banana","貓":"cat","狗":"dog"}
print(dic["蘋果"])

# while 迴圈 = 如果判斷是ture就會一直重複執行 除非判斷是false才會停止

# i=i+1等於i+=1
i=1
while i<=5:
    print(i)
    i += 1
print("迴圈結束")

#猜數字遊戲

secret_num = 77
guess = None

while secret_num != guess:
    guess = int(input("請輸入終極數字:"))
    if guess >secret_num:
        print("請再猜少一點")
    elif guess < secret_num:
        print("請再猜大一點")
print("蹦！恭喜您猜對了！")

secret_num = 77
guess = None

#限制猜測3次的遊戲
secret_num = 77
guess = None
guess_count = 0
guess_limit = 3
out_of_limit = False


while secret_num != guess and not(out_of_limit):
    guess_count +=1
    if guess_count<=guess_limit:
        guess = int(input("請輸入終極數字:"))
        if guess >secret_num:
            print("請再猜少一點")
        elif guess < secret_num:
            print("請再猜大一點")
    else:
        out_of_limit = True
if out_of_limit:
    print("抱歉~您輸了！")
else:
    print("蹦！恭喜您猜對了！")

#for 迴圈

# for 變數 in 字串or列表：
    # 要重複執行的程式碼

for letter in "小林你好":
    print(letter)

for num in [0,1,2,3,4]:
    print(num)

for num in range(6):
    print(num)

for num in range(2,7):
    print(num)

print(pow(2,6))

def power(bese_num,pow_num):
    result = bese_num
    for index in range(pow_num-1):
        result = result * bese_num
    return result

print(power(4,2))

#二維列表&巢狀迴圈、[[0,1,2,3]] = 二維列表
# row = 行 col = 列
nums = [
    [0,1,2],
    [3,4,5],
    [6,7,8],
    [9]
]
print(nums[2][2])

#巢狀迴圈
for row in nums:
    for col in row:
        print(col)

# 檔案的讀取、寫入
# open("絕對路徑", mode="開啟模式")

# 絕對路徑 ex: C:/Users/peiju/OneDrive/桌面/舉例用.txt
# 相對路徑 以程式的位置做延伸 ex: 123.txt
# mode="r" 讀取
# mode="w" 複寫
# mode="a" 在原先的資料後寫東西

file = open("舉例用.txt", mode="r")
print(file.read())
#關閉已開啟的資料
file.close()
#只讀一行
print(file.readline())
#讀出每一行的迴圈
file = open("舉例用.txt", mode="r")
for line in file:
    print(line)
#把每一行的資料放到列表裡面
file = open("舉例用.txt", mode="r")
print(file.readlines())
file.close()
file = open("舉例用.txt", mode="w")
file.write("hi")
file.close()
file = open("舉例用.txt", mode="a")
file.write(" lin")
file.close()
# encoding = utf-8 就可以支援中文
file = open("舉例用.txt", mode="a", encoding="utf-8")
file.write("\n妳好")
file.close()
#下面這段寫法等於428-430的寫法 with會自動close檔案
with open("舉例用.txt", mode="a", encoding="utf-8") as file:
    file.write("\n妳好啊")

#模組module的使用(使用自己寫的module)
import tool
print(tool.name)
print(tool.age)
print(tool.max_num(2,5,65))

#找module位置(找官方內建module)
import sys
print(sys.path)

#找第三方須下載的module
#pip 套件管理工具
#將numpy改名成np 就是在原本的名字後面加as 後面輸入自己想改的名字
import numpy as np

#類別class、物件object
class Phone:
    def __init__(self,os,number,is_waterproof):
        self.os = os
        self.number = number
        self.is_waterproof = is_waterproof

phone1 = Phone("ios",+886983937538,True)
print(phone1.os)
print(phone1.number)
print(phone1.is_waterproof)
phone2 = Phone("andriod",+886933963338,False)
print(phone2.os)
print(phone2.number)
print(phone2.is_waterproof)

#問答程式
from question import Question

test = [
    "1+3=?\n(a) 2 \n(b) 3 \n(c) 4\n\n",
    "1公尺等於幾公分?\n(a) 10\n(b) 100\n(c) 1000\n\n",
    "香蕉是什麼顏色?\n(a) 黑色\n(b) 黃色\n(c) 白色\n\n"
]

questions = [
    Question(test[0],"c"),
    Question(test[1],"b"),
    Question(test[2],"b")
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.description)
        if answer == question.answer:
            score += 1
    print("妳得到" +  str(score) + "分，共" + str(len(questions)) + "題")

run_test(questions)

#物件函式
class Phone:
    def __init__(self,os,number,is_waterproof):
        self.os = os
        self.number = number
        self.is_waterproof = is_waterproof
    def is_ios(self):
        if self.os == "ios":
            return True
        else:
            return False
    def add(self,number1,number2):
        return number1 + number2
        
phone1 = Phone("ios",+886983937538,True)
print(phone1.is_ios())
print(phone1.add(5,6))

#繼承
from student import Student

student1 = Student("小林",25,"高科大")
student1.print_name()
