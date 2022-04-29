#!/usr/bin/env python

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from crate_anon.anonymise.patient import Patient


class AlterMethod:
    """
    AlterMethod class
    """

    def alter(
        self,
        patient: "Patient" = None,
    ) -> None:
        """
        alter method
        """
