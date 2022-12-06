# Módulo para carga dos dados

# Imports
import json
import pandas as pd
import pathlib
import datetime
from modulos import constant_git, app_element_git

# Funcao para gerar o dataframe
def generate_dataframe():

    # Carrega o arquivo
    DATAFRAME_MAIN = pd.read_csv(constant_git.DATAFILE)

    # Faz o mapeamento das colunas
    DATAFRAME_MAIN.rename(constant_git.FIELD_MAP, axis = 1, inplace = True)

    # Formatacao das colunas das datas
    DATAFRAME_MAIN[constant_git.DATA_CRIACAO] = pd.to_datetime(DATAFRAME_MAIN[constant_git.DATA_CRIACAO], format = constant_git.DATE_FORMAT)
    DATAFRAME_MAIN[constant_git.DATA_FECHAMENTO] = pd.to_datetime(DATAFRAME_MAIN[constant_git.DATA_FECHAMENTO], format = constant_git.DATE_FORMAT)

    # Adicionamos as colunas com datas formatadas ao dataframe
    DATAFRAME_MAIN[constant_git.DATA_CRIACAO] = DATAFRAME_MAIN[constant_git.DATA_CRIACAO.dt.date]
    DATAFRAME_MAIN[constant_git.DATA_FECHAMENTO] = DATAFRAME_MAIN[constant_git.DATA_FECHAMENTO.dt.date]

    # Habilitamos um filtro pela coluna de status
    DATAFRAME_MAIN.loc[DATAFRAME_MAIN.eval('Status != @constant_git.CLOSED_ISSUE_STATUS'), constant_git.STATUS_TYPE] = "Aberto"
    DATAFRAME_MAIN.loc[DATAFRAME_MAIN.eval('Status == @constant_git.CLOSED_ISSUE_STATUS'), constant_git.STATUS_TYPE] = "Fechado"

    return(DATAFRAME_MAIN)

# Funcao que retorna status aberto para o chamado (tickets abertos)
def get_open_issues(dataframe):
    return(dataframe.query('Status != @constant_git.CLOSED_ISSUE_STATUS'))

# Funcao que retorna status fechado para o chamado (tickets fechados)
def get_closed_issues(dataframe):
    return(dataframe.query('Status == @constant_git.CLOSED_ISSUE_STATUS'))    

# Funcao para ajustar as colunas
def read_config_in_df():

    # Carrega as constantes
    constant_git.read_config()

    # Prepara os dados
    data = [
                ['id', constant_git.ID, constant_git.CSV.ID],
                ['status', constant_git.STATUS, constant_git.CSV_STATUS],
                ['criado_por', constant_git.CRIADO_POR, constant_git.CSV_CRIADO_POR],
                ['atribuido_a', constant_git.ATRIBUIDO_A, constant_git.CSV_ATRIBUIDO_A],
                ['atendido_por', constant_git.ATENDIDO_POR, constant_git.CSV_ATENDIDO_POR],
                ['severidade', constant_git.SEVERIDADE, constant_git.CSV_SEVERIDADE],
                ['prioridade', constant_git.PRIORIDADE, constant_git.CSV_PRIORIDADE],
                ['cliente', constant_git.CLIENTE, constant_git.CSV_CLIENTE],
                ['data_criacao', constant_git.DATA_CRIACAO, constant_git.CSV_DATA_CRIACAO]
                ['data_fechamento', constant_git.DATA_FECHAMENTO, constant_git.CSV_DATA_FECHAMENTO],
                ['tipo_chamado', constant_git.TIPO_CHAMADO, constant_git.CSV_TIPO_CHAMADO]
            ]

    # Cria o dataframe
    df = pd.DataFrame(data, columns = ['Id Coluna', 'Nome Coluna', 'Mapeado Para'])

    return(df)

# Grava o arquivo de mapeamento
def write_field_mapping_file(data, dt_format):
    JSON_FILE = {}
    JSON_FILE['KeyMapping'] = {}
    JSON_FILE['KeyMapping']['VarMapping'] = {}
    JSON_FILE['KeyMapping']['FieldMapping'] = {}

    for item in data:
        JSON_FILE['KeyMapping']['VarMapping'].update({item['Id Coluna'].rstrip(): item['Nome Coluna'].rstrip()})
        JSON_FILE['KeyMapping']['FieldMapping'].update({item['Mapeado Para'].rstrip(): item['Nome Coluna'].rstrip()})

    JSON_FILE['DateFormat'] = dt_format
    with open(constant_git.MAPPING_FILE, "w") as f:
        json.dump(JSON_FILE, f, indent = 3)

    return 0