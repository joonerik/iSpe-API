# Backend
From this folder you can run a mocked backend server to provide a API to change JSON-files for the project.

## Run
To run the server
```
python3 server.py
```

Or if you are planning on developing more on the server, this command is handy
```
nodemon --exec python3 server.py
```

## Entries
The following entries are available in the API

### answers/user_id
    Methods: GET, POST

    Send and receive the answers made by a user at ID

### question/question_id
    Methods: GET

    Receive a question by ID

### config/user_id
    Methods: GET

    Receive configuration for user at ID

### login/user_id
    Methods: GET

    Receive if the user exists

    Returns: {"status": Boolean}

### register
    Methods: POST

    Registers a new user

## Test
If you want to test the API, run the server and open a GET-path in your browser. To send a POST, use a tool like Postman og curl.

## Curl

### GET

    curl http://localhost:8080/<entry>

### POST

    curl --header "Content-Type: application/json" \
        --request POST \
        --data '{<data>}' \
        http://localhost:8080/<entry>