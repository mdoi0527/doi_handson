<p align="center">
  <a href="https://symmetrical-adventure-qkqey2e.pages.github.io/">
    <img alt="Detection as Code rules" src="./src/images/icon.png" width="60" />
  </a>
</p>
<h1 align="center">
  Detection as Codeルール集
</h1>

## 🚀 このリポジトリについて

このリポジトリは、Sigmaのルール集を管理し、それらのルールを共有するためのウェブサイトを構築するためのものです。

## 🧐 このリポジトリの構成

このリポジトリは、Gatsbyという静的サイト構築ツールを使用して構築されています。Gatsbyによって構築されたウェブサイトは、GitHub Pagesを使用してホスティングされています。

主なディレクトリ構成は以下の通りです。

```sh
.
├── /.devcontainer/devcontainer.json     # GitHub Codespacesの設定ファイル
├── /.github/workflows/deploy.yml        # デプロイ用のGitHub Actionsの設定ファイル
├── /src/                                # ウェブサイトのソースコード
│   ├── /images/                         # 画像ファイル
│   └── /pages/                          # ウェブサイトのページ
└── /rules/sigma/                        # Sigmaルールファイル置き場
```

## 📂 ルールの追加の仕方

1. `/rules/sigma/`ディレクトリに、Sigmaルールファイルを追加します。
2. 追加したファイルを本リポジトリにプッシュします。
3. GitHub Actions（ワークフローの定義は[こちら](./.github/workflows/deploy.yml)）によって、ルールファイルが自動的にウェブサイトに反映されます（約2分程度かかります）。
4. GitHub Actionsの結果画面にWebサイトのURLが表示されるので、そちらにアクセスして追加したルールを確認します。
