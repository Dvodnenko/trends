from sqlalchemy import MetaData, create_engine
from sqlalchemy.orm import registry, sessionmaker

from .core.config import settings


naming_conventions: dict[str, str] = {
    'ix': 'ix_%(column_0_label)s',
    'uq': 'uq_%(table_name)s_%(column_0_name)s',
    'ck': 'ck_%(table_name)s_%(constraint_name)s',
    'fk': 'fk_%(table_name)s_%(column_0_name)s_%(referred_table_name)s',
    'pk': 'pk_%(table_name)s',
}

metadata: MetaData = MetaData(naming_convention=naming_conventions)
mapping_registry: registry = registry(metadata=metadata)

engine = create_engine(url=settings.postgresurl, echo=False)
Session = sessionmaker(engine)
