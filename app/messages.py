"""Friendly messsages"""

from fastapi import APIRouter
import json

router = APIRouter()


@router.get('/hello')
async def hello():
    """Returns a friendly greeting 👋"""
    
    message = "How you doin?"
    
    value = {
        "messsage": message
        }

    return json.dumps(value)
    pass