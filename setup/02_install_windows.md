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

Gitとuvが何をする道具か、この設定が何のためにあるかは、[第1回の解説](../units/0_setup/0_setup_guide.md)の3章にあります。3行目は、GitHubから自分のコミットを取り込む（プル）ときの動き方を決める設定です。別のパソコンで作業したコミットを取り込むときに、そのまま合わせる動き方にします。

## 4. 講座のフォルダを用意する

1. `C:\medimg` フォルダを作る
2. 授業のページから第1回の配布ファイル（zip）をダウンロードする
3. zipを右クリックして「すべて展開」を選び、展開先に `C:\medimg` を指定する
4. `C:\medimg\medical_imaging` フォルダができたことを確かめる

このフォルダが、この講座の作業をすべて入れる**講座のフォルダ**です。第2回以降は、授業のページから配布される教材を、このフォルダの `units` に足していきます（[第1回の解説](../units/0_setup/0_setup_guide.md)の9章）。

## 5. Pythonの環境を作る

```powershell
cd C:\medimg\medical_imaging
uv sync
```

Python本体と、講座で使うライブラリがまとめて入ります。Pythonを別にインストールする必要はありません。初回は数分かかります。新しいライブラリを使う回では、配布ファイルに新しい `pyproject.toml` と `uv.lock` が入っているので、上書きしてからもう一度実行します。

## 6. VS Codeで開く

```powershell
code .
```

1. 右下に「推奨の拡張機能をインストールしますか」と表示されたら、インストールを選ぶ
2. 左下のアカウントのアイコンから、GitHubアカウントでサインインし、Copilotを使えるようにする
3. ノートブック（`.ipynb`）を開き、右上の「カーネルの選択」で `.venv` を選ぶ

## 7. 自分のGitHubにリポジトリを作る

VS Codeのソース管理（`Ctrl+Shift+G`）で「GitHub に公開（Publish to GitHub）」を押し、**非公開（private）**のリポジトリを作ります。詳しい手順は [第1回の解説](../units/0_setup/0_setup_guide.md) の6章にあります。

## 8. 動作を確かめる

[units/0_setup/0_setup_check.ipynb](../units/0_setup/0_setup_check.ipynb) を開き、上から順に実行します。すべて「OK」と表示されれば完了です。

## 9. 3D Slicerを入れる（第5回までに）

範囲2と範囲3で使います。手順は [2-2の手順書](../units/2_dicom/2-2_slicer_guide.md) の「1. 3D Slicerを入れる」を見てください。

## 10. うまくいかないとき

### `winget` が見つからない

Microsoft Storeで「アプリ インストーラー」を検索し、更新してから、PowerShellを開き直します。

### `code`、`git`、`uv` が見つからない

PowerShellを閉じて開き直してから、もう一度実行します。それでも見つからない場合は、パソコンを再起動します。

### カーネルの一覧に `.venv` が表示されない

1. リポジトリのフォルダで `uv sync` を実行したか確かめる
2. VS Codeで `Ctrl+Shift+P` を押し、「Python: Select Interpreter」で `.venv` の中のPythonを選ぶ
3. `Ctrl+Shift+P` で「Developer: Reload Window」を実行し、もう一度カーネルを選ぶ

### 「変更の同期」でエラーが出た

表示されたメッセージをコピーして、Copilotの解説役に意味を聞きます。それでも解決しない場合は、講座のフォルダを別の場所にコピーして残してから、教員に相談してください。

### Windowsのユーザー名に日本語が含まれている

多くの場合はそのまま使えます。インストールや `uv sync` でパスに関するエラーが出た場合は、教員に相談してください。

