from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.crud import crud_alcadas_cliente, crud_configuracao_cliente, crud_tipos_rating_cliente, crud_cliente
from app.schemas.alcadas_cliente import AlcadasCliente, AlcadasClienteCreate
from typing import List, Any

router = APIRouter()


@router.get("/", response_model=List[AlcadasCliente])
def read_alcadas_cliente_all(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
) -> Any:
    """
    Get All AlcadasCliente.
    """
    alcadas_cliente = crud_alcadas_cliente.get_multi_alcadas_cliente(db, skip=skip, limit=limit)
    return alcadas_cliente


@router.get("/{id_cliente}", response_model=List[AlcadasCliente])
def read_alcadas_cliente(
    id_cliente: int,
    db: Session = Depends(deps.get_db),
) -> AlcadasCliente:
    """
    Get AlcadasCliente by id_cliente.
    """
    cliente = crud_cliente.get_cliente(db, id_cliente)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")
    alcadas_cliente = crud_alcadas_cliente.get_all_alcadas_cliente(db, id_cliente)
    if alcadas_cliente is None:
        raise HTTPException(status_code=404, detail="AlcadasCliente not found")
    return alcadas_cliente


@router.post("/", response_model=AlcadasCliente)
def create_alcadas_cliente(
        *,
        db: Session = Depends(deps.get_db),
        alcadas_cliente_in: AlcadasClienteCreate,
        id_cliente: int,
        id_tipo_rating: int,
) -> Any:
    """
    Create AlcadasCliente.
    """
    configuracao_cliente = crud_configuracao_cliente.get_configuracao_cliente(db, id_cliente)
    if configuracao_cliente is None:
        raise HTTPException(status_code=404, detail="ConfiguracaoCliente not found")

    tipos_rating_cliente_in_db = crud_tipos_rating_cliente.get_unic_tipos_rating_cliente(db, id_tipo_rating)
    if tipos_rating_cliente_in_db is None:
        raise HTTPException(status_code=404, detail="TiposRatingCliente  not found")

    created_alcadas_cliente = crud_alcadas_cliente.create_alcadas_cliente(
        db=db,
        alcadas_cliente=alcadas_cliente_in,
        id_cliente=id_cliente,
        id_tipo_rating=id_tipo_rating
    )
    return created_alcadas_cliente


@router.put("/{id_alcadas}", response_model=AlcadasCliente)
def update_alcadas_cliente(
        id_alcadas: int,
        *,
        db: Session = Depends(deps.get_db),
        id_cliente: int,
        id_tipo_rating: int,
        limite_minimo_aprovacao: float,
        limite_maximo_aprovacao: float,
        perfil_aprovador: str,
        percentual_aprovacao: float,
) -> Any:
    """
    Update AlcadasCliente by id_alcadas.
    """
    alcadas_cliente_data = {
        "id_cliente": id_cliente,
        "id_tipo_rating": id_tipo_rating,
        "limite_minimo_aprovacao": limite_minimo_aprovacao,
        "limite_maximo_aprovacao": limite_maximo_aprovacao,
        "perfil_aprovador": perfil_aprovador,
        "percentual_aprovacao": percentual_aprovacao,
    }

    alcadas_cliente_in_db = crud_alcadas_cliente.get_unic_alcadas_cliente(db, id_alcadas)
    if alcadas_cliente_in_db is None:
        raise HTTPException(status_code=404, detail="AlcadasCliente not found")

    tipos_rating_cliente = crud_tipos_rating_cliente.get_unic_tipos_rating_cliente(db, id_tipo_rating)
    if tipos_rating_cliente is None:
        raise HTTPException(status_code=404, detail="TiposRatingCliente  not found")

    cliente = crud_cliente.get_cliente(db, id_cliente)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")

    alcadas_cliente_updated = crud_alcadas_cliente.update_alcadas_cliente(
        db, db_obj=alcadas_cliente_in_db, obj_in=alcadas_cliente_data
    )
    return alcadas_cliente_updated



@router.delete("/{id_alcadas}", response_model=dict)
def delete_alcadas_cliente(
        id_alcadas: int,
        db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete AlcadasCliente by id_alcadas.
    """
    get_alcadas_cliente_in_db = crud_alcadas_cliente.get_alcadas_cliente(db, id_alcadas)
    if get_alcadas_cliente_in_db is None:
        raise HTTPException(status_code=404, detail="AlcadasCliente not found")

    crud_alcadas_cliente.delete_alcadas_cliente(db, get_alcadas_cliente_in_db)

    return {"message": "ConfiguracaoCliente deleted successfully"}
