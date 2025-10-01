# Python websocket backend

## Requests from frontend
### Define
- User define their array which they want to sort
```
{
    "type": "define",
    "cmd": "init",
    "array": [64, 34, 25, 12, 22, 11, 90],
    "sorting: "bs"
}
```

### Random
- Randomly generated array with size (min, max) and range in which you want to generate array in.
```
{
    "type": "random",
    "cmd": "generate",
    "minSize": 1,
    "maxSize": 100,
    "minRange": 5,
    "maxRange": 500,
}
```

## Response from backend
### Define
- Array given by the user.
```
{
    "type":"define",
    "cmd": "compare",
    "i": i,
    "j": j,
    "array": arr
}
```
```
{
    "type":"define",
    "cmd": "swap",
    "i": i,
    "j": j,
    "array": arr
}
```

```
{
    "type":"define",
    "cmd": "done",
    "array" arr
}
```

### Random
```
{
    "type": "random",
    "cmd": 
}
```


### Current:
{
    "type": "random",
    "cmd": "generate",
    "minSize": 1,
    "maxSize": 5,
    "minRange": 5,
    "maxRange": 500,
    "sorting": "bs"
}

Response:
{
  "type": "random",
  "cmd": "compare",
  "array": [
    102,
    325,
    148,
    132
  ],
  "sorting": "bs",
  "minSize": 0,
  "maxSize": 0,
  "minRange": 0,
  "maxRange": 0,
  "i": 0,
  "j": 1
}

# v0.0.2
Testing for algorithm, Send this to the worker to start the process with Array from the front-end:

Run: gunicorn src.app:app

```json
{
    "sorting": "bs",
    "array": [6,5,4,3],
    "user_id": 111111,
    "run_id": 222222
}
```