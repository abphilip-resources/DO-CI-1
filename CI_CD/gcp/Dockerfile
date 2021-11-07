# Use a python image
FROM python:3.10

# Set the working directory in the container to /app
WORKDIR /app

# Add the current directory to the container as /app
COPY . /app

# pip install flask
RUN pip install --upgrade pip && \
    pip install \
        Flask \
        awscli \
        flake8 \
        pylint \
        pytest \
        pytest-flask

# Expose the default flask port 8080
EXPOSE 8080

# Execute the Flask app
ENTRYPOINT ["python"]
# Healthcheck for the app
HEALTHCHECK CMD curl --fail http://localhost:8080/ || exit 1
# Run the flask app
CMD ["/app/app.py"]
