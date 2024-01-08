from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.api import deps
from app.crud import crud_configuracao_cliente as crud
from app.crud import crud_cliente, crud_aprovadores_cliente, crud_tipos_rating_cliente, crud_alcadas_cliente
from app.schemas.configuracao_cliente import ConfiguracaoCliente, ConfiguracaoClienteCreate
from app.schemas.cliente import ClienteResponse, AprovadoresClienteResponse, TiposRatingClienteResponse, AlcadasClienteResponse
from typing import List, Any

router = APIRouter()


@router.get("/", response_model=List[ConfiguracaoCliente])
def read_configuracoes_cliente(
        db: Session = Depends(deps.get_db),
        skip: int = 0,
        limit: int = 100,
) -> Any:
    configuracoes_cliente = crud.get_multi_configuracao_cliente(db, skip=skip, limit=limit)
    return configuracoes_cliente


@router.get("/{id_cliente}", response_model=ClienteResponse)
def read_configuracao_cliente(
    id_cliente: int,
    db: Session = Depends(deps.get_db),
) -> ClienteResponse:
    """
    Get ConfiguracaoCliente by ID.
    """
    get_configuracao_cliente = crud.get_configuracao_cliente(db, id_cliente)
    if get_configuracao_cliente is None:
        raise HTTPException(status_code=404, detail="ConfiguracaoCliente not found")

    configuracao_cliente = crud.get_configuracao_cliente_join(db, id_cliente)
    if configuracao_cliente is None:
        raise HTTPException(status_code=404, detail="ConfiguracaoCliente not found")

    aprovadores_cliente = crud_aprovadores_cliente.get_all_aprovadores_cliente(db, id_cliente)
    if aprovadores_cliente is None:
        aprovadores_cliente_response = []
    else:
        aprovadores_cliente_response = [
            AprovadoresClienteResponse(
                cargo_aprovador=aprovador.cargo_aprovador,
                login_aprovador=aprovador.login_aprovador,
                perfil_aprovador=aprovador.perfil_aprovador,
                percentual_peso_aprovador=aprovador.percentual_peso_aprovador,
            )
            for aprovador in aprovadores_cliente
        ]


    tipos_rating_cliente = crud_tipos_rating_cliente.get_all_tipos_rating_cliente(db, id_cliente)
    if tipos_rating_cliente is None:
        tipos_rating_clienteResponse = []
    else:
        tipos_rating_clienteResponse = [
            TiposRatingClienteResponse(
                codigo_rating=tiposratingcliente.codigo_rating,
                descricao_rating=tiposratingcliente.descricao_rating,
                prob_default_inicial=tiposratingcliente.prob_default_inicial,
                prob_default_final=tiposratingcliente.prob_default_final,
            )
            for tiposratingcliente in tipos_rating_cliente
        ]

    alcadas_cliente = crud_alcadas_cliente.get_all_alcadas_cliente(db, id_cliente)
    if alcadas_cliente is None:
        alcadas_cliente_response = []
    else:
        alcadas_cliente_response = [
            AlcadasClienteResponse(
                limite_minimo_aprovacao=alcadascliente.limite_minimo_aprovacao,
                limite_maximo_aprovacao=alcadascliente.limite_maximo_aprovacao,
                perfil_aprovador=alcadascliente.perfil_aprovador,
                percentual_aprovacao=alcadascliente.percentual_aprovacao,
            )
            for alcadascliente in alcadas_cliente
        ]

    retorn_all = ClienteResponse(
        id=id_cliente,
        configuracao_cliente={
            "id_tipo_limite":get_configuracao_cliente.id_tipo_limite,
            "id_limite":get_configuracao_cliente.id_limite,
            "id_input_carteira":get_configuracao_cliente.id_input_carteira,
            "id_conversao":get_configuracao_cliente.id_conversao,
            "valor_base_proprietaria":get_configuracao_cliente.valor_base_proprietaria,
            "qtd_dias_validade_analise":get_configuracao_cliente.qtd_dias_validade_analise,
            "qtd_dias_intervalo_minimo_aprovacoes":get_configuracao_cliente.qtd_dias_intervalo_minimo_aprovacoes,
            "qtd_dias_intervalo_maximo_aprovacoes":get_configuracao_cliente.qtd_dias_intervalo_maximo_aprovacoes,
            "aprovadores_cliente": aprovadores_cliente_response,
            "tipos_rating_cliente": tipos_rating_clienteResponse,
            "alcadas_cliente":alcadas_cliente_response,
        })
    return retorn_all


@router.post("/", response_model=ConfiguracaoCliente)
def create_configuracao_cliente(
        *,
        db: Session = Depends(deps.get_db),
        configuracao_cliente_in: ConfiguracaoClienteCreate,
) -> Any:
    """
    Create ConfiguracaoCliente.
    """
    cliente = crud_cliente.get_cliente(db, id=configuracao_cliente_in.id_cliente)
    if not cliente:
        raise HTTPException(status_code=404, detail="Cliente not found")
    existing_configuracao = crud.get_configuracao_cliente_by_cliente_id(db, cliente_id=configuracao_cliente_in.id_cliente)
    if existing_configuracao:
        raise HTTPException(status_code=400, detail="A ClientConfiguration already exists for this client")
    configuracao_cliente = crud.create_configuracao_cliente(db, obj_in=configuracao_cliente_in)
    return configuracao_cliente


@router.put("/{id_cliente}", response_model=ConfiguracaoCliente)
def update_configuracao_cliente(
        id_cliente: int,
        *,
        db: Session = Depends(deps.get_db),
        id_tipo_limite: int,
        id_limite: int,
        id_input_carteira: int,
        id_conversao: int,
        valor_base_proprietaria: float,
        qtd_dias_validade_analise: int,
        qtd_dias_intervalo_minimo_aprovacoes: int,
        qtd_dias_intervalo_maximo_aprovacoes: int,
) -> Any:
    """
    Update ConfiguracaoCliente by ID.
    """
    configuracao_cliente_data = {
        "id_tipo_limite": id_tipo_limite,
        "id_limite": id_limite,
        "id_input_carteira": id_input_carteira,
        "id_conversao": id_conversao,
        "valor_base_proprietaria": valor_base_proprietaria,
        "qtd_dias_validade_analise": qtd_dias_validade_analise,
        "qtd_dias_intervalo_minimo_aprovacoes": qtd_dias_intervalo_minimo_aprovacoes,
        "qtd_dias_intervalo_maximo_aprovacoes": qtd_dias_intervalo_maximo_aprovacoes,
    }

    configuracao_cliente_in_db = crud.get_configuracao_cliente(db, id_cliente)
    if configuracao_cliente_in_db is None:
        raise HTTPException(status_code=404, detail="ConfiguracaoCliente not found")



    configuracao_cliente_updated = crud.update_configuracao_cliente(
        db, db_obj=configuracao_cliente_in_db, obj_in=configuracao_cliente_data
    )
    return configuracao_cliente_updated


@router.delete("/{id_cliente}", response_model=dict)
def delete_configuracao_cliente(
        id_cliente: int,
        db: Session = Depends(deps.get_db),
) -> Any:
    """
    Delete ConfiguracaoCliente by ID.
    """
    configuracao_cliente_in_db = crud.get_configuracao_cliente(db, id_cliente)
    if configuracao_cliente_in_db is None:
        raise HTTPException(status_code=404, detail="ConfiguracaoCliente not found")

    crud.delete_configuracao_cliente(db, configuracao_cliente_in_db)

    return {"message": "ConfiguracaoCliente deleted successfully"}