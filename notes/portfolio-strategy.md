# Praveen Mangalagiri: Portfolio and Resume Strategy

_Research date: 2026-10-06. Source resume: `Praveen-Mangalagiri-TPM-DRE-Resume.docx`_

## 1. How recruiters find people now

- **LinkedIn Recruiter** searches on title, skills, location and boolean keywords. It matches mostly against the **headline, job titles, Skills section and About**. The headline is the field that carries the most weight in search.
- LinkedIn matching is now LLM-based and groups skills into "clusters". Using the same vocabulary everywhere (headline, titles, bullets, skills) builds a stronger cluster than one long keyword dump.
- One guide claims profiles with 5 or more relevant skills are found up to 31x more often. Fill all skill slots and pin the top 3.
- Turn on **Open to Work (recruiters only)**. It is private to the current employer.
- **ATS (Workday, Greenhouse, Lever, iCIMS):** use a single-column .docx with standard headings and no tables or text boxes for key content. Spell out each acronym once, e.g. "Engineering Change Notice (ECN)".

## 2. Target roles and the keywords they use

The resume has two lanes. Keep **two resume variants**. LinkedIn and the website can blend both.

| Lane | Typical titles | Keywords to include (✗ = missing from current resume) |
|---|---|---|
| **Design Release Engineer** (OEMs, Tier 1s: Ford, GM, Stellantis, Nissan, Toyota, Magna, Expleo, Hinduja) | DRE, Sr. DRE, Product Design & Release Engineer, BIW/Closures DRE | BOM ✗, ECN / ECR / ECO ✗, DFMEA ✗, PFMEA ✗, APQP ✗, PPAP ✗, design freeze / TKO ✗, Teamcenter, CATIA V5, NX, GD&T, tolerance stack-up, DVP&R, NVH, sealing, spot weld / adhesive joining ✗ |
| **Hardware / Vehicle TPM** (EV and AV: Lucid, Rivian, Zoox, Waymo, Tesla, Nuro, Aurora, Scout, Slate) | Technical Program Manager – Vehicle Hardware, Vehicle Integration Engineer, NPI Program Manager | schedule & milestones, Gantt / MS Project / Smartsheet ✗, dependency management, risk register ✗, cross-functional (systems, safety, supply chain, manufacturing), NPI ✗, EVT/DVT/PVT ✗ (AV companies use these), build readiness, SOP, sensor integration, autonomous hardware |

Spell out tools: write **"Jira, Confluence"** instead of "Atlassian", because recruiters search for the product names.

## 3. Resume fixes (current .docx)

**Must fix**
1. **Lucid role dates vs. tense.** The dates say "06/2025 – 06/2026" but the bullets use present tense ("Own", "Lead"). If he is still there, write "06/2025 – Present". If not, switch to past tense and explain the gap.
2. **Patent labels.** Confirmed pending, so the numbers can be used on the resume and the site. The "18/790,943" numbers are **U.S.** application numbers, not PCT. Write: *U.S. Patent Application No. 18/790,943 (Patent Pending)*. Drop the internal Nissan docket codes (NTCNA-…), which mean nothing outside Nissan.
3. **Very few metrics.** Only Ford has one ($12M). Add numbers wherever he can defend them: number of parts or assemblies released, ECNs processed, build issues closed, teams coordinated, prototype builds supported, days of launch delay avoided, weight or cost deltas.
4. **"LinkedIn" has no URL.** Use the full vanity URL, e.g. linkedin.com/in/praveen-mangalagiri.
5. **Inconsistent locations.** Rivian and Canoo entries need the same location format as the others.
6. **Undergraduate degree missing.** Add the BS/BE if he has one. Some ATS filters require a bachelor's.

**Should fix**
- Summary: open with the target title and a hook. *"Design Release Engineer and Vehicle Hardware TPM with 9 years taking BIW, chassis and autonomous-sensor structures from concept to SOP at Lucid, Nissan, Rivian and Ford."* Client OEM names are his strongest asset, so put them in line one.
- Consultancy formatting: "Goken America | Client: Lucid Motors" is good. Keep it, and on LinkedIn put the OEM name in the title line, e.g. "Design Engineer – Lucid Motors (via Goken America)", so searches on the OEM find him.
- Cut the coursework line (Thermo, CFD, Gas Turbines). It is noise for this level of experience.
- Turn the competencies list into 3 groups: **Engineering**, **Program**, **Tools**.

## 4. LinkedIn profile

- **Headline (220 chars):** `Design Release Engineer | Vehicle Hardware TPM | BIW & Body Structures · Autonomous Sensor Integration · EV Launch | Lucid · Nissan · Rivian · Ford | Teamcenter · CATIA · GD&T`
- **About:** first 2 lines are visible without expanding, so lead with the result. Then 3 short paragraphs (what he does, proof points, what he is looking for), ending with a keyword line.
- **Featured:** link to the portfolio site, the published patents and the resume PDF.
- **Skills:** fill all slots and pin *Design Release*, *Body-in-White*, *Technical Program Management*.
- **Custom URL**, and a banner image that matches the website's look.

## 5. Website: what modern engineering portfolios look like in 2026

Trends worth using:
- **Typography-led hero.** A large, confident headline instead of a stock car photo.
- **Bento grid.** Modular tiles for programs, metrics and patents. Easy to scan in 30 seconds.
- **Case studies that show process.** Problem → constraints → approach → outcome. This is also the standard way to stay NDA-safe: use generic renders or diagrams and functional descriptions, with no client CAD, logos or title blocks.
- **Lightweight, fast, mobile-first, accessible**, with dark and light themes.
- **Machine-readable.** schema.org `Person` JSON-LD, good meta tags and a downloadable ATS resume, so AI sourcing tools and Google parse it correctly.

### Proposed site structure (single page with case-study sections)

1. **Hero:** name, a one-line value statement, the OEM names, and two buttons: *Download Resume*, *Contact*.
2. **Impact strip:** 9 yrs · 6 OEM/EV programs · 3 patents pending · ~$12M cost savings · L4 AV integration.
3. **Concept → SOP lifecycle:** an interactive timeline (Concept → Requirements → Design → Release → Prototype → Launch → SOP) showing which program he owned at each stage. This is the signature visual and fits his "lifecycle" story.
4. **Case studies (bento grid, 4–5 cards):**
   - L4 autonomous roof/sensor structure integration (Lucid)
   - Underbody and rear floor release plus the windshield launch save (Nissan Pathfinder / QX60)
   - Skateboard launch: resident engineer, build-stopper triage (Rivian)
   - $12M BIW cost optimization (Ford)
   - Occupant package & ergonomics (Canoo)
5. **Patents:** 3 "Patent Pending" cards, each with the title, the U.S. application number and a one-line plain-English description.
6. **Toolkit:** grouped skill chips (CAD / PLM / Analysis / Program).
7. **Contact:** email and LinkedIn. **No phone number on the public site.**

**Visual direction:** "engineering drawing meets premium EV." A near-black / off-white palette, one accent (electric teal or signal orange), thin blueprint grid lines, monospaced labels for specs, and subtle scroll motion. Lucid and Rivian websites are the tone reference, but the design should be original.

**Hosting:** a static site (one HTML/CSS/JS bundle) on GitHub Pages, Netlify or Vercel, with a custom domain (e.g. praveenmangalagiri.com, about $12/yr).

## 6. Open questions for Praveen

- Is he still at Lucid, or has the contract ended?
- Which lane comes first: DRE or TPM?
- Any numbers he can defend (part count, ECNs, issues closed, team size)?
- Undergraduate degree?
- A headshot, and any shareable non-proprietary images (personal CAD, sketches, public program photos)?

## Sources
- [LinkedIn profile optimization for recruiters (ATS Verification, 2026)](https://atsverification.com/blog/how-to-optimize-linkedin-profile-for-recruiters/)
- [LinkedIn profile optimization guide 2026 (ResumeGeni)](https://resumegeni.com/blog/linkedin-profile-optimization-2026)
- [How recruiters use LinkedIn (Careerflow)](https://www.careerflow.ai/blog/how-recruiters-use-linkedin)
- [Web design trends 2026 (Firebrand)](https://firebrandagency.com/articles/web-design-trends-2026)
- [Web design trends for 2026 (DEV)](https://dev.to/admiracreativos/web-design-trends-for-2026-what-developers-need-to-know-4n1g)
- [Personal website for engineers (techinterview.org)](https://www.techinterview.org/post/3233474627/personal-website-portfolio-engineers/?format=md)
- [Confidential engineering portfolio (GrabCAD)](https://blog.grabcad.com/blog/2015/05/19/confidential-engineering-portfolio/)
- [Design Release Engineer – BIW/Closure posting (Expleo)](https://expleo-jobs-in-en.icims.com/jobs/53029/design-release-engineer---biw-closure/job)
- [Design Release Engineer posting (Hinduja Tech)](https://hindujatech.com/perm-postings/design-release-engineer)
- [Zoox Sr/Staff TPM – Compute Hardware](https://jobs.lever.co/zoox/d9496a78-88b3-4c62-bea2-0eb61288aa9c)
- [Waymo TPM – Hardware Programs](https://zerogtalent.com/space-jobs/waymo/technical-program-manager-hardware-programs-7671186)
