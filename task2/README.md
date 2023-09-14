# API Documentation

This documentation provides an overview of a simple REST API built with FastAPI, SQLAlchemy, and MYSQL for CRUD operations on a "person" resource. This API allows you to create, read, update, and delete person records.

## Table of Contents

- [API Documentation](#api-documentation)
  - [Table of Contents](#table-of-contents)
  - [Introduction](#introduction)
  - [Getting Started](#getting-started)
    - [Prerequisites](#prerequisites)
    - [Installation](#installation)
    - [Running the API](#running-the-api)
  - [API Endpoints](#api-endpoints)
    - [Create a Person](#create-a-person)
    - [Get a Person by ID](#get-a-person-by-id)
    - [Update a Person](#update-a-person)
    - [Delete a Person](#delete-a-person)
  - [Request and Response Formats](#request-and-response-formats)
  - [Sample Usage](#sample-usage)
    - [Create a Person](#create-a-person-1)
    - [Get a Person by ID](#get-a-person-by-id-1)
    - [Update a Person](#update-a-person-1)
    - [Delete a Person](#delete-a-person-1)
 
## Introduction

The API is designed to perform CRUD operations on a "person" resource. It provides endpoints for creating, retrieving, updating, and deleting person records in a MySQL database. The API is built using FastAPI and SQLAlchemy.

## Getting Started

### Prerequisites

Before you begin, ensure you have met the following requirements:

- Python and pip installed on your PC.
- MYSQL installed and running locally, or you have a MYSQL connection URI.

### Installation

1. Clone this repository to your local machine:

   ```bash
   git clone https://github.com/Horlarmmy/HNG-Tasks/
   ```

2. Navigate to the project directory:

   ```bash
   cd task2
   ```

3. Install the project dependencies:

   ```bash
   pip install -r requirements.txt
   ```

### Running the API

1. Start the MYSQL server if not already running.

2. Start the API by running:

   ```bash
   uvicorn main:app --reload
   ```

   The API will be available at `http://localhost:8000`.

## API Endpoints

### Create a Person

- **URL:** `/api/`
- **Method:** `POST`
- **Request Body:**

  ```json
  {
    "name": "John Doe",
  }
  ```

- **Response:**

```json
Status: 200 OK
Content-Type: application/json

  {
    "id": 1,
    "name": "John Doe"
  }
```

### Get a Person by ID

- **URL:** `/api/id`
- **Method:** `GET`
- **Response:**

```json
Status: 200 OK
Content-Type: application/json

  {
    "id": 1,
    "name": "John Doe"
  }

```

### Update a Person

- **URL:** `/api/id`
- **Method:** `PUT`
- **Request Body:**

  ```json
  {
    "name": "Updated Name",
  }
  ```

- **Response:**

```json
Status: 200 OK
Content-Type: application/json

{
  "id": 1,
  "name": "Updated Name"
}
```

### Delete a Person

- **URL:** `/api/id`
- **Method:** `DELETE`
- **Response:** `204 No Content`

## Request and Response Formats

- **Request Format:** Requests should be sent in JSON format.
- **Response Format:** Responses are in JSON format.

Note: Replace `{id}` in the URLs with the actual ID of the user you want to retrieve, update, or delete.

## Error Handling
The API returns the following in case of an error:

```json
Status: Error Code 400
Content-Type: application/json

{
    "detail": "Error Message"
}
```

## Testing
- Postman was used to test the API. The collection of the test requests can be found here:

    [![Run in Postman](https://run.pstmn.io/button.svg)](https://app.getpostman.com/run-collection/27453333-98cba097-2f3c-4bb6-92bd-99da33f5fd9e?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D27453333-98cba097-2f3c-4bb6-92bd-99da33f5fd9e%26entityType%3Dcollection%26workspaceId%3D377a6ae1-5702-4db6-82b4-c3e7c002ac52)

## UML Diagram


## License
<p align="left">
<img src="https://img.shields.io/packagist/l/laravel/framework" alt="License">
</p>