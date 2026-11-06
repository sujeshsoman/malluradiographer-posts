# @malluradiographer Instagram style guide

Canvas: https://claude.ai/artifact/D43oZ8Bmx5Gq18mdrsq49d  (copy the last artboard; change only <title>, <h1>, <p>)
Renderer: claude/render_post.py + claude/post-template.html in this repo (all 12 monthly themes built in). Run: /usr/bin/python3 claude/render_post.py --title T --fact F --out f.jpg  (month = today UK date; --print-theme shows it). Use /usr/bin/python3 (it has Playwright).
To make the canvas artboard match, copy the last artboard and change only <title>, <h1>, <p>.
Copy: title 3-8 words; fact 15-35 words; UK English. Caption <2,000 chars, hook + bullets + "💡" tip + "📚 Source:" + CTA + 10-14 hashtags.
Never post twice in a day; never repeat a topic or the same modality two posts in a row.

## Standing rules (added 2026-11-01 by Sujesh – apply to all automated posts)
- Slide fact: richer than before, about 40-60 words (2-3 short sentences: what it is, why it happens, why it matters to practice). Must still fit the card without clipping; shrink only if needed. Title stays 3-8 words.
- Every slide must show small corner text: "Read the caption for more 👇". The renderer has no option for it and must not be edited, so after rendering, overlay it with Pillow (bottom-left, small, semi-transparent white, clear of the bottom-right logo; draw the 👇 with an emoji font such as Noto Color Emoji, or fall back to a drawn arrow) and save as the final JPG. Check it visually.
- Caption: more detailed than before (still under 2,000 chars): hook, fuller explanation (3-5 sentences), 3-4 emoji bullets, "💡" tip, a fuller reference line "📚 Source: <publication – article title>" (add a second reference where one exists), exact CTA, save/share nudge, 10-14 hashtags.

## Post workflow (added 2026-11-01 – use for every create/improve request, scheduled or manual)
1. Pull skills first. Invoke the matching skills from the library via the Skill tool before drafting: instagram-agent:ig-caption (caption, search terms, lint), instagram-agent:ig-carousel (if the idea is list/step shaped), instagram-agent:ig-reel / ig-story (if that format fits), instagram-agent:ig-audit (what has worked), instagram-agent:ig-plan (format and timing). Add copywriting, storytelling, audience-analysis or visual-description skills where the library has them. Finish every text with instagram-agent:ig-human (remove AI-sounding phrasing).
2. Instagram agent pass (the instagram-agent skills are the IGagent layer): choose format (static, carousel, Reel, story), check first-line hook survives the "... more" cut, one clear CTA, hashtag set, save/share mechanic, accessibility (alt text).
3. Deliver a full draft: hook, concise body, CTA, visual direction (slide title/fact/theme), hashtags, plus a 2-3 line rationale naming the skills applied and what the Instagram pass changed.
4. Improving an existing post: analyse it first with the same framework (hook, clarity, accuracy, CTA, hashtags, format fit), list specific weaknesses, then rewrite with the changes marked.
5. Scheduled runs: skills are used to shape the copy only. All Standing rules, fact verification, no-repeat checks and the publishing steps still apply unchanged; if a skill is unavailable, continue without it and never block publishing.

## Posts made
- 2026-10-19: CT Scanning Began in London (first patient CT scan, 1 Oct 1971) — Classic neon navy, yellow logo — posted
- 2026-10-19: Never Underestimate the MRI Magnet (always-on superconducting field) — Classic neon navy, yellow logo — posted
- 2026-10-19: Why Is the MRI So Loud? (gradient coil noise) — Classic neon navy, yellow logo — posted
- 2026-10-19: Why Is Water Zero on CT? (Hounsfield units) — Classic neon navy, yellow logo — posted
- 2026-10-19: Why Tc-99m Is Nuclear Medicine's Favourite — Classic neon navy, yellow logo — posted
- 2026-10-19: Why Does Distance Cut Your Dose? (inverse square law) — Classic neon navy, yellow logo — posted
- 2026-10-19: What Is the Larmor Frequency? (MRI) — Classic neon navy, yellow logo — posted
- 2026-10-19: How Does an Ultrasound Probe Work? (piezoelectric effect) — Classic neon navy, yellow logo — posted
- 2026-10-19: What Do CT Window Settings Do? (window level/width) — Classic neon navy, yellow logo — posted
- 2026-10-19: T1 or T2: What's Bright Where? (MRI T1 vs T2 contrast) — Classic neon navy, yellow logo — source: Radiopaedia – T1 weighted image; T2 weighted image — posted https://www.instagram.com/p/Dery4urFzou/
- 2026-10-20: What Is the Anode Heel Effect? (X-ray tube intensity gradient) — Classic neon navy, yellow logo — image posts/2026-10-20-anode-heel-effect.jpg — source: Radiopaedia – Anode heel effect — posted https://www.instagram.com/p/Det7EDsFrfl/
- 2026-10-22: Who Won the CT Nobel Prize? (1979 Nobel, Cormack and Hounsfield) — Classic neon navy, yellow logo — image posts/2026-10-22-ct-nobel-prize.jpg — source: NobelPrize.org – The Nobel Prize in Physiology or Medicine 1979 — posted (permalink not returned by Make)
- 2026-10-23: Who Justifies the Exposure? IR(ME)R Explained (referrer vs practitioner, justification) — Classic neon navy, yellow logo — image posts/2026-10-23-irmer-justification.jpg — source: Society of Radiographers – IR(ME)R 2017 practitioner guidance — posted (permalink not returned by Make)
- 2026-10-24: Why Do Gallstones Cast Shadows? (ultrasound acoustic shadowing) — Classic neon navy, yellow logo — image posts/2026-10-24-acoustic-shadowing.jpg — source: Radiopaedia – Acoustic shadowing — posted (permalink not returned by Make)
- 2026-10-25: What Does Grid Ratio Mean? (anti-scatter grid ratio vs dose) — Classic neon navy, yellow logo — image posts/2026-10-25-grid-ratio.jpg — source: Radiopaedia – Grids — posted (permalink not returned by Make)
- 2026-10-26: Why Is PET Always in a Hurry? (F-18 FDG half-life ~110 min) — Classic neon navy, yellow logo — image posts/2026-10-26-pet-fdg-half-life.jpg — source: FDA – Fludeoxyglucose F 18 Injection prescribing information — posted (permalink not returned by Make)
- 2026-10-27: What Is Beam Hardening on CT? (polychromatic beam, streaks and cupping) — Classic neon navy, yellow logo — image posts/2026-10-27-beam-hardening.jpg — source: Radiopaedia – Beam hardening — posted (permalink not returned by Make)
- 2026-10-28: Why Is It Called an X-ray? (Röntgen's 1895 discovery, 'X' for unknown) — Classic neon navy, yellow logo — image posts/2026-10-28-why-called-x-ray.jpg — source: NobelPrize.org – Wilhelm Conrad Röntgen biographical — posted (permalink not returned by Make)
- 2026-10-29: Higher Frequency, Shallower Scan (ultrasound frequency vs penetration and resolution) — Classic neon navy, yellow logo — image posts/2026-10-29-ultrasound-frequency.jpg — source: Radiopaedia – Ultrasound physics — posted (permalink not returned by Make)
- 2026-10-31: Why AP Chest Makes Hearts Look Bigger (AP magnification, cardiothoracic ratio on PA) — Classic neon navy, yellow logo — image posts/2026-10-31-ap-chest-heart-size.jpg — source: Radiopaedia – Increased cardiothoracic ratio — posted (permalink not returned by Make)
- 2026-11-01: How Gadolinium Brightens MRI (gadolinium shortens T1, enhancement bright on T1) — Royal violet, red logo — image posts/2026-11-01-gadolinium-t1.jpg — source: Radiopaedia – Gadolinium-based contrast agents — posted (permalink not returned by Make)
- 2026-11-02: DRLs Are Not Dose Limits (UK national DRLs, third quartile, local review under IR(ME)R) — Royal violet, red logo — image posts/2026-11-02-drl-not-dose-limit.jpg — source: GOV.UK – National Diagnostic Reference Levels (NDRLs) from 11 December 2025 — posted (permalink not returned by Make)
- 2026-11-03: Why Metal Blanks Out MRI Images (susceptibility artefact, gradient echo vs spin echo) — Royal violet, red logo — image posts/2026-11-03-mri-susceptibility-artefact.jpg — source: Radiopaedia – Magnetic susceptibility artifact — posted (permalink not returned by Make)
- 2026-11-04: Higher kVp, Lower Contrast (kVp, penetration vs subject contrast, Compton scatter) — Royal violet, red logo — image posts/2026-11-04-kvp-contrast.jpg — source: Radiopaedia – Tube voltage — posted (permalink not returned by Make)
- 2026-11-05: Why Do Cysts Glow Behind? (ultrasound posterior acoustic enhancement) — Royal violet, red logo — image posts/2026-11-05-posterior-enhancement.jpg — source: Radiopaedia – Acoustic enhancement — posted (permalink not returned by Make)
- 2026-11-06: What Does CT Pitch Mean? (table travel per rotation vs beam width, dose vs image quality) — Royal violet, red logo — image posts/2026-11-06-ct-pitch.jpg — source: Radiopaedia – Pitch (CT)
