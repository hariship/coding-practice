# Run this to check your functions:
#   python exercises\04_build\check.py
# You don't need to change this file.

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import build

# (function name, what to call it with, the right answer)
TESTS = [
    ("split_bill", (1000, 4, 10), 275.0),
    ("split_bill", (900, 3, 0), 300.0),
    ("split_bill", (1000, 3, 5), 350.0),
    ("split_bill", (100, 3, 0), 33.33),
    ("to_hours", (150,), "2h 30m"),
    ("to_hours", (45,), "0h 45m"),
    ("to_hours", (60,), "1h 0m"),
    ("count_words", ("the quick brown fox",), 4),
    ("count_words", ("hello",), 1),
    ("count_words", ("",), 0),
    ("biggest", ([3, 9, 2],), 9),
    ("biggest", ([-5, -1, -8],), -1),
    ("biggest", ([7],), 7),
    ("count_over", ([500, 1200, 80, 3000], 1000), 2),
    ("count_over", ([1000, 999], 1000), 0),
    ("count_over", ([], 1000), 0),
]

failed = 0
not_started = set()
for name, args, expected in TESTS:
    call = f"{name}({', '.join(repr(a) for a in args)})"
    try:
        got = getattr(build, name)(*args)
    except NotImplementedError:
        not_started.add(name)
        failed += 1
        continue
    except Exception as e:
        got = f"an error: {type(e).__name__}: {e}"
    if got == expected:
        print(f"PASS  {call} gave {expected!r}")
    else:
        failed += 1
        print(f"FAIL  {call} should give {expected!r} but gave {got!r}")

for name in sorted(not_started):
    print(f"TODO  {name} is not written yet")

print()
if failed:
    print(f"{failed} of {len(TESTS)} checks not passing yet. Keep going!")
    sys.exit(1)
print(f"All {len(TESTS)} checks passed. Time to open your PR.")
