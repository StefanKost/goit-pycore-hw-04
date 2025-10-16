from pathlib import Path
from decimal import Decimal
from typing import Tuple, Union
from salary import read_salary_data


def total_salary(path: Union[str, Path]) -> Tuple[Decimal, Decimal]:
    salary_data = read_salary_data(path)

    if not salary_data:
        return Decimal(0), Decimal(0)

    salaries = [item["salary"] for item in salary_data]
    total = Decimal(sum(salaries))
    average = Decimal(total / len(salaries))
    return total, average


def main() -> None:
    current_dir = Path(__file__).parent
    salary_file = current_dir.parent / "data" / "salary_file.txt"

    try:
        total, average = total_salary(salary_file)
        print(f"Загальна сума заробітної плати: {total}, Середня заробітна плата: {average}")
    except FileNotFoundError as e:
        print(f"FileNotFoundError: {e}")
    except Exception as e:
        print(f"Error: {e}")


if __name__ == "__main__":
    main()
