# Venue
 The intended long term purpose is to make end-to-end event scheduling, setup, and searching functionality. The functionality should be something similar to EventBrite, Meetup.com, or anything of the sort
 
# Sub-Modules 
## [Location](location/README.md)
The location submodule is used to create location data for events and users. It is a web-service built via fastAPI and utilizing a Postgres database with an immutable dataset behind a redis cache. 