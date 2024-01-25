
# Description
The Location service is built to store event and user location data. It utilizes a Postgres Database,  FastAPI, and a Redis Cache. The idea behind it is to allow customers/users to set address data and be able to performantly retrieve it for other services. This project was done first due to it having the least amount of complexity and just g et familiar with some of the ecosystem. 

# Goals
1. Get familiar with FastAPI
2. Get familiar with setting up tests
3. Play around with the Redis Client
4. Configure a project that is super easy to setup

# Current Coverage (1/25/2024)
![Coverage Report](docs%2Fimage%2Fcoverage-report.png)

# How to Run Project
Everything can be setup via a docker-compose start up command. There is a volume mount for persisting the Postgres database that was setup via FlyWay, but there is not data that was seeded into it yet. 

```bash
# Note: I think there might be an issue on first run. Will double check


# Get a GOOGLE API KEY for Google Maps API. Currently using the geolocate API 
https://developers.google.com/maps
# Save API KEY IN .profile/.bash_profile
echo "export GOOGLE_MAPS_API_KEY=${API_KEY}" >> ~./bash_profile

# Make sure you are in the location module
cd /location 
# Make sure docker is installed and running
docker-compose up --build
# In browser
http://localhost:8000/docs#/default

# Sample Request
curl -X 'POST' \
  'http://localhost:8000/address/' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -d '{
  "address_line_one": "20 W 34th St",
  "city": "New York",
  "state_or_province": "NY",
  "zip_or_postal": "10001",
  "country_code": "US"
}'
```
![OpenAPI-sample.png](docs%2Fimage%2FOpenAPI-sample.png)


# New Lessons/Technologies 

<b>Python</b>: Still trying to get familiar with Python syntax and how to write a pythonic application. In this specific project the async defs seem a bit overkill and a couple of things feel a bit off. Even though they don't offer much utility, I wanted to play around with them

<b>Virtual Environments via Python</b>: I haven't utilized pip build system for any project or had a multi-directory structure. 

<b>Fast API</b>: I have only used Django and FastApi for playing around with webservices. From a comparison point of view, I liked FastAPI a lot. It wasn't super opinionated and seemed easy enough to setup. The integration around OpenAPI was pretty awesome

<b>psycopg2</b>: There are multiple options regarding connecting to a database. I generally like to stay away from ORM if possible and lean towards a low-level solution. Personally, I thought it was easy enough to use and pretty similar to JDBC. 

<b>Pydantic</b>: I don't think I touched enough to have much of an opinion yet. 

<b>Redis</b>: I used Redis for a couple of Scala projects. I didn't find it overly different using python. 

<b>Docker</b>: I took a course a couple of months ago. Using docker-compose to setup a project is super nice. 

# TODO:
1. Make environmental variables a bit more flexible and easier to inject
2. Create logging decorators to cut down on boilerplate of timing and logging functions
3. Create Unit Tests

# Doubts: 
There isn't a ton of complexity in the Location service and generally I think it is super easy to read. My main reservation with it is that it is composed similiarity to a Java/Scala project. Most of the examples on setting up a FastApi project had it composed more like a script rather than the Object Oriented Structure that I went for. I chose my structure to hide implementation details and to make Unit Testing a bit easier when added, but I didn't see a ton of other people doing it the same way online, so I have the inkling that while this service might be okay/good code, it could be bad Python. I would love to get a more experienced developer some critiques on project setup or what they would do differently.   