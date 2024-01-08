from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.crud import crud_limites_proposta, crud_propostas_contraparte, crud_cliente
from app.schemas.limites_proposta import LimitesPropostaCreate, LimitesProposta
from typing import List, Any

router = APIRouter()


@router.get("/", response_model=List[LimitesProposta])
def read_limites_proposta_all(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
) -> Any:
    """
    Get All LimitesProposta.
    """
    limites_proposta = crud_limites_proposta.get_multi_limites_proposta(db, skip=skip, limit=limit)
    return limites_proposta


@router.post("/", response_model=LimitesProposta)
def create_limites_proposta(
    *,
    db: Session = Depends(deps.get_db),
    limites_proposta: LimitesPropostaCreate,
    id_contraparte: int,
    id_cliente: int,
) -> Any:
    """
    Create LimitesProposta.
    """
    cliente = crud_cliente.get_cliente(db, id_cliente)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")

    propostas_contraparte = crud_propostas_contraparte.get_unic_propostas_contraparte(db, id_contraparte)
    if propostas_contraparte is None:
        raise HTTPException(status_code=404, detail="PropostaContraparte not found")

    created_limites_proposta = crud_limites_proposta.create_limites_proposta(
        db=db,
        limites_proposta=limites_proposta,
        id_cliente=id_cliente,
        id_contraparte=id_contraparte
    )
    return created_limites_proposta


@router.get("/{id_cliente}", response_model=List[LimitesProposta])
def read_limites_proposta(
    id_cliente: int,
    db: Session = Depends(deps.get_db),
) -> LimitesProposta:
    """
    Get LimitesProposta by id_cliente.
    """
    cliente = crud_cliente.get_cliente(db, id_cliente)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")

    limites_proposta = crud_limites_proposta.get_all_limites_proposta(db, id_cliente)
    if limites_proposta is None:
        raise HTTPException(status_code=404, detail="LimitesProposta not found")
    return limites_proposta


@router.put("/{id_limites}", response_model=LimitesProposta)
def update_limites_proposta(
        id_limites: int,
        *,
        db: Session = Depends(deps.get_db),
        id_cliente: int,
        id_contraparte: int,
        id_proposta: int,
        tipo_limite: int,
        rating: int,
        valor_limite: float,
        valor_carteira: float,
        carteira_mwm: float,
) -> Any:
    """
    Update LimitesProposta by id_limites.
    """
    limites_proposta_data = {
        "id_cliente": id_cliente,
        "id_contraparte": id_contraparte,
        "id_proposta": id_proposta,
        "tipo_limite": tipo_limite,
        "rating": rating,
        "valor_limite": valor_limite,
        "valor_carteira": valor_carteira,
        "carteira_mwm": carteira_mwm,
    }

    limites_proposta_in_db = crud_limites_proposta.get_unic_limites_proposta(db, id_limites)
    if limites_proposta_in_db is None:
        raise HTTPException(status_code=404, detail="LimitesProposta  not found")

    cliente = crud_cliente.get_cliente(db, id_cliente)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")

    propostas_contraparte = crud_propostas_contraparte.get_configuracao_cliente(db, id_contraparte)
    if propostas_contraparte is None:
        raise HTTPException(status_code=404, detail="PropostaContraparte not found")

    limites_proposta_updated = crud_limites_proposta.update_limites_proposta(
        db, db_obj=limites_proposta_in_db, obj_in=limites_proposta_data
    )
    return limites_proposta_updated


@router.delete("/{id_limites}", response_model=dict)
def deletelimites_proposta(
        id_limites: int,
        db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete LimitesProposta by id_limites.
    """
    get_limites_proposta_in_db = crud_limites_proposta.get_limites_proposta(db, id_limites)
    if get_limites_proposta_in_db is None:
        raise HTTPException(status_code=404, detail="LimitesProposta not found")

    crud_limites_proposta.delete_limites_proposta(db, get_limites_proposta_in_db)

    return {"message": "LimitesProposta deleted successfully"}