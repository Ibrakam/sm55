from database.models import UserPost, Comment, Hashtag, PostPhoto
from database import get_db


def register_user_post_db(user_id, main_text, hashtags):
    with next(get_db()) as db:
        new_user_post = UserPost(user_id=user_id, main_text=main_text, hashtags=hashtags)
        db.add(new_user_post)
        db.commit()
        return True


def get_all_users_posts_db():
    with next(get_db()) as db:
        all_user_post = db.query(UserPost).all()
        return all_user_post


def get_exact_user_post_db(user_id):
    with next(get_db()) as db:
        exact_user_post = db.query(UserPost).filter_by(user_id=user_id).all()
        if exact_user_post:
            return exact_user_post
        return False


def get_exact_post_db(post_id):
    with next(get_db()) as db:
        exact_user_post = db.query(UserPost).filter_by(id=post_id).first()
        if exact_user_post:
            return exact_user_post
        return False


def delete_exact_post_db(post_id):
    with next(get_db()) as db:
        ex_del_user_post = db.delete(UserPost).filter_by(id=post_id).first()
        if ex_del_user_post:
            return ex_del_user_post
        return False


def update_user_post_db(post_id, change_info, new_info):
    with next(get_db()) as db:
        exact_com = db.query(UserPost).filter_by(id=post_id).first()
        if exact_com:
            if change_info == "main_text":
                exact_com.main_text = new_info
            elif change_info == "hashtags":
                exact_com.hashtags = new_info
            db.commit()
            return True
        return False


###################################################################

def register_coment_db(user_id, post_id, text):
    with next(get_db()) as db:
        new_comment = Comment(user_id=user_id, text=text, post_id=post_id)
        db.add(new_comment)
        db.commit()
        return True


def get_exact_coment_db(comment_id):
    with next(get_db()) as db:
        exact_com = db.query(Comment).filter_by(id=comment_id).first()
        if exact_com:
            return exact_com
        return False


def delete_exact_coment(comment_id):
    with next(get_db()) as db:
        ex_del_com = db.delete(Comment).filter_by(id=comment_id).first()
        if ex_del_com:
            return ex_del_com
        return False


def all_post_coment_db(post_id):
    with next(get_db()) as db:
        exact_coment = db.query(Comment).filter_by(id=post_id).all()
        if exact_coment:
            return exact_coment
        return False


def all_user_coment_db(user_id):
    with next(get_db()) as db:
        exact_coment = db.query(Comment).filter_by(user_id=user_id).all()
        if exact_coment:
            return exact_coment
        return False


def update_coment_db(comment_id, new_info):
    with next(get_db()) as db:
        exact_coment = db.query(Comment).filter_by(id=comment_id).first()
        if exact_coment:
            exact_coment.text = new_info
            db.commit()
            return True
        return False


def get_hashtag(hashtag):
    with next(get_db()) as db:
        hash = db.query(Hashtag).filter_by(id="#" + hashtag).first()
        if hash:
            return hash
        return False


def add_hashtag(hashtag):
    with next(get_db()) as db:
        hashtag1 = Hashtag(hashtag=hashtag)
        db.add(hashtag1)
        db.commit()
        return True


# def add_post_photo(post_id, photo_url):
#     with next(get_db()) as db:
#         photo = PostPhoto(post_id=post_id, photo_path=photo_url)
#         db.add(photo)
#         db.commit()
#         return True
