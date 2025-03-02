import sys
import markdown


# python file-converter.py markdown inputfile outputfile
# マークダウンを HTML に変換するプログラム
def markdown_to_HTML_converter(inputfile, outputfile):
    # ファイルの読み込み
    try:
        with open(inputfile, "r", encoding="utf-8") as f:
            contents = f.read()

    except FileNotFoundError:
        print(f"入力ファイル'{inputfile}'が見つかりません。")
        return
    except IOError:
        print(f"入力ファイル'{inputfile}'の読み込み中にエラーが発生しました。")
        return
    except UnicodeDecodeError:
        print(f"入力ファイル'{inputfile}'のエンコーディングが不正です。")
        return

    # HTMLに変換
    html_contents = markdown.markdown(contents)

    # ファイルの書き込み
    try:
        with open(outputfile, "w", encoding="utf-8") as f:
            f.write(html_contents)

    except IOError:
        print(f"出力ファイル'{outputfile}'の書き込み中にエラーが発生しました。")
        return

    print(f"'{inputfile}'の内容をHTMLファイル'{outputfile}'に変換しました。")


if __name__ == "__main__":
    argv = sys.argv

    if len(argv) < 2:
        print("エラー: コマンドが指定されていません。")
        print("使用可能なコマンド: markdown")
        sys.exit(1)

    command = argv[1]

    if command == "markdown":
        if len(argv) < 4:
            print("エラー: 必要な引数が不足しています。")
        else:
            markdown_to_HTML_converter(argv[2], argv[3])

    else:
        print(f"エラー: '{command}' は無効なコマンドです。")
        print("使用可能なコマンド: markdown")
