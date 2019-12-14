from pathlib import Path

ROOT_DIR = Path(__file__).absolute().parent


class Config:
    SQLALCHEMY_DATABASE_URI = f'sqlite:///{ROOT_DIR}/db.sqlite'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
