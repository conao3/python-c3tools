from typing import Any


def gen_schema(tgt: dict[str, Any]) -> dict[str, Any]:
    if isinstance(tgt, dict):
        return {
            "type": "object",
            "required": [k for k in tgt.keys()],
            "properties": {k: gen_schema(v) for k, v in tgt.items()},
        }
    elif isinstance(tgt, list):
        return {
            "type": "array",
            "items": gen_schema(tgt[0]) if len(tgt) else {"type": "object"},
        }
    elif isinstance(tgt, (int, float)):
        return {"type": "number"}
    elif isinstance(tgt, str):
        return {"type": "string"}
    elif isinstance(tgt, bool):
        return {"type": "boolean"}
    else:
        raise Exception(f"Unknown type: {tgt}")
