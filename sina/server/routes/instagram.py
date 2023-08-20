from fastapi import APIRouter
from server.utils.instagram import InstagramUser

router = APIRouter(prefix='/instagram')


@router.get('/')
def get_folloews():

    user = InstagramUser()
    followers = user.find_user()

    return {
        'followers': followers
    }