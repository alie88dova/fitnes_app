from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Table, Column, Boolean

metadata = MetaData()

PersProgram = Table(
    "PersProgram",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("file_path", String, nullable=False),
    Column("client_id", Integer, nullable=False),
    Column("trainer_id", Integer, nullable=False)
)


