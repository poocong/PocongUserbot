# We're using Ubuntu 20.10
FROM ximfine/xremix:groovy

#
# Clone repo and prepare working directory
#
RUN git clone -b alpha https://github.com/X-Newbie/XBot-Remix /home/userbot/
RUN mkdir /home/userbot/bin/
WORKDIR /home/userbot/

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/X-Newbie/XBot-Remix/alpha/requirements.txt

CMD ["python3","-m","userbot"]
