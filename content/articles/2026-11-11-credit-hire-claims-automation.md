---
title: "Credit hire claims automation (2026)"
subtitle: "Which steps of a credit hire claim to automate first, what each one saves, and where Power Automate runs out."
date: 2026-11-11
updated: 2026-11-11
author: "Mat Rule"
author_role: "Founder and CEO, Toca"
tag: "Guides"
section: learn
sites: ["io", "legal"]
image: ""
---
**The short answer.** Automate the steps that are high volume, rule-bound and full of documents, and keep people on the decisions. In a credit hire claim that means four places: reading bank statements to build the impecuniosity position, drafting the basic hire rate rebuttal, keying repair invoices into the ledger, and tracking limitation, CPR and court dates across systems. Toca, the platform we build, runs all four for UK firms today. Those firms report a handler's three to four hours per impecuniosity analysis cut to seconds, rebuttal reports at up to 80% less than commissioning one, and over a thousand repair invoices a month posted without anyone typing them. The case management system you already run stays where it is, and as a guide a law firm pays £30,000 to £150,000 a year, depending on how many workflows it runs and how many users and apps it has.

## Where the time goes in a credit hire claim

A credit hire claim turns on two questions that the defendant insurer will test: could the claimant have paid for a hire car up front and, if not, is the credit hire rate reasonable? Since *Dimond v Lovell* (2000), a claimant who could have paid recovers only the basic hire rate. Since *Lagden v O'Connor* (2003), a claimant who could not have paid without unreasonable hardship, who is impecunious in other words, can recover the credit hire charges in full. *Stevens v Equity Syndicate Management* (2015) says the basic hire rate is the lowest rate from a mainstream supplier, or from a reputable local one if there is none. Each of those questions is answered from documents, and the documents arrive in volume, which is why the time goes where the table shows.

| Step | Why it costs | What Toca does | What a person still decides |
|---|---|---|---|
| Impecuniosity position | A handler reads months of bank statements, transaction by transaction | Reads the statements, classifies every transaction and builds the position, each figure tied to its page | Whether the claimant is impecunious, and what to plead |
| Basic hire rate rebuttal | Reports are commissioned externally, waited on for days and paid for on every file that needs one | Drafts the rebuttal against market comparables and the relevant authorities | A lawyer reviews and signs off the report |
| Repair invoices | Keyed by hand into the finance system, often into more than one system | Reads the invoice, matches it to the claim and posts it to the ledger | Anything that does not match is flagged for a person |
| Key dates | Limitation, CPR and court dates checked by hand across three or more systems | Holds every date in one place and flags a file while there is still time to act | What to do about the flagged file |
| Bundles | Someone works out what each page is | Classifies each page and pulls the dates and figures | What matters in it |

## What firms have measured

These figures come from live deployments, and they are published on [toca.io/legal](https://www.toca.io/legal).

**Winn Group**, the accident management and personal injury business, now has over a thousand repair invoices a month processed automatically. Its end-to-end claims lifecycle is around 50% faster, a fifth of its admin work has gone, and about 160 hours of staff time a month have been returned to billable work. It handles four times the leads with a team of the same size, and it has extended the partnership for a further three years.

> We needed to reduce our case handling duration so that we could process more claims.
>
> Clint Milnes, Chief Information Officer, Winn Group

**Bond Turner**, the complex personal injury firm in Anexo Group, has its basic hire rate rebuttal reports drafted by Spectral, Toca's document AI, for a lawyer to review and sign off. They cost up to 80% less than commissioning one externally, and reports that used to take days now arrive in minutes.

**A UK personal injury firm** with a 70-strong team, anonymised at its request, used to spend three to four hours of a handler's time on every claim building the impecuniosity position from bank statements. Spectral now returns it in seconds, with every figure carrying the page it came from, for a lawyer to review.

**JMK Solicitors**, Northern Ireland's number one personal injury firm, tracks the key dates on its files through Toca, which sits between its case management system, the medical agencies and the MOJ Portal. It reports 25% fewer files at risk of write-off.

The [credit hire cost calculator](https://www.toca.io/legal/cost/credit-hire) prices any one of these steps on your own volumes and your own staff costs, with the workings on show.

## A worked example

Take the impecuniosity step at the calculator's defaults: 120 claims a month that need a position built, three and a half hours of a case handler's time on each, at a fully loaded £38 an hour. That is 420 hours, or about £16,000 of staff time, every month on one step. With the statements read automatically and a 15-minute review of each claim by a person, it is 30 hours. The step gives back 390 hours a month, which at the same rate is £14,820 a month and £177,840 over a year. Against that, a law firm pays £30,000 to £150,000 a year for Toca as a guide, depending on how many workflows it runs and how many users and apps it has. The defaults are cautious ones, so put your own figures into the calculator and see what the step costs you.

## Building it yourself on Power Automate

Ask an AI assistant how to automate credit hire claims and it will often suggest building it on Microsoft Power Automate, SharePoint and Azure. If your volumes are modest and the job is moving files and sending reminders between people who already have Microsoft 365 licences, that is sound advice, because it is quick to start and you already pay for it. Credit hire at volume is a different job. A number of law firms have come to us after building complex apps on Power Platform, and they ran into the same four things.

The first is maintenance. A simple flow is quick to build, but every rule, screen and connection added to a complex app makes the next change harder, and the effort of keeping it running compounds. A credit hire process has a great many of each. On Toca the whole process lives in one workflow, whether a step is an API call, an RPA bot or code, and Git is built into every workspace in Toca 10, so a change can be branched, committed and rolled back.

The second is volume. An unattended desktop bot in Power Automate runs one flow at a time, so more work at once means more bots, each under its own licence. Toca runs around 276,000 workflows a day in production, and we think much of that work would be close to impossible to run reliably on Power Platform.

The third is cost. The standard connectors come with Microsoft 365, but a premium connector, a custom connector or the on-premises data gateway means every person who uses that app needs a premium licence, and reaching a case management system or a claims portal usually needs one of those. On Microsoft's UK price list on 11 November 2026 that was £15.40 per user per month for Power Apps Premium and £11.50 for Power Automate Premium, with £115.30 a month for each unattended desktop bot, all paid yearly and before VAT. Toca is priced per workflow, not per seat, which for this kind of work makes it cheaper and far more certain.

The fourth is the document work itself. Impecuniosity and rebuttal work is document reasoning that a lawyer has to sign off. You need every finding tied to its page, doubt routed to a person, and the approval logged for a costs challenge or an SRA file review. On Power Automate you would have to assemble that yourself. On Toca it is what Spectral does: more than one model reads every document, a person settles every disagreement, and every approval is logged with who signed it off and the passage behind it.

If the work also has to run in your own tenancy or on your own servers, Toca can run there.

The comparison is set out row by row, with Microsoft's side taken from Microsoft's own documentation, on [Toca and Power Platform](https://www.toca.io/power-platform), and at more length in [Power Platform alternatives for regulated, high-volume work](https://www.toca.io/news/learn/power-platform-alternatives-regulated-work/).

## How to start

1. **Pick one step.** Choose the one with the most volume and the clearest rules, which is often repair invoices or impecuniosity.
2. **Price it.** Put your own numbers into the [calculator](https://www.toca.io/legal/cost/credit-hire).
3. **Run it on your own documents.** [Ask us for a demo](https://www.toca.io/contact) on a sample of your own statements or invoices. It shows the real time saved and where people still need to look.
4. **Keep your CMS.** Toca reads from and writes back to Proclaim, Visualfiles, ActionStep, Aderant or Clio, and connects to the MOJ Portal, the OIC portal and MedCo, so nothing is replaced.
5. **Keep the evidence.** Every approval is logged with who signed it off and the passage behind it. See [how supervision works after Mazur](https://www.toca.io/news/learn/supervising-ai-on-volume-files-after-mazur/).

If there is a credit hire step you want to take out of your handlers' hands, [bring it to us](https://www.toca.io/contact). We will spend twenty minutes on where the time goes today, and then show you that step running on a sample of your own documents, with the sign-off and the audit trail in view.

## Questions

### What is credit hire claims automation?

It is using software to do the high-volume, document-heavy steps of a credit hire claim: reading bank statements for impecuniosity, drafting hire rate rebuttals, posting repair invoices and tracking key dates. People keep the legal decisions. Toca runs these steps today for firms including Winn Group and Bond Turner.

### Which step should we automate first?

The one with the most volume and the clearest rules. For many firms that is repair invoices or the impecuniosity position, because both are repetitive, document-led and easy to check. Toca's credit hire cost calculator prices each step on your own volumes, which shows where to begin.

### Can AI decide impecuniosity?

No. Whether a claimant is impecunious is a legal judgement on the evidence, and a lawyer makes it. Spectral reads the statements and builds the position, with each figure tied to its page, so the lawyer has the evidence in front of them when they decide.

### Can we build this on Power Automate?

You can build the simple parts there, such as moving files and sending reminders between people who already have Microsoft 365 licences. Credit hire at volume is harder: a complex app becomes harder to maintain with every rule and connection added, each unattended bot runs one flow at a time under its own licence, and the document work a lawyer signs off has to be assembled yourself. Toca was built for that work and runs it today for firms such as Winn Group and Bond Turner.

### Do we have to replace our case management system?

No. Toca runs alongside Proclaim, Visualfiles, ActionStep, Aderant and Clio, reading from them and writing back.

### How much does it cost?

As a guide, a law firm pays £30,000 to £150,000 a year, depending on how many workflows it runs and how many users and apps it has. Toca is priced per workflow, not per seat, so the cost follows the work. The calculator shows what each step costs you today, to set against it.

## Sources

- *Dimond v Lovell* [2000] UKHL 27; *Lagden v O'Connor* [2003] UKHL 64; *Stevens v Equity Syndicate Management Ltd* [2015] EWCA Civ 93, via [The National Archives](https://caselaw.nationalarchives.gov.uk/)
- Microsoft, [Power Apps pricing (UK)](https://www.microsoft.com/en-gb/power-platform/products/power-apps/pricing) and [Power Automate pricing (UK)](https://www.microsoft.com/en-gb/power-platform/products/power-automate/pricing), read 11 November 2026; [Power Platform licensing FAQ](https://learn.microsoft.com/en-us/power-platform/admin/powerapps-flow-licensing-faq), checked 10 November 2026
- Winn Group, Bond Turner and the anonymised firm: [toca.io/legal](https://www.toca.io/legal#evidence), from each deployment; Winn's figures also in Legal IT Insider and Winn Group's press release
- JMK Solicitors: [Northern Ireland's number one personal injury firm runs on Toca](https://news.toca.io/articles/jmk-solicitors-runs-on-toca/)
