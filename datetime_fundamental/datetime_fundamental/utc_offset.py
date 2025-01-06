from datetime import datetime, timedelta, timezone
from dateutil import tz

ET = timezone(timedelta(hours=-5))
#dt = datetime.now(ET)
dt = datetime(2017, 12, 30, 15, 9,3, tzinfo=ET)
print(dt)

IST = timezone(timedelta(hours=5, minutes=30))
print(dt.astimezone(IST))
print(dt.replace(tzinfo= timezone.utc))
print(dt.astimezone(timezone.utc))

eut = tz.gettz('America/New_York')
last = datetime(2017, 12, 30, 15,9,3, tzinfo=eut)
print(last)
first = datetime(2017, 10, 1, 15,23,25, tzinfo=eut)
print(last)

# Daylight Savings Forward

spring_ahead_159am = datetime(2017,12,3,1,59,59)
print(f"Spring ahead time (1:59:59) : {spring_ahead_159am.isoformat()}" )


spring_ahead_3am = datetime(2017,12,3,3,0,0)
print(f"Spring ahead time (3:00:00) : {spring_ahead_3am.isoformat()}")

print(f"Total elpased time = {(spring_ahead_3am-spring_ahead_159am).total_seconds()}")

EST = timezone(timedelta(hours=-5))
EDT = timezone(timedelta(hours=-4))

spring_ahead_159am = spring_ahead_159am.replace(tzinfo=EST)
print(f"Spring ahead time (1:59:59) with time zone : {spring_ahead_159am.isoformat()}")

spring_ahead_3am = spring_ahead_3am.replace(tzinfo=EDT)
print(f"Spring ahead time (3:00:00) with time zone : {spring_ahead_3am.isoformat()}")

print(f"Total elpased time = {(spring_ahead_3am-spring_ahead_159am).total_seconds()}")

eastern = tz.gettz("US/Eastern")

spring_ahead_159am = datetime(2017,12,3,1,59,59, tzinfo=eastern)
print(f"Spring ahead time (1:59:59) with dev util: {spring_ahead_159am.isoformat()}" )

spring_ahead_3am = datetime(2017,12,3,3,0,0,tzinfo=eastern)
print(f"Spring ahead time (3:00:00) with dev util: {spring_ahead_3am.isoformat()}")

# Daylight Savings Backwords
first_1am = datetime(2017,11,5,1,0,0,tzinfo=eastern)
print(f"First_1am time: {first_1am.isoformat()}")
print(tz.datetime_ambiguous(first_1am))


second_1am = datetime(2017,11,5,1,0,0,tzinfo=eastern)
print(f"second_1am time: {second_1am.isoformat()}")
print((second_1am-first_1am).total_seconds())

first_1am = first_1am.astimezone(tz.UTC)
print(f"First_1am in UTC: {first_1am.isoformat()}")

second_1am = second_1am.astimezone(tz.UTC)
print(f"second_1am in UTC: {second_1am.isoformat()}")
print((second_1am-first_1am).total_seconds())



