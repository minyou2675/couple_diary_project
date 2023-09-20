FROM python

WORKDIR /couple_diary_project
ADD requirements.txt /couple_diary_project/requirements.txt

#StatReloader에서 멈추는 문제 해결용 환경변수
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get -y update

#레디스 서버 설치
RUN apt install redis-server -y
RUN service redis-server start

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
RUN pip install gunicorn
# RUN systemctl start gunicorn
# RUN systemctl enable gunicorn
