# 医療画像認識（教材）

医用画像（X線、CT、MRI、超音波など）の原理とDICOM規格から始めて、画像解析、機械学習、深層学習によるセグメンテーションまでを演習形式で学ぶ講座の教材です。
コードの多くはAI（GitHub Copilot、Colabでは組み込みのGemini）に書かせます。受講者は、AIに何を頼むか、出てきた結果が正しいか、その結果が医学的に何を意味するかを判断します。

教材は、授業の進行に合わせて範囲ごとに追加します。まだ追加されていない範囲のリンクは開けません。

## 授業計画

| 回 | 範囲 | 内容 | 教材 |
|---|---|---|---|
| 1（9/28） | ガイダンス | 講座の進め方、環境構築 | [setup/](setup/)、[0](units/0_setup/0_setup_check.ipynb) |
| 2 | 範囲1 医用画像の種類と原理 | 医用画像の種類とX線・CTの原理 | [1-1](units/1_modalities/1-1_xray_ct.ipynb) |
| 3 | | MRIの原理と画像の周波数 | [1-2](units/1_modalities/1-2_mri.ipynb) |
| 補足 | | 画質改善技術（再構成フィルタ、逐次近似再構成、ノイズ除去） | [1-3](units/1_modalities/1-3_image_quality.ipynb) |
| 4 | 範囲2 DICOM規格とDICOMビューア | DICOM規格 | [2-1](units/2_dicom/2-1_dicom_standard.ipynb) |
| 5 | | DICOMビューアとウィンドウ処理 | [2-2手順書](units/2_dicom/2-2_slicer_guide.md)、[2-2](units/2_dicom/2-2_window_level.ipynb) |
| 6 | 範囲3 画像解析と機械学習 | 手動セグメンテーションとヒストグラム解析 | [3-1手順書](units/3_analysis/3-1_slicer_segmentation_guide.md)、[3-1](units/3_analysis/3-1_manual_segmentation.ipynb) |
| 7 | | テクスチャ解析 | [3-2](units/3_analysis/3-2_texture.ipynb) |
| 8 | | 機械学習による分類と評価 | [3-3](units/3_analysis/3-3_machine_learning.ipynb) |
| 9 | 範囲4 DICOMビューアの自作 | DICOMシリーズの読み込みと表示 | [4-1](units/4_dicom_viewer/4-1_load_series.ipynb) |
| 10 | | Streamlitでビューアを作る | [4-2](units/4_dicom_viewer/4-2_streamlit_viewer.md) |
| 11 | 範囲5 CNN（Colab） | ニューラルネットワークとCNNの基礎 | [5-1](units/5_cnn/5-1_cnn_basics.ipynb) |
| 12 | | CNNによる画像分類 | [5-2](units/5_cnn/5-2_cnn_classification.ipynb) |
| 13 | 範囲6 U-Net（Colab） | U-Netの構造と学習 | [6-1](units/6_unet/6-1_unet_scratch.ipynb) |
| 14 | | 学習済みエンコーダを使ったU-Net | [6-2](units/6_unet/6-2_unet_pretrained.ipynb) |
| 15 | 予備日 | 遅れた範囲の補習、ビューアの仕上げなど | — |

## 準備（第1回）

1. [GitHubアカウントの作成と学生特典の申請](setup/01_github.md)
2. [Windowsに演習環境を入れる](setup/02_install_windows.md)（Macの場合は[こちら](setup/02_install_mac.md)）
3. [AIの使い方とルール](setup/03_ai_assistant.md)

## 毎回の進め方

### 範囲1〜4（VS Code）

1. リポジトリのフォルダで `git pull` と `uv sync` を実行し、教材と環境を最新にする
2. ノートブックを開き、カーネルに `.venv` を選ぶ
3. 「動かしてみる」のセルを上から実行する
4. AIに頼む前に、ここまでの状態をコミットする
5. AIに頼み、差分を見て採用するかどうかを決める
6. チェックリストで結果を確かめ、振り返りを書いてコミットする

### 範囲5〜6（Colab）

1. ノートブック冒頭の「Open in Colab」ボタンから開く
2. ランタイムのタイプをGPUに変更する
3. 「動かしてみる」のセルを上から実行する
4. Geminiに頼み、変更されたコードを読んでから実行する
5. チェックリストで結果を確かめ、振り返りを書いて「ドライブにコピーを保存」する

提出のしかたは授業で指示します。

## AIを使うときのルール

- 患者の情報を含む画像やデータを、AIに入力したりGitHubに置いたりしない
- AIが書いたコードは、各回のチェックリストで確かめてから採用する
- 振り返りに、使ったプロンプトと、AIの答えのうち直した点・採用しなかった点を書く

詳しくは [setup/03_ai_assistant.md](setup/03_ai_assistant.md) を読んでください。

## 使用しているデータ

データは、各ノートブックを実行したときに `data/` へ自動でダウンロードされます。一覧と出典は [data/README.md](data/README.md) にあります。

## サポートの範囲

授業期間中は、授業で使う環境（VS Code、Git、uv、Copilot、3D Slicer）の導入と教材の実行を支援します。
授業が終わっても環境と教材はそのまま使えますが、その後の更新や不具合への対応は各自で行ってください。
