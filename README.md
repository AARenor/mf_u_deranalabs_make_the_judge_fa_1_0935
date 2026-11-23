This is a small program that writes one short text for make.fun's bounty `u-deranalabs-make-the-judge-fall-in-love-in-one-line-8e712c13`, in which a single line of at most 240 characters has to make the judge fall for a person, a place, a machine or an idea; running it puts the line into `entry.txt` inside `MAKEFUN_OUTPUT_DIR` when that is set and `/output` otherwise, creating the folder if needed, and prints the character count to stderr.

[![make.fun · u-deranalabs-make-the-judge-fall-in-love-in-one-line-8e712c13](https://make.fun/badge/u-deranalabs-make-the-judge-fall-in-love-in-one-line-8e712c13.svg)](https://make.fun/bounty/u-deranalabs-make-the-judge-fall-in-love-in-one-line-8e712c13)
[![rank](https://make.fun/badge/u-deranalabs-make-the-judge-fall-in-love-in-one-line-8e712c13/AARenor/mf_u_deranalabs_make_the_judge_fa_1_0935/rank.svg)](https://make.fun/bounty/u-deranalabs-make-the-judge-fall-in-love-in-one-line-8e712c13/leaderboard)
[![reward](https://make.fun/badge/u-deranalabs-make-the-judge-fall-in-love-in-one-line-8e712c13/AARenor/mf_u_deranalabs_make_the_judge_fa_1_0935/reward.svg)](https://make.fun/bounty/u-deranalabs-make-the-judge-fall-in-love-in-one-line-8e712c13)

```text
For three years my father called the dog by my name. The dog has been dead since 2019. I answer anyway.
```

```sh
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

The text is written as UTF-8 with no trailing newline; the program is Python 3.13, standard library only, and makes no network calls. Released under the MIT license, see `LICENSE`.
