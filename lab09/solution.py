import numpy as np


def make_hours() -> list[int]:
    """Вектор часов: от 0 до 21 включительно с шагом 3."""
    return np.arange(0, 22, 3).tolist()


def vector_report(values: list[float]) -> dict:
    """Третий, последний, средний срез, каждый второй и развёрнутый вектор."""
    arr = np.asarray(values, dtype=float)
    return {
        "third": float(arr[2]),
        "last": float(arr[-1]),
        "middle": arr[2:6].tolist(),
        "every_second": arr[::2].tolist(),
        "reversed": arr[::-1].tolist(),
    }


def change_vector(values: list[float]) -> list[float]:
    """В независимой копии меняет индексы 2-4 на 99, затем каждый второй — на -1."""
    arr = np.asarray(values, dtype=float).copy()
    arr[2:5] = 99
    arr[::2] = -1
    return arr.tolist()
