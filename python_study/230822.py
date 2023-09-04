# del, pop()으로 리스트 요소 제거
list_a = [0, 1, 2, 3, 4, 5]
print("# 리스트의 요소 하나 제거하기")
del list_a[1]
print("del list_a[1] : ", list_a)
list_a.pop(2)
print("list_a.pop(2) : ", list_a)
print()


# for문 사용해보기
array = [273, 32, 103, 57, 52]

for element in array:
    print(element)
print()


# range() 사용해보기
sum = 0

for i in range(10):
    print(i)
    sum += i
print(sum)
print()

for i in range(2, 10):
    for j in range(1, 10):
        print(f"{i} * {j} = {i * j}", end = "   ")
    print()
print()


# for 리스트 내포
a = [1, 2, 3, 4]
result = []

for num in a:
    result.append(num * 3)

print(result)

result = []
result = [num * 3 for num in a]
print(result)
print()


# 1부터 10까지 출력 - 1
print("------------- 1부터 10까지 출력 - 1 -------------")
for i in range(1, 11):
    print(i)
print()


# 1부터 10까지 출력 - 2
print("------------- 1부터 10까지 출력 - 2 -------------")
for i in range(1, 11):
    print(i)
print()


# 10부터 1까지 출력하기
print("------------- 10부터 1까지 출력하기 -------------")
a = 10
for i in range(10):
    print(a)
    a -= 1
print()


# 1부터 100까지의 합 구하기
print("------------- 1부터 100까지의 합 구하기 -------------")
sum = 0
for i in range(1, 101):
    sum += i
print(sum)
print()


# 1부터 100가지의 수 중 짝수의 합 구하기
print("------------- 1부터 100까지의 수 중 짝수의 합 구하기 -------------")
sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum += i
print(sum)
print()


# 1, -2, 3, 4, ... 99, -100의 합 구하기
print("------------- 1, -2, 3, 4, ... 99, -100의 합 구하기 -------------")
sum = 0
for i in range(1, 101):
    if i % 2 == 0:
        sum -= i
    else:
        sum += i
print(sum)
print()


# 계승 구하기
print("------------- 계승 구하기 -------------")
tact = 1
a = 5
for i in range(5):
    tact *= a
    a -= 1
print(tact)
print()


# 약수 구하기
print("------------- 약수 구하기 -------------")
n = int(input("숫자를 입력하세요 : "))

for i in range(1, n + 1):
    if n % i == 0:
        print(f"{i}\t", end="")
print()
print()


# 구구단 생긴거 바꾸기
for i in range(1, 10):
    for dan in range(2, 10):
        print(f"{dan} * {i} = {dan * i}\t", end="")
    print()
print()


# 딕셔너리
dict_a = {
    "name":"어벤져스 엔드게임",
    "type":"히어로 무비"
}

print(dict_a)
print(dict_a["name"])
print(dict_a["type"])

dict_b = {
    "director":["안소니 루소", "조 루소"],
    "cast":["아이언맨", "타노스", "토르", "닥터스트레인지", "헐크"]
}

print(dict_b["director"])
print(dict_b["cast"])
print()