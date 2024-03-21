FROM debian as open-api-generation
ARG HOST="host.docker.internal"
ARG PORT=8000
ENV HOST ${HOST}
ENV PORT ${PORT}
WORKDIR /docs/open-api
RUN apt-get update && apt-get install -y curl
CMD ["curl", "http://host.docker.internal:8000/openapi.json", "-o", "open-api.json"]

FROM openapitools/openapi-generator-cli
WORKDIR clients
COPY --from=open-api-generation open-api.json .
RUN generate


