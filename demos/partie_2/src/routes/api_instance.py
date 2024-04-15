from fastapi import APIRouter, Response, BackgroundTasks

from schemas.Instance import Instance

from utils.pulumi import delete_resource, is_not_valid_field
from utils.size import is_not_valid_size, get_enum_value
from utils.provider import is_not_valid_provider
from utils.instance import new_instance
from utils.common import is_true

router = APIRouter()

@router.post("")
def create_instance(payload: Instance, response: Response, bt: BackgroundTasks):
    if is_not_valid_field(payload.name):
        response.status_code = 400
        return {
            'status': 'ko',
            'error': 'invalid project name'
        }

    if is_not_valid_field(payload.project):
        response.status_code = 400
        return {
            'status': 'ko',
            'error': 'invalid resource name'
        }

    if is_not_valid_size(payload.size):
        response.status_code = 400
        return {
            'status': 'ko',
            'error': 'invalid size'
        }

    if is_not_valid_provider(payload.provider):
        response.status_code = 400
        return {
            'status': 'ko',
            'error': 'invalid provider'
        }

    if payload.asynchronous:
        result = {
            'status': 'ok',
            'async': True
        }
        response.status_code = 202
        bt.add_task(new_instance, payload.name, payload.project, payload.region, payload.zone, get_enum_value(payload.size), payload.provider)
    else:
        result = new_instance(payload.name, payload.project, payload.region, payload.zone, get_enum_value(payload.size), payload.provider)
        response.status_code = 201 if is_true(result['status']) else 500
    return result

@router.delete("/{project}/{name}")
def delete_instance(project: str, name: str, response: Response, bt: BackgroundTasks):
    if is_not_valid_field(project):
        response.status_code = 400
        return {
            'status': 'ko',
            'error': 'invalid project name'
        }

    if is_not_valid_field(name):
        response.status_code = 400
        return {
            'status': 'ko',
            'error': 'invalid resource name'
        }

    bt.add_task(delete_resource, project, name)
    return {
        'status': 'ok',
        'async': True
    }
