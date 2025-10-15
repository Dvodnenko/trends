from dotenv import load_dotenv
from pydantic_settings import BaseSettings


load_dotenv()

class Settings(BaseSettings):

    ## Platforms
    REDDIT_CLIENT_ID: str
    REDDIT_SECRET: str
    TWITTER_BEARER: str

    ## Databases
    PG_NAME: str
    PG_USER: str
    PG_PASSWORD: str
    PG_PORT: str
    PG_HOST: str

    ## LLMs
    GEMINI_API_KEY: str

    ## Special
    @property
    def postgresurl(self) -> str:
        url = "postgresql+psycopg2://{PG_USER}:{PG_PASSWORD}@{PG_HOST}:{PG_PORT}/{PG_NAME}".format(
                PG_USER=self.PG_USER,
                PG_PASSWORD=self.PG_PASSWORD,
                PG_HOST=self.PG_HOST,
                PG_NAME=self.PG_NAME,
                PG_PORT=self.PG_PORT
            )
        return url

settings = Settings()
