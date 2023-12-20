import os

unit_folder = os.path.dirname(__file__)


def mock_html(html_name: str) -> str:
    with open(os.path.join(unit_folder, f"mock/{html_name}.html")) as file:
        html = file.read()
    return html
