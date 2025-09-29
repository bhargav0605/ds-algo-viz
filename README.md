# DS-Algorithm Visualization

### Rough Diagram:
![Architecture](./Blank%20diagram.png)

### Front-end
- ReactJS very basics.

### Gateway service (GoLang)
- Consumes events from the Redis Streams.
- Play, Pause, Resume and Stop functionality for front-end.

### Redis Streams (Holds all the events)
- Holds all the events.

### Data Structure and Algorithm services
- Python and Go services which puts the events in the Redis streams.

