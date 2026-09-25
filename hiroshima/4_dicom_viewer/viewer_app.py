"""DICOMビューア（第10回で作る）

実行方法（リポジトリのフォルダで）:
    uv run streamlit run units/4_dicom_viewer/viewer_app.py
"""
import streamlit as st

st.title("DICOM Viewer")

folder = st.text_input("DICOMフォルダのパス")

if folder:
    st.write(f"選択したフォルダ: {folder}")
    # TODO（基本課題1〜2）: 4-1で作った関数でシリーズを読み込み、表示する
    # TODO（基本課題3）: スライダーでスライスを選べるようにする
    # TODO（基本課題4）: ウィンドウ幅・レベルを調整できるようにする
    # TODO（基本課題5）: シリーズを選べるようにする
