from project.api_call.likesApi import LikesApi


def is_profile_photo_liked(account_id, user):
    photo_id = user.photo_id.split('_')[1]
    return True if LikesApi(account_id).is_liked(user_id=user.user_id, item_id_obj=photo_id)[0] == 1 else False


def add_like_to_profile_photo(account_id, user):
    if not is_profile_photo_liked(account_id=account_id, user=user):
        photo_id = user.photo_id.split('_')[1]
        LikesApi(account_id).add(owner_id=user.user_id, item_id_obj=photo_id)
        return True
    return False
