# BeautifulSoup 모듈로 날씨 가져오기
from bs4 import BeautifulSoup
from urllib import request

target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

soup = BeautifulSoup(target, 'html.parser')


for location in soup.select('location'):
    print('도시 :', location.select_one('city').string)
    print('날씨 :', location.select_one('wf').string)
    print('최저기온 :', location.select_one('tmn').string)
    print('최고기온 :', location.select_one('tmx').string)
    print()


# flask 모듈
from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello():
    return "<h1>Hello World!</h1>"


# BeautifulSoup 스크레이핑 실행하기
from bs4 import BeautifulSoup
from urllib import request

app = Flask(__name__)


@app.route("/")
def hello():
    target = request.urlopen("http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=108")

    soup = BeautifulSoup(target, 'html.parser')

    output = ""
    for location in soup.select('location'):
        output += "<h3>{}</h3>".format(location.select_one('city').string)
        output += "날씨 : {}</br>".format(location.select_one('wf').string)
        output += "최저/최고 기온 : {}/{}".format(location.select_one('tmn').string, location.select_one('tmx').string)
        output += "<hr/>"
    return output


# 함수 데코레이터 기본
def test(function):
    def wrapper():
        print("인사가 시작되었습니다.")
        function()
        print("인사가 종료되었습니다.")
    return wrapper

@test
def hello():
    print("hello")

hello()
print()


# # 쉬운 모듈 만들기
# import test_module as test


# radius = test.number_input()
# print(test.get_circumference(radius))
# print(test.get_circle_area(radius))
# print()


# # 모듈 이름을 출력하는 모듈 만들기
# import test_module as test

# print("# 모듈의 __name__ 출력하기")
# print(__name__)
# print()


# 엔트리 포인트를 확인하는 모듈
import test_module as test

radius = test.number_input()
print(test.get_circumference(radius))
print(test.get_circle_area(radius))
print()


# 패키지 만들기
import test_package.module_a as a
import test_package.module_b as b

print(a.var_a)
print(b.var_b)
print()


# __init__.py의 용도
from test_package import *

print(module_a.var_a)
print(module_b.var_b)
print()


# 딕셔너리로 객체 만들기
students = [
    {"name": "윤인성", "korean": 87, "math": 98, "english": 88, "science": 95},
    {"name": "연하진", "korean": 92, "math": 98, "english": 96, "science": 98},
    {"name": "구지연", "korean": 76, "math": 96, "english": 94, "science": 90},
    {"name": "나선주", "korean": 98, "math": 92, "english": 96, "science": 92},
    {"name": "윤아린", "korean": 95, "math": 98, "english": 98, "science": 98},
    {"name": "윤명월", "korean": 64, "math": 88, "english": 92, "science": 92},
]

print("이름", "총점", "평균", sep="\t")

for student in students:
    score_sum = student["korean"] + student["math"] + \
        student["english"] + student["science"]
    score_average = score_sum / 4
    print(student["name"], score_sum, score_average, sep="\t")
print()


# 함수로 객체 만들기
def create_student(name, korean, math, english, science):
    return {
        "name": name,
        "korean": korean,
        "math": math,
        "english": english,
        "science": science
    }


def student_get_sum(student):
    return student["korean"] + student["math"] + \
        student["english"] + student["science"]


def student_get_average(student):
    return student_get_sum(student) / 4


def student_to_string(student):
    return "{}\t{}\t{}".format(\
        student["name"],\
        student_get_sum(student),\
        student_get_average(student))


students = [
    create_student("윤인성", 87, 98, 88, 95),
    create_student("연하진", 92, 98, 96, 98),
    create_student("구지연", 76, 96, 94, 90),
    create_student("나선주", 98, 92, 96, 92),
    create_student("윤아린", 95, 98, 98, 98),
    create_student("윤명월", 64, 88, 92, 92)
]


print("이름", "총점", "평균", sep="\t")
for student in students:
    print(student_to_string(student))
print()



# 클래스로 객체 만들기
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science


students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]


for student in students:
    print(student.name, student.korean, student.math, student.english, student.science)
print()


# 클래스 내부에 함수(메소드) 선언하기
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    
    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    

    def get_average(self):
        return self.get_sum() / 4
    

    def to_string(self):
        return f"{self.name}\t{self.get_sum()}\t{self.get_average()}"

students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]


for student in students:
    print(student.to_string())


# isinstance()
class Human:
    def __init__(self):
        pass

class Student(Human):
    def __init__(self):
        pass

student = Student()

print("isinstance(student, Human) : ", isinstance(student, Human))
print("type(student) == Human : ", type(student) == Human)
print()


# 
class Student:
    def study(self):
        print("공부를 합니다.")


class Teacher:
    def teach(self):
        print("공부를 가르칩니다.")


classroom = [Student(), Student(), Student(), Student(), Teacher()]


for person in classroom:
    if isinstance(person, Student):
        person.study()
    elif isinstance(person, Teacher):
        person.teach()
print()


# __str__() 함수
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    
    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    

    def get_average(self):
        return self.get_sum() / 4
    

    def __str__(self):
        return f"{self.name}\t{self.get_sum()}\t{self.get_average()}"

students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

print("이름", "총점", "평균", sep="\t")
for student in students:
    print(str(student))
print()


# __str__() 함수
class Student:
    def __str__(self):
        return "공부를 합니다."

class Teacher:
    def __str__(self):
        return "공부를 가르칩니다."


classroom = [Student(), Student(), Student(), Student(), Teacher()]


for person in classroom:
    print(str(person))
print()


# 크기 비교 함수
class Student:
    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

    
    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    

    def get_average(self):
        return self.get_sum() / 4
    

    def __str__(self):
        return f"{self.name}\t{self.get_sum()}\t{self.get_average()}"


    def __eq__(self, value):
        return self.get_sum() == value.get_sum()
    
    def __ne__(self, value):
        return self.get_sum() != value.get_sum()
    
    def __gt__(self, value):
        return self.get_sum() > value.get_sum()
    
    def __ge__(self, value):
        return self.get_sum() >= value.get_sum()
    
    def __lt__(self, value):
        return self.get_sum() < value.get_sum()
    
    def __le__(self, value):
        return self.get_sum() <= value.get_sum()
    

students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

student_a = Student("윤인성", 87, 98, 88, 95)
student_b = Student("연하진", 92, 98, 96, 98)

print("student_a == student_b = ", student_a == student_b)
print("student_a != student_b = ", student_a != student_b)
print("student_a > student_b = ", student_a > student_b)
print("student_a >= student_b = ", student_a >= student_b)
print("student_a < student_b = ", student_a < student_b)
print("student_a <= student_b = ", student_a <= student_b)
print()


# 클래스 변수
class Student:
    count = 0

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        Student.count += 1
        print(f"{Student.count}번째 학생이 생성되었습니다.")

students = [
    Student("윤인성", 87, 98, 88, 95),
    Student("연하진", 92, 98, 96, 98),
    Student("구지연", 76, 96, 94, 90),
    Student("나선주", 98, 92, 96, 92),
    Student("윤아린", 95, 98, 98, 98),
    Student("윤명월", 64, 88, 92, 92)
]

print()
print(f"현재 생성된 총 학생 수는 {Student.count}명입니다.")
print()


# 클래스 함수
class Student:
    count = 0
    students = []

    @classmethod
    def print(cls):
        print("====== 학생 목록 ======")
        print("이름\t총점\t평균")
        
        for student in cls.students:
            print(str(student))
        print("======= ======= =======")

    def __init__(self, name, korean, math, english, science):
        self.name = name
        self.korean = korean
        self.math = math
        self.english = english
        self.science = science

        Student.count += 1
        Student.students.append(self)

    def get_sum(self):
        return self.korean + self.math + self.english + self.science
    
    def get_average(self):
        return self.get_sum() / 4
    
    def __str__(self):
        return f"{self.name}\t{self.get_sum()}\t{self.get_average()}"
    

Student("윤인성", 87, 98, 88, 95)
Student("연하진", 92, 98, 96, 98)
Student("구지연", 76, 96, 94, 90)
Student("나선주", 98, 92, 96, 92)
Student("윤아린", 95, 98, 98, 98)
Student("윤명월", 64, 88, 92, 92)
Student("김미화", 82, 56, 98, 88)
Student("김연화", 88, 74, 78, 92)
Student("박아현", 97, 92, 88, 95)
Student("서준서", 45, 52, 72, 78)

Student.print()
print()