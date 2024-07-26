# Use the official Python image from the Docker Hub
FROM python:3.9-slim-buster 

# Set the working directory inside the container
WORKDIR /personal-portfolio

# Copy requirements.txt file from host into working directory
COPY requirements.txt .

# Install the Python dependencies
RUN pip3 install -r requirements.txt

# Copy all files from current directory to working directory in the container
COPY . .

# Define the command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0"]

# Expose port 5000 to allow external access to the Flask app
EXPOSE 5000