# app/core/deps.py

from fastapi import Header, HTTPException

FAKE_USERS = {
    "token-ava": {"name": "Ava", "role": "admin"},
    "token-leo": {"name": "Leo", "role": "student"},
}


def get_current_user(x_token: str = Header(...)):
    user = FAKE_USERS.get(x_token)

    if not user: 
        raise HTTPException(
            status_code=401, 
            detail="Invalid token"
        ) 

    return user