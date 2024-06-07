#!/bin/sh

# データベースが起動するのを待つ
until nc -z db 5432; do
    echo "Waiting for the database to start..."
    sleep 1
done

# マイグレーションを実行
python manage.py migrate

# サーバーを起動
exec "$@"
