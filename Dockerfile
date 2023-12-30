# Pythonのイメージを使用
FROM python:3.12

# 作業ディレクトリを設定
WORKDIR /usr/src/app

# 必要なパッケージをインストール
COPY requirements.txt ./
RUN pip install --upgrade pip \
    pip install --no-cache-dir -r requirements.txt

# アプリケーションのソースをコピー
COPY . .

# コンテナがリッスンするポート番号を指定（必要に応じて）
EXPOSE 8000
