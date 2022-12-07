# Script de criação do dashboard
# https://dash.plotly.com/dash-html-components

# Imports
import traceback
import pandas as pd
import plotly.express as px
import dash_core_components as dcc
import dash_bootstrap_components as dbc
import dash_html_components as html
from dash.dependencies import Input, Output

# Modulos customizados para os usarios
from app_git import app_git
from modulos import data_operations_git, constant_git

# Funcao que gera o layout da pagina
def get_layout():

    try:

        # Carrega os dados
        df_issues = data_operations_git.generate_dataframe()

        # Agrupa os dados
        df1 = df_issues.groupby([constant_git.STATUS])[constant_git.ID].count().reset_index(name = "Total Chamados")
        grp = df_issues.groupby([constant_git.DATA_CRIACAO, constant_git.TIPO_CHAMADO])[constant_git.ID]
        df2 = grp.count().reset_index(name = "Total Chamados")
        df3 = df_issues.groupby([constant_git.PRIORIDADE])[constant_git.ID].count().reset_index(name = "Total Chamados")

        # Geracao do container para acomodar os graficos
        layout = dbc.Container([
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id = 'my-line',
                                      figure = px.line(df2,
                                                       x = constant_git.DATA_CRIACAO,
                                                       y = 'Total Chamados',
                                                       color = constant_git.TIPO_CHAMADO,
                                                       title = 'Chamados de Suporte por Data de Criaca'))
                        ],
                        width = 12)
                    ],
                    style = {'padding-bottom': '10px'},
                    no_gutters = True),
                    dbc.Row([
                        dbc.Col([
                            dcc.Graph(id = 'my-pie2',
                                      figure = px.pie(df3,
                                                      values = 'Total Chamados',
                                                      names = constant_git.PRIORIDADE,
                                                      title = 'Chamados de Suporte por Prioridade',
                                                      hole = 0.3))
                        ],
                        width = 6),
                        dbc.Col([
                            dcc.Graph(id = 'my-pie',
                                      figure = px.pie(df1,
                                                      values = 'Total Chamados',
                                                      names = constant_git.STATUS,
                                                      title = 'Chamados de Suporte por Status'))
                        ],
                        width = 6),
                    ],
                    style = {'padding-bottom': '10px'},
                    no_gutters = True)
                ],
                fluid = True)
        return layout
    except:
        layout = dbc.Jumbotron(
                    [
                        html.Div([
                            html.H1("500: Internal Server Error", className = "text-danger"),
                            html.Hr(),
                            html.P(f"Following Exception Ocurred: "),
                            html.Code(traceback.format_exc())
                        ],
                        style = constant_git.NAVITEM_STYLE)
                    ]
                )
        return layout
