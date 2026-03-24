import json

def serialize(obj) -> str:
    return json.dumps(obj.to_dict())

def deserialize(data: str) -> dict:
    return json.loads(data)