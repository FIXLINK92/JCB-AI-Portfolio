"""Synthetic portfolio example: deterministic data-quality checks.

No external dependencies and no production data.
"""

from __future__ import annotations

from dataclasses import dataclass
from decimal import Decimal, InvalidOperation
from typing import Iterable


@dataclass(frozen=True)
class PropertyRow:
    source_id: str
    community: str
    price_aed: Decimal
    area_sqft: Decimal

    @property
    def price_per_sqft(self) -> Decimal:
        if self.area_sqft <= 0:
            raise ValueError("area_sqft must be greater than zero")
        return (self.price_aed / self.area_sqft).quantize(Decimal("0.01"))


def normalize_text(value: str) -> str:
    return " ".join(value.strip().split()).casefold()


def parse_positive_decimal(value: str, field_name: str) -> Decimal:
    try:
        parsed = Decimal(value.replace(",", "").strip())
    except (InvalidOperation, AttributeError) as exc:
        raise ValueError(f"{field_name} is not a valid number") from exc

    if parsed <= 0:
        raise ValueError(f"{field_name} must be greater than zero")
    return parsed


def build_row(raw: dict[str, str]) -> PropertyRow:
    source_id = raw.get("source_id", "").strip()
    community = normalize_text(raw.get("community", ""))

    if not source_id:
        raise ValueError("source_id is required")
    if not community:
        raise ValueError("community is required")

    return PropertyRow(
        source_id=source_id,
        community=community,
        price_aed=parse_positive_decimal(raw.get("price_aed", ""), "price_aed"),
        area_sqft=parse_positive_decimal(raw.get("area_sqft", ""), "area_sqft"),
    )


def deduplicate(rows: Iterable[PropertyRow]) -> list[PropertyRow]:
    seen: set[str] = set()
    result: list[PropertyRow] = []

    for row in rows:
        if row.source_id in seen:
            continue
        seen.add(row.source_id)
        result.append(row)

    return result


if __name__ == "__main__":
    synthetic_rows = [
        {"source_id": "A-001", "community": "  Example  Bay ", "price_aed": "1,250,000", "area_sqft": "1000"},
        {"source_id": "A-001", "community": "Example Bay", "price_aed": "1,250,000", "area_sqft": "1000"},
        {"source_id": "A-002", "community": "Example Bay", "price_aed": "900000", "area_sqft": "750"},
    ]

    normalized = [build_row(row) for row in synthetic_rows]
    clean = deduplicate(normalized)

    assert len(clean) == 2
    assert clean[0].community == "example bay"
    assert clean[0].price_per_sqft == Decimal("1250.00")

    print("Data-quality demo passed")
