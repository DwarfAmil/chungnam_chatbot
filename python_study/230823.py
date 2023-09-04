# 딕셔너리
dict = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "ingredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

print(f"name: {dict['name']}")
print(f"type: {dict['type']}")
print(f"ingredient: {dict['ingredient']}")
print(f"origin: {dict['origin']}")
print()

dict["name"] = "8D 건조 망고"
print(f"name: {dict['name']}")
print()


# random() 함수 사용하기
import random

# 임의의 실수를 반환
print(random.random())
# A ~ B 사이의 임의의 숫자를 반환
print(random.randint(1, 5))
# A ~ B 사이의 임의의 숫자를 반환 (B는 포함되지 않음)
print(random.randrange(1, 5))
print()

 
 # 로또 번호 생성기
lotto = []

while len(lotto) < 6:
    a = random.randint(1, 45)

    if a not in lotto:
        lotto.append(a)
print(lotto)
print()


# 키가 존재하는지 확인하고 값에 접근하기
dict = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "indredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

key = input("> 접근하고자 하는 키 : ")

if key in dict:
    print(dict[key])
else:
    print("존재하지 않는 키입니다.")
print()


# get() 함수 사용하기 (키가 존재하지 않는 경우 None 반환)
dict = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "indredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

value = dict.get("존재하지 않는 키")
print("값:", value)

if value == None:
    print("존재하지 않는 키에 접근했었습니다.")
print()


# for 반복문과 딕셔너리 (딕셔너리 내부에 있는 키가 변수 key에 하나씩 대입됨)
dict = {
    "name": "7D 건조 망고",
    "type": "당절임",
    "indredient": ["망고", "설탕", "메타중아황산나트륨", "치자황색소"],
    "origin": "필리핀"
}

for key in dict:
    print(key, ":", dict[key])
print()


# 딕셔너리 문제 3번
numbers = [1, 2, 6, 8, 4, 3, 2, 1, 9, 5, 4, 9, 7, 2, 1, 3, 5, 4, 8, 9, 7, 2, 3]
counter = {}

for number in numbers:
    if number in counter:
        counter[number] += 1
    else:
        counter[number] = 1
print(counter)
print()


# 딕셔너리 문제 4번
character = {
    "name": "기사",
    "level": 12,
    "items": {
        "sword": "불꽃의 검",
        "armor": "풀플레이트"
    },
    "skill": ["베기", "세게 베기", "아주 세게 베기"]
    }

for key in character:
    if type(character[key]) is dict:
        for key2 in character[key]:
            print(key2, ":", character[key][key2])
    elif type(character[key]) is list:
        for item in character[key]:
            print(key, ":", item)
    else:
        print(key, ":", character[key])
print()


# 리스트와 범위를 조합해서 사용하기
array = [273, 32, 103, 57, 52]

for i in range(len(array)):
    print(f"{i}번째 반복 : {array[i]}")
print()


# 역 반복문
for i in range(4, 0 - 1, -1):
    print(f"현재 반복 변수 : {i}")
print()


# while 반복문
i = 0
while i < 10:
    print(f"{i}번째 반복입니다.")
    i += 1
print()


# 해당하는 값 모두 제거하기
list = [1, 2, 1, 2]
value = 2

while value in list:
    list.remove(value)
print(list)
print()


# cantinue 키워드
numbers = [5, 15, 6, 20, 7, 25]

for number in numbers:
    if number < 10:
        continue
    print(number)
print()


# enumerate() 함수와 리스트
example_list = ["요소A", "요소B", "요소C"]

print("단순 출력")
print(example_list)
print()

print("enumerate() 함수 적용 출력")
print(enumerate(example_list))
print()

print("반복문과 조합하기")
for i, value in enumerate(example_list):
    print(f"{i}번째 요소는 {value}입니다.")
print()


# 딕셔너리의 items() 함수와 반복문 조합하기
example_dictionary = {
    "키A": "값A",
    "키B": "값B",
    "키C": "값C"
}

print("# 딕셔너리의 items() 함수")
print(f"items() : {example_dictionary.items()}")
print()

print("# 딕셔너리의 items() 함수와 반복문 조합하기")

for key, element in example_dictionary.items():
    print(f"dictionary[{key}] = {element}")
print()


# 리스트 내포 사용하기
array = [i * i for i in range(0, 20, 2)]
print(array)
print()


# 리스트 내포 조건문
array = ["사과", "자두", "초콜릿", "바나나", "체리"]
output = [fruit for fruit in array if fruit != "초콜릿"]
print(output)
print()


# reversed() 함수와 이터레이터
numbers = [1, 2, 3, 4, 5, 6]
r_num = reversed(numbers)

print("reversed_numbers : ", r_num)
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print(next(r_num))
print()


# *로 피라미드 만들기
for j in range(10):
    for i in range(19):
        if 19 // 2 + j >= i >= 19 // 2 - j:
            print("*", end="")
        else:
            print(" ", end="")
    print()
print()


# *로 다이아몬드 만들기
for j in range(10):
    for i in range(19):
        if 19 // 2 + j >= i >= 19 // 2 - j:
            print("*", end="")
        else:
            print(" ", end="")
    print()
for j in range(9, -1, -1):
    for i in range(19):
        if 19 // 2 + j >= i >= 19 // 2 - j:
            print("*", end="")
        else:
            print(" ", end="")
    print()


# *로 바.람.개.비 만들기
for i in range(10):
    for j in range(20):
        if j >= 10:
            if i <= (j - 10) * -1 + 9:
                print("*", end=" ")
            else:
                print(" ", end=" ")

        else:
            if i >= j:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()
for i in range(10):
    for j in range(19, -1, -1):
        if j >= 10:
            if i >= j - 10:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        
        if j <= 9:
            if i <= (j - 9) * -1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    print()
print()


# 금붕어 키우기
# 금붕어 수컷의 애칭을 지어주세요
# 금붕어 암컷의 애칭을 지어주세요
# 어항 수용 금붕어 수는 1000마리 입니다
# 금붕어 수컷과 암컷은 새끼낳습니다. 1턴 마다 1~10마리 랜덤으로 태어납니다.
# 숫놈과 암놈은 각각 동등하게 태어나며, 태어난 자식끼리도 1~10마리 랜덤으로 새끼를 낳습니다.
# 2회턴부터 턴마다 랜덤으로 암수 1~5쌍이 죽습니다. (2마리 ~ 10마리)

# 몇턴 만에 1000마리가 차는지 출력하시오


fish_a = input("금붕어 수컷의 애칭을 지어주세요 : ")
fish_b = input("금붕어 암컷의 애칭을 지어주세요 : ")
print("=============================================")

fish_count = 2

turn = 0

fish_discount = 0

while fish_count < 1000:
    turn += 1
    print(f"{turn}턴\t", end="")
    fish_plus = random.randrange(0, 10 + 1, 2) * (fish_count // 2)
    fish_count += fish_plus
    if turn >= 2:
        fish_discount = random.randrange(0, 10 + 1, 2)
        fish_count -= fish_discount

    print(f"{fish_count}마리\t{fish_plus}마리 추가\t{fish_discount}마리 감소")

    if fish_count >= 1000:
        print(f"{turn}턴 만에 {fish_count}마리가 차게 되었습니다.")
