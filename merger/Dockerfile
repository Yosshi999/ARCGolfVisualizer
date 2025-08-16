FROM python:3.12-slim

# unzip ツール追加
RUN apt-get update && apt-get install -y --no-install-recommends unzip \
    && rm -rf /var/lib/apt/lists/*

# 非rootユーザー作成
RUN useradd -m sandboxuser

# 作業ディレクトリ
WORKDIR /app

# merge.py と entrypoint をコピー
COPY merge.py /app/merge.py
COPY entrypoint.sh /app/entrypoint.sh

# 所有者変更
RUN chown -R sandboxuser:sandboxuser /app

# 実行ユーザー切り替え
USER sandboxuser

# エントリーポイント実行
CMD ["bash", "/app/entrypoint.sh"]
