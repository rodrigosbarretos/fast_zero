from http import HTTPStatus


def test_root_deve_retornar_200_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'message': 'Olá Mundo!'}


def test_ola_html_retornar_200_e_html_com_ola_mundo(client):
    response = client.get('/html')
    assert response.status_code == HTTPStatus.OK
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


# def test_create_user(client):
#     response = client.post(
#         '/users/',
#         json={
#             'username': 'alice',
#             'email': 'alice@example.com',
#             'password': 'secret',
#         },
#     )
#     assert response.status_code == HTTPStatus.CREATED
#     assert response.json() == {
#         'username': 'alice',
#         'email': 'alice@example.com',
#         'id': 1,
#     }


# def test_read_users(client):
#     response = client.get('/users/')
#     assert response.status_code == HTTPStatus.OK
#     assert response.json() == {
#         'users': [
#             {
#                 'username': 'alice',
#                 'email': 'alice@example.com',
#                 'id': 1,
#             }
#         ]
#     }


# def test_update_user(client):
#     response = client.put(
#         '/users/1',
#         json={
#             'username': 'bob',
#             'email': 'bob@example.com',
#             'password': 'mynewpassword',
#         },
#     )
#     assert response.status_code == HTTPStatus.OK
#     assert response.json() == {
#         'username': 'bob',
#         'email': 'bob@example.com',
#         'id': 1,
#     }


# def test_update_user_error(client):
#     response = client.put(
#         '/users/2',
#         json={
#             'username': 'bob',
#             'email': 'bob@example.com',
#             'password': 'mynewpassword',
#         },
#     )
#     assert response.status_code == HTTPStatus.NOT_FOUND
#     assert response.json() == {'detail': 'User not found'}


# def test_read_user(client):
#     response = client.get('/users/1')

#     assert response.status_code == HTTPStatus.OK
#     assert response.json() == {
#         'username': 'bob',
#         'email': 'bob@example.com',
#         'id': 1,
#     }


# def test_read_user_error(client):
#     response = client.get('/users/2')

#     assert response.status_code == HTTPStatus.NOT_FOUND
#     assert response.json() == {'detail': 'User not found'}


# def test_delete_user(client):
#     response = client.delete('/users/1')

#     assert response.status_code == HTTPStatus.OK
#     assert response.json() == {'message': 'User deleted'}


# def test_delete_user_error(client):
#     response = client.delete('/users/2')

#     assert response.status_code == HTTPStatus.NOT_FOUND
#     assert response.json() == {'detail': 'User not found'}
