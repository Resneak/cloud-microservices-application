Cloud-Based Airline Booking Service

This project demonstrates a cloud-based airline booking service built using FastAPI, SQLAlchemy, and Docker. It provides a comprehensive backend solution for managing bookings, payments, notifications, and flight management in a microservices architecture.

Features
- Booking Service: Manage bookings with CRUD operations.
- Payment Service: Handle payment transactions.
- Notification Service: Send notifications to users.
- Flight Management Service: Manage flight details and availability.

Tech Stack
- Backend: FastAPI
- Database: SQLAlchemy
- Containerization: Docker

Getting Started
- Prerequisites
- Docker
- Docker Compose

Installation
1. Clone the repository:
git clone https://github.com/Resneak/cloud-microservices-application.git
cd cloud-microservices-application

2. Start the services using Docker Compose:
docker-compose up --build

Usage
- Access the Booking Service API at http://localhost:8000
- Access the Payment Service API at http://localhost:8001
- Access the Notification Service API at http://localhost:8002
- Access the Flight Management Service API at http://localhost:8003

API Documentation
Each service provides API documentation via Swagger UI:

- Booking Service: http://localhost:8000/docs
- Payment Service: http://localhost:8001/docs
- Notification Service: http://localhost:8002/docs
- Flight Management Service: http://localhost:8003/docs

Medium Article
For more details about the project, read the full article on Medium: https://shorturl.at/IZwmP
