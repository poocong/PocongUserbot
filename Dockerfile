# We're using Ubuntu 20.10
FROM xnewbie/xbot:groovy

#
# Clone repo and prepare working directory
#
RUN git clone -b alpha https://github.com/X-Newbie/XBot-Remix /home/xubot/
RUN mkdir /home/xubot/bin/
WORKDIR /home/xubot/

# Upgrade pip
RUN pip install --upgrade pip

#Install python requirements
RUN pip3 install -r https://raw.githubusercontent.com/X-Newbie/XBot-Remix/alpha/requirements.txt

CMD ["python3","-m","userbot"]
