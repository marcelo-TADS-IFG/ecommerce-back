# app/utils/jwt_middleware.py
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from jose import jwt
from starlette.middleware.base import BaseHTTPMiddleware
from jose import jwt
from app.services.user_service import UserService
from app.utils.settings import settings



app = FastAPI()


class JWTMiddleware(BaseHTTPMiddleware):

    allowed_paths = [
         "/docs",
        "/openapi.json",
        "/user/save",
        "/user/login",
    ]

    async def dispatch(self, request: Request, call_next):

        if (request.url.path in self.allowed_paths):
            return await call_next(request)

        try:
            token = request.headers.get("Authorization")
            token = jwt.decode(
                token.removeprefix("Bearer "), settings.jwt_key, settings.jwt_algorithm
            )

            user_db = UserService().get_user_by_username(username=token["username"])
            if user_db is None:
                return JSONResponse(
                    status_code=401,
                    content="Usuário não encontrado!",
                )

        except Exception as e:
            return JSONResponse(
                status_code=401,
                content="Token de acesso inválido ou não enviado!",
            )

        response = await call_next(request)
        return response


app.add_middleware(JWTMiddleware)