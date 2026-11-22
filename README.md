# ESAT Practice

Timed 15-minute ESAT practice sets (10 questions each, the real test's pace of 27 questions in 40 minutes), with worked solutions. Static site on GitHub Pages.

- **Levels**: each module starts with **Foundation** sets (easier than the real test, for building confidence), then **ESAT level** sets pitched at the NSAA/ENGAA Section 1 standard: multi-step questions, answers in symbols, statement combinations and data tables.
- **Sets**: fixed 10-question sets per module. Finishing a set marks it done and records the best score. Use **Mark as done** to set or clear the status by hand.
- **Quick mix**: 10 questions from the chosen modules, starting with ones not yet seen or answered wrongly.
- **Progress**: kept in the browser's localStorage. **Export** and **Import** back it up as JSON.
- Answer options are shuffled for each session.

## Adding questions

Foundation questions live in `tools/questions.py`, ESAT-level ones in `tools/questions_esat.py`. Every question has an independent check in `tools/verify.py`. After editing:

```
pip install sympy
python3 tools/questions.py   # verifies all answers, then writes questions.js
```

The build fails if a keyed answer doesn't match its check, or if a question has no check. A new set is created automatically when questions are added with a new `set` number.
