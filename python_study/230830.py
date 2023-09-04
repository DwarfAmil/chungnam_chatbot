# # 가비지 컬렉터 : 변수 저장한 경우
# class Test:
#     def __init__(self, name):
#         self.name = name
#         print(f"{self.name} - 생성되었습니다.")
    
#     def __del__(self):
#         print(f"{self.name} - 파괴되었습니다.")

# a = Test("A")
# b = Test("B")
# c = Test("C")
# print()


# 프라이빗 변수
import math

class Circle:
    def __init__(self, radius):
        self.__radius = radius
    
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    
    def get_area(self):
        return math.pi * (self.__radius ** 2)
    
circle = Circle(10)
print("# 원의 둘레와 넓이를 구합니다.")
print("원의 둘레 : ", circle.get_circumference())
print("원의 넓이 : ", circle.get_area())
print()


# 게터, 세터
class Circle:
    def __init__(self, radius):
        self.__radius = radius
    
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    
    def get_area(self):
        return math.pi * (self.__radius ** 2)
    
    def get_radius(self):
        return self.__radius
    
    def set_radius(self, value):
        if value <= 0:
            raise TypeError("길이는 양의 숫자여야 합니다.")
        self.__radius = value

circle = Circle(10)
print("# 원의 둘레와 넓이를 구합니다.")
print("원의 둘레 : ", circle.get_circumference())
print("원의 넓이 : ", circle.get_area())
print()

print("# __radius에 접근합니다.")
print(circle.get_radius())
print()

circle.set_radius(2)
print("# 반지름을 변경하고 원의 둘레와 넓이를 구합니다.")
print("원의 둘레 : ", circle.get_circumference())
print("원의 넓이 : ", circle.get_area())
print()


# 데코레이터를 사용해 게터와 세터 만들기
class Circle:
    def __init__(self, radius):
        self.__radius = radius
    
    def get_circumference(self):
        return 2 * math.pi * self.__radius
    
    def get_area(self):
        return math.pi * (self.__radius ** 2)
    
    @property
    def radius(self):
        return self.__radius

    @radius.getter
    def radius(self):
        return self.__radius
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise TypeError("길이는 양의 숫자여야 합니다.")
        self.__radius = value

print("# 데코레이터를 사용한 Getter와 Setter")
circle = Circle(10)
print("원의 반지름 : ", circle.radius)
circle.radius = 2
print('변경된 반지름 : ', circle.radius)
print()

# print("# 강제로 예외를 발생시킵니다.")
# circle.radius = -10
# print()


# 상속의 활용
class Parent:
    def __init__(self):
        self.value = "테스트"
        print("Parent 클래스의 __init__() 메소드가 호출되었습니다.")
    
    def test(self):
        print("Parent 클레스의 test() 메소드입니다.")

class Child(Parent):
    def __init__(self):
        super().__init__()
        print("Child 클래스의 __init__() 메소드가 호출되었습니다.")

child = Child()
child.test()
print(child.value)
print()


# # 사용자 정의 예외 클래스 만들기
# class CustomException(Exception):
#     def __init__(self):
#         Exception.__init__(self)

# raise CustomException


# # 자식 클래스로써 부모의 함수 재정의(오버라이드)하기
# class CustomException(Exception):
#     def __init__(self):
#         Exception.__init__(self)
#         print("### 내가 만든 오류가 생성되었어요! ###")

#     def __str__(self) -> str:
#         return "오류가 발생했어요"
    
# raise CustomException


# # 자식 클래스로써 부모에 없는 새로운 함수 정의하기
# class CustomException(Exception):
#     def __init__(self):
#         Exception.__init__(self, message, value)
#         self.message = message
#         self.value = value

#     def __str__():
#         return self.message

#     def print(self):
#         print("###### 오류 정보 ######")
#         print("메시지 : ", self.message)
#         print("값 : ", self.value)

# try:
#     raise CustomException("딱히 이유 없음", 273)
# except CustomException as e:
#     e.print()


# 계산기
result1 = 0
result2 = 0

def adder1(num):
    global result1
    result1 += num
    return result1

def adder2(num):
    global result2
    result2 += num
    return result2

adder1(1)
print(result1)
adder2(3)
print(result2)
adder1(5)
print(result1)
adder2(9)
print(result2)
print()


# class로 만들기
class Calculator:
    def __init__(self):
        self.result = 0

    def adder(self, num):
        self.result += num
        return self.result
    
cal1 = Calculator()
cal2 = Calculator()

cal1.adder(3)
cal1.adder(3)
cal1.adder(5)
cal1.adder(7)

print(cal1.result)
print(cal2.result)
print()


# class
class Service:
    secret = "영구는 배꼽이 두 개다"

    def setname(self, name):
        self.name = name

    def sum(self, a, b):
        result = a + b
        print(f"{self.name}님 {a} + {b}은 {result}입니다.")

pey = Service()
pey.setname("홍길동")
pey.sum(1, 1)

pel = Service()
pel.setname("고길동")
pel.sum(3, 1)
print()


# FourCal
class FourCal:
    def setdata(self, first, second):
        self.first = first
        self.second = second
    
    def sum(self):
        result = self.first + self.second
        return result
    
    def sub(self):
        result = self.first - self.second
        return result
    
    def mul(self):
        result = self.first * self.second
        return result
    
    def div(self):
        result = self.first / self.second
        return result

a = FourCal()
a.setdata(4, 2)

b = FourCal()
b.setdata(3, 7)

print(a.sum())
print(a.sub())
print(a.mul())
print(a.div())

print(b.sum())
print(b.sub())
print(b.mul())
print(b.div())
print()


# class
class HousePark:
    lastname = "박"

    def __init__(self, name):
        self.fullname = self.lastname + name

    def travel(self, where):
        print(f"{self.fullname}, {where} 여행을 가다.")

    def love(self, other):
        print(f"{self.fullname}, {other.fullname} 사랑에 빠졌네")

    def fight(self, other):
        print(f"{self.fullname}, {other.fullname} 싸우네")

    def __add__(self, other):
        print(f"{self.fullname}, {other.fullname} 결혼했네")

    def __sub__(self, other):
        print(f"{self.fullname}, {other.fullname} 이혼했네")

class HouseKim(HousePark):
    lastname = "김"

    def travel(self, where, day):
        print(f"{self.fullname}, {where} 여행 {day}일 가다.")

pey = HousePark("응용")
pes = HouseKim("이현")
pey.travel("시간")
pes.travel("시간", 10)
pey.love(pes)
pey + pes
pey.fight(pes)
pey - pes
print()


# id
a = 3
print(id(3))
print(id(a))
b = a
print(id(b))