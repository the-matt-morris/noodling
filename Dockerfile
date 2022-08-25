# Pull Python 3.10 image
FROM python:3.10.6

# Copy necessary app files into container
WORKDIR /app
COPY . /app

# Install Python dependencies
RUN pip install -r app/requirements.txt

# Expose port
EXPOSE 8501

ENTRYPOINT [ "streamlit", "run" ]
CMD ["app.py"]
