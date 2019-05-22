from sqlalchemy import Column, Integer, String, Sequence
import connector


class Usuario(connector.Manager.Base):
    __tablename__ = 'users'
    id = Column(Integer, Sequence('users_id'), primary_key=True)
    nombre = Column(String(50))
    apellido = Column(String(12))
    clave = Column(String(120))
