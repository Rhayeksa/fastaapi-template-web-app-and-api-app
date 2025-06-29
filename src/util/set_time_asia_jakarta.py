from datetime import datetime

import pytz
import tzlocal


async def set_time_asia_jakarta():
    tz = None
    if tzlocal.get_localzone_name() != "Asia/Jakarta":
        tz = pytz.timezone("Asia/Jakarta")
    return datetime.now(tz).replace(tzinfo=None)
