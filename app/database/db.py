from sqlalchemy import Column, Integer, Table, Text
from sqlalchemy.orm import registry

from app.dreams.models import Dream

mapper_registry = registry()


dream_table = Table(
    "dreams",
    mapper_registry.metadata,
    Column("id", Integer, primary_key=True, index=True),
    Column("description", Text),
)


def start_mappers():
    mapper_registry.map_imperatively(Dream, dream_table)
