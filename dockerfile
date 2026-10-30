#use a Python image
FROM python:3.12-slim

#set the working folder inside the container
WORKDIR /app

#copy the project files into the container
COPY . .

#run the inventory management program
CMD ["python", "OOP Week 8 Inventory management.py"]