import sys


class file_manipulator:

    def __int__(self):
        pass

    # reverse inputpath outputpath
    # inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成します。
    def reverse(self, inputpath, outputpath):

        # ファイルの読み込み
        try:
            with open(inputpath, "r") as f:
                contents = f.read()
        except FileNotFoundError:
            print(f"入力ファイル{inputpath}が見つかりません。")
            return
        except IOError:
            print(f"入力ファイル{inputpath}の読み込み中にエラーが発生しました。")
            return

        # 反転
        reverse_contents = contents[::-1]

        # ファイルの書き込み
        try:
            with open(outputpath, "w") as f:
                f.write(reverse_contents)
        except IOError:
            print(f"出力ファイル{outputpath}の書き込み中にエラーが発生しました。")
            return

        print(f"{inputpath}の内容を反転して、{outputpath}に保存しました。")

    # copy inputpath outputpath
    # inputpath にあるファイルのコピーを作成し、outputpath として保存します。
    def copy(self, inputpath, outputpath):
        # ファイルの読み込み
        try:
            with open(inputpath, "r") as f:
                contents = f.read()

        except FileNotFoundError:
            print(f"入力ファイル{inputpath}が見つかりません。")
            return
        except IOError:
            print(f"入力ファイル{inputpath}の読み込み中にエラーが発生しました。")
            return

        # ファイルの書き込み
        try:
            with open(outputpath, "w") as f:
                f.write(contents)

        except IOError:
            print(f"出力ファイル{outputpath}の書き込み中にエラーが発生しました。")
            return

        print(f"{inputpath}の内容をコピーして、{outputpath}に保存しました。")

    # duplicate-contents inputpath n
    # inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製します。
    def duplicate_contents(self, inputpath, duplicate_count):
        # ファイルの読み込み
        try:
            with open(inputpath, "r") as f:
                contents = f.read()

        except FileNotFoundError:
            print(f"入力ファイル{inputpath}が見つかりません。")
            return
        except IOError:
            print(f"入力ファイル{inputpath}の読み込み中にエラーが発生しました。")
            return

        # 指定回数複製
        duplicated_contents = contents * duplicate_count

        # ファイルの書き込み
        try:
            with open(inputpath, "w") as f:
                f.write(duplicated_contents)

        except IOError:
            print(f"出力ファイル{inputpath}の書き込み中にエラーが発生しました。")
            return

        print(
            f"{inputpath}の内容を{duplicate_count}回複製して、{inputpath}に保存しました。"
        )

    # replace-string inputpath needle newstring
    # inputpath にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換えます。
    def replace_string(self, inputpath, needle, newstring):
        # ファイルの読み込み
        try:
            with open(inputpath, "r") as f:
                contents = f.read()

        except FileNotFoundError:
            print(f"入力ファイル{inputpath}が見つかりません。")
        except IOError:
            print(f"入力ファイル{inputpath}の読み込み中にエラーが発生しました。")
            return

        if needle not in contents:
            print(f"入力ファイル {inputpath} の中に '{needle}' は含まれていません。")
            return

        # 文字列置き換え
        replaced_contents = contents.replace(needle, newstring)

        # ファイルの書き込み
        try:
            with open(inputpath, "w") as f:
                f.write(replaced_contents)

        except IOError:
            print(f"出力ファイル{inputpath}の書き込み中にエラーが発生しました。")
            return

        print(f"{inputpath}の内容を{needle}から{newstring}に書き換えました。")


if __name__ == "__main__":
    argv = sys.argv
    if len(argv) < 2:
        print("エラー: コマンドが指定されていません。")
        print("使用可能なコマンド: reverse, copy, duplicate-contents, replace-string")
        sys.exit(1)

    command = argv[1]
    manipulator = file_manipulator()

    if command in ["reverse", "copy"]:
        if len(argv) < 4:
            print("エラー: 必要な引数が不足しています。")
        else:
            if command == "reverse":
                manipulator.reverse(argv[2], argv[3])
            else:
                manipulator.copy(argv[2], argv[3])

    elif command == "duplicate-contents":
        if len(argv) < 4:
            print("エラー: 必要な引数が不足しています。")
        else:
            try:
                duplicate_count = int(argv[3])
                manipulator.duplicate_contents(argv[2], duplicate_count)
            except ValueError:
                print("エラー: duplicate-contents の引数は整数である必要があります。")

    elif command == "replace-string":
        if len(argv) < 5:
            print("エラー: 必要な引数が不足しています。")
        else:
            manipulator.replace_string(argv[2], argv[3], argv[4])

    else:
        print(f"エラー: '{command}' は無効なコマンドです。")
        print("使用可能なコマンド: reverse, copy, duplicate-contents, replace-string")
