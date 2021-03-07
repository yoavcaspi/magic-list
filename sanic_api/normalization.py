from typing import List, Dict


def normalize_value(value: Dict[str, str]) -> str:
    return [val
            for key, val in value.items()
            if "val" in key.lower()][0]


def normalize_list(values: List[Dict[str, str]]) -> Dict[str, str]:
    return {value["name"]: normalize_value(value) for
            value in values}
