boarder = {"1": " ", "2": " ", "3": " ", "4": " ", "5": " ", "6": " ", "7": " ", "8": " ", "9": " "}
boarder_keys = []

for key in boarder:
    boarder_keys.append(key)


def visual_board(board_num):
    print(board_num["7"] + "|" + board_num["8"] + "|" + board_num["9"])
    print("-+-+-")
    print(board_num["4"] + "|" + board_num["5"] + "|" + board_num["6"])
    print("-+-+-")
    print(board_num["1"] + "|" + board_num["2"] + "|" + board_num["3"])


def game():
    turn = "X"
    count = 0
    for i in range(8):
        visual_board(boarder)
        print("Your turn, " + turn + "! Where should I go?")
        move = input()
        if boarder[move] == " ":
            boarder[move] = turn
            count += 1
            print()
        else:
            print("It's already filled.\nWhere would you like to go?")
            print()
            continue

        if count >= 5:
            if boarder["1"] == boarder["2"] == boarder["3"] != " ":
                visual_board(boarder)
                print("\nGame End\n")
                print("---------- > " + turn + " < Winner! ----------")
                break
            elif boarder["4"] == boarder["5"] == boarder["6"] != " ":
                visual_board(boarder)
                print("\nGame End\n")
                print("---------- > " + turn + " < Winner! ----------")
                break
            elif boarder["7"] == boarder["8"] == boarder["9"] != " ":
                visual_board(boarder)
                print("\nGame End\n")
                print("---------- > " + turn + " < Winner! ----------")
                break
            elif boarder["1"] == boarder["4"] == boarder["7"] != " ":
                visual_board(boarder)
                print("\nGame End\n")
                print("---------- > " + turn + " < Winner! ----------")
                break
            elif boarder["2"] == boarder["5"] == boarder["8"] != " ":
                visual_board(boarder)
                print("\nGame End\n")
                print("---------- > " + turn + " < Winner! ----------")
                break
            elif boarder["3"] == boarder["6"] == boarder["9"] != " ":
                visual_board(boarder)
                print("\nGame End\n")
                print("---------- > " + turn + " < Winner! ----------")
                break
            elif boarder["1"] == boarder["5"] == boarder["9"] != " ":
                visual_board(boarder)
                print("\nGame End\n")
                print("---------- > " + turn + " < Winner! ----------")
                break
            elif boarder["3"] == boarder["5"] == boarder["7"] != " ":
                visual_board(boarder)
                print("\nGame End\n")
                print("---------- > " + turn + " < Winner! ----------")
                break

        if count == 9:
            print("\nGame End\n")
            print("It's a tie.")

        if turn == "X":
            turn = "O"
        else:
            turn = "X"


if __name__ == "__main__":
    game()