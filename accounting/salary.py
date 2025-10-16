from pathlib import Path
from decimal import Decimal
from typing import List, TypedDict, Union


class EmployeeDict(TypedDict):
    name: str
    salary: Decimal


def read_salary_data(file_path: Union[str, Path]) -> List[EmployeeDict]:
    path = Path(file_path)
    if not path.exists():
        raise FileNotFoundError(f"File '{file_path}' not found")

    salaries: List[EmployeeDict] = []
    with path.open('r', encoding='utf-8') as file:
        for line in file:
            line = line.strip()
            if line:
                try:
                    name, salary = line.split(',')
                    salaries.append({"name": name.strip(), "salary": Decimal(salary.strip())})
                except ValueError:
                    continue

    return salaries
