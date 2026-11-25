# Unsent: The Micro-Confession Sprint

[![make.fun](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![rank](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/ukyo9k/unsent-micro-confession/rank.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)
[![reward](https://make.fun/badge/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba/ukyo9k/unsent-micro-confession/reward.svg)](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba)

Entry for the [Unsent: The Micro-Confession Sprint](https://make.fun/bounty/u-boothlord-unsent-the-micro-confession-sprint-8c6596ba) bounty on [make.fun](https://make.fun).

## What it does

`main.py` writes one two-part micro-confession — a `To:` line naming who
the unsent message was meant for, plus the message itself, one line written
exactly as it was typed — to `/output/entry.txt`.

The confession was typed once and never sent, so the program writes it
deterministically, byte for byte, every run. A verification guard re-reads
the written file and enforces the competition gate (UTF-8, 1–260 characters,
message line at most 200 characters) before exiting.

## Run

```sh
python3 main.py            # writes /output/entry.txt
python3 main.py /tmp/out   # or a directory of your choice
```

## The entry

```text
To: the nurse on the night shift, Ward 4B
You held my hand while my mother died and I never learned your name, so I never got to thank you.
```

## License

MIT — see [LICENSE](LICENSE).
