from dash import Dash

from src.layout import serve_layout

app = Dash(__name__)
app.title = "Patent Intelligence"
app.layout = serve_layout()

if __name__ == "__main__":
    app.run(debug=True, port=8050)
