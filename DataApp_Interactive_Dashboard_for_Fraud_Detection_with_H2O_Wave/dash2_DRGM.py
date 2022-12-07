# Mini-Projeto 3 - Data App - Dashboard Interativo Para Detecção de Fraudes com H2O Wave

# Importacao dos pacotes
import h2o
import random
import numpy as np
import pandas as pd
from h2o_wave import Q, main, app, ui, site, data
import matplotlib.pyplot as plt

# Funcao para carregamento dos dados
def carrega_dados():
	dados = pd.read_csv('dados/application_data.csv')
	return dados

# Carrega os dados
dataset = carrega_dados()

# Define a pagina da aplicacao (dashboard)
page = site['/dashboard']

############################################################################################################################

# Cabecalho do dashboard
card = page.add('header', ui.header_card(box = '1 1 9 2',
										 title = 'Data App - Dashboard Interativo para Deteccao de Fraudes com H2O Wave',
										 subtitle = 'Mini-Projeto 3',
										 icon = 'ExploreData'))


############################################################################################################################

# Gráfico de Total de Rendimentos Por Tipo de Rendimento e Gênero (Gráfico de Barras)
# https://wave.h2o.ai/docs/layout

# Preparamos os dados contidos no dataset completo
# Selecionamos as colunas que farao parte deste grafico
df_bar = dataset.loc[:200,['NAME_INCOME_TYPE', 'AMT_INCOME_TOTAL', 'CODE_GENDER']]

# Grafico 1
grafico1 = page.add('bar_plot', ui.plot_card(box = '1 3 4 4', 
									         title = 'Total de Rendimentos Por Tipo de Rendimento e Gênero',
									         data = data(fields = df_bar.columns.tolist(), rows = df_bar.values.tolist()),
									         plot = ui.plot(marks = [ui.mark(type = 'interval', 
									  								         x = '=NAME_INCOME_TYPE', 
									  								         y = '=AMT_INCOME_TOTAL',
									  								         color = '=CODE_GENDER', 
									  								         dodge = 'auto')])))

############################################################################################################################

# Grafico de clientes por Escolaridade (Grafico de Dispersao)

# Preparacao dos dados
df_point = dataset.loc[:200,['DAYS_REGISTRATION', 'DAYS_ID_PUBLISH', 'NAME_EDUCATION_TYPE']]

# Grafico - box = '1 3 5 2'
grafico2 = page.add('point_plot', ui.plot_card(box = '5 3 5 2',
											   title = 'Clientes por Escolaridade',
											   data = data(fields = df_point.columns.tolist(), rows = df_point.values.tolist()),
											   plot = ui.plot([ui.mark(type = 'point',
											   						   x = '=DAYS_REGISTRATION',
											   						   y = '=DAYS_ID_PUBLISH',
											   						   color = 'NAME_EDUCATION_TYPE')])))

############################################################################################################################

# Grafico de Total de Rendimentos por Total de Credito (Grafico de Bolhas)

# Preparacao dos dados
df_point_sized = dataset.loc[:200,['AMT_INCOME_TOTAL', 'AMT_CREDIT', 'AMT_ANNUITY']]

# Grafico
grafico3 = page.add('point_plot_sized', ui.plot_card(box = '5 5 5 2',
											   		 title = 'Total de Rendimentos por Total de Credito',
											   		 data = data(fields = df_point_sized.columns.tolist(), rows = df_point_sized.values.tolist()),
											   		 plot = ui.plot([ui.mark(type = 'point',
											   						   		 x = '=AMT_INCOME_TOTAL',
											   						   		 y = '=AMT_CREDIT',
											   						   		 size = '=AMT_ANNUITY')])))

############################################################################################################################

# Gráfico de Total de Rendimentos Por Tipo de Rendimento e Status Familiar (Gráfico de Barras Empilhado)

# Prepara os dados
df_bar_stacked = dataset.loc[:200,['AMT_INCOME_TOTAL', 'NAME_INCOME_TYPE', 'NAME_FAMILY_STATUS']]

# Gráfico
grafico4 = page.add('df_bar_stacked', ui.plot_card(box = '1 7 9 4',
											       title = 'Total de Rendimentos Por Tipo de Rendimento e Status Familiar',
											       data = data(fields = df_bar_stacked.columns.tolist(), rows = df_bar_stacked.values.tolist()),
											       plot = ui.plot(marks = [ui.mark(type = 'interval', 
																			       x = '=NAME_INCOME_TYPE', 
																			       y = '=AMT_INCOME_TOTAL',
																			       color = '=NAME_FAMILY_STATUS', 
																			       stack = 'auto')])))

#######################################################################################################################

# Gráfico de Total de Rendimentos Por Tipo de Empréstimo (Gráfico de Linha)

# Prepara os dados
df_line = dataset.loc[:200,['SK_ID_CURR', 'AMT_INCOME_TOTAL']]

# Gráfico
grafico5 = page.add('df_line', ui.plot_card(box = '1 11 5 4',
	                                        title = 'Total de Rendimentos Por Tipo de Empréstimo',
											data = data(fields=df_line.columns.tolist(), rows = df_line.values.tolist()),
											plot = ui.plot(marks = [ui.mark(type = 'line', 
																		    x = '=SK_ID_CURR', 
																		    y = '=AMT_INCOME_TOTAL', 
																		    curve = 'smooth')])))

#######################################################################################################################

# Gráfico de Total de Rendimentos Por Tipo de Rendimento e Estado Civil (Gráfico de Área)

# Prepara os dados
df_area = dataset.loc[:200,['AMT_INCOME_TOTAL','NAME_EDUCATION_TYPE','NAME_FAMILY_STATUS']]

# Gráfico
grafico6 = page.add('df_area', ui.plot_card(box = '6 11 4 4',
									        title = 'Total de Rendimentos Por Tipo de Rendimento e Estado Civil',
									        data = data(fields = df_area.columns.tolist(), rows = df_area.values.tolist()),
									        plot = ui.plot(marks = [ui.mark(type = 'area',
									 								        x = '=NAME_EDUCATION_TYPE', 
									 								        y = '=AMT_INCOME_TOTAL',
									 								        color = '=NAME_FAMILY_STATUS')])))

#######################################################################################################################

# Gráfico de Total de Rendimentos Por Tipo de Empréstimo (Gráfico de Linha Step)

# Prepara os dados
df_line_step = dataset.loc[:100,['SK_ID_CURR', 'AMT_INCOME_TOTAL']]

# Gráfico
grafico7 = page.add('df_line_step', ui.plot_card(box = '1 15 5 4',
	                                           title = 'Total de Rendimentos Por Tipo de Empréstimo (Step)',
    										   data = data(fields = df_line_step.columns.tolist(), rows = df_line_step.values.tolist()),
											   plot=ui.plot([ui.mark(type = 'path', 
											   	                     x = '=SK_ID_CURR', 
											   	                     y = '=AMT_INCOME_TOTAL', 
											   	                     curve = 'step' )])))

#######################################################################################################################

# Gráfico de Total de Rendimentos Por Tipo de Residência (Gráfico de Barras)

# Prepara os dados
df_b = dataset.loc[:200,['AMT_INCOME_TOTAL', 'NAME_HOUSING_TYPE']]

# Gráfico
grafico8 = page.add('df_b', ui.plot_card(box = '6 15 4 4',
										 title = 'Total de Rendimentos Por Tipo de Residência',
										 data = data(fields = df_b.columns.tolist(), rows = df_b.values.tolist()),
										 plot = ui.plot([ui.mark(type = 'interval', 
										 	                     x = '=NAME_HOUSING_TYPE', 
										 	                     y = '=AMT_INCOME_TOTAL' )])))

page.save()

 