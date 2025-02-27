from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from backend.contrib.models import BaseModel

class CentroTreinamentoModel(BaseModel):
    __tablename__ = 'centros_treinamento'

    pk_id: Mapped[int] = mapped_column(Integer, primary_key=True)
    nome: Mapped[str] = mapped_column(String(10), nullable=False)
    endereco: Mapped[str] = mapped_column(String(60), unique=True, nullable=False)
    proprietario: Mapped[str] = mapped_column(String(10), nullable=False)
    atleta: Mapped['AtletaModel'] = relationship(back_populates='centro_treinamento')
    