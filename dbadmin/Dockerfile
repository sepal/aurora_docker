FROM postgres:9.5
WORKDIR /root
ADD ./start.sh /root
RUN chmod +x start.sh
ENTRYPOINT ["./start.sh"]