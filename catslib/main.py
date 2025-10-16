from pathlib import Path
from typing import List, Union
from cat import read_cat_data, CatDict
import json


def get_cats_info(path: Union[str, Path]) -> List[CatDict]:
    return read_cat_data(path)


def main() -> None:
    current_dir = Path(__file__).parent
    cats_file = current_dir.parent / "data" / "cats.txt"

    try:
        print(json.dumps(get_cats_info(cats_file), indent=2))
    except FileNotFoundError as e:
        print(f"CatFileNotFound: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
