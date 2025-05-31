import os
from pathlib import Path

from markdown_it.utils import read_fixture_file
import mdformat
import pytest

FIXTURE_PATH = Path(__file__).parent / "fixtures.md"
FIXTURE_ALIGNED_PATH = Path(__file__).parent / "fixtures_aligned.md"
fixtures = read_fixture_file(FIXTURE_PATH)
fixtures_aligned = read_fixture_file(FIXTURE_ALIGNED_PATH)


@pytest.mark.parametrize(
    "line,title,text,expected", fixtures, ids=[f[1] for f in fixtures]
)
def test_fixtures(line, title, text, expected):
    os.environ.pop("MDFORMAT_DOLLARMATH_USE_ALIGNED", None)
    output = mdformat.text(text, extensions={"dollarmath"})
    assert output.rstrip() == expected.rstrip(), output


@pytest.mark.parametrize(
    "line,title,text,expected", fixtures_aligned, ids=[f[1] for f in fixtures_aligned]
)
def test_fixtures_aligned(line, title, text, expected):
    os.environ["MDFORMAT_DOLLARMATH_USE_ALIGNED"] = "1"
    output = mdformat.text(text, extensions={"dollarmath"})
    assert output.rstrip() == expected.rstrip(), output
