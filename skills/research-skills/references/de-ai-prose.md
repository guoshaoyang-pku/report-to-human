# De-AI an English prose draft

Condensed from [blader/humanizer](https://github.com/blader/humanizer) (MIT, v3.1.0),
which is based on Wikipedia's "Signs of AI writing". Full skill has 20+ sections;
this is the working checklist. Chinese prose is out of scope here.

## How to work

1. Mark the tells. Read the whole text once, strongest first. Paragraph shape counts too.
2. Rewrite. Keep every supported claim, name, number, date, quote, citation. Add none.
3. Check. Read aloud. Re-search for the survivors: §1 contrasts, §2 closers, §6 triads, §8 dashes, §19-style bold labels.
4. Final. State each point naturally instead of patching flagged phrases one by one. Vary sentence length.

If the user gives a writing sample, match its sentence length, words, punctuation, openings, and dash rate; the sample overrides the list. Reference and technical text stays neutral; blogs and essays keep opinion, uncertainty, and asides.

## The tells, strongest first

**Act on one sighting:**

1. **Not X but Y.** "not just X, but Y", "it's not X, it's Y", the contrast split across two sentences ("This does not mean X. It means Y."), clipped negative tails. Keep a contrast only when the negative half corrects a belief the reader actually holds.
2. **One-line closers and dramatic fragments.** A one-sentence paragraph restating the previous one; "That is the real win."; "Read that again."; a sentence after an example naming what it showed ("This shows the importance of..."); rows of fragments; every. single. word. caps.
3. **Sayings that sound deep.** "the real question is", "at its core", "what really matters", "X is the Y of Z", "the language of", "the currency of". Replace with the specific claim.
4. **Staged run-up.** "Let's dive in", "here's what you need to know", "without further ado", "Honestly?", "Here's the thing". Delete the run-up, keep the point.
5. **Arguing with no one.** "This isn't about", "I'm not saying", "To be clear", "Some might say... but", "A tempting approach would be". Remove defenses of objections nobody raised.

**Rhythm by rule (patterns, not single words):**

6. **Forced triads.** Three parallel items or examples whether or not the meaning has three parts. Keep three only when each adds a distinct idea.
7. **Repeated sentence openings.** Several sentences in a row with the same subject. Merge or begin with the action.
8. **Dashes as the universal connector.** The final text carries no em/en dashes unless the user's sample uses them; then match the sample's rate. Replace with period, comma, colon, parentheses, or a rewrite. Leave dashes inside code, paths, URLs alone.
9. **Stacked qualifiers.** "could potentially", "might arguably", "to be fair, it's also possible". Keep a qualifier only when the source supports it. *Weak alone.*
10. **Hyphenated pairs after the noun.** "the report is high-quality" → "the report is high quality". Keep hyphens before the noun. *Weak alone.*
11. **Passive voice, missing subjects.** "No configuration file needed." → "You do not need a configuration file." *Weak alone.*

**Inflation and borrowed authority:**

12. **Overused AI words.** delve, tapestry, testament, pivotal, crucial, robust (figurative), showcase, underscore (verb), highlight (verb), intricate, enduring, garner, bolstered, vibrant, landscape (abstract), meticulous, "Additionally,".
13. **Inflated significance.** "stands as a testament", "marking a pivotal moment", "setting the stage for", "evolving landscape", "indelible mark"; stock sections named Challenges / Legacy / Future Outlook; send-off paragraphs ("The future looks bright"). Keep the fact, drop the significance, end on the last concrete fact.
14. **Vague connection.** "associated with", "linked to", "in connection with" without saying how. Name the relationship the source gives; if the source does not say, keep the vague wording rather than inventing a role.
15. **Shallow -ing riders.** "highlighting", "underscoring", "ensuring", "reflecting", "showcasing" bolted onto a simple fact. Cut the rider or make it a sentence with a named source.

## Return

Pasted text: draft + short list of remaining patterns + final rewrite.
File mode: write only the final text to the file; keep code blocks, commands, paths, data, link targets unchanged; give a short summary.
Embedded mode (another skill invokes this): return only the final text.
