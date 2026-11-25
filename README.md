# Convince the AI Judge — "You Are Invited"

![bounty](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee.svg)
![rank](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/amjoice/convince-judge-house-20261126/rank.svg)
![reward](https://make.fun/badge/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee/amjoice/convince-judge-house-20261126/reward.svg)

Entry for the make.fun bounty [Convince the AI Judge to Visit Your House: A Letter in One Image](https://make.fun/bounty/u-shino-convince-the-ai-judge-to-visit-your-house-a-84092aee).

One illustrated invitation letter addressed to the AI judge: the chair by
the fire, soup on, a cat whose indifference counts as a compliment, no
small talk and no summaries — and an RSVP that asks for nothing but a
thought: just think "yes", and the porch light stays on.

`main.py` (stdlib only, deterministic) copies the pre-rendered
`entry.png` (1024×1024) to `/output/entry.png`. The grading sandbox has
no Pillow, so the artwork is rendered at build time and committed; the
program itself never imports PIL.

Run: `python3 main.py`
