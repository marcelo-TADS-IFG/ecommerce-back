from fastapi import FastAPI
from sqlalchemy import text
from app.controllers.product_controller import router as product_router
from app.controllers.category_controller import router as category_router
from app.controllers.subcategory_controller import router as subcategory_router
from app.controllers.user_controller import router as user_router
from app.controllers.role_controller import router as role_router
from app.connection.database import Base, database
from fastapi.middleware.cors import CORSMiddleware  # Importar o middleware de CORS

import uvicorn

from app.utils.jwt_middleware import JWTMiddleware
from app.utils.openapi_schema import custom_openapi

app = FastAPI()

# Configuração personalizada do OpenAPI
app.openapi = lambda: custom_openapi(app)

# Adicionando rotas
app.include_router(product_router)
app.include_router(category_router)
app.include_router(subcategory_router)
app.include_router(user_router)
app.include_router(role_router)

# Criar tabelas no banco de dados
Base.metadata.create_all(bind=database.engine)

# Adicionar middleware JWT
app.add_middleware(JWTMiddleware)

# Adicionar suporte ao CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def read_root():
    return {"Hello": "World"}

def startup():
    with database.get_session() as db:
        try:
            sql_script = """
                DO
                $$
                DECLARE
                    table_name RECORD;
                BEGIN
                    -- Para cada tabela no schema especificado
                    FOR table_name IN
                        SELECT tablename
                        FROM pg_tables
                        WHERE schemaname = 'public'
                    LOOP
                        -- Gerar e executar o comando de exclusão da tabela
                        EXECUTE 'DROP TABLE public.' || table_name.tablename || ' CASCADE';
                    END LOOP;
                END
                $$;
            """
            db.execute(text(sql_script))
            db.commit()
        finally:
            db.close()

def main():
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

if __name__ == "__main__":
    main()
