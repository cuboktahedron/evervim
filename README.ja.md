# evervim.vim

## 概要:
edit evernote on vim.

## 要件:
python及びpythonを有効にしてコンパイルしたvimが必要です。
vimのコマンドラインから:echo has('python')と実行し、1が表示されていれば利用できます。

以下のpythonパッケージを使用しています。

* markdown
* py-gfm
* emailipy

よくわからんがemailipyをimportしたら、lxmlでエラーになるんで
lxmlのパッケージを以下から取得して入れなおしたら動いたよ。
http://www.lfd.uci.edu/~gohlke/pythonlibs/#lxml

