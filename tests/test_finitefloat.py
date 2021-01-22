import math
from typing import SupportsFloat, SupportsIndex, Union

import pytest

from finitefloat import NotFinite, finitefloat


class SupF(SupportsFloat):
    def __init__(self, x: float) -> None:
        self.x = x

    def __float__(self) -> float:
        return self.x


class SupI(SupportsIndex):
    def __init__(self, ix: int) -> None:
        self.ix = ix

    def __index__(self) -> int:
        return self.ix


@pytest.mark.parametrize(
    "x", [0.1, 1, True, SupF(0.1), SupI(1), "0.1", b"0.1", bytearray(b"0.1")]
)
def test_normal(x: Union[SupportsFloat, SupportsIndex, str, bytes, bytearray]) -> None:
    finfloat = finitefloat(x)
    assert isinstance(finfloat, finitefloat)
    assert isinstance(finfloat, float)
    assert finfloat == float(finfloat) == float(x)


@pytest.mark.parametrize(
    "x",
    [
        math.nan,
        math.inf,
        -math.inf,
        SupF(math.nan),
        "nan",
        b"nan",
        bytearray(b"nan"),
    ],
)
def test_not_finite(
    x: Union[SupportsFloat, SupportsIndex, str, bytes, bytearray]
) -> None:
    with pytest.raises(NotFinite):
        finitefloat(x)
