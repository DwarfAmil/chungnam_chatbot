def solution(my_string, is_prefix):
    answer = 1
    a = len(my_string) - 1
    b = "".join(reversed(is_prefix))
    print(b)
    print(len(b))
    for i in b:
        if i != my_string[a]:
            answer = 0
            print(a)
            return answer
        
        if a - 1 < 0:
            answer = 0
            print(a)
            return answer
        else:
            a -= 1
    return answer

if __name__ == "__main__":
    print(solution("asdf", "fdsa"))