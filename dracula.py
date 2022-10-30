"""
Once upon a time ...
"""

class Vampire:
    def __init__(
        self,
        location: str, birth_date: int,
        death_date: int, weaknesses: list[str],
    ) -> None:
        self.location = location
        self.birth_date = birth_date
        self.death_date = death_date
        self.weaknesses = weaknesses

    @property
    def age(self) -> int:
        return self._calc_age()

    def _calc_age(self) -> int:
        return self.death_date - self.birth_date


# ... there was a guy named Vlad

Dracula = Vampire(
    location='Transylvania',
    birth_date=1428,
    death_date=1476,
    weaknesses=['Sunlight', 'Garlic'])
