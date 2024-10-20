# Use the official Python image from the Docker Hub
FROM python:3.12

# Install the necessary build tools and dependencies for distutils


# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file first to leverage Docker cache
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . .

# Set the environment variable for Django
ENV PYTHONUNBUFFERED=1

# Expose the port that the app runs on
EXPOSE 8000

# Command to run the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
