FROM ubuntu:latest
MAINTAINER jan.szumiec@gmail.com
RUN apt update && apt upgrade
RUN add-apt-repository --yes ppa:js-reynaud/kicad-4
RUN apt update
RUN apt install kicad


