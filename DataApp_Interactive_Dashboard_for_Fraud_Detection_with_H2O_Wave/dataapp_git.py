# Arquivo principal do nosso programa

# Importacao das bibliotecas/pacotes
import dash
import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

# Carrega o arquivo de conexao da app
from app_A import app_A
from app_A import server

# Conecta aos modulos de paginas e outros modulos
from paginas import dashboard_A, overview_A, settings_A
from modulos import navbar_A, constant_A

# Carregando as configuracoes
CONFIG_OBJECT = constant_A.read_config()

# Configura uma divisao de uma area do dashboard para acomodar um conteudo
content = html.Div(id = "page-content", style = constant_A.CONTENT_STYLE, className = "p-3 pt-4 pb-3")


# Configura o layout
app_A.layout = html.Div([dcc.Location(id = "url"), navbar_A.layout, content])

# Callback contendo as funcoes para carregar cada uma das paginas
@app_A.callback(Output('page-content', 'children'), [Input('url', 'pathname')])
def display_page(pathname):
	if pathname == '/paginas/dashboard_A' or pathname == '/':
		return dashboard_A.get_layout()
	elif pathname == '/paginas/overview_A':
		return overview_A.get_layout()
	elif pathname == '/paginas/settings_A':
		return settings_A.get_layout()
	else:
		return dbc.Jumbotron(
			[
				html.Div([
					html.H1("404: Not Found", className = "text-danger"),
					html.Hr(),
					html.P(f"Pagina {pathname} nao encontrada...")
				],
				style = constant_A.NAVITEM_STYLE)
			]
		)

# Titulo
app_A.title = 'Data App - Dashboard Interativo para Analise de Chamados de Suporte'

# Executor do programa
if __name__ == '__main__':
	app_A.run_server(debug = False, port = 3000, host = '127.0.0.2', threaded = True)