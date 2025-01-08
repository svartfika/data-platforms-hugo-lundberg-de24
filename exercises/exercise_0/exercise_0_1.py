# a)

student = {"id": 101, "name": "Erika", "is_active": True, "age": 45}


# b) Simple validation

student_validation = {
    "id": isinstance(student.get("id"), int),
    "name": isinstance(student.get("name"), str),
    "is_active": isinstance(student.get("is_active"), bool),
    "age": isinstance(student.get("age"), int),
}

for k, v in student_validation.items():
    print(f"{k}: {v}")

is_all_valid = all(v for v in student_validation.values())
print(f"All fields valid: {is_all_valid}")


# c, d) Function for validating a JSON array

users = [
    {"id": 101, "name": "Erika", "is_active": True, "age": 45},
    {"id": 102, "name": "Marcus", "is_active": True, "age": 34},
    {"id": 103, "name": "David", "is_active": False, "age": 29},
    {"id": 104, "name": "Anna", "is_active": True, "age": 41.5},
    {"id": 106, "name": "Ingrid", "is_active": "NOPE", "age": 8},
]


def schema_validation(data: list[dict] | dict) -> dict:
    """Returns dictionary mapping invalid row indexes to dict of field errors."""

    if isinstance(data, dict):
        data = [data]

    rows_issues = {}
    for i, row in enumerate(data):
        row_validation = {
            "id": isinstance(row.get("id"), int),
            "name": isinstance(row.get("name"), str),
            "is_active": isinstance(row.get("is_active"), bool),
            "age": isinstance(row.get("age"), int),
        }

        if not all(v for v in row_validation.values()):
            row_errors = {
                i: {k: row.get(k) for k, v in row_validation.items() if v is False}
            }
            rows_issues.update(row_errors)

    return rows_issues if rows_issues else {}


# Test all available data
for item in (student, users):
    print(schema_validation(item))
