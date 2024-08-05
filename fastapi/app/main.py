# from fastapi import FastAPI
#
# app = FastAPI()
#
# @app.get('/api/data')
# async def get_data():
#     response = {
#         'message': 'Hello World!'
#     }
#     return response


# from fastapi import FastAPI
# from sqlalchemy import create_engine
# from sqlalchemy.ext.declarative import declarative_base
# from sqlalchemy.orm import sessionmaker
# from sqlalchemy.exc import SQLAlchemyError
# from sqlalchemy import text
# import os

# # MySQL データベースの接続情報
# # DATABASE_URL = "mysql+aiomysql://user:password@localhost/dbname"
# DATABASE_URL = os.getenv('DATABASE_URL', 'mysql+pymysql://user:password@db:3306/dbname')
#
# # SQLAlchemy セットアップ
# engine = create_engine(DATABASE_URL)
# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# Base = declarative_base()
#
# # FastAPI インスタンス作成
# app = FastAPI()
#
# # @app.get("/")
# # async def read_root():
# #     try:
# #         # データベースセッションを作成
# #         session = SessionLocal()
# #         # 接続テスト
# #         session.execute("SELECT 1")
# #         return {"status": "OK"}
# #     except SQLAlchemyError:
# #         return {"status": "NG"}
# #     finally:
# #         session.close()
#
#
# @app.get("/")
# async def read_root():
#     try:
#         session = SessionLocal()
#         result = session.execute(text("SELECT * FROM users LIMIT 1")) # 存在確認したいテーブル名を指定
#         if result.fetchone():
#             return {"status": "OK"}
#         else:
#             return {"status": "Table empty or not found"}  # テーブルが存在しないか空の場合
#     except SQLAlchemyError as e:
#         print(f"Error: {e}")
#         return {"status": "NG"}  # 接続エラーの場合
#     finally:
#         session.close()


from fastapi import FastAPI
from sqlalchemy import create_engine, text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.exc import SQLAlchemyError
import os

# MySQL データベースの接続情報
DATABASE_URL = os.getenv('DATABASE_URL', 'mysql+pymysql://user:password@db:3306/dbname')

# SQLAlchemy セットアップ
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

# FastAPI インスタンス作成
app = FastAPI()

@app.get("/")
async def read_root():
    try:
        # データベースセッションを作成
        session = SessionLocal()
        # 接続テスト
        session.execute(text("SELECT 1"))
        return {"status": "OK"}
    except SQLAlchemyError as e:
        # エラーメッセージを取得して返す
        error_message = str(e)
        return {"status": "NG", "error": error_message}
    finally:
        session.close()

# @app.on_event("startup")
# def startup():
#     # データベースのテーブル作成などの初期化
#     Base.metadata.create_all(bind=engine)

