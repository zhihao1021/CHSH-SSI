from pydantic import BaseModel, Field


class Config(BaseModel):
    host: str = Field("0.0.0.0", const=True)
    port: int = Field(8080, const=True, ge=1, le=65535)


try:
    CONFIG = Config.parse_raw(open("config.json").read())
except:
    CONFIG = Config()

open("config.json", mode="w").write(CONFIG.json())
