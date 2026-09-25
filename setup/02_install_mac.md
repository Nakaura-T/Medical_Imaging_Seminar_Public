# Macに演習環境を入れる

## 1. 作業フォルダの場所を決める

作業フォルダは `~/medimg` に作ります。iCloud Driveと同期している「書類」や「デスクトップ」には置かないでください。

## 2. ツールを入れる

- VS Code：https://code.visualstudio.com/ からダウンロード。起動後、コマンドパレットで「Shell Command: Install 'code' command in PATH」を実行する
- Git：ターミナルで `xcode-select --install` を実行する
- uv：ターミナルで次を実行する

```bash
curl -LsSf https://astral.sh/uv/install.sh | sh
```

## 3〜9. 以降の手順

[Windows版](02_install_windows.md)の3以降と同じです。3D SlicerはMac版を入れます。パスは `C:\medimg` を `~/medimg` に読み替えてください。
