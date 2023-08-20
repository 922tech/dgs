from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordRequestForm
from datetime import  timedelta 
from server.utils.auth import authenticate, create_access_token, get_password, get_current_user
from server.settings import ACCESS_TOKEN_EXPIRE_MINUTES
from server.models.auth import User, Token


router = APIRouter(prefix='/login')


@router.post('/token', response_model=Token)
async def login_for_access_token(form_data:OAuth2PasswordRequestForm = Depends()):
    user = await authenticate(form_data.username, form_data.password)
    if not user:
        raise  HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                           detail='Could not validate cridentials',
                                           headers={"WWW-Authenticate":"Bearer"})
    
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={'sub':user.username}, expire_delta=access_token_expires)
    return {
        'access_token': access_token,
        'token_type':'bearer'
    }


@router.post('/signup/',status_code=status.HTTP_201_CREATED, tags=['Regiateration'])
async def signup(user:User):
    user.password = get_password(user.password)
    await user.insert()
    return {'response':f'user {user} registered successfully'}