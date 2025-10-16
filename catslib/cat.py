from pathlib import Path
from typing import List, TypedDict, Union


class CatDict(TypedDict):
    id: str
    name: str
    age: int


def read_cat_data(file_path: Union[str, Path]) -> List[CatDict]:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File '{file_path}' not found")

    cats: List[CatDict] = []
    with path.open('r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                try:
                    cat_id, name, age = line.split(',')
                    cats.append({
                        "id": cat_id.strip(),
                        "name": name.strip(),
                        "age": int(age.strip()),
                    })
                except ValueError:
                    print('Invalid cat record')
                    continue

    return cats
