# SPDX-License-Identifier: MIT
# Copyright (c) 2025 shun
"""Copyright compliance tests."""

from ament_copyright.main import main
import pytest


@pytest.mark.copyright
@pytest.mark.linter
def test_copyright() -> None:
    """Run copyright linter."""
    rc = main(argv=['.', 'test'])
    assert rc == 0, 'Found errors'
