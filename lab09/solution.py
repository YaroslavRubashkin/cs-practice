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


def cap_above(values: list[float], limit: float) -> list[float]:
    """Заменяет все значения больше limit на limit одной маской."""
    arr = np.asarray(values, dtype=float)
    arr[arr > limit] = limit
    return arr.tolist()


def celsius_to_fahrenheit(values: list[float]) -> list[float]:
    """Переводит весь вектор из Цельсия в Фаренгейты без цикла."""
    arr = np.asarray(values, dtype=float)
    return (arr * 9 / 5 + 32).tolist()
