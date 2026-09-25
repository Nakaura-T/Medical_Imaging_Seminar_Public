# Windowsに演習環境を入れる

## 1. 作業フォルダの場所を決める

作業フォルダは `C:\medimg` に作ります。

次の場所には置かないでください。

- **OneDriveの中**：「ドキュメント」や「デスクトップ」がOneDriveに同期されている場合も含みます。仮想環境の数千個のファイルが同期されて動作が遅くなったり、Gitの管理ファイルが壊れたりすることがあります。
- **日本語（全角文字）を含むパス**：一部のツールがパスを正しく扱えないことがあります。

## 2. ツールを入れる

PowerShellを開き、次のコマンドを1行ずつ実行します。

```powershell
winget install --id Microsoft.VisualStudioCode -e
winget install --id Git.Git -e
winget install --id astral-sh.uv -e
```

入れ終わったらPowerShellをいったん閉じて開き直し、次のコマンドで版数が表示されることを確かめます。

```powershell
code --version
git --version
uv --version
```

## 3. Gitの初期設定をする

```powershell
git config --global user.name "GitHubのユーザー名"
git config --global user.email "GitHubに登録したメールアドレス"
```

## 4. 教材を取得する

TODO: 配布方法が決まったら書く

## 5. Pythonの環境を作る

```powershell
cd C:\medimg\<リポジトリ名>
uv sync
```

Python本体もuvが自動で入れるので、別にインストールする必要はありません。

## 6. VS Codeで開く

```powershell
code .
```

1. 右下に「推奨の拡張機能をインストールしますか」と表示されたら、インストールを選ぶ
2. GitHubアカウントでCopilotにサインインする
3. ノートブックを開き、右上の「カーネルの選択」で `.venv` を選ぶ

TODO: 各手順の画面の画像

## 7. 動作を確かめる

[units/0_setup/0_setup_check.ipynb](../units/0_setup/0_setup_check.ipynb) を開き、上から順に実行します。すべて「OK」と表示されれば完了です。

## 8. 3D Slicerを入れる（第5回までに）

範囲2と範囲3で使います。ダウンロードページ（https://download.slicer.org/）からWindows版を入れます。

TODO: インストール手順と画面の画像

## 9. うまくいかないとき

### `winget` が見つからない

TODO

### `code`、`git`、`uv` が見つからない

PowerShellを開き直してから、もう一度実行してください。それでも見つからない場合は TODO

### カーネルの一覧に `.venv` が表示されない

TODO

### Windowsのユーザー名に日本語が含まれている

TODO
