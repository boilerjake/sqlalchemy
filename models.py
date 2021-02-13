from sqlalchemy import Column, create_engine, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session
from typing import Optional

engine = create_engine('sqlite:///LAME.db')
Base = declarative_base()
session = Session(engine)

class Person(Base):
    ''' Represents a human being.
    '''
    __tablename__ = 'people'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    gender = Column(String, default='male', nullable=False)
    date_of_birth = Column(String)

    def __repr__(self) -> str:
        return f'<Person {self.name}>'

    @classmethod
    def create(cls, name: str, gender: Optional[str] = None,
               date_of_birth: Optional[str] = None) -> 'Person':
        ''' Creates a new instance of Person. (Warning: does not add to the
            database automatically)
        '''
        new_person = cls(name=name, gender=gender, date_of_birth=date_of_birth)
        return new_person


Base.metadata.create_all(engine)
