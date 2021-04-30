from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, Text, DateTime


Base = declarative_base()


class Stock(Base):
  __tablename__ = 'stock'
  id = Column('id', Integer, primary_key=True)
  symbol = Column('symbol', String, unique=True)

  def __str__(self):
    return self.symbol


class Mention(Base):
  __tablename__ = 'mention'
  id = Column('id', Integer, primary_key=True)
  stock_id = Column(Integer, ForeignKey('stock.id'))
  message = Column(Text)
  source = Column(Text)
  url = Column(Text)
  created_at = Column(DateTime)

  def __str__(self):
    return self.url
