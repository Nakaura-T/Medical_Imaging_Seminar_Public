# データ

このフォルダの中身はGitで管理しません（この `README.md` を除く）。各回のノートブックが、必要なデータをここに自動でダウンロードします。

## 講座で使うデータ

| データ | 画像 | 使う回 | 保存先 | ライセンス |
|---|---|---|---|---|
| scikit-image付属の数値ファントム（Shepp-Logan） | 数値ファントム | 1-1 | （ライブラリに付属） | — |
| TCIA Pseudo-PHI-DICOM-Data | CT、MRI、X線（DICOM） | 1-2、2-1、2-2、3-1、4-1、4-2 | `data/pseudo_phi/` | CC BY 4.0 |
| pydicom付属のサンプル（JPEG 2000で圧縮された超音波画像） | 超音波（DICOM） | 4-1、4-2 | （ライブラリに付属） | pydicomの配布条件に従う |
| MedMNIST BreastMNIST | 乳腺超音波（悪性、正常・良性） | 3-2、3-3、5-1、5-2 | `data/medmnist/` | CC BY 4.0 |
| MedSegBench Covid19RadioMSBench | 胸部X線と肺野のマスク | 6-1、6-2 | `data/medsegbench/` | 学術・非営利の利用に限る |
| MedSegBench CovidQUExMSBench | 胸部X線と肺炎による陰影のマスク | 6-2（発展課題） | `data/medsegbench/` | CC BY-SA 4.0 |
| MedSegBench BusiMSBench | 乳腺超音波と腫瘤のマスク | 6-2（発展課題） | `data/medsegbench/` | CC BY-NC 4.0 |

ノートブックが作るファイルも、このフォルダに保存されます。

| ファイル・フォルダ | 作る回 | 使う回 |
|---|---|---|
| `masks/` | 3-1（3D Slicerで作ったマスクを置く） | 3-1 |
| `breastmnist_features.csv` | 3-2 | 3-3 |
| `ml_test_result.json` | 3-3 | 5-2 |
| `viewer_sample/` | 4-1 | 4-1、4-2 |
| `unet_scratch_result.json` | 6-1 | 6-2 |

## 出典

- **Pseudo-PHI-DICOM-Data**：Rutherford M, et al. A DICOM dataset for evaluation of medical image de-identification. *Scientific Data* 8, 183 (2021). https://doi.org/10.1038/s41597-021-00967-y ／ データセット：https://doi.org/10.7937/s17z-r072 。NCI Imaging Data Commons から取得します。**患者情報はすべて、匿名化の評価のために作られた架空のものです。**
- **MedMNIST**：Yang J, et al. MedMNIST v2 - A large-scale lightweight benchmark for 2D and 3D biomedical image classification. *Scientific Data* 10, 41 (2023). BreastMNISTの元データ：Al-Dhabyani W, et al. Dataset of breast ultrasound images. *Data in Brief* 28, 104863 (2020).
- **MedSegBench**：MedSegBench: A comprehensive benchmark for medical image segmentation in diverse data modalities. *Scientific Data* (2024). https://doi.org/10.1038/s41597-024-04159-2 。元データの出典は MedSegBench のプロジェクトページ（https://medsegbench.github.io/）に従います。

## 実際の患者のデータについて

講座では上の公開データだけを使います。
自分や家族の画像など、手元にあるDICOMファイルにも患者情報が含まれます。GitHubやAIサービスには置かないでください。
