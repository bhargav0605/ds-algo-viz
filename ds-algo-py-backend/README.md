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