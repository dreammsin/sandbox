FROM scratch
COPY * /app/

RUN echo 'testing testing 123'

EXPOSE 80