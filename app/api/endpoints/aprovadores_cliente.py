from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.crud import crud_aprovadores_cliente, crud_configuracao_cliente, crud_cliente
from app.schemas.aprovadores_cliente import AprovadoresClienteCreate, AprovadoresCliente
from typing import List, Any

router = APIRouter()


@router.get("/", response_model=List[AprovadoresCliente])
def read_aprovadores_cliente_all(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
) -> Any:
    """
    Get All AprovadoresCliente.
    """
    aprovadores_cliente = crud_aprovadores_cliente.get_multi_aprovadores_cliente(db, skip=skip, limit=limit)
    return aprovadores_cliente


@router.get("/{id_cliente}", response_model=List[AprovadoresCliente])
def read_aprovadores_cliente(
    id_cliente: int,
    db: Session = Depends(deps.get_db),
) -> AprovadoresCliente:
    """
    Get AprovadoresCliente by id_cliente.
    """
    cliente = crud_cliente.get_cliente(db, id_cliente)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")
    aprovadores_cliente = crud_aprovadores_cliente.get_all_aprovadores_cliente(db, id_cliente)
    if aprovadores_cliente is None:
        raise HTTPException(status_code=404, detail="AprovadoresCliente not found")
    return aprovadores_cliente


@router.post("/", response_model=AprovadoresCliente)
def create_aprovadores_cliente(
    *,
    db: Session = Depends(deps.get_db),
    aprovadores_cliente: AprovadoresClienteCreate,
    id_cliente: int,
) -> Any:
    """
    Create AprovadoresCliente.
    """
    configuracao_cliente = crud_configuracao_cliente.get_configuracao_cliente(db, id_cliente)
    if configuracao_cliente is None:
        raise HTTPException(status_code=404, detail="ConfiguracaoCliente not found")

    created_aprovadores_cliente = crud_aprovadores_cliente.create_aprovadores_cliente(
        db=db,
        aprovadores_cliente=aprovadores_cliente,
        id_cliente=id_cliente,
    )
    return created_aprovadores_cliente

@router.put("/{id_aprovador}", response_model=AprovadoresCliente)
def update_aprovadores_cliente(
        id_aprovador: int,
        *,
        db: Session = Depends(deps.get_db),
        id_cliente: int,
        cargo_aprovador: str,
        login_aprovador: str,
        perfil_aprovador: str,
        percentual_peso_aprovador: float,
) -> Any:
    """
    Update AprovadoresCliente by id_aprovador.
    """
    aprovadores_cliente_data = {
        "id_cliente": id_cliente,
        "cargo_aprovador": cargo_aprovador,
        "login_aprovador": login_aprovador,
        "perfil_aprovador": perfil_aprovador,
        "percentual_peso_aprovador": percentual_peso_aprovador,
    }

    aprovadores_cliente_in_db = crud_aprovadores_cliente.get_unic_aprovadores_cliente(db, id_aprovador)
    if aprovadores_cliente_in_db is None:
        raise HTTPException(status_code=404, detail="AprovadoresCliente  not found")

    cliente = crud_cliente.get_cliente(db, id_cliente)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")

    aprovadores_cliente_updated = crud_aprovadores_cliente.update_aprovadores_cliente(
        db, db_obj=aprovadores_cliente_in_db, obj_in=aprovadores_cliente_data
    )
    return aprovadores_cliente_updated


@router.delete("/{id_aprovador}", response_model=dict)
def delete_aprovadores_cliente(
        id_aprovador: int,
        db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete AprovadoresCliente by id_aprovador.
    """
    get_aprovadores_cliente_in_db = crud_aprovadores_cliente.get_aprovadores_cliente(db, id_aprovador)
    if get_aprovadores_cliente_in_db is None:
        raise HTTPException(status_code=404, detail="AprovadoresCliente not found")

    crud_aprovadores_cliente.delete_aprovadores_cliente(db, get_aprovadores_cliente_in_db)

    return {"message": "AprovadoresCliente deleted successfully"}
