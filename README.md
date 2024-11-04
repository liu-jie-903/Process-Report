# ROUTE進捗報告 2024/11/05

## 前回までの進捗
VRoid Studioで女の子のモデルを作成し、VRMファイルとしてBlenderにインポートする。Blender上で、VRMファイルのアーマチュア（キャラクターの骨格）をBVHファイルのアーマチュア（モーションキャプチャの骨格）に自動ウェイトを使用して適合させる。

## 今回の取り組み
### 概要
これらのプロセスをPythonを使って自動化するため、まずはBlenderのPython APIを利用して、VRoidモデルの腕の長さをBVHデータの腕の長さに一致させるコードを作成する。

### Pythonプログラムの説明
* VVRoidモデルの前腕と上腕がBVHデータより短いため、BVHの長さに合わせる調整を目標とする。
* VRoidおよびBVHアーマチュアの前腕と上腕の長さを取得し、Pythonコードを用いてVRoidモデルの前腕をBVHの前腕の長さに合わせてスケーリングする。
* 調整後のVRoidモデルとBVHの腕の長さを出力し、一致しているかどうかを確認できるようにする。

### 結果
* コンソール：
![image](https://github.com/user-attachments/assets/8c9badc3-fecf-4567-a21a-a84a461e9cf2)

* レイアウト：
![image](https://github.com/user-attachments/assets/400735f2-1102-4f5c-a963-0ff2f221ccd9)
![image](https://github.com/user-attachments/assets/897f5b55-5500-461b-b8f4-38973e97ddb2)

### 解決できなかったこと
* このプログラムは、`main`メソッドで、`ClassC c = new ClassA();`に変化したら、コンパイルエラーとなる。この原因について考察した。
* まず、`ClassC c = new ClassA();`のコードの意味は、クラスC型の変数ｃに`new ClassA()`で生成された`ClassA`クラスのインスタンスを代入しようとする。そして、`CLassC`クラスは`CLassA`クラスを継承しているため、`CLassC`の変数で`CLassA`のインスタンスを保持することができる。しかし、`ClassC c = new ClassA();`の場合、`c.print()`を呼び出すと、実際のオブジェクトの型が`CLassA`なので、`Classc`の`prirnt()`メソッドを呼び出せない。Javaは静的型付けを持つ言語であり、コンパイル時に変数やメソッドの型が決定されるため、変数`c`を通じて呼び出すことができるメソッドは`ClassA`のメソッドに限定される。
* 従って、もし`ClassA`のインスタンスに対して`ClassC`のメソッドを呼び出したい場合は、型キャストを使用して明示的に型を変換する必要がある。

## 今後の方針



### 参考文献
* 演習のウェブサイト
* 「基礎から始めるJavaのコンストラクタ 構文から上手な使い方まで」ENGINEER.CLUB　[[https://www.javadrive.jp/start/string/index14.html](https://www.bold.ne.jp/enginee](https://www.bold.ne.jp/engineer-club/java-constructor), 2023/11/11
