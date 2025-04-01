import pendulum

def get_date_diff_ymd(start_str: str, end_str: str) -> str:
    start = pendulum.parse(start_str)
    end = pendulum.parse(end_str)

    # 초기 계산: 연, 월, 일 수 차이 수동 계산
    years = end.year - start.year
    months = end.month - start.month
    days = end.day - start.day

    # 보정: 일수가 음수일 경우 이전 달에서 날짜 빼기
    if days < 0:
        months -= 1
        days += (start.add(months=months + 1).subtract(days=start.day)).days

    # 보정: 개월이 음수일 경우 이전 해에서 월수 빼기
    if months < 0:
        years -= 1
        months += 12

    return f"{years}년 {months}개월 {days}일"