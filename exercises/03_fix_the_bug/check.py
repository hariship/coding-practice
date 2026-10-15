# Run this to check your fixes:
#   python exercises\03_fix_the_bug\check.py
# You don't need to change this file.

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import bugs

# (function name, what to call it with, the right answer)
TESTS = [
    ("count_to", (3,), [1, 2, 3]),
    ("count_to", (1,), [1]),
    ("can_vote", (18,), True),
    ("can_vote", (30,), True),
    ("can_vote", (17,), False),
    ("add_typed", ("5", "3"), 8),
    ("add_typed", ("10", "20"), 30),
    ("average", ([2, 4, 6, 8],), 5),
    ("average", ([10, 20],), 15),
    ("greeting", (9,), "morning"),
    ("greeting", (14,), "afternoon"),
    ("greeting", (20,), "evening"),
    ("total_price", ([100, 250, 50],), 400),
    ("total_price", ([],), 0),
]

failed = 0
for name, args, expected in TESTS:
    call = f"{name}({', '.join(repr(a) for a in args)})"
    try:
        got = getattr(bugs, name)(*args)
    except Exception as e:
        got = f"an error: {type(e).__name__}: {e}"
    if got == expected:
        print(f"PASS  {call} gave {expected!r}")
    else:
        failed += 1
        print(f"FAIL  {call} should give {expected!r} but gave {got!r}")

print()
if failed:
    print(f"{failed} of {len(TESTS)} checks failed. Keep going!")
    sys.exit(1)
print(f"All {len(TESTS)} checks passed. Time to open your PR.")
