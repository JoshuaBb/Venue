FROM debian
ARG HOST="host.docker.internal"
ARG PORT=8000
ENV HOST ${HOST}
ENV PORT ${PORT}
WORKDIR /docs/open-api
RUN apt-get update && apt-get install -y curl
CMD ["curl", "http://host.docker.internal:8000/openapi.json", "-o", "open-api.json"]

