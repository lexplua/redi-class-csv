import csv
from typing import List, Optional, Sequence
from pathlib import Path


def get_csv_filename() -> Path:
    ## TODO: Task 1: return path to csv file in data_files directory
    return Path()


def fetch_csv_content(filename: str) -> List:
    lines = [
        ## TODO: Task 2: fetch content from CSV file with path=filename
    ]
    return lines


def add_record(filename: Path, record_id: int, author: str, book_name: str):
    ## TODO: Task 3: Add record to file with fields from arguments
    return


def get_next_id(filename: Path) -> int:
    ## TODO: Task 4: return correct next_id.
    ## Next id -> max id in file + 1
    return 0


def get_field_names(filename: Path) -> Optional[Sequence[str]]:
    ## TODO: Task 5: read field names from CSV file
    return []
