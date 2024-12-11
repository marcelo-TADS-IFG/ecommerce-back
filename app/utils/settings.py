# app/utils/settings.py
from pydantic_settings import BaseSettings

class Settings(BaseSettings):
    """
    Classe que representa as configurações do aplicativo Ecommerce.

    Atributos:
        app_name (str): O nome do aplicativo.
        jwt_key (str): A chave utilizada para gerar e verificar tokens JWT.
        jwt_algorithm (str): O algoritmo utilizado para assinar os tokens JWT.
    """

    app_name: str = "Ecommerce API"
    jwt_key: str = "F4B8134F83FC63B7CF1C8D2E7A5F1EFE50BABC387D8344AB9A0ABD59F998C32E"
    jwt_algorithm: str = "HS256"


settings = Settings()