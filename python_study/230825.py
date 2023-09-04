# 반복문으로 팩토리얼 구하기
def for_factorial(n):
    fact = 1
    for i in range(1, n+1):
        fact *= i
    return fact

print("1! : ", for_factorial(1))
print("2! : ", for_factorial(2))
print("3! : ", for_factorial(3))
print("4! : ", for_factorial(4))
print("5! : ", for_factorial(5))
print()


# 재귀함수로 팩토리얼 구하기
def factorial(n):
    if n <= 1:
        return 1
    else:
        return n * factorial(n-1)

print("1! : ", factorial(1))
print("2! : ", factorial(2))
print("3! : ", factorial(3))
print("4! : ", factorial(4))
print("5! : ", factorial(5))
print()


# 재귀함수로 피보나치 수열 구하기
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)
    
print("fibonacci(35) : ", fibonacci(35))
print()


# 재귀 함수로 피보나치 수열 구하기
counter = 0

def fibonacci(n):
    # global 키워드를 붙이지 않으면 지역변수로 인식하며 위에 선언한 counter 지역 변수가 참조 되어서 오류가 발생한다.
    global counter
    counter += 1

    if n <= 1:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)
    
print("fibonacci(35) : ", fibonacci(35))
print()


# 메모화를 사용한 피보나치 수열 구하기
# 메모화를 사용하면 한 번 계산한 값을 저장해 두었다가 다시 사용한다.
# 딕셔너리를 사용하여 이미 계산했었던 값을 저장해두고 꺼내서 사용하기에 코드 실행속도가 빨라진다.
dictionary = {
    1: 1,
    2: 1
}

def fibonacci(n):
    if n in dictionary:
        return dictionary[n]
    else:
        output = fibonacci(n-1) + fibonacci(n-2)
        dictionary[n] = output
        return output
    
print("fibonacci(10) : ", fibonacci(10))
print("fibonacci(20) : ", fibonacci(20))
print("fibonacci(30) : ", fibonacci(30))
print("fibonacci(40) : ", fibonacci(40))
print("fibonacci(50) : ", fibonacci(50))
print()


# list 평탄화
def flattan(data):
    output = []
    for item in data:
        if type(item) == list:
            output += flattan(item)
        else:
            output.append(item)
    return output

print(flattan([1, 2, 3, [4, [5, 6]], 7, 8, [9, 10]]))


# tuple
a, b = (10, 20)
print(a, b)
a, b = b, a
print(a, b)


# divmod()
a, b = 97, 40
divmod(a, b)


#함수의 매개 변수로 함수 전달하기
def call_10_times(func):
    for i in range(10):
        func()

def print_hello():
    print("안녕하세요.")

call_10_times(print_hello)


# map()함수와 filter()함수
def power(item):
    return item * item

def under_3(item):
    return item < 3

list_input_a = [1, 2, 3, 4, 5]

output_a = map(power, list_input_a)
print("# map() 함수의 실행결과")
print("map(power, list_input_a) : ", output_a)
print("map(power, list_input_a) : ", list(output_a))
print()

output_b = filter(under_3, list_input_a)
print("# filter() 함수 실행결과")
print("filter(under_3, list_input_a) : ", output_b)
print("filter(under_3, list_input_a) : ", list(output_b))


# lambda
power = lambda x: x * x
under_3 = lambda x: x < 3

list_input_a = [1, 2, 3, 4, 5]

output_a = map(power, list_input_a)
print("# map() 함수의 실행결과")
print("map(power, list_input_a) : ", output_a)
print("map(power, list_input_a) : ", list(output_a))
print()

output_b = filter(under_3, list_input_a)
print("# filter() 함수 실행결과")
print("filter(under_3, list_input_a) : ", output_b)
print("filter(under_3, list_input_a) : ", list(output_b))


# 인라인 lambda
list_input_a = [1, 2, 3, 4, 5]

output_a = map(lambda x: x * x, list_input_a)
print("# map() 함수의 실행결과")
print("map(power, list_input_a) : ", output_a)
print("map(power, list_input_a) : ", list(output_a))
print()

output_b = filter(lambda x: x < 3, list_input_a)
print("# filter() 함수 실행결과")
print("filter(under_3, list_input_a) : ", output_b)
print("filter(under_3, list_input_a) : ", list(output_b))