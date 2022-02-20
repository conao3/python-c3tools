from typing import Any


def gen_schema(tgt: Any) -> dict[str, Any]:
    is_int = False
    if isinstance(tgt, str):
        try:
            # try parse tgt as int
            is_int = isinstance(int(tgt), int)
        except:  # noqa
            pass

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
    elif is_int or isinstance(tgt, (int, float)):
        return {"type": "number"}
    elif isinstance(tgt, str):
        return {"type": "string"}
    elif isinstance(tgt, bool):
        return {"type": "boolean"}
    elif isinstance(tgt, type(None)):
        return {"type": "string"}
    else:
        raise Exception(f"Unknown type: {tgt}")


def gen_parameter_schema(tgt: list[dict[str, Any]]) -> dict[str, Any]:
    def gen_parameter_schema_1(tgt: dict[str, Any]) -> dict[str, Any]:
        return dict(
            {"schema": gen_schema(tgt["example"]), "in": "query", "name": tgt["name"]},
            **(
                {
                    "description": tgt.get("description", ""),
                }
                if tgt.get("description")
                else {}
            ),
            **(
                {
                    "required": tgt["required"],
                }
                if tgt.get("required")
                else {}
            ),
        )

    return {
        "parameters": [gen_parameter_schema_1(elm) for elm in tgt],
    }
