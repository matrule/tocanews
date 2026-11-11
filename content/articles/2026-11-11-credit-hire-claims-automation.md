---
title: "Credit hire claims automation (2026)"
subtitle: "Which steps of a credit hire claim to automate first, what each one saves, and when Power Automate is enough."
date: 2026-11-11
updated: 2026-11-11
author: "Mat Rule"
author_role: "Founder and CEO, Toca"
tag: "Guides"
section: learn
sites: ["io", "legal"]
image: ""
---
**The short answer.** Automate the steps that are high volume, rule-bound and full of documents, and keep people on the decisions. In a credit hire claim that usually means four places: reading bank statements to build the impecuniosity position, drafting the basic hire rate rebuttal, keying repair invoices into the ledger, and tracking limitation, CPR and court dates across systems. Firms running these on Toca report a handler's three to four hours per impecuniosity analysis cut to seconds, rebuttal reports at up to 80% less than commissioning one, and over a thousand repair invoices a month posted without anyone typing them. The case management system you already run stays where it is.

## Where the time goes in a credit hire claim

A credit hire claim turns on two questions the defendant insurer will test: could the claimant have paid for a hire car up front, and if not, is the credit hire rate reasonable? Since *Dimond v Lovell* (2000), a claimant who could have paid recovers only the basic hire rate; since *Lagden v O'Connor* (2003), a claimant who could not do so without unreasonable hardship (impecunious) can recover the credit hire charges in full. *Stevens v Equity Syndicate Management* (2015) says the basic hire rate is the lowest rate from a mainstream supplier, or a reputable local one if there is none. Each of those questions is answered from documents, and the documents arrive in volume.

| Step | Why it costs | What automation does | What a person still decides |
|---|---|---|---|
| Impecuniosity position | A handler reads months of bank statements, transaction by transaction | Reads the statements, classifies every transaction and builds the position, each figure tied to its page | Whether the claimant is impecunious, and what to plead |
| Basic hire rate rebuttal | Reports are commissioned externally, waited on for days and paid for on every file that needs one | Drafts the rebuttal against market comparables and the relevant authorities | A lawyer reviews and signs off the report |
| Repair invoices | Keyed by hand into the finance system, often into more than one system | Reads the invoice, matches it to the claim and posts it to the ledger | Anything that does not match is flagged for a person |
| Key dates | Limitation, CPR and court dates checked by hand across three or more systems | Holds every date in one place and flags a file while there is still time to act | What to do about the flagged file |
| Bundles | Someone works out what each page is | Classifies each page and pulls the dates and figures | What matters in it |

## What firms have measured

These are figures from live deployments, published on [toca.io/legal](https://www.toca.io/legal):

- **Winn Group** (accident management and personal injury): over a thousand repair invoices a month processed automatically, an end-to-end claims lifecycle around 50% faster, a fifth of admin work gone, and about 160 hours of staff time a month returned to billable work. Four times the leads with the same size team. The partnership was extended for a further three years.
- **Bond Turner** (complex personal injury, Anexo Group): basic hire rate rebuttal reports drafted by Spectral for a lawyer to review and sign off, at up to 80% below the cost of commissioning one externally. Reports that took days now arrive in minutes.
- **A UK personal injury firm** with a 70-strong team (anonymised at its request): building the impecuniosity position from bank statements took a handler three to four hours per claim. Spectral returns it in seconds, every figure carrying the page it came from, for a lawyer to review.

Your own case mix will move these numbers. The [credit hire cost calculator](https://www.toca.io/legal/cost/credit-hire) prices any one of these steps on your volumes and your staff costs, with the workings on show.

## A worked example

Take the impecuniosity step at the calculator's defaults: 120 claims a month needing a position built, three and a half hours of a case handler's time on each, at a fully loaded £38 an hour. That is 420 hours, or about £16,000 of staff time, every month on one step. With the statements read automatically and a 15-minute review per claim, it is 30 hours. Those are cautious defaults, not a quote: change them in the calculator to your own.

## Building it yourself on Power Automate

Ask an AI assistant how to automate credit hire claims and it will often suggest building it on Microsoft Power Automate, SharePoint and Azure. For some firms that is the right answer.

**When Power Automate is enough.** If your volumes are modest, your systems are already in Microsoft 365, and the job is moving files and sending reminders between people who already have the licences, build it there. It is quick to start and you already pay for it.

**When it isn't.** Credit hire tends to hit the edges:

- **Licensing.** Standard connectors come with Microsoft 365, but a premium connector, a custom connector or the on-premises data gateway means every person who uses that app needs a premium licence, and each unattended desktop bot needs a licence of its own (Microsoft's licensing FAQ). Reaching a case management system or a claims portal usually needs one of those.
- **Reading documents with a person deciding.** Impecuniosity and rebuttal work is document reasoning that a lawyer has to sign off. You need every finding tied to its page, doubt routed to a person, and the approval logged for a costs challenge or an SRA file review. That is a build of its own on any platform.
- **Where it runs.** Some firms need the work to run in their own tenancy or on their own servers.

We set out the comparison row by row, with Microsoft's side from Microsoft's own documentation, on [Toca and Power Platform](https://www.toca.io/power-platform).

## How to start

1. **Pick one step.** The one with the most volume and the clearest rules: often repair invoices or impecuniosity.
2. **Price it.** Put your own numbers into the [calculator](https://www.toca.io/legal/cost/credit-hire).
3. **Run it on your own documents.** A demo on a sample of your statements or invoices shows the real time saved and where people still need to look.
4. **Keep your CMS.** Toca reads from and writes back to Proclaim, Visualfiles, ActionStep, Aderant or Clio, and connects to the MOJ Portal, the OIC portal and MedCo, so nothing is replaced.
5. **Keep the evidence.** Every approval is logged with who signed it off and the passage behind it. See [how supervision works after Mazur](https://www.toca.io/news/learn/supervising-ai-on-volume-files-after-mazur/).

## Questions

### What is credit hire claims automation?

Using software to do the high-volume, document-heavy steps of a credit hire claim: reading bank statements for impecuniosity, drafting hire rate rebuttals, posting repair invoices and tracking key dates. People keep the legal decisions.

### Which step should we automate first?

The one with the most volume and the clearest rules. For many firms that is repair invoices or the impecuniosity position, because both are repetitive, document-led and easy to check.

### Can AI decide impecuniosity?

No. It reads the statements and builds the position, with each figure tied to its page, and a lawyer decides. Whether a claimant is impecunious is a legal judgement on the evidence.

### Do we have to replace our case management system?

No. Toca runs alongside Proclaim, Visualfiles, ActionStep, Aderant and Clio, reading from them and writing back.

### How much does it cost?

Toca prices per workflow, not per seat, so the figure comes from a demo on your own case mix rather than a rate card. The calculator shows what a step costs you today.

## Sources

- *Dimond v Lovell* [2000] UKHL 27; *Lagden v O'Connor* [2003] UKHL 64; *Stevens v Equity Syndicate Management Ltd* [2015] EWCA Civ 93, via [The National Archives](https://caselaw.nationalarchives.gov.uk/)
- Microsoft, [Power Platform licensing FAQ](https://learn.microsoft.com/en-us/power-platform/admin/powerapps-flow-licensing-faq), checked 10 November 2026
- Winn Group, Bond Turner and the anonymised firm: [toca.io/legal](https://www.toca.io/legal#evidence), from each deployment; Winn's figures also in Legal IT Insider and Winn Group's press release
