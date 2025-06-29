from datetime import datetime

import pytz
import tzlocal


# async def convert_time_to_asia_jakarta(date_time: datetime) -> datetime:
async def convert_time_to_asia_jakarta(dt: datetime) -> datetime:
    # # tz = None
    # if tzlocal.get_localzone_name() != "Asia/Jakarta":
    #     tz = pytz.timezone("Asia/Jakarta")
    #     print(f"\n>>> tz: {tz}")
    #     return tz.localize(date_time).replace(tzinfo=None)
    # return date_time.replace(tzinfo=None)
    jakarta = pytz.timezone("Asia/Jakarta")
    if dt.tzinfo is None:
        return jakarta.localize(dt).replace(tzinfo=None)
    return dt.astimezone(jakarta).replace(tzinfo=None)
