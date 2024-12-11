# Ecommerce Back

- Model (Modelo):
    - Aqui você define as classes que correspondem às entidades do sistema (como Produto, Cliente, Pedido), além de suas propriedades e métodos.

- Controller:
    - Faz a ligação entre a UI (que no nosso caso não será foco) ou API e a lógica de negócios.
    - Os controllers são responsáveis por lidar com as requisições HTTP e passar os dados corretos para as camadas de serviço.

- Service:
    - Contém a lógica de negócios.
    - A camada de serviços é responsável por manipular os dados e as regras da aplicação, chamando os métodos do repository para obter, criar, atualizar ou deletar informações.

- Repository:
    - Lida com a persistência de dados (banco de dados, API externa, etc.).
    - Aqui você tem métodos que lidam diretamente com as operações de CRUD, mas sem lógica de negócios.

# Estrutura de diretórios

```bash
app/
    models/
        product_model.py
    controllers/
        product_controller.py
    services/
        product_service.py
    repositories/
        product_repository.py
```

# 1. Criando o Modelo "Produto" (Model Layer)
A primeira coisa que vamos fazer é criar o modelo para o produto. Ele vai refletir a estrutura básica do que é um produto na nossa aplicação.

Em FastAPI, usamos Pydantic para definir nossos modelos. O modelo será usado para validar os dados das requisições e mapear para o banco de dados (ou outras fontes de dados).

```python
from pydantic import BaseModel

# Definindo a estrutura básica de um produto
class ProductBase(BaseModel):
    name: str # Nome do produto
    price: float # Preço do produto

# Modelo usado na criação de um novo produto
class ProductCreate(ProductBase):
    pass  # Não há novos campos além dos de ProductBase

# Modelo com o ID incluído, usado para leitura de dados
class Product(ProductBase):
    id: int # O ID é gerado automaticamente pelo banco de dados

```

## Explicação:
- ProductBase define os atributos básicos de um produto (nome e preço).
- ProductCreate é um modelo utilizado apenas na criação de um produto (poderia ser estendido com mais campos).
- Product inclui o ID do produto, que é gerado automaticamente pelo banco de dados. orm_mode permite a conversão fácil entre objetos do ORM e Pydantic.

---

# 2. Criando o Repositório para o Produto (Repository Layer)

O repositório lida com a persistência dos dados. Para esta aula, vamos simular o acesso a um banco de dados com uma lista em memória.

```python
from app.models.product_model import ProductCreate
from typing import List

# Simulação de um banco de dados em memória
class ProductRepository:
    def __init__(self):
        # Simulação de dados
        self.products = [] # Lista que armazenará os produtos
        self.current_id = 1 # ID único para cada produto

    def get_all_products(self) -> List[dict]:
        return self.products

    def get_product_by_id(self, product_id: int) -> dict:
        for product in self.products:
            if product['id'] == product_id:
                return product
        return None

    def create_product(self, product: ProductCreate) -> dict:
        new_product = {
            "id": self.current_id,
            "name": product.name,
            "price": product.price
        }
        self.products.append(new_product)
        self.current_id += 1
        return new_product

    def delete_product(self, product_id: int) -> bool:
        for product in self.products:
            if product['id'] == product_id:
                self.products.remove(product)
                return True
        return False
```

## Explicação:
- Lista `self.products:` Esta lista armazena os produtos. Cada produto é um dicionário com `id`, `name` e `price`.

- Métodos
    - `get_all_products`: Retorna todos os produtos.
    - `get_product_by_id`: Busca um documento pelo ID.
    - `create product`: Cria e adiciona um novo produto a lista.
    - `delete_product`: Remove um produto pelo ID.

---

# 3. Criando o Serviço para o Produto (Service Layer)

O serviço é onde vamos colocar a lógica de negócios relacionada ao produto. Ele vai usar o repositório para realizar as operações e aplicar regras de negócio se necessário.

```python
from app.repositories.product_repository import ProductRepository
from app.models.product_model import ProductCreate

class ProductService:
    def __init__(self):
        self.repository = ProductRepository()   # Instância do repositório

    # Retorna todos os produtos
    def get_all_products(self):
        return self.repository.get_all_products()

    # Retorna um produto pelo ID
    def get_product_by_id(self, product_id: int):
        return self.repository.get_product_by_id(product_id)

    # Cria um novo produto
    def create_product(self, product: ProductCreate):
        return self.repository.create_product(product)

    # Remove um produto pelo ID
    def delete_product(self, product_id: int):
        return self.repository.delete_product(product_id)
```
## Eplicação:
- O `ProductService` interage com o `ProductRepository` para realizar as operações de CRUD.
- Aqui poderíamos adicionar regras de negócio, como validação do preço ou nome do produto antes de chamar o repositório..

---

# 4. Criando o Controller para Gerenciar Requisições (Controller Layer)
O controller será responsável por lidar com as requisições HTTP e direcioná-las para o serviço correto.

No controlador, os endpoints FastAPI chamam o serviço, que lida com a lógica de negócios e interage com o repositório.

```python
from fastapi import APIRouter, HTTPException
from app.services.product_service import ProductService
from app.models.product_model import Product, ProductCreate

router = APIRouter()
service = ProductService()

@router.get("/products", response_model=list[Product])
def get_all_products():
    return service.get_all_products()

@router.get("/products/{product_id}", response_model=Product)
def get_product_by_id(product_id: int):
    product = service.get_product_by_id(product_id)
    if not product:
        raise HTTPException(status_code=404, detail="Product not found")
    return product

@router.post("/products", response_model=Product)
def create_product(product: ProductCreate):
    return service.create_product(product)

@router.delete("/products/{product_id}")
def delete_product(product_id: int):
    deleted = service.delete_product(product_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Product not found")
    return {"message": "Product deleted successfully"}
```

## Explicação:
- O `ProductController` é responsável por chamar o `ProductService` para executar as operaçãoes de CRUD.
- Ele age como intermediário entre as requisições HTTP e o serviço.
- GET /products: Retorna todos os produtos.
- GET /products/{product_id}: Busca um produto pelo ID.
- POST /products: Cria um novo produto.
- DELETE /products/{product_id}: Remove um produto pelo ID.

---

# 5. Configuração Principal (main.py)
O arquivo principal main.py integra o FastAPI e as rotas.

```python
from fastapi import FastAPI
from app.controllers.product_controller import router as product_router

app = FastAPI()

app.include_router(product_router)

@app.get("/")
def read_root():
    return {"message": "Welcome to the Product API"}
```

## Explicação:

Este arquivo inicializa o FastAPI e registra as rotas definidas no controller de produtos. Quando a aplicação é executada, ela ficará pronta para responder às requisições HTTP.