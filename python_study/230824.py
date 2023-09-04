# 함수 사용해보기
def print_3_times():
    print("안녕하세요")
    print("안녕하세요")
    print("안녕하세요")

print_3_times()
print()


# 매개변수의 기본
def print_n_times(value, n):
    for i in range(n):
        print(value)

print_n_times("안녕하세요", 5)
print()


# 가변 매개변수
def print_n_times(n, *values):
    for i in range(n):
        for value in values:
            print(value)
        print()

print_n_times(3, "안녕하세요", "즐거운", "파이썬 프로그래밍")
print()


# 키워드 매개변수
def print_n_times(*values, n=2):
    for i in range(n):
        for value in values:
            print(value)
        print()
    
print_n_times("안녕하세요", "즐거운", "파이썬 프로그래밍", n=3)
print()


# 자료와 함께 리턴하기
def return_test():
    return 100

value = return_test()
print(value)
print()


# 범위 내부의 정수를 모두 더하는 함수
def sum_all(start, end):
    output = 0
    for i in range(start, end + 1):
        output += i
    return output

print(f"0 to 100 : {sum_all(0, 100)}")
print(f"0 to 1000 : {sum_all(0, 1000)}")
print(f"50 to 100 : {sum_all(50, 100)}")
print(f"500 to 1000 : {sum_all(500, 1000)}")
print()


# 기본 매개변수와 키워드 매개변수를 활용하여 범위 내부의 정수를 모두 더하는 함수
def sum_all(start = 0, end = 100, step = 1):
    output = 0
    for i in range(start, end + 1, step):
        output += i
    return output

print(f"A. {sum_all(0, 100, 10)}")
print(f"B. {sum_all(end = 100)}")
print(f"C. {sum_all(end = 100, step = 2)}")
print()


# 파일 열고 닫기
file = open("basic.txt", "w")

file.write("Hello Python Programming...!")

file.close()


# with 키워드
with open("basic.txt", "w") as file:
    file.write("Hello Python Programming...!")


# 파일 읽기
with open("basic.txt", "r") as file:
    contents = file.read()
print(contents)
print()


# 랜덤하게 1000명의 키와 몸무게 만들기
import random
hanguls = list("가나다라마바사아자차카타파하")

with open("info.txt", "w") as file:
    for i in range(1000):
        name = random.choice(hanguls) + random.choice(hanguls)
        weight = random.randrange(40, 100)
        height = random.randrange(140, 200)
        file.write(f"{name}, {weight}, {height}\n")


# 반복문으로 파일 한 줄씩 읽기
with open("info.txt", "r") as file:
    for line in file:
        (name, weight, height) = line.strip().split(", ")

        if (not name) or (not weight) or (not height):
            continue

        bmi = int(weight) / ((int(height) / 100) ** 2)
        result = ""
        if 25 <= bmi:
            result = "과체중"
        elif 18.5 <= bmi:
            result = "정상 체중"
        else:
            result = "저체중"

        print('\n'.join([
            "이름: {}",
            "몸무게: {}",
            "키: {}",
            "BMI: {}",
            "결과: {}"
        ]).format(name, weight, height, bmi, result))
        print()
print()