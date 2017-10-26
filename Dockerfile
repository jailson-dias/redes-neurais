FROM python:3

RUN apt-get update -y
# RUN apt update -y && apt install -y git
# RUN git clone https://github.com/jailson-dias/redes-neurais.git
RUN mkdir redes-neurais
WORKDIR /redes-neurais/

# COPY package.json /usr/src/package.json
# COPY lib/ /usr/src/lib
# COPY services/ /usr/src/services
# more volumes

# ADD . /redes-neurais/

# RUN npm install --production --silent

# RUN apt install bash
# EXPOSE 8002

CMD [ "bash"]