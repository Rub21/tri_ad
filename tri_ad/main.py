"""Script to read a file and return X large number of records.
Author: @Rub21
Run:
    python main.py \
    --file_path=https://amp-spacemaps-technical-challenge.s3-ap-northeast-1.amazonaws.com/spacemaps_technical_challenge.txt \
    --large_numbers=100
"""

import click
from smart_open import open

# This value can be set up according to the hardware memory configuration, it for reading extremely large files
CHUNK_SIZE = 100


def sort_tuples(list_tuples, large_numbers):
    """Sort list of tuples and return max x large numbers
    Args:
        list_tuples: list of tuples
        large_numbers: x largest number of items to return
    Returns:
        List of tuples that has max numbers
    """
    list_tuples.sort(key=lambda item: item[1], reverse=True)
    list_max_tuples = list_tuples[0:large_numbers]
    return list_max_tuples


def read_file_sort(file_path, large_numbers):
    """Read a file and sort the rows: format <unique record identifier><white_space><numeric value>
    Args:
        file_path: URL/path file
        large_numbers: x largest number of items to return
    Returns:
        List of tuples
    """
    # Check input type for large_numbers
    if type(large_numbers) not in [int]:
        raise TypeError("The large_numbers must be integer.")
    # Check value for large_numbers
    if large_numbers <= 0:
        raise ValueError("The large_numbers can not be negative or 0.")

    bunch = []

    try:
        with open(file_path, "r", encoding="utf8") as file_source:
            file_source.seek(499)
            file_content = file_source.readlines()
            for line in file_content:
                if line.strip():
                    key, value = line.split(" ")
                    value = int(value)
                    bunch.append((key, value))
                    if len(bunch) == CHUNK_SIZE:
                        bunch = sort_tuples(bunch, large_numbers)
            bunch = sort_tuples(bunch, large_numbers)
    except FileNotFoundError as err:
        raise ValueError("File does not exist.")
    except IOError as err:
        raise ValueError("The file in the URL does not exist.")
    if len(bunch) == 0:
        raise ValueError("Empty file or  the file contain less than 499 bytes.")
    return bunch


@click.command(
    short_help="Script to read a file and return X large number of records."
)
@click.option(
    "-f",
    "--file_path",
    help="Path to a file, it can be a url or a local file.",
    required=True,
    type=str,
    default="https://amp-spacemaps-technical-challenge.s3-ap-northeast-1.amazonaws.com/spacemaps_technical_challenge.txt",
)
@click.option(
    "-x",
    "--large_numbers",
    help="Number of records to return that contains large numbers",
    required=True,
    type=int,
    default=20,
)
def main(file_path, large_numbers):
    """Starting function"""
    results = read_file_sort(file_path, large_numbers)
    # Print in the require format
    for row in results:
        print(*row)


if __name__ == "__main__":
    main()
