import os
from datetime import datetime

def health():
    vdate = datetime.now()
    return {
        'status': 'ok',
        'time': vdate.isoformat(),
        'alive': True
    }
