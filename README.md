# ROUTE進歩報告 2024/11/05

## 今回までやっていたこと
VRoid Studioを使って女の子のモデルを作成し、VRMファイルとしてBlenderにインポートした。BlenderでVRMファイルのアーマチュア（人形モデル）をBVHファイルのアーマチュア（骨格）に合わせて自動ウェイトを設定した。

## 今回行ったこと
### 概要
* 以上のプロセスをPythonで自動的に行われるように

### 結果
* `ClassA a = new ClassC();`の場合：
![screenshot1_1](https://github.com/2023-ynu-programming-II/assignment05-liu-jie-903/assets/147288297/d4065a23-b958-446c-a42f-7c0c0f297ea8)
* `ClassC c = new ClassA();`の場合：
![screenshot1_2](https://github.com/2023-ynu-programming-II/assignment05-liu-jie-903/assets/147288297/a36f025e-7e4d-4302-a776-00bbeda687d4)

### 解決できなかったこと
* このプログラムは、`main`メソッドで、`ClassC c = new ClassA();`に変化したら、コンパイルエラーとなる。この原因について考察した。
* まず、`ClassC c = new ClassA();`のコードの意味は、クラスC型の変数ｃに`new ClassA()`で生成された`ClassA`クラスのインスタンスを代入しようとする。そして、`CLassC`クラスは`CLassA`クラスを継承しているため、`CLassC`の変数で`CLassA`のインスタンスを保持することができる。しかし、`ClassC c = new ClassA();`の場合、`c.print()`を呼び出すと、実際のオブジェクトの型が`CLassA`なので、`Classc`の`prirnt()`メソッドを呼び出せない。Javaは静的型付けを持つ言語であり、コンパイル時に変数やメソッドの型が決定されるため、変数`c`を通じて呼び出すことができるメソッドは`ClassA`のメソッドに限定される。
* 従って、もし`ClassA`のインスタンスに対して`ClassC`のメソッドを呼び出したい場合は、型キャストを使用して明示的に型を変換する必要がある。

## 今後の方針



### 参考文献
* 演習のウェブサイト
* 「基礎から始めるJavaのコンストラクタ 構文から上手な使い方まで」ENGINEER.CLUB　[[https://www.javadrive.jp/start/string/index14.html](https://www.bold.ne.jp/enginee](https://www.bold.ne.jp/engineer-club/java-constructor), 2023/11/11
