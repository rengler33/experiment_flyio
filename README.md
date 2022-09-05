# re3_dev

Playground @ re3.dev

## Development

This project has a development container available.

First, it will be necessary to configure environment variables. Copy the `.env.example` file to `.env` and fill the necessary environment variables. Docker compose will automatically pick up the variables.

`cp dev/.env.example dev/.env`

To run the development container, run:

```sh
docker compose -f dev/docker-compose.yml up
```

This will run the development webserver with hot-reloading.

You can also attach to the container for development purposes with VS Code.
