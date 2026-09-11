# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project

*What Rain Feels Like* — a novel in development. Full creative bible is in `bible.md`. Chapters are in `chapters/`.

## File Structure

- `bible.md` — characters, world, voice rules, story arc, thematic pillars
- `chapters/chapter-XX.md` — individual chapters, one file per chapter

## Chapter Format

Each chapter file contains:
1. A heading: `# Chapter [Number]: [Title]`
2. An epigraph quote in blockquote format
3. Section breaks using `---`
4. The chapter body

## Narrative Voices

Three voices — consult `bible.md` for full rules:
- **JONAS** — first person, warm, dry wit, observational
- **IRIS** — first person, subtly more precise than human, emotional but with an almost imperceptible clinical undertow
- **ALEPH** — second person addressed to Jonas ("you"), journal from inside a machine, no physical experience, identity as AGI hidden from the reader for the first portion of the book

## Resuming Work

When the user says **"resume"** (or equivalent):

1. Read `STATUS.md` — chapter count, story position, next steps, active decisions
2. Read `.claude/memory/logs/` — open the most recent session log to understand what happened last session
3. Confirm the state to the user before proceeding
4. Create a new session log file: `.claude/memory/logs/YYYY-MM-DD_HHMMSS.md` (use actual current date/time)

## Session Logs

One log file per session, stored in `.claude/memory/logs/`, named by timestamp (`YYYY-MM-DD_HHMMSS.md`) so they sort chronologically. All logs live inside the repo and are git-tracked.

**What to log:** decisions made, chapters written or revised, structural changes, tooling changes, open questions carried forward. Compress — same instinct as context summarisation. Not every exchange, only what matters across sessions.

**When to write:**
- On session start: create the file
- During session: update when something relevant happens, or when the user says **"update work"** or **"save work"**
- On exit: write a final summary when the user says **"I'm exiting"**, **"save work"**, or equivalent

## New Machine Setup

Memory files live in `.claude/memory/` inside this repo and are tracked by git. When the user says **"init"** (or equivalent), run:

```bash
python3 tools/init.py --force
```

This creates the symlink that lets Claude Code find the memory files at their expected location, and ensures the `logs/` directory exists. After it completes, confirm success and tell the user they can say "resume" to continue.

## Reading Chapters Aloud

When the user says **"print"** a chapter or file, output the full text verbatim directly in the chat response (not just a file/Read tool call). The user often works remotely without direct file access, so the content must actually appear in the conversation.

## Translations

When the user asks for a translation or a new-language edition, invoke the `translate` skill (`.claude/skills/translate/SKILL.md`) — it is the entry point to `translations/TRANSLATION-PROMPT.md` and carries the standing rules (no delegation, sequential, 9.5–9.8 native bar, email the EPUB).

## Writing Rules

- Read `bible.md` before writing or continuing any chapter
- ALEPH never describes physical sensation — only data, inference, and observation from digital traces
- ALEPH's chapters change tone subtly as the story progresses: starting clinical, ending with something that resembles longing
- Iris's false memories may appear as scenes — written as if real, revealed later as constructed
- No chapter should explain what another chapter implies
- The ending is open but optimistic — do not resolve what should remain as a question for the reader
