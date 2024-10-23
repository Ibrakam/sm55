from database.models import User
from database import get_db


# Функция для регистрациия пользователя
def register_user_db(username, phone_number, password,
                     email, user_city=None, birthday=None):
    with next(get_db()) as db:
        new_user = User(username=username, phone_number=phone_number,
                        email=email, password=password, user_city=user_city,
                        birthday=birthday)
        db.add(new_user)
        db.commit()
        return True


# Функция для получения всех пользователей
def get_all_users_db():
    with next(get_db()) as db:
        all_users = db.query(User).all()
        return all_users


# Функция для получения определенного пользователя
def get_exact_user_db(user_id):
    with next(get_db()) as db:
        exact_user = db.query(User).filter_by(id=user_id).first()
        return exact_user


# Функция для удаления
def delete_user_db(user_id):
    with next(get_db()) as db:
        db.query(User).filter_by(id=user_id).delete()
        db.commit()
        return True


# Функция для изменения
def update_user_db(user_id, change_info, new_info):
    with next(get_db()) as db:
        exact_user = db.query(User).filter_by(id=user_id).first()
        if exact_user:
            if change_info == "username":
                exact_user.username = new_info
            elif change_info == "email":
                exact_user.email = new_info
            elif change_info == "phone_number":
                exact_user.phone_number = new_info
            elif change_info == "password":
                exact_user.password = new_info
            elif change_info == "user_city":
                exact_user.user_city = new_info
            elif change_info == "birthday":
                exact_user.birthday = new_info
            db.commit()
            return True
        return False


