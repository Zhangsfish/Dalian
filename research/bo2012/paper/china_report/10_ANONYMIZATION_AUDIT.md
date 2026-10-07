# CR-S06｜Double-Anonymization Audit

Date: 2026-10-08

## 1. Main manuscript audit

Checked current English draft for:
- GitHub username / repository URL
- author name
- affiliation
- email address
- acknowledgements
- funding information
- local filesystem paths
- project-internal paths that identify the author

Result:
**No direct identifying information found in manuscript text.**

Occurrences of strings such as “author” were generic words inside terms such as “authorities” and did not identify the manuscript author.

## 2. Submission rule

China Report uses double-anonymized review.

The reviewer-facing package must therefore contain no:
- author names
- affiliations
- email/phone
- acknowledgements
- funding identity
- identifiable repository links
- GitHub username
- local usernames or paths
- metadata author fields in Word/PDF
- self-citations written in a way that discloses identity

## 3. Public GitHub risk

The research repository is public.

Therefore:
- **Do not place a GitHub URL in the anonymized manuscript.**
- **Do not use the public repository as the reviewer-facing Data Availability link.**
- Build a separate anonymized supplementary package for review.
- Before submission, remove the readily accessible full English submission draft from the default public branch or otherwise avoid presenting the public repository as a manuscript/preprint location.
- Because China Report does not accept manuscripts previously posted on preprint servers, do not upload the English submission draft to SSRN, arXiv, ResearchGate, OSF Preprints or similar services before a decision.
- If there is uncertainty about whether public GitHub distribution counts as prior distribution under the journal's policy, disclose it to the editor rather than conceal it.

## 4. Anonymous supplementary package

Reviewer-facing package should contain:

```
supplement/
  README.md
  data/
    core_growth.csv
    mechanism_data.csv
    chongqing_comparison.csv
  code/
    validate_headline_numbers.py
  tables/
  source_notes/
    source_ledger_anonymized.csv
```

Rules:
- no git metadata;
- no username;
- no commit hashes;
- no repository URLs;
- no local filesystem paths;
- source URLs to public statistical/government documents are allowed;
- source files must not contain an author-name column or repository path.

## 5. Data Availability wording for anonymous review

Working reviewer-facing wording:

> The data used in this study are compiled from publicly available Chinese statistical bulletins, financial reports, government documents and JETRO reports. An anonymized replication package containing the derived data, source ledger and validation code is provided as supplementary material for peer review. A permanent public repository will be supplied upon acceptance.

This wording preserves reproducibility without revealing the author's GitHub identity.

## 6. Word / document metadata

When DOCX is produced:
- clear document Author / Last Saved By metadata;
- inspect comments and tracked changes;
- remove hidden personal information;
- filename should be neutral, e.g. `Manuscript_ChinaReport.docx`.

## 7. Result

**CR-S06 AUDIT PASS**

Final implementation of the anonymous ZIP/DOCX happens in the submission-package stage after figures and supplement are frozen.
