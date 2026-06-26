# これは何か
AtCoder で使う Python のテンプレートです。
実行したいファイルの指定が簡単にできるのが特徴です。

# 使い方
## Python のプログラムを実行する場合
一般的な
```console
$ python a.py
```
を実行する代わりに
```console
$ python main.py a
```
で実行します。コンテスト中にコマンドの右端のアルファベットを変えるだけで、実行ファイルを変えられるのが嬉しい点です。これに対し、従来はカーソルを `.py` の直前まで持っていく必要があり、これが手間です。

## ファイルの内容を初期化する場合
`a.py` ~ `g.py` の内容を初期化したい場合は `init_file.sh` を実行してください。実行コマンドは次の通りです。
```console
$ ./init_file.sh
```

# フォルダ名について
本リポジトリ名は長いのでそのまま `git clone` をするとフォルダ名が長いかと思います。フォルダ名が `folder_name` となるように `git clone` するには次のように書けばよいです。
```console
$ git clone https://github.com/NAVYSHUNTA/atcoder_python_script_selector.git folder_name
```

例えば、 `folder_name` を `atcoder` で指定する場合は、以下のように書きます。
```console
$ git clone https://github.com/NAVYSHUNTA/atcoder_python_script_selector.git atcoder
```
