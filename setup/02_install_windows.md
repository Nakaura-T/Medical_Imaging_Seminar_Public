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
git config --global pull.rebase false
```

3行目は、教材を更新する（`git pull`）ときの動き方を決める設定です。自分のコミットと教員の更新を、そのまま合わせる動き方にします。

## 4. 教材を取得する

```powershell
mkdir C:\medimg
cd C:\medimg
git clone https://github.com/Nakaura-T/Medical_Imaging_Seminar_Public.git
cd Medical_Imaging_Seminar_Public
```

教材は授業の進行に合わせて追加されます。新しい教材を受け取るときは、このフォルダで次を実行します（VS Codeのソース管理の「…」メニューの「プル」でも同じです）。

```powershell
git pull
```

公開された教材のファイルは、後から教員が書き換えることはありません。自分で編集してコミットしたファイルがあっても、`git pull` で競合は起きません。

## 5. Pythonの環境を作る

```powershell
uv sync
```

Python本体と、講座で使うライブラリがまとめて入ります。Pythonを別にインストールする必要はありません。初回は数分かかります。教材を更新したときに、ライブラリが追加されていることもあるので、`git pull` のあとにも実行します。

## 6. VS Codeで開く

```powershell
code .
```

1. 右下に「推奨の拡張機能をインストールしますか」と表示されたら、インストールを選ぶ
2. 左下のアカウントのアイコンから、GitHubアカウントでサインインし、Copilotを使えるようにする
3. ノートブック（`.ipynb`）を開き、右上の「カーネルの選択」で `.venv` を選ぶ

## 7. 動作を確かめる

[units/0_setup/0_setup_check.ipynb](../units/0_setup/0_setup_check.ipynb) を開き、上から順に実行します。すべて「OK」と表示されれば完了です。

## 8. 3D Slicerを入れる（第5回までに）

範囲2と範囲3で使います。手順は [2-2の手順書](../units/2_dicom/2-2_slicer_guide.md) の「1. 3D Slicerを入れる」を見てください。

## 9. うまくいかないとき

### `winget` が見つからない

Microsoft Storeで「アプリ インストーラー」を検索し、更新してから、PowerShellを開き直します。

### `code`、`git`、`uv` が見つからない

PowerShellを閉じて開き直してから、もう一度実行します。それでも見つからない場合は、パソコンを再起動します。

### カーネルの一覧に `.venv` が表示されない

1. リポジトリのフォルダで `uv sync` を実行したか確かめる
2. VS Codeで `Ctrl+Shift+P` を押し、「Python: Select Interpreter」で `.venv` の中のPythonを選ぶ
3. `Ctrl+Shift+P` で「Developer: Reload Window」を実行し、もう一度カーネルを選ぶ

### `git pull` でエラーが出た

表示されたメッセージをコピーして、Copilotの解説役に意味を聞きます。それでも解決しない場合は、自分の作業を別のフォルダにコピーして残してから、教員に相談してください。

### Windowsのユーザー名に日本語が含まれている

多くの場合はそのまま使えます。インストールや `uv sync` でパスに関するエラーが出た場合は、教員に相談してください。

