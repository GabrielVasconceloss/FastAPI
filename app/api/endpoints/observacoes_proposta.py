from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.crud import crud_observacoes_proposta, crud_configuracao_cliente, crud_cliente, crud_propostas_contraparte
from app.schemas.observacoes_proposta import ObservacoesPropostaCreate, ObservacoesProposta
from typing import List, Any

router = APIRouter()


@router.get("/", response_model=List[ObservacoesProposta])
def read_observacoes_proposta_all(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
) -> Any:
    """
    Get All ObservacoesProposta.
    """
    observacoes_proposta = crud_observacoes_proposta.get_multi_observacoes_proposta(db, skip=skip, limit=limit)
    return observacoes_proposta


@router.post("/", response_model=ObservacoesProposta)
def create_observacoes_proposta(
        *,
        db: Session = Depends(deps.get_db),
        observacoes_proposta_in: ObservacoesPropostaCreate,
        id_cliente: int,
        id_contraparte: int,
) -> Any:
    """
    Create ObservacoesProposta.
    """
    cliente = crud_cliente.get_cliente(db, id_cliente)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")

    propostas_contraparte = crud_propostas_contraparte.get_unic_propostas_contraparte(db, id_contraparte)
    if propostas_contraparte is None:
        raise HTTPException(status_code=404, detail="PropostaContraparte not found")

    created_observacoes_proposta = crud_observacoes_proposta.create_observacoes_proposta(
        db=db,
        observacoes_proposta_in=observacoes_proposta_in,
        id_cliente=id_cliente,
        id_contraparte=id_contraparte,
    )
    return created_observacoes_proposta


@router.get("/{id_cliente}", response_model=List[ObservacoesProposta])
def read_observacoes_proposta(
    id_cliente: int,
    db: Session = Depends(deps.get_db),
) -> ObservacoesProposta:
    """
    Get ObservacoesProposta by id_cliente.
    """
    cliente = crud_cliente.get_cliente(db, id_cliente)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")


    observacoes_proposta = crud_observacoes_proposta.get_all_observacoes_proposta(db, id_cliente)
    if observacoes_proposta is None:
        raise HTTPException(status_code=404, detail="ObservacoesProposta not found")
    return observacoes_proposta


@router.put("/{id_observacoes}", response_model=ObservacoesProposta)
def update_observacoes_proposta(
        id_observacoes: int,
        *,
        db: Session = Depends(deps.get_db),
        id_cliente: int,
        id_proposta: int,
        id_contraparte: int,
        tipo_observacao: int,
        observacao_vigente: str,
        observacao_sugerido: str,
        observacao_aprovado: str,
) -> Any:
    """
    Update ObservacoesProposta by id_observacoes.
    """
    observacoes_proposta_data = {
        "id_cliente": id_cliente,
        "id_proposta": id_proposta,
        "id_contraparte": id_contraparte,
        "tipo_observacao": tipo_observacao,
        "observacao_vigente": observacao_vigente,
        "observacao_sugerido": observacao_sugerido,
        "observacao_aprovado": observacao_aprovado,
    }
    observacoes_proposta_in_db = crud_observacoes_proposta.get_unic_observacoes_proposta(db, id_observacoes)
    if observacoes_proposta_in_db is None:
        raise HTTPException(status_code=404, detail="ObservacoesProposta  not found")

    cliente = crud_cliente.get_cliente(db, id_cliente)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")

    propostas_contraparte = crud_propostas_contraparte.get_unic_propostas_contraparte(db, id_contraparte)
    if propostas_contraparte is None:
        raise HTTPException(status_code=404, detail="PropostaContraparte not found")

    observacoes_proposta_db_updated = crud_observacoes_proposta.update_observacoes_proposta(
        db, db_obj=observacoes_proposta_in_db, obj_in=observacoes_proposta_data)
    return observacoes_proposta_db_updated


@router.delete("/{id_observacoes}", response_model=dict)
def delete_observacoes_proposta(
        id_observacoes: int,
        db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete ObservacoesProposta by ObservacoesProposta.
    """
    observacoes_proposta = crud_observacoes_proposta.get_observacoes_proposta(db, id_observacoes)
    if observacoes_proposta is None:
        raise HTTPException(status_code=404, detail="ObservacoesProposta not found")

    crud_observacoes_proposta.delete_observacoes_proposta(db, observacoes_proposta)

    return {"message": "ObservacoesProposta deleted successfully"}