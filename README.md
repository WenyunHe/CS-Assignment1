# Competitor News

The Competitor News codebase contains an app getting competitor news.

## Set up

1.  Run docker-compose.

    ```shell
    docker-compose up -d
    ```

## Local development

Follow the instructions below to get the app up and running on your machine.

1.  Install Python 3.10 and a recent version of NPM.
1.  View the list of available tasks
    ```shell
    make
    ```

## Backend

Here are a few tasks that are useful when running the backend app.
Make sure they all run on your machine.

1.  Run install
    ```shell
    make backend/install
    ```

1.  Run tests
    ```shell
    make backend/test
    ```

1.  Run server
    ```shell
    make backend/run
    ```

## Frontend

Here are a few tasks that are useful when running the frontend app.
Make sure they all run on your machine.

1.  Run tests
    ```shell
    make frontend/install
    ```

1.  Run server
    ```shell
    make frontend/run
    ```
