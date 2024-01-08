from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.crud import crud_propostas_contraparte, crud_configuracao_cliente, crud_cliente, crud_limites_proposta, crud_observacoes_proposta
from app.schemas.propostas_contraparte import PropostaContraparteCreate, PropostaContraparte
from typing import List, Any, Dict
from datetime import datetime
from app.schemas.proposta import PropostaResponse, ObservacoesPropostaResponse, LimitesPropostaResponse, PropostaResponseBase

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



@router.get("/{id_cliente}", response_model=PropostaResponse)
def read_propostas_contraparte(
    id_cliente: int,
    db: Session = Depends(deps.get_db),
) -> PropostaResponse:
    """
    Get PropostaContraparte by id_cliente.
    """
    def cap_limites_proposta(id_contraparte_list):
        limites_proposta = crud_limites_proposta.get_all_limites_proposta_id_contraparte(db, id_cliente, id_contraparte_list)
        if limites_proposta is None:
            limites_proposta_response = []
        else:
            limites_proposta_response = [
                LimitesPropostaResponse(
                    id=limites.id,
                    id_cliente=limites.id_cliente,
                    id_proposta=limites.id_proposta,
                    id_contraparte=limites.id_contraparte,
                    tipo_limite=limites.tipo_limite,
                    rating=limites.rating,
                    valor_limite=limites.valor_limite,
                    valor_carteira=limites.valor_carteira,
                    carteira_mwm=limites.carteira_mwm,
                )
                for limites in limites_proposta
            ]

        return limites_proposta_response

    def cap_observacoes_proposta(id_contraparte_list):
        observacoes_proposta = crud_observacoes_proposta.get_all_observacoes_propostaid_contraparte(db, id_cliente, id_contraparte_list)
        if observacoes_proposta is None:
            observacoes_proposta_response = []
        else:
            observacoes_proposta_response = [
                ObservacoesPropostaResponse(
                    id=observacoes.id,
                    id_cliente=observacoes.id_cliente,
                    id_proposta=observacoes.id_proposta,
                    id_contraparte=observacoes.id_contraparte,
                    tipo_observacao=observacoes.tipo_observacao,
                    observacao_vigente=observacoes.observacao_vigente,
                    observacao_sugerido=observacoes.observacao_sugerido,
                    observacao_aprovado=observacoes.observacao_aprovado,
                )
                for observacoes in observacoes_proposta
            ]
        return observacoes_proposta_response

    propostas_contraparte_query = crud_propostas_contraparte.get_all_propostas_contraparte(db, id_cliente)
    if propostas_contraparte_query is None:
        propostas_contraparte_response = []
    else:
        propostas_contraparte_response = [
            PropostaResponseBase(
                id=contraparte.id,
                data_aprovacao_limite= contraparte.data_aprovacao_limite,
                grupo= contraparte.grupo,
                tipo_limite= contraparte.tipo_limite,
                data_proposta= contraparte.data_proposta,
                tipo_analise= contraparte.tipo_analise,
                status= contraparte.status,
                valor_utilizado_conversao= contraparte.valor_utilizado_conversao,
                proposta_response= cap_limites_proposta(contraparte.id),
                observacoes_proposta= cap_observacoes_proposta(contraparte.id),
            )
            for contraparte in propostas_contraparte_query

        ]


    cliente = crud_cliente.get_cliente(db, id_cliente)
    if cliente is None:
        raise HTTPException(status_code=404, detail="Cliente not found")


    res = PropostaResponse(id_cliente=id_cliente, propostas_contraparte=propostas_contraparte_response)

    return res



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