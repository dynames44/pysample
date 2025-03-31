# filter - P 245
# map - P250
# os - P274
# trackback - P280
# json - P282
# urllib - P284
# faker - P289

import datetime
#from datetime import datetime, date, time, timedelta
# datetime.datetime : 날짜 + 시간
now : datetime.datetime = datetime.datetime.now()
dt : datetime.datetime = datetime.datetime(2025, 3, 31, 10, 30)
print("now datetime::::",now)
print("datetime::::",dt)

#날짜
toDay : datetime.date  = datetime.date.today()  # 오늘 날짜
d2 : datetime.date = datetime.date(2025, 3, 31)
print("toDay::::",toDay)
print("d2::::",d2)
print("year::::",toDay.year)
print("month::::",toDay.month)
print("day::::",toDay.day)
print("weekday::::",toDay.weekday())

#시간 
nowTime : datetime.time = datetime.time(21,15,30)
print("nowTime::::",nowTime)

#datetime → 문자열
nowStr :str = now.strftime("%Y-%m-%d")
print("nowStr::::",type(nowStr))
print("nowStr::::",nowStr)

#날짜, 초차이 계산 
day1 : datetime.datetime = datetime.datetime.strptime("2025-10-10 14:15", "%Y-%m-%d %H:%M")
day2 : datetime.datetime = datetime.datetime.strptime("2025-11-15 00:00", "%Y-%m-%d %H:%M")
print("Days diff::::",(day2-day1).days)
print("Seconds diff:::",(day2-day1).seconds)

#다양한 날짜 계산은 별도 모듈 사용 
from dateutil.relativedelta import relativedelta
dateDiff = relativedelta(day2, day1)

print("Years  :::", dateDiff.years)
print("Months :::", dateDiff.months)
print("Days   :::", dateDiff.days)
print("Hours  :::", dateDiff.hours)
print("Minutes:::", dateDiff.minutes)

#기준시간에 대한 날짜,시간 증가, 감소 : Ex.) 하루전, 한시간후
from datetime import timedelta
tomorrow : datetime.datetime = now + timedelta(days=1)
oneHourAgo  : datetime.datetime = now - timedelta(hours=1)

print("tomorrow  :::", tomorrow)
print("oneHourAgo  :::", oneHourAgo)

# import calendar
# calendar.isleap(2024)  # 윤년 여부 → True
# calendar.monthrange(2025, 3)  # (요일, 일 수) → (5, 31)

#슬립 사용 
import time as timeFunc
print(":::::::", datetime.datetime.now())
# timeFunc.sleep(3)
# print(":::::::", datetime.datetime.now())

#datetime 관련 라이브러리 
import pendulum

#현재시간 & 문자형 변환 : 타임존 지정은 필수 
tz = pendulum.local_timezone()
_now = pendulum.now(pendulum.local_timezone())
_today = pendulum.today(pendulum.local_timezone())

print("tz:::::",tz)
print("_now:::::",_now.format('YYYY-MM-DD'))
print("_today:::::",type(_today.format('YYYY-MM-DD')))

#기준일간 일자 (시간) 차이 계산 
start = pendulum.parse("2025-01-20")
end = pendulum.parse("2025-02-28")

# exact=True *년 *월 *일 같이 하나의 통으로 계산 
diff1 = end.diff(start, exact=True)
print("diff1:::::",diff1)

# 일수 차이
days_diff = end.diff(start).in_days()

# 개월 차이 (소수점 포함 X, 정확히 달 단위)
months_diff = end.diff(start).in_months()

# 연도 차이 (정확히 12개월 기준)
years_diff = end.diff(start).in_years()

print("일수 차이  :", days_diff)      # → 39
print("개월 차이 :", months_diff)    # → 1
print("연도 차이 :", years_diff)     # → 0