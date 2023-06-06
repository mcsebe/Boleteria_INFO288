FROM rabbitmq

# Define environment variables.
ENV RABBITMQ_USER user_rabbit
ENV RABBITMQ_PASSWORD TZ3a2iU7h7u5AjeGvGj5!efMBVVvSQ
ENV RABBITMQ_PID_FILE /var/lib/rabbitmq/mnesia/rabbitmq

ADD init.sh /init.sh
RUN sed -i -e 's/\r$//' init.sh
RUN chmod +x /init.sh
EXPOSE 15672

# Define default command
CMD ["/init.sh"]