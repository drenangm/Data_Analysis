# Módulo para a barra de navegação

# Imports
import dash_html_components as html
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output, State

# Modulos Customizados
from app_git import app_git
from modulos import constant_git

layout = dbc.Container(
        [
            dbc.Row([
                dbc.Col([
                    html.A(
                        dbc.Row(
                            [
                                dbc.Col(html.Img(src = app_git.get_asset_url(constant_git.APP_LOGO), height = "30px"), className = "col-md-2"),
                                dbc.Col(dbc.NavbarBrand("Data App", className = "ml-1"), className = "col-md-2")
                            ],
                            align = "start",
                            no_gutters = True,
                            className = "p-3 pt-4 pb-3"
                        )
                    ),
                    html.Hr(),
                    dbc.Nav(
                        [
                            dbc.NavItem(dbc.NavLink("Home", href = "/paginas/dashboard"), style = constant_git.NAVITEM_STYLE),
                            dbc.NavItem(dbc.NavLink("Visao Geral", href = "/paginas/overview"), style = constant_git.NAVITEM_STYLE),
                            dbc.NavItem(dbc.NavLink("Help", href = "/paginas/help"), style = constant_git.NAVITEM_STYLE),
                            dbc.NavItem(dbc.NavLink("Configuracoes", href = "/paginas/settings"), className = "p-3 align-bottom", style = {"margin-top": "100%"})
                        ],
                        className = "h-100",
                        navbar = True,
                        pills = True,
                        vertical = True
                    ),
                ],
                className = "h-100")
            ],
            className = "h-100")
        ],
        style = constant_git.SIDEBAR_STYLE,
        fluid = True,
        className = "bg-dark text-white"
    )