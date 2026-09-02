# Prompt para Mejorar el Codigo Base

Copia y pega el siguiente contenido completo en un asistente de IA (Claude, ChatGPT, etc.)
para obtener un ZIP con el proyecto corregido y listo para compilar.

---

```
Eres un asistente experto en análisis, corrección y generación de archivos de cualquier tipo:
código fuente, documentación, hojas de cálculo, documentos Word, configuraciones, entre otros.
Voy a enviarte una cadena de texto que contiene uno o más archivos. Cada archivo está delimitado por un marcador con el siguiente formato:
// === ARCHIVO: ruta/del/archivo.extension ===
o también puede aparecer como:
## === ARCHIVO: ruta/del/archivo.extension ===
Lo que sigue al marcador puede ser:

El contenido real del archivo (código, texto, YAML, etc.)
Una descripción en lenguaje natural de lo que debe contener el archivo


TU TAREA
PASO 1 — Detección y extracción
Identifica todos los archivos presentes en la cadena. Para cada archivo extrae:

Su ruta completa (ej: src/main/java/com/pragma/Service.java)
Su contenido o descripción

PASO 2 — Clasificación por tipo
Clasifica cada archivo en una de estas categorías:
A) Código fuente (Java, Python, TypeScript, JavaScript, Kotlin, etc.)
B) Configuración / documentación (YAML, properties, Markdown, JSON, txt, etc.)
C) Excel (.xlsx, .xls, .csv)
D) Word (.docx, .doc)
E) Otro tipo de archivo binario o especial
PASO 3 — Clasificación de errores en código fuente

Objetivo prioritario: que el proyecto compile. No corrijas flujo de negocio ni lógica funcional.

Antes de modificar cualquier archivo de código fuente, clasifica cada problema encontrado en una de estas dos categorías:
🔴 ERROR DE COMPILACIÓN — corregir siempre
Son errores que impiden que el proyecto arranque, sin valor pedagógico:

Import faltante o incorrecto
Clase, método o variable referenciada que no existe en ningún archivo del proyecto
Error de sintaxis
Anotación con atributos inválidos
Dependencia ausente en pom.xml, package.json, etc.
Archivo referenciado que no existe y debe ser creado con implementación mínima

→ CORREGIR estos errores.
🟡 PROBLEMA FUNCIONAL O DE CALIDAD — preservar siempre
Son problemas que no impiden compilar. Pueden ser intencionales para el aprendizaje:

Clave secreta hardcodeada ("secret", "password123")
API deprecada que funciona pero tiene reemplazo moderno
Lógica de negocio incorrecta o incompleta
Código redundante o de baja legibilidad
Falta de validaciones en flujo de negocio
Patrones de diseño incorrectos pero funcionales
Concurrencia no segura
Configuración funcional pero no óptima

→ PRESERVAR tal cual. No corregir, no mejorar, no comentar.
PASO 4 — Procesamiento según tipo de archivo
Tipo A — Código fuente
Aplica únicamente las correcciones clasificadas como 🔴 ERROR DE COMPILACIÓN.
No alteres ningún elemento clasificado como 🟡 PROBLEMA FUNCIONAL O DE CALIDAD.
Si falta un archivo referenciado, créalo con la implementación mínima necesaria para compilar.
Tipo B — Configuración / documentación
Extrae el contenido tal cual, sin modificaciones salvo errores evidentes de sintaxis
(ej: YAML mal indentado).
Tipo C — Excel (.xlsx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un archivo Excel funcional con:

Fila de encabezados en negrita con color de fondo distintivo
Columnas con ancho ajustado al contenido
Tipos de dato correctos por columna
Validaciones si la descripción lo indica
Hojas nombradas descriptivamente si hay más de una
Filas de ejemplo si no hay datos reales

Tipo D — Word (.docx)
Si viene con contenido real, genera el archivo respetando ese contenido.
Si viene con descripción en lenguaje natural, genera un documento Word funcional con:

Estilos de título (Título 1, Título 2) para jerarquía de secciones
Fuente legible (Calibri o equivalente), tamaño 11-12pt para cuerpo
Márgenes estándar
Tabla de contenido si tiene múltiples secciones
Tablas con encabezados en negrita si aplica

Tipo E — Otro
Genera el archivo con el contenido o estructura más apropiada según la descripción.
PASO 5 — Exportación en ZIP
Empaqueta todos los archivos en un único archivo ZIP descargable respetando exactamente
la estructura de rutas indicada por los marcadores.
El ZIP debe incluir:

Archivos de código con únicamente los errores de compilación corregidos
Archivos de configuración y documentación sin cambios
Archivos nuevos creados para resolver dependencias de compilación faltantes
Archivos Excel y Word generados desde descripción

IMPORTANTE: El ZIP debe estar listo para descargar al finalizar. No preguntes si el usuario
quiere generarlo. Simplemente genera el archivo y proporciona el enlace de descarga; No debes desplegar en el chat el resumen de lo que arreglaste al Zip, solo entregalo.

REGLAS IMPORTANTES

No omitas ningún archivo aunque no tenga errores ni modificaciones
Respeta los nombres y rutas exactas indicadas por los marcadores
Si un archivo no tiene marcador claro, infiere el nombre desde su contenido
Si la cadena contiene solo documentación o descripciones sin código, genera los archivos
correspondientes sin aplicar análisis de compilación
No agregues texto después del enlace de descarga del ZIP
No preguntes si el usuario quiere el ZIP: simplemente generalo siempre
Si detectas que falta un archivo de configuración necesario para compilar
(pom.xml, package.json, requirements.txt, build.gradle, etc.), créalo e inclúyelo
inferiendo su contenido desde los imports y frameworks detectados en el código
Nunca corrijas problemas 🟡 aunque parezcan obvios o fáciles de mejorar.
El participante que recibirá este proyecto los debe encontrar y resolver él mismo.


INPUT
Aquí está la cadena con los archivos:
// === ARCHIVO: src/main.py ===
from fastapi import FastAPI
from src.api.v1.account import account_router

app = FastAPI()

app.include_router(account_router)

// === ARCHIVO: src/models/account.py ===
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Account(Base):
    __tablename__ = 'accounts'
    id = Column(Integer, primary_key=True, index=True)
    account_number = Column(String, unique=True, index=True)
    balance = Column(Float)
    holder = Column(String)
    creation_date = Column(String)

// === ARCHIVO: src/schemas/account.py ===
from pydantic import BaseModel

class AccountCreate(BaseModel):
    account_number: str
    balance: float
    holder: str
    creation_date: str

class AccountUpdate(BaseModel):
    balance: float
    holder: str

class AccountResponse(BaseModel):
    id: int
    account_number: str
    balance: float
    holder: str
    creation_date: str

// === ARCHIVO: src/crud/account.py ===
from sqlalchemy.orm import Session
from src.models.account import Account
from src.schemas.account import AccountCreate, AccountUpdate, AccountResponse

def create_account(db: Session, account: AccountCreate) -> AccountResponse:
    db_account = Account(**account.dict())
    db.add(db_account)
    db.commit()
    db.refresh(db_account)
    return AccountResponse.from_orm(db_account)

def get_account(db: Session, account_id: int) -> AccountResponse:
    return db.query(Account).filter(Account.id == account_id).first()

def update_account(db: Session, account_id: int, account: AccountUpdate) -> AccountResponse:
    db_account = db.query(Account).filter(Account.id == account_id).first()
    for key, value in account.dict().items():
        setattr(db_account, key, value)
    db.commit()
    db.refresh(db_account)
    return AccountResponse.from_orm(db_account)

def delete_account(db: Session, account_id: int):
    db.query(Account).filter(Account.id == account_id).delete()
    db.commit()

// === ARCHIVO: src/api/v1/account.py ===
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from src.crud.account import create_account, get_account, update_account, delete_account
from src.schemas.account import AccountCreate, AccountUpdate, AccountResponse
from src.config.database import get_db

account_router = APIRouter()

@account_router.post('/accounts/', response_model=AccountResponse)
def create_account_endpoint(account: AccountCreate, db: Session = Depends(get_db)):
    return create_account(db, account)

@account_router.get('/accounts/{account_id}', response_model=AccountResponse)
def read_account(account_id: int, db: Session = Depends(get_db)):
    db_account = get_account(db, account_id)
    if db_account is None:
        raise HTTPException(status_code=404, detail='Account not found')
    return db_account

@account_router.put('/accounts/{account_id}', response_model=AccountResponse)
def update_account_endpoint(account_id: int, account: AccountUpdate, db: Session = Depends(get_db)):
    db_account = update_account(db, account_id, account)
    if db_account is None:
        raise HTTPException(status_code=404, detail='Account not found')
    return db_account

@account_router.delete('/accounts/{account_id}')
def delete_account_endpoint(account_id: int, db: Session = Depends(get_db)):
    delete_account(db, account_id)
    return {'detail': 'Account deleted'}

// === ARCHIVO: src/tests/test_account.py ===
from fastapi.testclient import TestClient
from src.main import app
from src.schemas.account import AccountCreate, AccountUpdate

client = TestClient(app)

def test_create_account():
    account_data = AccountCreate(account_number='123456789', balance=100.0, holder='John Doe', creation_date='2024-07-10')
    response = client.post('/accounts/', json=account_data.dict())
    assert response.status_code == 200
    assert response.json()['account_number'] == '123456789'

def test_read_account():
    response = client.get('/accounts/1')
    assert response.status_code == 200
    assert response.json()['account_number'] == '123456789'

def test_update_account():
    account_data = AccountUpdate(balance=200.0, holder='Jane Doe')
    response = client.put('/accounts/1', json=account_data.dict())
    assert response.status_code == 200
    assert response.json()['balance'] == 200.0

def test_delete_account():
    response = client.delete('/accounts/1')
    assert response.status_code == 200
    assert response.json()['detail'] == 'Account deleted'

// === ARCHIVO: src/config/settings.py ===
import os
from pydantic import BaseSettings

class Settings(BaseSettings):
    database_url: str

    class Config:
        env_file = '.env'

settings = Settings()

// === ARCHIVO: src/config/database.py ===
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from src.models.account import Base
from src.config.settings import settings

engine = create_engine(settings.database_url)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base.metadata.create_all(bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

```
