from sqlalchemy import select

from fast_zero.models import User


def test_create_user(session):
    new_user = User(username='alice', password='secret', email='teste@test')
    # Unit of Work
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'alice'))
    # session.refresh(new_user)

    assert user.username == 'alice'
