# 日本語説明｜AI First FDE Skill

多くの企業が「AI First」を目指しています。ですが、最初の問いを間違えることがよくあります。

よくある問いは、こうです。

- どのモデルを使うべきか？
- チャットボットを作るべきか？
- 社内データをつなぐべきか？

もちろん大事な問いです。ですが、最初に見るべきものはそこではありません。

本当に見るべきなのは、会社の日々の仕事です。誰がその仕事をしているのか。データはどこにあるのか。誰が見てもよいのか。どの手順は人間の確認が必要なのか。AI が間違えた時、誰が止めるのか。

**AI First FDE Skill** は、AI agent を Forward Deployed Engineer（FDE）として動かすための実践的な Skill Suite です。

これは普通のプロンプトではありません。抽象的な AI コンサル資料でもありません。agent に、まず現場の業務を理解させてから、技術設計と導入計画を作らせるためのものです。

この Skill は、人員削減ではなく変革を前提にします。AI を、残業、手戻り、待ち時間、context switching、反復的な事務作業を減らすためのものとして位置付けます。同時に、経験豊富な社員を reviewer、trainer、approver、process owner、改善リーダーとして活かします。

## 何を解決するのか？

この Skill Suite は、企業の AI 導入を次のような実行可能な手順に分解します。

1. まず AI を入れるべき業務フローを見つける
2. データ、権限、利用者、責任者を整理する
3. organization architecture、approval route、relationship map、informal blocker map を作る
4. 分散ナレッジを LLM Wiki / source-of-truth structure に整理する
5. AI に任せられる作業と、人間の確認が必要な作業を分ける
6. 小さく安全な PoC とパイロットを設計する
7. 技術アーキテクチャと展開計画を作る
8. 社員がなぜ使わないのか、どこで止まるのかを観察する
9. 問題が起きた時に調査、修正、ロールバックできるようにする
10. レビュー、運用、公開用の安全な資料を作る

## なぜ東アジア企業向けなのか？

日本、台湾、香港、韓国、シンガポールなどの企業では、AI 導入は技術だけの問題ではありません。

次のような要素も重要です。

- 経営層との合意
- 部門間の調整
- リスク回避
- 面子と責任の問題
- ベテラン社員の習慣
- 表向きは賛成しても、実際には使われない抵抗
- AI が人員削減を意味するのではないかという不安

ここを無視すると、AI 導入はデモで止まり、日々の仕事には入りません。

## 何がより完全なのか？

この Skill は、隣接 capabilities を FDE workflow に接続できます。

- architecture diagram / relationship graph で組織構造と影響力を可視化する
- LLM Wiki / knowledge graph で分散した企業ナレッジを整理する
- Claude Code、Codex、Cursor、Hermes、OpenRouter、OpenCode / OpenCLI-style tools などの agent runtime を計画する
- security、evaluation、deployment、documentation skills を接続し、production handoff まで扱う

## 誰のためのものか？

- 企業 AI 導入コンサルタント
- システムインテグレーター
- AI プロダクトチーム
- 社内 AI 推進担当者
- AI 戦略を実際の業務フローに落とし込みたいチーム

## 一言でいうと

AI agent を「現場で動ける Forward Deployed Engineer（FDE）」に変える Skill Suite です。先に診断し、組織を可視化し、知識を整理し、次に設計し、小さく試し、安全に展開し、最後に定着を確認します。
