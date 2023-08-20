from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from datetime import  timedelta , datetime
from jose import JWTError, jwt
from passlib.context import CryptContext
from server.models.auth import UserInDB, TokenData, User
import server.settings as settings


pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_scheme =  OAuth2PasswordBearer(tokenUrl=settings.TOKEN_URL)



def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)


def get_password(password):
    return pwd_context.hash(password)


async def get_user(username:str):
    user = await User.find_user(username)
    if user is not None:
        user_data = user.dict()
        return UserInDB(**user_data)
    

async def authenticate(username: str, password:str):
    user = await get_user(username)

    if not user:
        return False
    
    elif not verify_password(password, user.password):
        return False
    
    else:
        return user


def create_access_token(data:dict, expire_delta:timedelta or None = None):
    to_encode  = data.copy()
    if expire_delta:
        expire =  datetime.utcnow() + expire_delta
    else:
        expire = datetime.utcnow() + timedelta(minutes=15)
    to_encode.update({'exp':expire})
    encoded_jwt = jwt.encode(to_encode, settings.SECRET_KEY, algorithm=settings.ALGORITHM)
    return encoded_jwt


async def get_current_user(token:str = Depends(oauth2_scheme)):

    credentials_exception = HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
                                           detail='Could not validate cridentials',
                                           headers={"WWW-Authenticate":"Bearer"})
    
    try:
        payload = jwt.decode(token, settings.SECRET_KEY, algorithms=settings.ALGORITHM)
        username: str = payload.get('sub')

        if username is None:
            raise credentials_exception
        
        token_data = TokenData(username=username)
    except JWTError:
        raise credentials_exception
    
    user = await get_user(db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return user


async def get_current_active_user(current_user: UserInDB = Depends(get_current_user)):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail = "Inactive user")
    return current_user

