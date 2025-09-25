def average(notas: dict[str, float]) -> float:
    """Calculate the average grade from a dictionary of student grades."""
    if not notas or any(x is None for x in notas.values()):
        return 0
    return sum(notas.values()) / len(notas)
