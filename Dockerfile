# We're using Ubuntu 20.10
FROM mrmiss/userbutt:latest

#
# Clone repo and prepare working directory
#
RUN git clone -b pocong https://github.com/poocong/Pocong-Userbot /home/pocong/
RUN mkdir /home/pocong/bin/
WORKDIR /home/pocong/

CMD ["python3","-m","userbot"]
