# 数字を、判断の味方に。
## 『FACTFULNESS』を学ぶ日本語の自習教材
ニュースに驚いたとき、仕事の数字で迷ったとき。結論の前に、分母と比較対象を確かめる練習をしましょう。

統計の予備知識がない社会人向けの、独自に作成した非公式教材です。本書の代替や公式な要約ではありません。

## 学習目標
- 思い込みに気づき、10の本能を自分の言葉で説明する。
- ニュース・広告・グラフの比較対象、割合、変化、不確実性を確認する。
- 判断の根拠と限界を記録し、仕事や日常へ適用する。

## 推奨学習順
まず「はじめに」と基礎を読み、10の本能を順に学び、総合演習と1週間の実践へ進んでください。各章20〜30分を目安に、解答を見る前に自分の判断を書きます。

- [はじめに](00_introduction.md)
- [データを見るための基礎](01_data_basics.md)
- [分断本能](02_gap_instinct.md)
- [ネガティブ本能](03_negativity_instinct.md)
- [直線本能](04_straight_line_instinct.md)
- [恐怖本能](05_fear_instinct.md)
- [過大視本能](06_size_instinct.md)
- [パターン化本能](07_generalization_instinct.md)
- [宿命本能](08_destiny_instinct.md)
- [単純化本能](09_single_perspective_instinct.md)
- [犯人捜し本能](10_blame_instinct.md)
- [焦り本能](11_urgency_instinct.md)
- [総合演習](12_integrated_exercises.md)
- [日常での実践と振り返り](13_practice_plan.md)
- [付録・解答解説](appendix.md)
- [参考文献・出典](references.md)

## 編集・サイト生成
Markdownが教材の原本です。Python 3で `python -m pip install -r requirements.txt`、続いて `python tools/build.py` を実行すると `docs/` にHTMLが生成されます。`python -m http.server 8000 --directory docs` で確認できます。

GitHub PagesはSettings → PagesでSourceを「Deploy from a branch」、ブランチをmain、フォルダを/docsに設定すると公開できます。ビルド検証用のGitHub Actionsも同梱しています。
