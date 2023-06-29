from pydantic import BaseModel


class AddPersProgramm(BaseModel):
    name: str
    client_id: int
    trainer_id:int
    file_path: str

