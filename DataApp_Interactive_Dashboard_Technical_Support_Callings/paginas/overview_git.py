# Página de overview

# Importacao
import traceback
import pandas as pd
import dash
import dash_table
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

# Modulos Customizados para os usuarios
from app_A import app_A
from modulos import app_element_A, data_operations_A, constant_A

# Funcao para obter o layout
def get_layout():

	try:

		# Preparacao do dataframe
		df = data_operations_A.generate_dataframe()
		df1 = df[[constant_A.ATRIBUIDO_A, constant_A.ID]]
		df1 = df1.groupby([constant_A.ATRIBUIDO_A])[constant_A.ID].count().reset_index(name = "Total")
		df2 = df[[constant_A.ATENDIDO_POR, constant_A.ID]]
		df2 = df2.groupby([constant_A.ATENDIDO_POR])[constant_A.ID].count().reset_index(name = "Total")

		# Layout
		layout = dbc.Container([
				 dbc.Row([
				 		dbc.Col([
				 		dbc.Card([dbc.CardHeader("Objetivo do Dashboard"),
				 				  dbc.CardBody([html.H2("Data App", className = "card-text")])], className = "shadow p-3 bg-light rounded")], width = 3),
				 		dbc.Col([
				 		dbc.Card([dbc.CardHeader("Numero de Chamados Analisados"),
				 				  dbc.CardBody([html.H2("300", className = "card-text")])], className = "sahdow p-3 bg-light rounded")], width = 3),
				 		dbc.Col([
				 		dbc.Card([dbc.CardHeader("Periodo de Coleta de Dados"),
				 				  dbc.CardBody([hmtl.H2("2020-2021", className = "card-text")])], className = "shadow p-3 bg-light rounded")], width = 3),
				 		dbc.Col([
				 		dbc.Card([dbc.CardHeader("Em Caso de Duvidas Envie E-mail Para:"),
				 				  dbc.CardBody([hmtl.H2("Suporte DSA", className = "card-text")])], className = "shadow p-3 bg-light rounded")], width = 3)],
				 		className = "pb-3"),
				 dbc.row([
				 		dbc.Col(dbc.Card([
				 				dbc.CardHeader(f"Total de Chamados Por {constant_A.ATRIBUIDO_A}"),
				 				app_element_A.generate_dashtable(identifier = "table1", dataframe = df1)],
				 				className = "shadow p-3 bg-light rounded"), width = 6),
				 		dbc.Col(dbc.Card([
				 				dbc.CardHeader(f"Total de Chamados Por {constant_A.ATENDIDO_POR}"),
				 				app_element_A.generate_dashtable(identifier = "table2", dataframe = df2)],
				 				className = "shadow p-3 bg-light rounded"), width = 6)
				])
		],
		fluid = True)

		return layout
	except:
		layout = dbc.Jumbotron(
					[
						html.Div([
							html.H1("500: Internal Server Error", className = "text-danger"),
							html.Hr(),
							html.P("O seguinte error ocorreu:"),
							html.Code(traceback.format_exc())
						],
						style = constant_A.NAVITEM_STYLE)
					]
				)
		return layout