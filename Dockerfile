# We're using Ubuntu 20.10
FROM ximfine/xproject:buster

#
# Clone repo and prepare working directory
#
RUN git clone -b pocong https://github.com/poocong/Pocong-Userbot /root/userbot/
RUN mkdir /root/userbot/.bin
WORKDIR /root/userbot

#
# Make open port TCP
#
EXPOSE 80 443

#Upgrade pip
RUN pip install --upgrade pip

#Install python requiremets
#RUN pip3 install -r https://raw.githubusercontent.com/poocong/Pocong-Userbot/pocong/requirements.txt

CMD ["python3","-m","userbot"]
