# We're using Ubuntu 20.10
FROM xnewbie/xremix:remix
USER xnewbie

#
# Clone repo and prepare working directory
#
RUN git clone -b x-sql-extended https://github.com/X-Newbie/XBot-Remix /root/userbot
RUN mkdir /root/userbot/.bin
WORKDIR /root/userbot

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/X-Newbie/XBot-Remix/x-sql-extended/requirements.txt

CMD ["python3","-m","userbot"]
