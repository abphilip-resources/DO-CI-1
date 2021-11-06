FROM alpine                                             
# The base image to use

RUN apk add --no-cache \
        bash           \
        httpie         \
        jq &&          \
        which bash &&  \
        which http &&  \
        which jq
# Install the required packages

COPY entrypoint.sh /usr/local/bin/entrypoint.sh
COPY sample_push_event.json /sample_push_event.json
# Copy the entrypoint script to the /usr/local/bin directory

ENTRYPOINT ["entrypoint.sh"]
# Run the entrypoint script
