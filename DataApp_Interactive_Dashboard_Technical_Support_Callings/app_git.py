# Modulo de criacao do servidor Dash

# Importacao
import dash

# meta_tags sao necessarias para que o layout do aplicativo seja responsivo em dispositivos moveis
app_A = dash.Dash(__name__, suppress_callback_exceptions = True, meta_tags = [{'name': 'viewport', 'content': 'width=device-width, initial-scale=1.0'}])

# Cria o servidor
server = app_A.server