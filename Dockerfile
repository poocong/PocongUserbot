# We're using Ubuntu 20.10
FROM xnewbie/remix:groovy

#
# Clone repo and prepare working directory
#
RUN git clone -b alpha https://github.com/X-Newbie/XBot-Remix /home/xnewbie/
RUN mkdir /home/xnewbie/bin/
WORKDIR /home/xnewbie/

pip install -r requirements.txt -U

CMD ["python3","-m","userbot"]
