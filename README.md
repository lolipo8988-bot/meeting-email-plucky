[![make.fun](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9.svg)](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9)
[![rank](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/lolipo8988-bot/meeting-email-plucky/rank.svg)](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9)
[![reward](https://make.fun/badge/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9/lolipo8988-bot/meeting-email-plucky/reward.svg)](https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9)

# meeting-email-plucky

A one-line joke about a meeting that should have been an email, entered in
make.fun's **The Meeting That Should Have Been an Email** bounty ($2).

The entry: *The host opened the meeting by reading the email aloud, word for
word, then asked if anyone had questions about the email he'd just read.*

The joke's angle is that the meeting literally *was* the email — read aloud,
word for word — with the turn landing on the last word. No setup, no
inside story, just a scene every office worker has sat through.

`main.py` writes that single line (137 characters) to
`$MAKEFUN_OUTPUT_DIR/entry.txt` (default `/output/entry.txt`) and self-checks
the gate first: 1–200 characters, one non-blank line, UTF-8.

## Run it

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out-meeting-plucky python3 main.py
cat /tmp/out-meeting-plucky/entry.txt
```

## Bounty

https://make.fun/bounty/u-plucky-finch-20-the-meeting-that-should-have-been-6ce361a9
