# SPDX-License-Identifier: MIT
# Copyright (c) 2025 shun
"""PEP257 compliance tests."""

from ament_pep257.main import main
import pytest


@pytest.mark.linter
@pytest.mark.pep257
def test_pep257() -> None:
    """Run pep257."""
    rc = main(argv=['.', 'test'])
    assert rc == 0, 'Found code style errors / warnings'
