# We're using Ubuntu 20.10
FROM xnewbie/rmx:groovy

#
# Clone repo and prepare working directory
#
RUN git clone -b alpha https://github.com/X-Newbie/XBot-Remix /home/xnewbie/
RUN mkdir /home/xnewbie/.bin/
WORKDIR /home/xnewbie/

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/X-Newbie/XBot-Remix/alpha/requirements.txt

CMD ["python3","-m","userbot"]
