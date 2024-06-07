# ベースイメージとしてPythonを使用
FROM --platform=linux/amd64 python:3.10-slim

# 作業ディレクトリを設定
WORKDIR /app

# 必要なパッケージをインストール
RUN pip install --upgrade pip
RUN apt-get update \
    && apt-get install -y netcat-openbsd

# 依存関係ファイルをコピー
COPY requirements.txt .

# 依存関係をインストール
RUN pip install -r requirements.txt

# アプリケーションのコードをコピー
COPY . .

# スタートアップコマンドを定義
CMD ["sh", "entrypoint.sh"]
