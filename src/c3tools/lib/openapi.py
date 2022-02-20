from typing import Any


def gen_schema(arg: Any) -> dict[str, Any]:
    is_int = False
    if isinstance(arg, str):
        try:
            # try parse arg as int
            is_int = isinstance(int(arg), int)
        except ValueError:
            pass

    if isinstance(arg, dict):
        return {
            "type": "object",
            "required": [k for k in arg.keys()],
            "properties": {k: gen_schema(v) for k, v in arg.items()},
        }
    elif isinstance(arg, list):
        return {
            "type": "array",
            "items": gen_schema(arg[0]) if len(arg) else {"type": "object"},
        }
    elif is_int or isinstance(arg, (int, float)):
        return {"type": "number"}
    elif isinstance(arg, str):
        return {"type": "string"}
    elif isinstance(arg, bool):
        return {"type": "boolean"}
    elif isinstance(arg, type(None)):
        return {"type": "string"}
    else:
        raise Exception(f"Unknown type: {arg}")


def gen_parameter_schema(arg: list[dict[str, Any]]) -> dict[str, Any]:
    def gen_parameter_schema_1(arg: dict[str, Any]) -> dict[str, Any]:
        return dict(
            {"schema": gen_schema(arg["example"]), "in": "query", "name": arg["name"]},
            **(
                {
                    "description": arg.get("description", ""),
                }
                if arg.get("description")
                else {}
            ),
            **(
                {
                    "required": arg["required"],
                }
                if arg.get("required")
                else {}
            ),
        )

    return {
        "parameters": [gen_parameter_schema_1(elm) for elm in arg],
    }
