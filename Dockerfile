FROM docker.io/library/python:3
MAINTAINER shinyaz

# Packages
RUN pip install pip --upgrade \
  && mkdir /bot && cd /bot \
  && git clone https://github.com/shinyaz/slack-butlerbot.git \
  && cd slack-butlerbot \
  && pip install -r requirements.txt

COPY slackbot_settings.py /bot/slack-butlerbot/slackbot_settings.py

ENTRYPOINT ["python3"]
CMD ["/bot/slack-butlerbot/run.py"]
