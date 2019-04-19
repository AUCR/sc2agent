FROM python:3.7-alpine AS sc2agent
ENV REPLAY_FILE_PATH=/opt/scagent/replays/

MAINTAINER Wyatt Roersma <wyatt@aucr.io>
RUN adduser -D scagent
RUN mkdir /opt/scagent/
COPY sc2agent /opt/scagent/
COPY requirements.txt /opt/scagent/
COPY setup.py /opt/scagent/
COPY sc2agent_cli.py /opt/scagent/
RUN apk update
RUN apk upgrade

RUN pip install -r /opt/scagent/requirements.txt
RUN python /opt/scagent/setup.py install
COPY boot.sh  /opt/scagent/
RUN mkdir /opt/scagent/replays/
RUN chmod a+x /opt/scagent/boot.sh
RUN chown -R scagent:scagent /opt/
USER scagent

ENTRYPOINT ["./boot.sh"]
