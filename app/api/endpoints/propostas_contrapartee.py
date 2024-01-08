from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.crud import crud_propostas_contraparte, crud_configuracao_cliente, crud_cliente, crud_tipos_rating_cliente
from app.schemas.propostas_contraparte import PropostaContraparteCreate, PropostaContraparte
from typing import List, Any
from datetime import datetime

router = APIRouter()


@router.get("/", response_model=List[PropostaContraparte])
def read_propostas_contraparte_all(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
) -> Any:
    """
    Get All PropostaContraparte.
    """
    propostas_contraparte = crud_propostas_contraparte.get_multi_propostas_contraparte(db, skip=skip, limit=limit)
    return propostas_contraparte

@router.get("/{id_cliente}", response_model=List[PropostaContraparte])
def read_propostas_contraparte(
    id_cliente: int,
    db: Session = Depends(deps.get_db),
) -> PropostaContraparte:
    """
    Get PropostaContraparte by id_cliente.
    """
    cliente = crud_cliente.get_cliente(db, id_cliente)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")
    propostas_contraparte = crud_propostas_contraparte.get_all_propostas_contraparte(db, id_cliente)
    if propostas_contraparte is None:
        raise HTTPException(status_code=404, detail="PropostaContraparte not found")
    return propostas_contraparte



@router.post("/", response_model=PropostaContraparte)
def create_propostas_contraparte(
    *,
    db: Session = Depends(deps.get_db),
    propostas_contraparte: PropostaContraparteCreate,
    id_cliente: int,
) -> Any:
    """
    Create PropostaContraparte.
    """
    cliente = crud_cliente.get_cliente(db, id_cliente)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")

    created_propostas_contraparte = crud_propostas_contraparte.create_propostas_contraparte(
        db=db,
        propostas_contraparte=propostas_contraparte,
        id_cliente=id_cliente,
    )
    return created_propostas_contraparte


@router.put("/{id_proposta}", response_model=PropostaContraparte)
def update_propostas_contraparte(
        id_proposta: int,
        *,
        db: Session = Depends(deps.get_db),
        id_cliente: int,
        data_aprovacao_limite: datetime,
        grupo: str,
        tipo_limite: str,
        data_proposta: datetime,
        tipo_analise: float,
        status: int,
        valor_utilizado_conversao: float,
) -> Any:
    """
    Update PropostaContraparte by id_proposta.
    """
    propostas_contraparte_data = {
        "id_cliente": id_cliente,
        "data_aprovacao_limite": data_aprovacao_limite,
        "grupo": grupo,
        "tipo_limite": tipo_limite,
        "data_proposta": data_proposta,
        "tipo_analise": tipo_analise,
        "status": status,
        "valor_utilizado_conversao": valor_utilizado_conversao,
    }

    propostas_contraparte_in_db = crud_propostas_contraparte.get_unic_propostas_contraparte(db, id_proposta)
    if propostas_contraparte_in_db is None:
        raise HTTPException(status_code=404, detail="PropostaContraparte  not found")

    cliente = crud_cliente.get_cliente(db, id_cliente)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")

    propostas_contraparte_updated = crud_propostas_contraparte.update_propostas_contraparte(
        db, db_obj=propostas_contraparte_in_db, obj_in=propostas_contraparte_data
    )
    return propostas_contraparte_updated


@router.delete("/{id_proposta}", response_model=dict)
def delete_propostas_contraparte(
        id_proposta: int,
        db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete PropostaContraparte by id_aprovador.
    """
    get_propostas_contraparte_in_db = crud_propostas_contraparte.get_aprovadores_cliente(db, id_proposta)
    if get_propostas_contraparte_in_db is None:
        raise HTTPException(status_code=404, detail="PropostaContraparte not found")

    crud_propostas_contraparte.delete_aprovadores_cliente(db, get_propostas_contraparte_in_db)

    return {"message": "PropostaContraparte deleted successfully"}