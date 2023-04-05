FROM scratch
COPY * /

# https://hub.docker.com/_/scratch
CMD ["echo", "hello people!"]