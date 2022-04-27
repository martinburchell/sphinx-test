from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from test.foo import Bar


class RefOne():
    def __init__(bar: "Bar"):
        pass
