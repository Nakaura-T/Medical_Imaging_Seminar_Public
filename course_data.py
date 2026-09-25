"""講座で使う公開データを data/ にダウンロードする。

ノートブックからは次のように使う（VS Code ではリポジトリのフォルダが作業フォルダになる）。

    from course_data import fetch
    ct_dir = fetch("ct")

DICOM は TCIA の Pseudo-PHI-DICOM-Data（CC BY 4.0）を、NCI Imaging Data Commons から取得する。
このデータの患者情報は、評価用に作られた架空のものである。
出典: Rutherford M, et al. A DICOM dataset for evaluation of medical image de-identification.
      Scientific Data 8, 183 (2021). https://doi.org/10.1038/s41597-021-00967-y
"""
from pathlib import Path

DATA_DIR = Path(__file__).resolve().parent / "data"
DICOM_DIR = DATA_DIR / "pseudo_phi"

# 名前 → (SeriesInstanceUID, 説明)
# 「_phi」が付くものは架空の患者情報が入った版、付かないものは TCIA が匿名化した版。
SERIES = {
    "ct": ("1.3.6.1.4.1.14519.5.2.1.8700.9668.908280910349343034469562931670",
           "CT 腹部〜骨盤（CT urogram、152枚、匿名化版）"),
    "ct_phi": ("2.25.45367868844278747809947145409050295798",
               "CT 腹部〜骨盤（上と同じ画像、架空の患者情報入り）"),
    "mr": ("1.3.6.1.4.1.14519.5.2.1.8700.9668.742023011153680994651574212561",
           "MRI 上腹部〜骨盤 横断像（HASTE、26枚、匿名化版）"),
    "mr_t1": ("1.3.6.1.4.1.14519.5.2.1.8700.9668.742289597814431183824175493382",
              "MRI 上腹部 横断像（T1強調 FLASH、19枚、匿名化版。mr と同じ患者）"),
    "mr_sag": ("1.3.6.1.4.1.14519.5.2.1.8700.9668.304300462951325495163664256660",
               "MRI 上腹部〜骨盤 矢状断像（HASTE、26枚、匿名化版）"),
    "cr": ("1.3.6.1.4.1.14519.5.2.1.8700.9668.230087604482545573335222218707",
           "腹部X線（CR、1枚、匿名化版）"),
    "cr_phi": ("2.25.30562807935945476104184698489410272758",
               "腹部X線（上と同じ画像、架空の患者情報入り）"),
}


def fetch(name):
    """シリーズをダウンロードし、DICOM ファイルが入ったフォルダを返す。取得済みなら何もしない。"""
    uid, _ = SERIES[name]
    folder = DICOM_DIR / name
    if folder.exists() and any(folder.glob("*.dcm")):
        return folder
    import logging

    from idc_index import IDCClient  # 取得するときだけ読み込む（初回は索引のダウンロードに時間がかかる）

    logging.getLogger().setLevel(logging.WARNING)  # ダウンロード中の細かいログを出さない
    print(f"ダウンロード中: {name}（{SERIES[name][1]}）")
    folder.mkdir(parents=True, exist_ok=True)
    IDCClient().download_from_selection(seriesInstanceUID=uid, downloadDir=str(folder),
                                        dirTemplate=None, show_progress_bar=False)
    return folder


def list_series():
    """使えるシリーズの名前と説明を表示する。"""
    for name, (_, description) in SERIES.items():
        print(f"{name:8s} {description}")
