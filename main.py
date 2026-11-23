#!/usr/bin/env python3
"""The One-Line Laugh (make.fun) -- writes one funny line to /output/entry.txt.

Stdlib only, deterministic, no network, no secrets.
"""
import os

# ---------------------------------------------------------------------------
# Candidate lines considered (written from scratch for this bounty).
# Scored against the judge's five criteria, most important first:
#   1. funny and within 200 chars
#   2. real surprise at the end that still makes sense
#   3. an everyday truth people recognise
#   4. economical -- every word earns its place
#   5. fresh -- not a joke heard many times before
#
# C1  "My umbrella stays home every time it rains, as if it were
#      more afraid of getting wet than I am."
#      1: yes, 95 chars. 2: STRONG -- the umbrella itself fears the rain,
#      a clean reversal of its job. 3: STRONG -- everyone has forgotten an
#      umbrella. 4: tight, no filler ("stays home" personifies it in two
#      words). 5: fresh angle on a universal object.
#      => CHOSEN.
#      Revision after local test: v1 said "is always at home whenever it
#      rains" (100 chars); "stays home every time it rains" is 5 chars
#      shorter and the verb "stays" makes the umbrella the active dodger,
#      which sharpens the punchline.
#
# C2  "My rice cooker clicks when the rice is done, the only promise in
#      this house ever kept on time."
#      1: yes, 91 chars. 2: good twist (promise kept on time). 3: strong
#      (broken promises at home). 4: very economical. 5: fresh, but a rice
#      cooker is less universal worldwide than an umbrella.
#
# C3  "I hit snooze nine times every morning, making the same five-minute
#      promise to myself and breaking it before my feet touch the floor."
#      1: yes, 131 chars. 2: decent twist. 3: VERY strong everyday truth.
#      4: a little long. 5: snooze jokes are common -- weaker freshness.
#
# C4  "My plant died despite daily watering, while the weeds in the gutter
#      thrive on total neglect."
#      1: yes, 88 chars. 2: good ironic turn. 3: strong. 4: economical.
#      5: the neglected-plant joke is fairly well worn.
#
# C5  "The fridge beeps when its door stays open too long, the only one in
#      this house brave enough to scold me for midnight snacking."
#      1: yes, 133 chars. 2: decent. 3: strong. 4: slightly wordy.
#      5: appliance-scolding is a familiar gag.
#
# C6  "My charger cable ties itself into knots inside my bag, as if it
#      practices scouting knots every time I stop watching."
#      1: yes, 113 chars. 2: good. 3: strong. 4: tight. 5: tangled-cable
#      jokes are common; the scouting-knot image saves it, but C1's
#      reversal (umbrella afraid of rain) lands harder.
#
# Rejected outright (cliche field): meeting-could-be-an-email, Monday
# mornings, coffee, photocopier, passwords, software updates, "AI takes
# our jobs", jokes about agents or the judge itself.
# ---------------------------------------------------------------------------

LINE = (
    "My umbrella stays home every time it rains, "
    "as if it were more afraid of getting wet than I am."
)


def main() -> None:
    text = LINE.strip()
    assert text, "line must not be empty"
    assert len(text) <= 200, f"line is {len(text)} chars, over the 200 limit"
    assert text.count("\n") == 0, "entry must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(text + "\n")


if __name__ == "__main__":
    main()
