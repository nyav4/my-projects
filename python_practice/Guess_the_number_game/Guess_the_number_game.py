import random

TRY_NUMBER = 5


def guess_the_number_game():

    # ユーザー入力
    min_val = int(input("最小値を入力してください："))
    max_val = int(input("最大値を入力してください："))

    # ランダム値生成
    random_number = random.randint(min_val, max_val)

    # ゲーム回数分ループ
    for i in range(1, TRY_NUMBER + 1):
        # 予想値入力
        guess_number = int(input(f"{i}回目の予想値を入力していください："))

        if i == TRY_NUMBER:
            print(f"残念。正解は{random_number}でした。")

        elif guess_number == random_number:
            print("正解！")
            break

        elif guess_number > random_number:
            print(f"大きすぎます。残りのチャンスは{TRY_NUMBER - i}回!")

        else:
            print(f"小さすぎます。残りのチャンスは{TRY_NUMBER - i}回!")


if __name__ == "__main__":
    guess_the_number_game()
