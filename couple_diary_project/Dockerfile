FROM python

WORKDIR /couple_diary_project
ADD requirements.txt /couple_diary_project/requirements.txt

#StatReloader에서 멈추는 문제 해결용 환경변수
ENV PYTHONUNBUFFERED=1
ENV PYTHONDONTWRITEBYTECODE=1

RUN apt-get -y update

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
