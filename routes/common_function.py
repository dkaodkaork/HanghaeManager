import datetime


# 파라미터 date_format값은 'othertime' 과 'sametime'만 을 가지고 사용하면 좋을 것 같아욥!
def now_time(date_format):
    now = datetime.datetime.now()

    # 시간까지 저장하고 싶은 경우
    if(date_format == 'othertime'):
        return now
    else: # 시간 관계 없이 날짜만 영향 받고 싶은 경우 년-월-일 00:00:00 포맷
        date_format = '%Y-%m-%d'

        # now 문자열 포맷으로 바꿔주기 위해서 사용
        str_now = datetime.datetime.strftime(now, date_format)
        print(str_now)
        # 포맷 변경 후 Date 타입으로 변환
        date = datetime.datetime.strptime(str_now, date_format)
        print(type(date))
        print(date)
        return date
