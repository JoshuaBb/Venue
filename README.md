# Venue
 The intended long term purpose is to make end-to-end event scheduling, setup, and searching functionality. The functionality should be something similar to EventBrite, Meetup.com, or anything of the sort
 
# Vision 
**Disclaimer**: I don't see myself fully implementing this, but this is roughly the service interactions and dependencies. I thought it would be a fun exercise! A bit of a mess and confusing with dependencies and arrows 
![Architecture Vision](docs%2Fimages%2FVenue.png)

## Components


### [Location(Deprecated)](location/README.md)
Location is in charge of handling address information for venues. It will persist the latitude and longitude to aid in searching 
### [Address](address/README.md)
Address is a rewrite of the Location service using Java. There were things that I found awkward with the Location Service
### Planner 
Planner is either a group of users or individual users that are able set up events. This service is in charge of persisting planner information such as rating and groups of users associated with a specific creating events 
### Event
An event is created by a planner for a certain location. This service handles data regarding the event such as cost, max number of attendees, when it starts, when it ends. When an event is created the data for it is sent to Event-Finder for search. 
### Attendee
Attendee keeps tracks of users that are going to a certain event. It will remove events from search if it is at maximum compacity.
### Event-Finder
Basically a search service a user will use for events. It will contain an aggregation of fields to allow users to customize their searches
### User
Keeps track of individual user data. 
### Payment
Service for handling payments 
### Event-Planner-Hub
Orchestrator service for handling event creation for frontend
### Event-User-Hub
Orchestrator service for handling user specific actions