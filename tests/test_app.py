from fastapi.testclient import TestClient

from fast_zero.app import app


def test_root_deve_retornar_200_e_ola_mundo():
    client = TestClient(app)

    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'Olá Mundo!'}


def test_ola_html_retornar_200_e_html_com_ola_mundo():
    client = TestClient(app)

    response = client.get('/html')
    assert response.status_code == 200
    assert (
        response.text
        == """
    <html>
        <head>
            <title> Nosso olá mundo!</title>
        </head>
        <body>
            <h1> Olá Mundo </h1>
        </body>
    </html>"""
    )
