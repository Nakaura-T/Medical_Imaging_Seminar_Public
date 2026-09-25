---
title: "Session05: Session1-4 まとめ - 自然科学系論文を書くときの注意点"
author: "DSゼミナール3"
date: "2026年"
---

# Session05: Session1-4 まとめ

## 目的

この資料は、Session1-4 を休んだ人、または復習したい人のためのまとめです。

Session1-4 では、自然科学系論文を書くために必要な基本を扱いました。

- Session1: 研究とは何か、IMRAD、論文を書く順番
- Session2: Materials and Methods、Results、表・図・単位・有効数字
- Session3: Introduction、引用文献、Zotero、Pandoc
- Session4: Discussion、結果の解釈、限界、結論

ここでは細かい操作方法ではなく、**自然科学系論文を書くときに必ず注意すべき考え方**に絞って整理します。

---

# 1. 論文は「感想」ではなく「根拠のある主張」である

自然科学系論文では、自分の意見を自由に書くのではなく、データ・解析・先行研究に基づいて主張します。

重要なのは、次の3つを明確に分けることです。

| 種類 | 内容 | 根拠 |
|---|---|---|
| 事実 | 実際に得られた結果 | 自分のデータ |
| 解釈 | 結果から考えられる意味 | Results と先行研究 |
| 背景知識 | すでに知られていること | 引用文献 |

悪い例:

```markdown
LLM はとても有用であり、今後すべての診断に使われるべきである。
```

この文は、主張が強すぎるうえに、どの結果に基づくのかが不明です。

よい例:

```markdown
本研究では、GPT-4 が評価対象モデルの中で最も高い正答率を示した。この結果は、LLM が医学画像関連質問の回答支援に利用できる可能性を示している。
```

この文では、まず結果を示し、その範囲内で控えめに解釈しています。

---

# 2. IMRAD の役割を混ぜない

自然科学系論文の基本構造は IMRAD です。

| セクション | 役割 | 書くこと | 書かないこと |
|---|---|---|---|
| Introduction | なぜ研究するのか | 背景、先行研究、未解決の問題、目的 | 詳しい結果、深い考察 |
| Materials and Methods | どう調べたのか | 対象、データ、方法、解析、倫理 | 結果の解釈 |
| Results | 何が分かったのか | 数値、表、図、観察された結果 | 理由、意味づけ、感想 |
| Discussion | それは何を意味するのか | 主要結果、解釈、先行研究との関係、限界、結論 | Results にない新しい解析 |

IMRAD で最も多い失敗は、セクションの役割が混ざることです。

- Introduction に Results の数値を書きすぎる
- Results で「なぜそうなったか」を語りすぎる
- Discussion で新しい結果を追加する
- Methods に研究の意義を書きすぎる

各セクションを書くときは、常に「この文はこのセクションに置くべき文か」を確認します。

---

# 3. 書く順番は IMRAD の順番でなくてよい

論文は Introduction から読むことが多いですが、書く順番は必ずしも Introduction からである必要はありません。

初学者には、次の順番がおすすめです。

1. Results
2. Materials and Methods
3. Introduction
4. Discussion
5. Abstract
6. Title

理由は、Results が決まらないと、論文全体の主張が決まらないからです。

Results が決まると、次のことが見えてきます。

- 何を Methods に書く必要があるか
- Introduction でどの gap を示すべきか
- Discussion で何を解釈すべきか
- Abstract で何を強調すべきか

論文は、最初からきれいな英語を書く作業ではありません。まず、研究の骨格を正しく並べる作業です。

---

# 4. Introduction は「背景 -> 先行研究 -> gap -> 目的」で書く

Introduction は、読者を本研究の目的まで案内するセクションです。

基本構造は次の4段階です。

| 段落 | 役割 | 書く内容 |
|---|---|---|
| Paragraph 1 | Background | 研究テーマがなぜ重要か |
| Paragraph 2 | Previous studies | 先行研究で何が分かっているか |
| Paragraph 3 | Knowledge gap | まだ何が十分に分かっていないか |
| Paragraph 4 | Aim | 本研究では何を明らかにするか |

Introduction で注意すること:

- いきなり自分の研究結果を書かない
- 背景を広げすぎない
- 先行研究には citation を付ける
- gap を曖昧にしない
- 最後は本研究の目的で終える

悪い例:

```markdown
LLM は最近とても人気がある。本研究では Gemini が高い精度を示した。
```

よい流れ:

```markdown
LLM は医学分野で注目されている。
先行研究では、医学系質問への回答性能が評価されてきた。
しかし、モデル間や専門分野間の性能差は十分に整理されていない。
本研究では、複数の LLM の医学画像分析質問への正答率を比較した。
```

---

# 5. Materials and Methods は再現できるように書く

Materials and Methods の目的は、読者が「この研究がどのように行われたか」を理解できるようにすることです。

書くべき内容:

- 対象データ
- 除外基準または選択基準
- 評価対象モデル
- 質問・データの分類方法
- 解析手順
- 評価指標
- 統計解析
- 倫理的配慮

注意点:

- 「何となく集めた」ではなく、データの由来を明確にする
- 使用したモデル名やバージョンをできるだけ具体的に書く
- accuracy、平均、標準偏差などの指標の意味を明確にする
- 再現できない作業は、論文では弱点になる
- Results に出てくる表や図が、Methods の説明と対応しているか確認する

Methods は地味ですが、論文の信頼性を支える部分です。

---

# 6. Results は「何が起きたか」だけを書く

Results は、データから得られた結果を示すセクションです。

Results で書くこと:

- 全体のデータ数
- 分類ごとの件数
- 主要な評価指標
- モデル間の比較
- 図表で示した結果の説明

Results で書かないこと:

- なぜその結果になったか
- その結果が臨床的に何を意味するか
- 先行研究との詳しい比較
- 自分の感想

例:

```markdown
GPT-4 achieved the highest overall accuracy among the evaluated models.
```

これは Results に書けます。

```markdown
This result suggests that GPT-4 has superior reasoning ability and may be useful in clinical practice.
```

これは Discussion に書く内容です。

---

# 7. 表・図・数値は本文と対応させる

自然科学系論文では、表と図は「飾り」ではありません。本文の主張を支える証拠です。

注意点:

- 本文中で Table 1、Figure 1 のように参照する
- 表・図のタイトルと legend を書く
- 表・図に出した数値と本文の数値を一致させる
- 単位を統一する
- 小数点以下の桁数をそろえる
- 過度に細かい桁を避ける

例:

```markdown
The number of questions in each subspecialty is shown in Table 1.
```

```markdown
Overall model accuracy is summarized in Table 2.
```

```markdown
The distribution of model performance is shown in Figure 1.
```

表や図を入れたら、本文でも必ずその意味を説明します。

---

# 8. Discussion は Results の意味づけをする

Discussion は、Results で示した結果に対して「それは何を意味するのか」を説明するセクションです。

基本構造:

| 段落 | 役割 | 書く内容 |
|---|---|---|
| Paragraph 1 | Principal findings | 主要結果を簡潔にまとめる |
| Paragraph 2 | Interpretation | なぜその結果になったかを説明する |
| Paragraph 3 | Comparison and implications | 先行研究との関係、意義を書く |
| Paragraph 4 | Limitations | 研究の限界を書く |
| Paragraph 5 | Conclusion | 結果から言える範囲でまとめる |

Discussion で注意すること:

- Results の単なる繰り返しにしない
- Results にない新しい数値や解析を出さない
- 良い結果だけでなく、限界も書く
- 先行研究と比較する
- 結論を強く言いすぎない

よく使うトピック文:

```markdown
The main finding of this study was that ...
```

```markdown
One possible explanation for this finding is that ...
```

```markdown
Our findings are consistent with previous studies showing that ...
```

```markdown
This study has several limitations.
```

```markdown
In conclusion, ...
```

Discussion では、各段落の最初にトピック文を置くと、論理の流れが分かりやすくなります。

---

# 9. Citation は「他人の知識」に付ける

引用文献は、論文の信頼性を支える重要な要素です。

Citation が必要な文:

- 先行研究の結果を述べる文
- 既存のレビューやガイドラインの内容を述べる文
- 一般的な医学的・科学的知識を述べる文
- 自分の結果を先行研究と比較する文

Citation が不要な文:

- 本研究で得られた結果を述べる文
- 本研究の目的を述べる文
- 本研究の限界を述べる文
- Results から直接導かれる結論

Markdown / Pandoc では、次のように書きます。

```markdown
Previous studies have evaluated LLMs in radiology-related tasks [@citation_key].
```

複数の文献を引用する場合:

```markdown
Several studies have reported the potential of LLMs in medical applications [@citation_key_1; @citation_key_2].
```

`citation_key` は、必ず `references.bib` に存在するものを使います。

---

# 10. AI を使うときの注意

ChatGPT や Gemini は、論文作成の補助として有用です。

使ってよいこと:

- 日本語メモの整理
- 英語表現の改善
- 段落構成の確認
- Results と Discussion の混在チェック
- 表現を控えめにする提案

注意すべきこと:

- 存在しない論文を作ることがある
- DOI、著者名、雑誌名を間違えることがある
- Results にない数値を追加することがある
- Conclusion を強く言いすぎることがある
- 臨床応用を過度に断定することがある

AI に頼むときは、次のように制限を明確にします。

```text
以下の草稿を英語論文らしく整えてください。
ただし、Results にない数値や新しい解析は追加しないでください。
存在しない文献や DOI は作らないでください。
Conclusion は結果から言える範囲にしてください。
```

AI は下書きを整える道具であり、研究内容の正しさを保証するものではありません。

---

# 11. Abstract は最後に書く

Abstract は論文全体の要約です。

多くの自然科学系論文では、次の構造で書きます。

| 項目 | 書く内容 |
|---|---|
| Objective | 研究目的 |
| Materials and methods | 対象、方法、評価指標 |
| Results | 主要な数値結果 |
| Conclusion | 結果から言える結論 |

Abstract は短いですが、論文全体の内容と矛盾してはいけません。

注意点:

- 本文にない結果を書かない
- Results の主要数値を正確に書く
- Conclusion を強くしすぎない
- 略語は必要に応じて初出で説明する
- 最後に本文の Results、Discussion と照合する

Abstract は、Introduction より先に読まれることが多いですが、書くのは本文が固まった後が安全です。

---

# 12. 最終チェックリスト

論文を提出する前に、次を確認してください。

## 全体

- 研究目的が明確である
- IMRAD の役割が混ざっていない
- Results と Discussion が区別されている
- 主張がデータの範囲を超えていない
- Abstract と本文の内容が一致している

## Introduction

- 背景、先行研究、gap、目的の流れになっている
- 先行研究には citation が入っている
- Results の詳しい数値を書いていない

## Materials and Methods

- データの由来が分かる
- 対象、方法、評価指標、解析手順が分かる
- 他人が研究手順を追える程度に具体的である

## Results

- 表・図と本文が対応している
- 数値、単位、小数点以下の桁数がそろっている
- 解釈や感想を書きすぎていない

## Discussion

- 冒頭で主要結果をまとめている
- 結果の意味を説明している
- 先行研究との関係を書いている
- 限界を具体的に書いている
- Conclusion が結果から言える範囲に収まっている

## Citation

- 他人の知識や先行研究には citation がある
- `[@citation_key]` が `references.bib` に存在する
- AI が作った文献をそのまま使っていない


# まとめ

自然科学系論文を書くときに最も重要なのは、きれいな英語を書くことではありません。

まず、次の5点を守ることが重要です。

1. 研究目的を明確にする
2. IMRAD の役割を混ぜない
3. Results では結果だけを書く
4. Discussion では結果の意味を、限界を含めて説明する
5. 他人の知識には citation を付ける

英語表現は後から整えることができます。しかし、研究の論理構造が崩れていると、どれだけ英語が自然でも論文としては弱くなります。

論文作成では、**データから言えることを、根拠と限界を示しながら、読者に分かる順番で説明する**ことを意識してください。

---

# 補足: Markdown / Zotero / Pandoc の基本

ここからは本文とは別に、論文原稿を Markdown で作成し、Zotero の文献情報を使って Word ファイルに変換するための最小限の手順をまとめます。

## 1. Markdown 書式

Markdown は、プレーンテキストで見出し、箇条書き、表、画像などを書くための形式です。

### 見出し

```markdown
# Title
## Introduction
### Background
```

`#` の数が少ないほど大きな見出しになります。

### 箇条書き

```markdown
- item 1
- item 2
- item 3
```

番号付きリストは次のように書きます。

```markdown
1. First
2. Second
3. Third
```

### 強調

```markdown
**重要な語句**
```

### 表

```markdown
| Model | Accuracy |
|---|---|
| GPT-4 | 65.7% |
| Gemini-Pro | 62.3% |
```

### 画像

```markdown
![Figure 1. モデルの精度分布](./save_figures/Figure_1.png)
```

画像ファイルの場所と Markdown に書いたパスが一致していないと、Word 変換時に画像が表示されません。

## 2. Zotero で BibTeX 書類を出力する

Zotero は文献管理ソフトです。Pandoc で引用文献リストを作るには、Zotero から BibTeX 形式で文献情報を書き出します。

基本手順:

1. Zotero に使用する論文を登録する
2. 使用する文献を選択する
3. 右クリックして `Export Items...` を選ぶ
4. 形式として `BibTeX` を選ぶ
5. `references.bib` という名前で保存する
6. `paper.md` と同じフォルダに `references.bib` を置く

この授業では、原稿ファイルを `paper.md`、文献ファイルを `references.bib` として扱います。

## 3. Markdown での引用

Markdown / Pandoc では、本文中の引用を次の形式で書きます。

```markdown
Previous studies have evaluated LLMs in radiology-related tasks [@citation_key].
```

複数の文献をまとめて引用する場合は、セミコロンで区切ります。

```markdown
Several studies have reported the potential of LLMs in medical applications [@citation_key_1; @citation_key_2].
```

著者名を文中に出す場合も、文末に citation key を置きます。

```markdown
Bhayana et al. reported that ChatGPT achieved moderate accuracy on radiology board-style questions [@citation_key].
```

注意点:

- `citation_key` は `references.bib` の中に存在するものを使う
- 存在しない citation key を書くと、変換時に引用が正しく表示されない
- Introduction や Discussion で先行研究を書く文には citation を入れる
- 自分の Results を述べる文には通常 citation は不要

## 4. Pandoc で Word に変換する

Pandoc は、Markdown ファイルを Word などの形式に変換するツールです。

引用文献を使わない単純な変換:

```bash
pandoc paper.md -o paper.docx
```

引用文献を使って変換:

```bash
pandoc paper.md --citeproc --bibliography=references.bib -o paper.docx
```

授業用の Word スタイルを反映する場合:

```bash
pandoc paper.md --citeproc --bibliography=references.bib --reference-doc=Reference.docx -o paper.docx
```

確認すること:

- `paper.md` と `references.bib` が同じフォルダにある
- `--bibliography=references.bib` のファイル名が正しい
- `[@citation_key]` が `references.bib` に存在する
- 画像ファイルのパスが正しい
- 変換後の `paper.docx` を開き、引用、参考文献、表、図が正しく表示されている

Pandoc 変換は最後の仕上げではなく、途中で何度も実行して表示を確認すると修正しやすくなります。

## 5. CSL ファイルを参照する方法

CSL ファイルは、引用文献リストや本文中引用の表示スタイルを指定するためのファイルです。

たとえば、医学系でよく使われる Vancouver 形式にしたい場合は、`vancouver.csl` のような CSL ファイルを `paper.md` と同じフォルダに置きます。

Pandoc で変換するときに、`--csl` オプションで CSL ファイルを指定します。

```bash
pandoc paper.md --citeproc --bibliography=references.bib --csl=vancouver.csl --reference-doc=Reference.docx -o paper.docx
```

YAML header に書く場合は、次のように指定できます。

```markdown
---
title: "Paper title"
bibliography: references.bib
csl: vancouver.csl
---
```

注意点:

- `vancouver.csl` などの CSL ファイル名を正確に書く
- `paper.md`、`references.bib`、CSL ファイルを同じフォルダに置くと分かりやすい
- CSL を指定しても、`[@citation_key]` が `references.bib` に存在しない場合は正しく引用されない
- 変換後の Word ファイルで、本文中引用と参考文献リストの形式を必ず確認する
