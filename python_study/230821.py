# 유머를 조건문으로 구현
score = float(input("학점 입력 > "))

if score == 4.5:
    print("신")
elif 4.2 <= score < 4.5:
    print("교수님의 사랑")
elif 3.5 <= score < 4.5:
    print("현 체제의 수호자")
elif 2.8 <= score < 4.5:
    print("일반인")
elif 2.3 <= score < 4.5:
    print("일탈을 꿈꾸는 소시민")
elif 1.75 <= score < 4.5:
    print("오락문화의 선구자")
elif 1.0 <= score < 4.5:
    print("불가촉천민")
elif 0.5 <= score < 4.5:
    print("자벌레")
elif 0 < score < 4.5:
    print("플랑크톤")
elif score == 0:
    print("시대를 앞서가는 혁명의 씨앗")
print()


# 세 수 중 가장 큰 수 찾기 - 1
a = int(input("숫자를 입력하시오 > "))
b = int(input("숫자를 입력하시오 > "))
c = int(input("숫자를 입력하시오 > "))

if a > b:
    if a > c:
        print(f"{a}이 가장 큰 수 입니다.")
    else:
        print(f"{c}이 가장 큰 수 입니다.")
elif b > c:
    print(f"{b}이 가장 큰 수 입니다.")
else:
    print(f"{c}이 가장 큰 수 입니다.")
print()


# 세 수 중 가장 큰 수 찾기 - 2
max = int(input("숫자를 입력하시오 > "))
a = int(input("숫자를 입력하시오 > "))

if a > max:
    max = a

a = int(input("숫자를 입력하시오 > "))

if a > max:
    max = a

print(f"{max}이 가장 큰 수 입니다.")
print()


# 자판기 만들기
money = int(input("수중에 가진 돈을 입력해주세요 > "))

menu = [1000, 800, 900, 700, 600, 500]

if money < 1000:
    print(f"자판기의 음료수의 가격보다 돈이 부족합니다. 입력하신 금액 : {money}")
else:
    choice = int(input("메뉴를 골라주세요\n1. 콜라 2. 사이다 3. 환타 4. 밀키스 5. 솔의눈 6. 삼다수\n-------------------------------------------------------\n>"))
    choice -= 1

    print(f"남은 잔액은 {money - menu[choice]}입니다.")
print()


# pass 키워드
num = int(input("정수 입력 > "))

if num > 0:
    pass
else: 
    pass
print()


# list
list_a = [273, 32, 103, "문자열", True, False]

print(list_a[0])
print(list_a[1])
print(list_a[2])
print(list_a[1:3])
print()


# list 요소 변경
list_a = [273, 32, 103, "문자열", True, False]

list_a = "hi"

print(list_a[0])
print()


# list 접근 연산자 이중 사용
list_a = [273, 32, 103, "문자열", True, False]

print(list_a[3])
print(list_a[3][0])
print()


# 2중 list 구조
list_a = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print(list_a[1])
print(list_a[1][1])
print()


# list 연산자
list_a = [1, 2, 3]
list_b = [4, 5, 6]

print("# 리스트")
print(f"list_a = {list_a}")
print(f"list_b = {list_b}\n")
print("# 리스트 기본 연산자")
print(f"list_a + list_b = {list_a + list_b}")
print(f"list_a * 3 = {list_a * 3}\n")
print("# 리스트 길이 구하기")
print(f"len(list_a) = {len(list_a)}")
print()


# list 요소 추가
list_a = [1, 2, 3]

print("# 리스트 뒤에 요소 추가하기")
list_a.append(4)
list_a.append(5)
print(list_a, "\n")
print("# 리스트 중간에 요소 추가하기")
list_a.insert(0, 10)
print(list_a)
print()


# while 반복문 사용하기
treeHit = 0
while treeHit < 10:
    treeHit += 1
    print(f"나무를 {treeHit}번 찍었습니다.")
    if treeHit == 10:
        print("나무가 넘어갑니다.")
print()


# while 예제
prompt = """
1. Add
2. Del
3. List
4. Quit
    
Enter number : """

number = 0
while number != 4:
    number = int(input(prompt))
print()


# break 사용
coffee = 10
money = 300
while money:
    print("돈을 받았으니 커피를 줍니다.")
    coffee -= 1
    print(f"남은 커피 양은 {coffee}개 입니다.\n")
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break
print()


# break 사용해서 자판기
coffee = 10
while True:
    money = int(input("돈을 넣어 주세요 : "))
    if money == 300:
        print("커피를 줍니다.")
        coffee -= 1
    elif money > 300:
        print(f"거스름돈 {money - 300}원을 주고 커피를 줍니다.")
        coffee -= 1
    elif money < 300:
        print("돈을 다시 돌려주고 커피를 주지 않습니다.")
    
    if not coffee:
        print("커피가 다 떨어졌습니다. 판매를 중지합니다.")
        break

    print(f"남은 커피 양은 {coffee}개 입니다.")
print()


# while 예제
i = 0
while i < 10:
    print(f"{i}번째 반복입니다.")
    i += 1
print()


# 구구단
dan = int(input("몇 단을 출력할까요? : "))
i = 1
while i < 10:
    print(f"{dan} * {i} = {dan * i}")
    i += 1
print()


# 5초 동안 반복하기
import time

num = 0

target_tick = time.time() + 5
while time.time() < target_tick:
    num += 1

print(f"5초 동안 {num}번 반복했습니다.")


# break 복습
i = 0

while True:
    print(f"{i}번째 반복문입니다.")
    i += 1

    text = input("반복을 종료하시겠습니까? y/n : ")
    if text in ["Y", "y"]:
        print("반복을 종료합니다.")
        break
print()


# 별 찍기
i = 0
while i < 10:
    print("*" * i)
    i += 1
while i != 0:
    print("*" * i)
    i -= 1
print()


# 다중 반복문
i = 0
j = 0
while i < 10:
    j = 0
    print(f"i = {i}")
    while j < 10:
        print(f"j = {j}\t", end = "")
        j += 1
    print()
    i += 1
print()


# 구구단
dan = 1
i = 1
while dan < 10:
    i = 1
    while i < 10:
        print(f"{dan} * {i} = {dan * i}\t", end = "")
        i += 1
    dan += 1
    print()
print()