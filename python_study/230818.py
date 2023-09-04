# 숫자를 문자열로 바꾸기
int_a = 15

print(type(str(int_a)))
print()


# format() 함수 써보기
str_a = "{}".format(20)

print(str_a)
print(type(str_a))
print()

format_a = "{}만 원".format(5000)
format_b = "파이썬 열공하여 첫 연봉 {}만 원 만들기".format(5000)
format_c = "{} {} {}".format(3000, 4000, 5000)
# 타입 상관없이 format() 함수를 통하여 삽입가능
format_d = "{} {} {}".format(1, "문자열", True)

print(format_a)
print(format_b)
print(format_c)
print(format_d)

# 기호를 뒤로 밀기
h = "{:+5d}".format(52)
i = "{:+5d}".format(-52)
# 기호를 앞으로 밀기
j = "{:=+5d}".format(52)
k = "{:=+5d}".format(-52)
# 0으로 채우기
l = "{:+05d}".format(52)
m = "{:+05d}".format(-52)

print(h)
print(i)
print(j)
print(k)
print(l)
print(m)

# 15칸에 소수점 3자리까지 표시
a = "{:15.3f}".format(52.273)
# 15칸에 소수점 2자리까지 표시
b = "{:15.2f}".format(52.273)
# 15칸에 소수점 1자리까지 표시
c = "{:15.1f}".format(52.273)

print(a)
print(b)
print(c)
print()


# 대소문자로 바꾸는 함수 upper(), lower() 사용해보기
a = "Hello Python Programing...!"

print(a.upper())

print(a.lower())
print()


# 문자열 양옆의 공백 제거 함수 strip() 사용해보기
a = """
        안녕하세요
문자열의 함수를 알아봅니다."""

print(a)
print(a.strip())
print()


# 문자열의 구성을 파악하는 함수 is??() 사용해보기
# isalnum() 문자열이 알파벳 또는 숫자로만 되어있는지 확인
print("TrainA10".isalnum())
# isdigit() 문자열이 숫자로 인식될 수 있는 것 인지 확인
print("1240".isdigit())
print()


# 문자열 찾는 함수 find(), rfind() 사용해보기
# find() 왼쪽부터 탐색
a = "안녕안녕하세요".find("안녕")
print(a)

# rfind() 오른쪽부터 탐색
b = "안녕안녕하세요".rfind("안녕")
print(b)
print()


# 문자열과 in 연산자
print("안녕" in "안녕하세요")
print("잘가" in "안녕하세요")
print()


# 문자열 자르기 함수 split() 사용해보기
a = "10 20 30 40 50".split(" ")
print(a)
b = "10,20,30,40,50".split(",")
print(b)
print()


# 비교 연산자
print(10 == 100) # False
print(10 != 100) # True
print(10 < 100) # True
print(10 > 100) # False
print(10 <= 100) # True
print(10 >= 100) # False

print("가방" == "가방") # True
print("가방" != "하마") # True
print("가방" < "하마") # True
print("가방" > "하마") # False
print()


# if문 작성해보기
if True:
    print("True")
    print("True라고!")

number= int(input("정수 입력 > "))

if number > 0:
    print("양수")

if number < 0:
    print("음수")
print()


#number가 5의 배수인지 확인하기
number= int(input("정수 입력 > "))

if (number % 5) == 0 and number > 0:
    print("5의 배수")

if (number % 5) != 0:
    print("5의 배수가 아님")
print()


# 날짜/시간 출력하기
import datetime

now = datetime.datetime.now()
print(now.year)
print(now.month)
print(now.day)
print(now.hour)
print(now.minute)
print(now.second)
print()


# 나이 구하기
yourage = int(input("당신의 생년 > "))

print(now.year - yourage)
print()


# 날짜/시간 한 줄로 출력하기
print("{}년 {}월 {}일 {}시 {}분 {}초".format(
    now.year,
    now.month,
    now.day,
    now.hour,
    now.minute,
    now.second
))
print()


# 오전/오후 구분하기
if now.hour < 12:
    print("현재 시각은 {}시로 오전입니다.".format(now.hour))

if now.year >= 12:
    print("현재 시각은 {}시로 오후입니다.".format(now.hour))
print()


# 고궁 무료 입장 구분
age = int(input("당신의 나이를 알려주세요 > "))

if age >= 65 or age <= 5:
    print("무료 입장입니다.")
print()


# 첫 번째 수가 더 큰지 두 번째 수가 더 큰지 출력하기
a = float(input("첫 번째 숫자를 입력해주세요 > "))
b = float(input("두 번째 숫자를 입력해주세요 > "))

if a > b:
    print("처음 입력했던 {}가 {}보다 더 큽니다".format(a, b))

if a < b:
    print("두 번째로 입력했던 {}가 {}보다 더 큽니다".format(b, a))
print()


# if - else를 통해 홀수 짝수 구분
num = int(input("정수를 입력하시오 > "))

if num % 2 == 0:
    print("짝수입니다.")
else:
    print("홀수입니다.")
print()


# 택시 결정
money = int(input("수중에 있는 돈을 입력하시오 > "))

if money >= 5000:
    print("택시를 탄다")
elif money >= 2000:
    print("버스를 탄다")
else:
    print("걸어간다")
print()


# 성적에 따른 보상
score = int(input("성적을 입력하시오 > "))

if score >= 90:
    print("아이패드")
elif score >= 80:
    print("애플워치")
elif score >= 70:
    print("아무 일도 없음")
elif score >= 60:
    print("용돈 차감")
else:
    print("외출 금지")
print()


# 양수, 0, 음수 판별
a = int(input("정수 입력 > "))

if a < 0:
    print("음수")
elif a > 0:
    print("양수")
else:
    print("0")
print()


# 3의 배수 판별하기
a = int(input("정수 입력 > "))

if a % 3 == 0:
    print("3의 배수")
else:
    print("3의 배수 아님")
print()


# 나이의 따른 입장료
age = int(input("당신의 나이를 알려주세요 > "))

charge = 5000

if age < 8:
    print("0")
elif age < 60:
    print(charge)
else:
    print(charge / 2)
print()


# 3의 배수이면서 5의 배수 판별
a = int(input("정수 입력 > "))

if a % 3 == 0 and a % 5 == 0:
    print("3과 5의 배수")
else:
    print("3과 5의 배수 아님")
print()


# 나이의 따른 공원 입장료
age = int(input("당신의 나이를 알려주세요 > "))

if age >= 60 or age < 8:
    print("무료 입장입니다.")
else:
    print("5000원")
print()