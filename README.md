# fastapi-hello-world
"Hello World" API docker image built using FastAPI and Python
- Running on port 8080 default
- Quick run using docker: 
```bash
docker run -it --rm --network host raushanraja/fastapi-hello-world:latest
```


## Configuration

### Environment Variables

This application uses the following environment variables, which can be customized:

- `HOST`: (Default: `0.0.0.0`) - The default host address.
- `PORT`: (Default: `8080`) - The default port number.
- `RELOAD`: (Default: `True`) - A boolean indicating whether reload is enabled (`True` or `False`).


## Running the Application

1. **Run the Docker container with customized configuration:**

    ```bash
    docker run -e HOST="YOUR_HOST" -e PORT="YOUR_PORT" -e RELOAD="YOUR_RELOAD_VALUE" raushanraja/fastapi-hello-world:latest 
    ```

    Replace `YOUR_HOST`, `YOUR_PORT`, and `YOUR_RELOAD_VALUE` with your desired values.
    
    - `HOST`: Specify the desired host address.
    - `PORT`: Specify the port number.
    - `RELOAD`: Set to `True` or `False` based on your requirements.

2. **Run using docker-comopose:**
    ```yaml
    version: '3'
    services:
      fastapi:
        image: raushanraja/fastapi-hello-world:latest
        ports:
          - "8080:8080"
        environment:
          - HOST=0.0.0.0
          - PORT=8080
          - RELOAD=False
    ```

    ```base
    docker-compose up
    ```


## API Endpoints

#### GET /

- **Description**: Returns a "Hello World" message using the GET method.
- **Endpoint**: `http://localhost:8080/`
- **Return JSON**:
    ```json
    {
        "message": "Hello World",
        "method": "GET"
    }
    ```

#### POST /

- **Description**: Returns a "Hello World" message using the POST method.
- **Endpoint**: `http://localhost:8080/`
- **Return JSON**:
    ```json
    {
        "message": "Hello World",
        "method": "POST"
    }
    ```

#### PUT /

- **Description**: Returns a "Hello World" message using the PUT method.
- **Endpoint**: `http://localhost:8080/`
- **Return JSON**:
    ```json
    {
        "message": "Hello World",
        "method": "PUT"
    }
    ```

#### DELETE /

- **Description**: Returns a "Hello World" message using the DELETE method.
- **Endpoint**: `http://localhost:8080/`
- **Return JSON**:
    ```json
    {
        "message": "Hello World",
        "method": "DELETE"
    }
    ```

#### PATCH /

- **Description**: Returns a "Hello World" message using the PATCH method.
- **Endpoint**: `http://localhost:8080/`
- **Return JSON**:
    ```json
    {
        "message": "Hello World",
        "method": "PATCH"
    }
    ```

#### OPTIONS /

- **Description**: Returns a "Hello World" message using the OPTIONS method.
- **Endpoint**: `http://localhost:8080/`
- **Return JSON**:
    ```json
    {
        "message": "Hello World",
        "method": "OPTIONS"
    }
    ```

#### HEAD /

- **Description**: Returns a "Hello World" message using the HEAD method.
- **Endpoint**: `http://localhost:8080/`
- **Return JSON**:
    ```json
    {
        "message": "Hello World",
        "method": "HEAD"
    }
    ```

#### TRACE /

- **Description**: Returns a "Hello World" message using the TRACE method.
- **Endpoint**: `http://localhost:8080/`
- **Return JSON**:
    ```json
    {
        "message": "Hello World",
        "method": "TRACE"
    }
    ```
