# Hello World!
print("Hello World!")
print()


# 연산자 사용해보기
print(1 + 2)
print(3 * 50)
print(50 % 4)
print(50 / 4)
print()


# type() 사용해보기
print(type(23))
print(type("얀녕하세요"))
print(type(True))
print()


# 문자열 만들기
print("@ 하나만 출력합니다.")
print("Hello Python Programing...!")
print()

print("@ 여러 개를 출력합니다.")
print(10, 20, 30, 40, 50)
print("안녕하세요", "저의", "이름은", "박형진입니다!")
print()


# 문자열 내부에서 따음표 넣기
print("작은 따음표 출력 ''")
print('큰 따음표 출력 ""')
print("작은 따음표 출력 \'\'")
print("큰 따음표 출력 \"\"")
print()


# 오류 발생시키기 (Syntex error)
# print("""")


# escape(\) 문자 사용해보기
print("작은 따음표 출력 \'\'")
print("큰 따음표 출력 \"\"")
print("Hello\tWorld")
print("Hello\nWorld")
print("이름\t나이\t지역")
print("윤인성\t25\t강서구")
print("윤아린\t24\t강서구")
print("박형진\t19\t대구")
print()


# 여러줄 출력하기
print("비춰줘 넌 내 존재를 비춰줘\n길어져 나의 밤은 자꾸 길어져\n모두가 잠든 밤에 I think of u\n이 새벽에 이 새벽에")
print("""비춰줘 넌 내 존재를 비춰줘
지워져 내 감정에 눈물 지워져
더해줘 온 세상에 색을 더해줘
이 새벽에
""")


# 문자열 합치기 연산자
print("안녕" + "하세요")
print("안녕하세요" + "!")
# Type error 발생
# print("안녕하세요" + 1)
print()


# 문자열 반복 연산자
print("안녕하세요!!\t" * 3)
print()


# 문자 선택 연산자(인덱싱)
print("안녕하세요"[0])
print("안녕하세요"[1])
print("안녕하세요"[2])
print("안녕하세요"[3])
print("안녕하세요"[4])
print()


# 문자 선택 연산자(인덱싱) 뒤에서부터 시작
print("안녕하세요"[-1])
print("안녕하세요"[-2])
print("안녕하세요"[-3])
print("안녕하세요"[-4])
print("안녕하세요"[-5])
print()


# 문자열 범위 선택 연산자(슬라이싱)
print("안녕하세요"[0:3])
print("안녕하세요"[3:5])
print("안녕하세요"[3:])
print("안녕하세요"[:3])
print()


# 변수 만들기
hello = "안녕하세요"
print(hello)
hello = "안녕히가세요"
print(hello)
# Index error 발생
# print(hello[10])
print()


# 문자열 길이 구하기
print(len("어떤 문자열을 감싸주게되면"))
print()


# 정수, 실수
print(type(23))
print(type(-23))
print(type(23.123))
print()


# 정수 나누기 연산자(//)
print(5 / 2)
print(5 // 2)
print()


# 나머지 연산자(%)
print(5 % 2)
print()


# 제곱 연산자(**)
print(2 ** 3)
print()


# 연산자의 우선 순위
print(5 + 3 * 2)
print((5 + 3) * 2)
print()


# Type error 발생시키기 
string = "str"
number = 123
# print(string + number)


# 변수 만들고 사용하기
score = 120
print(score + 2)
print(score * 2)
print(score / 2)
print(score % 2)
print(score * score)
print()


# 원의 둘레와 넓이 구해보기
pi = 3.14159265
r = 10

print("원주율 = ", pi)
print("반지름 = ", r)
print("원의 둘레 = ", 2 * pi * r)
print("원의 넓이 = ", pi * pi * r)
print()


# 복합 대입 연산자
# 문자열도 복합 대입 연산자(+=, *=) 사용 가능
a = 10
a += 8
a -= 8
a *= 5
a /= 5
a %= 1
a **= 8


# 문자열 복합 대입 연산자
str = "안녕하세요"
str += "!"
print(str)
print()


# 사용자의 입력받기(input)
# input은 기본적으로 문자열로 입력을 받는다.
str = input("인사말을 입력하시오 > ")
print(type(str))
print(str)
print()


# 문자열을 숫자로 바꾸기(cast / casting)
str_a = input("입력 A > ")
int_a = int(str_a)

str_b = input("입력 B > ")
int_b = int(str_b)

print("문자열 자료 : ", str_a + str_b)
print("숫자 자료 : ", int_a + int_b)
print()


# 간단한 계산기(float() 사용)
input_a = float(input("첫 번째 숫자 > "))
input_b = float(input("두 번째 숫자 > "))

print("덧셈 결과 : ", input_a + input_b)
print("뺄셈 결과 : ", input_a - input_b)
print("곱셈 결과 : ", input_a * input_b)
print("나눗셈 결과 : ", input_a / input_b)
print()


# 성적표 만들어보기
student = []
eng = []
math = []
kor = []
py = []
for i in range(4):
    student.append(input("학생의 이름을 입력해주세요 > "))
    eng.append(int(input("영어 점수를 입력해주세요 > ")))
    math.append(int(input("수학 점수를 입력해주세요 > ")))
    kor.append(int(input("국어 점수를 입력해주세요 > ")))
    py.append(int(input("Python 점수를 입력해주세요 > ")))

print("                                      성적표                   ")
print("---------------------------------------------------------------------------------------")
print("이름\t|\t국어\t|\t영어\t|\t수학\t|\tPython\t|\t평균")
print("---------------------------------------------------------------------------------------")

for i in range(4):
    print(student[i], "\t|\t", eng[i], "\t|\t", math[i], "\t|\t", kor[i], "\t|\t", py[i], "\t|\t", (eng[i] + math[i] + kor[i] + py[i]) / 4)
print()