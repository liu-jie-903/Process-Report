# ROUTE進捗報告 2024/11/05

## 前回までの進捗
VRoid Studioで女の子のモデルを作成し、VRMファイルとしてBlenderにインポートする。Blender上で、VRMファイルのアーマチュア（キャラクターの骨格）をBVHファイルのアーマチュア（モーションキャプチャの骨格）に自動ウェイトを使用して適合させる。

## 今回の取り組み
### 概要
これらのプロセスをPythonを使って自動化するため、まずはBlenderのPython APIを利用して、VRoidモデルの腕の長さをBVHデータの腕の長さに一致させるコードを作成する。

### Pythonプログラムの説明
- VRoidモデルの前腕と上腕がBVHデータより短いため、BVHの長さに合わせる調整を目標とする。
- VRoidおよびBVHアーマチュアの前腕と上腕の長さを取得し、Pythonコードを用いてVRoidモデルの前腕をBVHの前腕の長さに合わせてスケーリングする。
- 調整後のVRoidモデルとBVHの腕の長さを出力し、一致しているかどうかを確認できるようにする。

### 結果
- **コンソール出力**:
    - コンソール上で、VRoidモデルとBVHの腕の長さが調整後に一致していることを確認できる。
    - コンソールの結果は以下の通り。
    ![image](https://github.com/user-attachments/assets/8c9badc3-fecf-4567-a21a-a84a461e9cf2)

- **Blenderレイアウト**:
    - Blenderでのビジュアル確認結果は以下の通り。
    ![image](https://github.com/user-attachments/assets/400735f2-1102-4f5c-a963-0ff2f221ccd9)
    ![image](https://github.com/user-attachments/assets/897f5b55-5500-461b-b8f4-38973e97ddb2)

- **現状の問題点**:
    - 調整後のVRoidモデルの腕の長さは数値的にはBVHと一致しているが、レイアウト上では、腕の形状が大きすぎ、向きも正しくない。
        - 向きについては、前腕が手に接続しているため、手の位置が固定されたまま前腕のみが動いた結果、前腕の動きが逆方向になっていると推測される。

### 課題と未解決事項
- 腕の形状がBVHに合わない原因を特定できていない。
- どのパラメータを調整すべきかが不明である。

## 今後の方針
- **VRMアーマチュアにBVHモーションを適用する準備**
    - 腕のスケーリング調整が成功したら、VRMモデル全体のボーンをBVHの各部位に合わせて調整する。
    - VRMとBVHのアーマチュア間でボーン名が異なる可能性があるため、各部位を対応付けるためのリストを作成し、同じ部位を持つボーンをマッピングする。
- **自動ウェイトを適用して頂点をVRMアーマチュアにバインド**
    - VRMモデルにBVHモーションを正確に反映させるために、VRMアーマチュアのボーンに自動ウェイトを適用し、頂点グループを調整する。
    - この工程はPythonコードを用いて自動化し、Blenderの`parent_set`メソッドを活用してウェイト設定を効率化する。
- **スクリプトを実行し、アニメーションを確認**
    - 必要な設定が整った段階でスクリプトを実行し、VRMアーマチュアがBVHの動きに合わせて正確に追従するか確認する。
    - Blenderのアニメーション再生機能を使って、VRMモデルがBVHのモーションに沿って正しくアニメーションするかテストする。
      
