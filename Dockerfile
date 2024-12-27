# Step 1: Use official Python image as base
FROM python:3.12-slim

# Step 2: Set the working directory inside the container
WORKDIR /app

# Step 3: Copy the requirements.txt file into the container
COPY requirements.txt .

# Step 4: Install dependencies
# Install system dependencies for psycopg2
RUN apt-get update && apt-get install -y libpq-dev gcc
RUN pip install --no-cache-dir -r requirements.txt

# Step 5: Copy the rest of the app into the container
COPY . .

# Step 6: Expose port 8000 to the outside world
EXPOSE 8000

# Step 7: Command to run the FastAPI app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
