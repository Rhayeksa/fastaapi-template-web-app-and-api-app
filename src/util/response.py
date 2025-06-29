from datetime import datetime
from http import HTTPStatus
from typing import Optional

# import numpy as np
from fastapi.encoders import jsonable_encoder
from fastapi.responses import JSONResponse

# from src.util.set_time_asia_jakarta import set_time_asia_jakarta


async def response(
    code: int,
    message: Optional[str] = None,
    page: Optional[dict] = None,
    data=None
):
    # start_time = await set_time_asia_jakarta()
    start_time = datetime.now()
    status = None
    try:
        code = HTTPStatus(code)
        status = code.phrase
    except Exception as e:
        print(f"\nError: {e}\n")
        message = str(e)
        data = None

    result = {
        "datetime": str(start_time),
        "status_code": code,
        "status": status,
        "message": message if message != None else status,
    }
    result.update({"page": page} if page != None else {})
    # result.update({"data": data.tolist() if isinstance(
    #     data, np.ndarray) else jsonable_encoder(data)})
    result.update({"data": jsonable_encoder(data)})
    # end_time = await set_time_asia_jakarta()
    # result.update({
    #     "time": {
    #         "time_start": str(start_time), "time_end": str(end_time), "time_response": str(end_time - start_time)
    #     }
    # })

    try:
        code = HTTPStatus(code)
    except:
        code = 500

    return JSONResponse(result, code)
