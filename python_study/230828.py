# #제너레이터 객체와 next() 함수
# def test():
#     print("A 지점 통과")
#     yield 1
#     print("B 지점 통과")
#     yield 2
#     print("C 지점 통과")

# output = test()

# print("D 지점 통과")
# a = next(output)
# print(a)
# print("E 지점 통과")
# b = next(output)
# print(b)
# print("F 지점 통과")
# c = next(output)
# print(c)
# # StopIteration 예외 발생.
# # next(output)


# 조건문으로 예외 처리하기
user_input = input("정수 입력 > ")

if user_input.isdigit():
    number_input_a = int(user_input)

    print("원의 반지름 : ", number_input_a)
    print("원의 둘레 : ", 2 * 3.14 * number_input_a)
    print("원의 넓이 : ", 3.14 * number_input_a * number_input_a)
else:
    print("정수를 입력하지 않았습니다.")
print()


# try except 구문으로 예외 처리하기
try:
    number_input_a = int(input("정수 입력 > "))
    print("원의 반지름 : ", number_input_a)
    print("원의 둘레 : ", 2 * 3.14 * number_input_a)
    print("원의 넓이 : ", 3.14 * number_input_a * number_input_a)
except:
    print("무언가 잘못되었습니다.")
print()


# 숫자로 변환되는 것들만 리스트에 넣기
list_a = ["52", "273", "32", "스파이", "103"]

list_num = []
for item in list_a:
    try:
        float(item)
        list_num.append(item)
    except:
        pass

print(f"{list_a} 내부에 있는 숫자는\n {list_num}입니다.")
print()


# try except else 구문
try:
    number_input_a = int(input("정수 입력 > "))
except:
    print("정수를 입력하지 않았습니다.")
else:
    print("원의 반지륾 : ", number_input_a)
    print("원의 반지륾 : ", 2 * 3.14 * number_input_a)
    print("원의 반지륾 : ", 3.14 * (number_input_a ** 2))
print()


# finally 구문
try:
    number_input_a = int(input("정수 입력 > "))

    print("원의 반지륾 : ", number_input_a)
    print("원의 반지륾 : ", 2 * 3.14 * number_input_a)
    print("원의 반지륾 : ", 3.14 * (number_input_a ** 2))
except:
    print("정수를 입력해달라고 했잖아요!")
else:
    print("예외가 발생하지 않았습니다.")
finally:
    print("일단 프로그램이 어떻게든 끝났습니다.")
print()


# 파일이 제대로 닫혔는지 확인하기
try:
    file = open("info.txt", "w")

    file.close()
except Exception as e:
    print(e)

print("# 파일이 제대로 닫혔는지 확인하기")
print("file closed : ", file.closed)
print()


# finally 구문을 이용해 파일 닫기
try:
    file = open("info.txt", "w")
except Exception as e:
    print(e)
finally:
    file.close()
    print("# 파일이 제대로 닫혔는지 확인하기")
    print("file closed : ", file.closed)
print()


# try except 구문이 끝난 후 파일 닫기
try:
    file = open("info.txt", "w")
except Exception as e:
    print(e)

file.close()
print("# 파일이 제대로 닫혔는지 확인하기")
print("file closed : ", file.closed)
print()


# try 구문 내부에서 return 키워드를 사용하는 경우
def test():
    print("test() 함수의 첫 줄입니다.")
    try:
        print("try 구문이 실행되었습니다.")
        return
        print("try 구문의 return 키워드 뒤입니다.")
    except:
        print("except 구문이 실행되었습니다.")
    else:
        print("else 구문이 실행되었습니다.")
    finally:
        print("finally 구문이 실행되었습니다.")
    print("test() 함수의 마지막 줄입니다.")

test()
print()


# while과 함께 사용하는 경우
print("프로그램이 시작되었습니다.")

while True:
    try:
        print("try 구문이 실행되었습니다.")
        break
        print("try 구문의 break 키워드 뒤입니다.")
    except:
        print("except 구문이 실행되었습니다.")
    finally:
        print("finally 구문이 실행되었습니다.")
    print("while 반복문의 마지막 줄입니다.")
print("프로그램이 종료되었습니다.")
print()


# 예외 객체
try:
    number_input_a = int(input("정수 입력 > "))

    print("원의 반지륾 : ", number_input_a)
    print("원의 반지륾 : ", 2 * 3.14 * number_input_a)
    print("원의 반지륾 : ", 3.14 * (number_input_a ** 2))
except Exception as exception:
    print("type(exception) : ", type(exception))
    print("exception : ", exception)
print()


# 예외 구분하기
list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력 > "))
    print("{}번째 요소 : {}".format(number_input, list_number[number_input]))
except ValueError:
    print("정수를 입력해주세요!")
except IndexError:
    print("리스트의 인덱스를 벗어났어요!")
print()


# 모든 예외 잡기
list_number = [52, 273, 32, 72, 100]

try:
    number_input = int(input("정수 입력 > "))
    print("{}번째 요소 : {}".format(number_input, list_number[number_input]))
except ValueError as exception:
    print("정수를 입력해주세요!")
    print("exception : ", exception)
except IndexError as exception:
    print("리스트의 인덱스를 벗어났어요!")
    print("exception : ", exception)
except Exception as exception:
    print("미리 파악하지 못한 예외가 발생했습니다.")
    print(type(exception), exception)
print()


# # raise 구문
# number = input("정수 입력 > ")
# number = int(number)

# if number > 0:
#     raise NotImplementedError
# else:
#     raise NotImplementedError
# print()


# math 모듈
import math

print(math.sin(1))
print(math.cos(1))
print(math.tan(1))
print(math.floor(2.5))
print(math.ceil(2.5))
print()


# from 구문
from math import sin, cos, tan, floor, ceil

print(sin(1))
print(cos(1))
print(tan(1))
print(floor(2.5))
print(ceil(2.5))
print()


# as 구문
import math as m

print(m.sin(1))
print(m.cos(1))
print(m.tan(1))
print(m.floor(2.5))
print(m.ceil(2.5))
print()


# random 모듈
import random

print("# random 모듈")

# random(): 0.0 <= x < 1.0 사이의 float를 리턴합니다.
print("- random(): ", random.random())

# uniform(min, max): 지정한 범위 사이의 float를 리턴합니다.
print("- uniform(10, 20): ", random.uniform(10, 20))

# randrange(): 지정한 범위의 int를 리턴합니다.
# - randrange(max): 0부터 max 사이의 값을 리턴합니다.
# - randrange(min, max): min부터 max 사이의 값을 리턴합니다.
print("- randrange(10): ", random.randrange(10))

# choice(list): 리스트 내부에 있는 요소를 랜덤하게 선택합니다.
print("- choice([1, 2, 3, 4, 5]): ", random.choice([1, 2, 3, 4, 5]))

# shuffle(list): 리스트의 요소들을 랜덤하게 섞습니다.
print("- shuffle([1, 2, 3, 4, 5]): ", random.shuffle([1, 2, 3, 4, 5]))

# sample(list, k=<숫자>): 리스트의 요소 중에 k개를 뽑습니다.
print("- sample([1, 2, 3, 4, 5], k=2): ", random.sample([1, 2, 3, 4, 5], k=2))
print()


# # sys 모듈
# import sys

# print(sys.argv)
# print("---")

# print("getwindowsversion : ()", sys.getwindowsversion())
# print("---")
# print("copyright : ", sys.copyright)
# print("---")
# print("version : ", sys.version)

# sys.exit()


# os 모듈
import os

print("현재 운영체제 : ", os.name)
print("현재 폴더 : ", os.getcwd())
print("현재 폴더 내부의 요소 : ", os.listdir())

os.mkdir("hello")
os.rmdir("hello")

with open("original.txt", "w") as file:
    file.write("hello")
os.rename("original.txt", "new.txt")

os.remove("new.txt")

os.system("dir")
print()


# datetime 모듈
import datetime

print("# 현재 시각 출력하기")
now = datetime.datetime.now()
print(now.year, "년")
print(now.month, "월")
print(now.day, "일")
print(now.hour, "시")
print(now.minute, "분")
print(now.second, "초")
print()

print("# 시간을 포맷에 맞춰 출력하기")
output_a = now.strftime("%Y.%m.%d %H:%M:%S")
output_b = "{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
)
output_c = now.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(
    "년",
    "월",
    "일",
    "시",
    "분",
    "초"
)
print(output_a)
print(output_b)
print(output_c)
print()


# 시간 처리하기
import datetime

now = datetime.datetime.now()

print("# datetime.timedelta로 시간 더하기")
after = now + datetime.timedelta(
    weeks=1,
    days=1,
    hours=1,
    minutes=1,
    seconds=1
)
print(after.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(
    "년",
    "월",
    "일",
    "시",
    "분",
    "초"
))
print()

print("# now.replace()로 1년 더하기")
output = now.replace(year=(now.year + 1))
print(output.strftime("%Y{} %m{} %d{} %H{} %M{} %S{}").format(
    "년",
    "월",
    "일",
    "시",
    "분",
    "초"
))
print()


# time 모듈
import time

print("지금부터 5초 동안 정지합니다!")
time.sleep(5)
print("프로그램을 종료합니다.")
print()


# urllib 모듈
from urllib import request

target = request.urlopen("https://google.com")
output = target.read()

print(output)
print()