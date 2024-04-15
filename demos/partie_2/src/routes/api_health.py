from fastapi import APIRouter

from utils.health import health

router = APIRouter()

@router.get("")
def get_health():
    return health()

@router.post("")
def post_health():
    return health()
