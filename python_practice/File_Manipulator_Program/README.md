# File_Manipulator_Program
    ファイル操作プログラム
    Recursion(<https://recursionist.io/>)のプロジェクトの一つ

## 実行方法
### 1. reverse：反転
inputpath にあるファイルを受け取り、outputpath に inputpath の内容を逆にした新しいファイルを作成
```sh
python File_Manipulator_Program.py reverse inputpath outputpath
``` 

### 2. copy：コピー
inputpath にあるファイルのコピーを作成し、outputpath として保存
```sh
python File_Manipulator_Program.py copy inputpath outputpath
```

### 3. duplicate-contents : 複製
inputpath にあるファイルの内容を読み込み、その内容を複製し、複製された内容を inputpath に n 回複製
```sh
python File_Manipulator_Program.py duplicate-contents inputpath n
```

### 3. replace-string : 置換
inputpath にあるファイルの内容から文字列 'needle' を検索し、'needle' の全てを 'newstring' に置き換え
```sh
python File_Manipulator_Program.py replace-string inputpath needle newstring
```
