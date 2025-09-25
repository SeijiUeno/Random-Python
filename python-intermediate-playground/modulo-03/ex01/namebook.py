from typing import Dict, List


def format_names(names_dic: Dict[str, str]) -> List[str]:
    """Return a list of full names built from a mapping .."""
    full_names: List[str] = []
    for first, last in names_dic.items():
        full_names.append(f"{first.capitalize()} {last.capitalize()}")
    return full_names
