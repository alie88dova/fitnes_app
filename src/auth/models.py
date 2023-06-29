from datetime import datetime
from sqlalchemy import MetaData, Integer, String, TIMESTAMP, ForeignKey, Table, Column, Boolean

metadata = MetaData()


user = Table(
    "user",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("name", String, nullable=False),
    Column("email", String, unique=True),
    Column("age", Integer),
    Column("date_create", TIMESTAMP, default=datetime.utcnow()),
    Column("last_enter", TIMESTAMP, default=datetime.utcnow()),
    Column("role", String),
    Column("special_key", String, nullable=True),
    Column("hashed_password", String, nullable=False),
    Column("is_active", Boolean, default=True, nullable=False),
    Column("is_superuser", Boolean, default=False, nullable=False),
    Column("is_verified", Boolean, default=False, nullable=False),


)

trainer = Table(
    "trainer",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("usr_id", Integer, ForeignKey("user.id"), nullable=False),
    Column("cost", Integer, nullable=False),
    Column("diploms", String)
)

