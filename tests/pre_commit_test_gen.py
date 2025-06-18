from pathlib import Path

from markdown_it.utils import read_fixture_file

FIXTURE_PATH = Path(__file__).parent / "fixtures.md"
fixtures = read_fixture_file(FIXTURE_PATH)
examples = []
titles = []
for fixture in fixtures:
    if fixture[-1] not in examples:
        examples.append(fixture[-1])
        titles.append(fixture[1])


with open(Path(__file__).parent / "pre-commit-test.md", "w") as f:
    f.write("# Dollar Math Examples\n\n")
    f.write("\n".join(map(lambda x: f"## {x[0]}\n\n{x[1]}", zip(titles, examples))))
