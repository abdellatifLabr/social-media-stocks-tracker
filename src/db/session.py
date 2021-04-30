import os
import sys
from contextlib import contextmanager

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from .models import Base

BASE_DIR = os.path.dirname(os.path.abspath(sys.modules['__main__'].__file__))

db_engine = create_engine(f'sqlite:////{BASE_DIR}/db.sqlite3')
Base.metadata.create_all(bind=db_engine)
Session = sessionmaker(bind=db_engine)


@contextmanager
def db_session():
  session = Session()
  try:
    yield session
    session.commit()
  except KeyboardInterrupt:
    session.commit()
  except Exception as error:
    session.rollback()
    raise error
  finally:
    session.close()
