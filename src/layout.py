from dash import html


def serve_layout():
    return html.Div(
        [
            html.Header("Patent Intelligence Dashboard", className="app-header"),
            html.Div(
                [
                    html.Div(
                        "Bubble Chart Placeholder",
                        id="bubble-chart",
                        className="module",
                    ),
                    html.Div(
                        "Radar Chart Placeholder", id="radar-chart", className="module"
                    ),
                    html.Div(
                        "Document Viewer Placeholder",
                        id="doc-viewer",
                        className="module",
                    ),
                ],
                className="main-grid",
            ),
        ]
    )
