---
title: "Power Platform alternatives for regulated, high-volume work (2026)"
subtitle: "When to keep Power Apps and Power Automate, when to look elsewhere, and how the main alternatives differ on hosting, AI and cost."
date: 2026-11-11
updated: 2026-11-11
author: "Mat Rule"
author_role: "Founder and CEO, Toca"
tag: "Comparisons"
section: learn
sites: ["io", "health", "legal"]
image: ""
---
**The short answer.** For regulated, high-volume work, our answer is Toca, the platform we build. It was made for the work Power Platform finds hardest: complex processes that cross several systems, read documents and leave the decision to a person. It runs around 276,000 workflows a day in production, among them eTriage for NHS trusts, claims for some of the UK's busiest law firms and payroll for around 1,750 schools. It is priced per workflow, not per seat, which is typically £1 per referral in NHS acute and general hospitals and £30,000 to £150,000 a year for a law firm. If all you need is everyday team apps inside Microsoft 365, keep Power Platform, because you have already paid for it. The other alternatives each suit a different job: Mendix and OutSystems for large portfolios of applications, Appian and Pega for case management across large organisations, and Camunda and UiPath for engineering-led orchestration and screen automation. We come up against most of them, and we say plainly below where each one fits.

## Why teams outgrow Power Platform

Power Platform is a sensible choice for a straightforward team app. The teams who come to us have run into the same few things, and the one that has brought a number of law firms to our door is how hard a complex app becomes to maintain.

A simple app in Power Apps and Power Automate is quick to build. The difficulty comes as it grows, and it does not grow in a straight line. Every rule, screen and connection added to a complex app makes the next change harder, and the firms we have spoken to found the effort of keeping it running compounding as they went. It does not help that when low-code runs out, server-side code is a Dataverse plug-in, written in C# on .NET Framework and run in a sandbox with a two-minute limit. Toca is built to keep a complex process maintainable. The whole process lives in one workflow, whether a step is an API call, an RPA bot or code, and Git is built into every workspace in Toca 10, so a change can be branched, committed and rolled back. When low-code runs out you write C# on .NET Core, React or Python in a browser IDE with full NuGet, and what you write becomes a drag-and-drop block in the same workflow and the same audit trail.

Volume is the second problem, and for the work we do it is the decisive one. Toca runs around 276,000 workflows a day, in production and not in a pilot, and we think much of that work would be close to impossible to run reliably on Power Platform. An unattended desktop bot there runs one flow at a time, so more work at once means more bots, each under its own licence, on Windows machines you register and look after. On Toca, RPA bots run anywhere and are managed centrally, in the same workflow as the API calls and connectors, under a service account you control.

Cost is the third. The standard connectors come with Microsoft 365, but as soon as an app uses a premium connector, a custom connector or the on-premises data gateway, every person who uses that app needs a premium licence. On Microsoft's UK price list on 11 November 2026, Power Apps Premium was £15.40 per user per month and Power Automate Premium £11.50 per user per month, while each unattended desktop bot (Power Automate Process) was £115.30 a month, all paid yearly and before VAT. The bill therefore moves with headcount and with the number of bots, which makes it hard to predict. Toca is priced per workflow, not per seat, which for this kind of work makes it cheaper and, just as importantly, far more certain. In NHS acute and general hospitals, for example, it is typically £1 per referral, with no other costs. For law firms, as a guide, it is £30,000 to £150,000 a year, depending on how many workflows they run and how many users and apps they have.

The fourth is AI on decisions that matter. Microsoft says Copilot Studio is not intended as a medical device, and it leaves clinical use to whoever builds with it. Some generative AI features can also process UK data outside the UK once an administrator allows it. Toca's document AI, Spectral, is UKCA-marked as a Class I medical device. More than one model reads every document, a person settles every disagreement, and the models can run inside your boundary. For eTriage and Spectral, Toca is the manufacturer and keeps the safety case, with a named Clinical Safety Officer.

Where it runs comes up less often than you might expect. Power Platform runs in Microsoft's cloud, in whichever region you choose, the UK included, and reaches systems on your own network through the on-premises data gateway. For most of the firms we speak to that is fine. It becomes the deciding factor for organisations that need the whole thing inside their own boundary, and Toca gives them that: it runs in Toca's UK cloud, in your own tenancy or on your own servers, air-gapped if the data cannot leave the building, and you choose for each deployment.

None of this matters for an approval flow in Teams. It matters when the process you are automating is the business itself, and that is the work Toca was built for.

## Toca and Power Platform side by side

The same points, set out in one table.

| Pressure point | Power Platform | Toca |
|---|---|---|
| Code when you need it | Dataverse plug-ins in C# on .NET Framework, in a sandbox with a two-minute limit | C# on .NET Core, React and Python with full NuGet, from a browser IDE. What you write becomes a drag-and-drop block in the same workflow and audit trail, and the IP is yours |
| Change control | Solutions and pipelines, with Git through Azure DevOps | Git built into every workspace in Toca 10: branch, commit and roll back |
| Systems with no API | Desktop flows on Windows machines you register, each unattended bot under its own licence | RPA bots run anywhere and are managed centrally, in the same workflow as API calls and connectors, under a service account you control |
| Cost | Per user and per bot: £15.40 per user per month for Power Apps Premium, £11.50 for Power Automate Premium, £115.30 a month for each unattended bot | Per workflow, not per seat: typically £1 per referral in NHS acute and general hospitals, with no other costs; £30,000 to £150,000 a year as a guide for law firms |
| AI on decisions that matter | Copilot Studio is not intended as a medical device; clinical use is left to whoever builds with it | Spectral is UKCA-marked as a Class I medical device. More than one model reads every document, a person settles every disagreement, and the models can run inside your boundary |
| Clinical and regulated work | Build a clinical app yourself and your organisation is its manufacturer, carrying the safety case | For eTriage and Spectral, Toca is the manufacturer and keeps the safety case with a named Clinical Safety Officer, under ISO 42001, ISO 27001 and Cyber Essentials Plus |
| Where it runs | Microsoft's cloud, in the region you choose; your network through a gateway | Toca's UK cloud, your own tenancy or your own servers, air-gapped if the data can't leave the building. You choose for each deployment |

Microsoft's side of the table comes from Microsoft's own documentation, which we checked on 10 November 2026, and from its UK price list on 11 November 2026, paid yearly and before VAT.

## Why teams choose Toca

Toca runs around 276,000 workflows a day across its customers, which is around 574 hours of automated work every 24 hours. It holds ISO/IEC 27001, ISO/IEC 42001 and Cyber Essentials Plus, and the work it runs is work that has to be right.

| Customer | Work | Result |
|---|---|---|
| NHS trusts | eTriage: the referral, patient record and decision on one screen | 15% of England's population will have their GP referrals to secondary care handled through eTriage |
| Winn Group | Repair invoices and the claims lifecycle | Around 160 hours of staff time returned every month |
| Bond Turner | Credit hire rate rebuttal reports | Up to 80% lower cost per report |
| JMK Solicitors | Key dates on personal injury files | 25% fewer files at risk of write-off |
| EPM | Payroll and pensions as a managed service | Payroll for around 1,750 schools, academies and trusts |

> We needed to reduce our case handling duration so that we could process more claims.
>
> Clint Milnes, Chief Information Officer, Winn Group

Toca now processes over a thousand repair invoices a month automatically for Winn Group, and the partnership has since been extended for a further three years.

If you have a process that has outgrown Power Platform, [bring it to us](https://www.toca.io/contact). We will spend twenty minutes on what you have built so far and where it is stuck, and then show you one step of it running end to end on a system like yours, with the sign-off and the audit trail in view.

## The other alternatives at a glance

Each of the other platforms has a job it is suited to. The table sets them beside Power Platform and Toca.

| Platform | What it is | Where it can run | Choose it when |
|---|---|---|---|
| **Power Platform** (Microsoft) | Low-code apps, automation and RPA inside Microsoft 365 | Microsoft's cloud, any region including the UK; on-premises systems through a gateway | You are on Microsoft 365, the work is team-level, and standard connectors cover it |
| **Toca** | UK-hosted low-code automation, integration, apps and document AI (Spectral) | Toca's UK cloud, your own tenancy, or your own servers, air-gapped if needed | You have regulated, high-volume processes across systems, with documents read and a person deciding |
| **Mendix** (Siemens) | Enterprise low-code application platform | Mendix Cloud, or your own cloud, Kubernetes or servers on the plans that allow it | You are building many complex applications with a large development team |
| **OutSystems** | Enterprise low-code application platform | OutSystems cloud; self-managed in your own infrastructure on some products and plans | You want a high-productivity platform for customer-facing and internal apps at scale |
| **Appian** | Process automation and case management | Appian Cloud, self-managed or hybrid | Case management and process orchestration are the centre of the work |
| **Pega** | Case management and decisioning | Pega Cloud, or client-managed on your own AWS, Azure or Google Cloud | You are a large enterprise with complex rules and decisioning across many channels |
| **Camunda** | Process orchestration (BPMN) for developers | SaaS, or self-managed on premises, in a private cloud or air-gapped | Your engineers want to orchestrate services and people with open standards |
| **UiPath** | RPA and agentic automation | UiPath cloud, or self-hosted | Automating many existing applications through their screens is the main job |

Plans and hosting terms change, and several vendors only allow self-hosting on particular plans, so check each vendor's own site before you draw up a shortlist.

## When to choose Toca, and when to choose something else

Toca is the stronger choice when:

- the process is regulated and has to stand up to an audit
- it runs at high volume and has to run reliably
- it crosses several systems, some of them with no API
- documents have to be read, with a person making the decision
- the app has become too complex to maintain where it is
- it has to run in the UK, in your own tenancy or on your own servers
- you want a cost that follows the work and is known in advance

That is the work it already does for NHS trusts, Winn Group, Bond Turner, JMK Solicitors and EPM.

Something else may fit better in these cases:

- **Power Platform**, for approvals in Teams, forms on SharePoint lists and flows that tidy an inbox, where the people building already have the licences and the data already lives in Microsoft 365.
- **Mendix or OutSystems**, when you are building a whole portfolio of complex applications with your own development team.
- **Appian or Pega**, when the heart of the problem is long-running case management and decisioning across a large organisation.
- **Camunda**, when your engineers want open-standard process orchestration and are happy to build the rest themselves.
- **UiPath**, when the main job is automating a large number of existing applications through their screens.

## How to choose

Four questions sort a shortlist quickly, and we have given Toca's answer to each.

**Start with the systems the work has to reach.** Regulated work rarely lives in one modern system, so count the connections you will need. That might be an EPR or a case management system, along with a portal that has no API, a finance ledger and a document store. For each one, ask how it is reached, whether through an API, through RPA working the screens or through code you write yourself, and ask who owns the connector on the day it breaks. On Toca all three sit in one workflow: APIs where they exist, RPA where they do not and C# when neither is enough.

**Then ask about the AI.** If the platform is going to read documents that lead to decisions, such as clinical letters, medical records or bank statements, you need to know how it shows where a finding came from, what it does when it is unsure, who signs off and what is logged. In health, ask whether it is a medical device and how it is marked. In law, ask how it evidences supervision after *Mazur*. Spectral was designed around these questions: more than one model reads every document, a person settles every disagreement, and it is UKCA-marked as a Class I medical device.

**Next, where the work has to run.** If data cannot leave your network, the shortlist narrows very quickly to the platforms you can run yourself. Ask each vendor exactly which product, which plan and which features run self-managed, because a simple yes to the general question can hide a good deal. Toca runs in its UK cloud, in your own tenancy or on your own servers, and Spectral's models can run inside your boundary too.

**Finish with the cost model.** Platforms charge per user, per bot, per app, per workflow or per unit of capacity, and the only fair way to compare them is to model your real volumes over three years. Remember to count the people who only ever approve a single step, because they are easy to leave out. Toca's model is short, because it is priced per workflow: typically £1 per referral in NHS acute and general hospitals, with no other costs.

## Using Power Platform and Toca together

None of this has to be a choice between the two. Toca apps can sign in through Microsoft Entra ID, and Toca's Microsoft 365, Teams and Azure connectors can read mailboxes, post to Teams and file to SharePoint. In the other direction, a Power Automate flow can start a Toca workflow through a webhook, and Copilot Studio agents can use Toca workflows as tools over MCP. Many teams settle on exactly this arrangement, keeping Power Platform for everyday work and running their regulated, high-volume processes on Toca. The full detail is on [Toca and Power Platform](https://www.toca.io/power-platform), set out row by row with Microsoft's side taken from Microsoft's own documentation.

## Questions

### What is the best alternative to Power Platform?

For regulated, high-volume work, Toca. It runs around 276,000 workflows a day for NHS trusts, law firms and schools' payroll, in its UK cloud, in your own tenancy or on your own servers. For other jobs, Mendix and OutSystems suit large portfolios of applications, Appian and Pega suit case management across large organisations, Camunda suits engineering-led orchestration and UiPath suits screen automation.

### How is Toca different from Power Platform?

Toca is built for complex, regulated processes at high volume. The whole process sits in one workflow with one audit trail, whether a step is an API call, an RPA bot or code, and code runs in C# on .NET Core, React and Python without a two-minute sandbox. Its document AI, Spectral, is UKCA-marked as a Class I medical device, and a person settles every disagreement between the models that read a document. It can run in its UK cloud, in your own tenancy or on your own servers, air-gapped if needed, and it is priced per workflow, not per seat. Many teams use both, with Power Platform for everyday team apps and Toca for the regulated, high-volume processes.

### Is there a UK-hosted alternative to Power Platform?

Yes. Toca is a UK company, and its platform runs in its UK cloud, in your own tenancy or on your own servers, air-gapped if required. Power Platform itself can run in Microsoft's UK region, with your own network reached through a gateway, so the real question is usually whether you need the platform inside your own boundary. Toca gives you that choice for each deployment.

### Why do Power Platform costs rise as you scale?

Because of the way the premium features are licensed. Once an app uses a premium connector, a custom connector or the on-premises data gateway, every user of that app needs a premium licence, and every unattended desktop flow that runs at the same time as another needs its own bot licence. Toca is priced per workflow, not per seat: typically £1 per referral in NHS acute and general hospitals, and £30,000 to £150,000 a year as a guide for law firms.

### Can we keep Power Platform and add another platform?

Yes, and many organisations do. They keep Power Platform for everyday team apps and run their regulated, high-volume processes on Toca, with the two joined through Entra ID sign-in, connectors, webhooks or MCP.

### Can AI agents use these platforms safely?

Several of them now let AI agents call workflows as tools, for example over MCP, and how safe that is depends on the controls around it. Ask what the agent is allowed to do, whether every call is logged and where a person signs off. Copilot Studio agents can use Toca workflows as tools over MCP, which keeps the agent inside a workflow with its own sign-offs and audit trail.

## Sources

- Microsoft, [Power Apps pricing (UK)](https://www.microsoft.com/en-gb/power-platform/products/power-apps/pricing) and [Power Automate pricing (UK)](https://www.microsoft.com/en-gb/power-platform/products/power-automate/pricing), read 11 November 2026; [Power Platform licensing FAQ](https://learn.microsoft.com/en-us/power-platform/admin/powerapps-flow-licensing-faq) and [regions overview](https://learn.microsoft.com/en-us/power-platform/admin/regions-overview), checked 10 November 2026
- Vendors' own sites for each platform's deployment options: [Mendix](https://www.mendix.com/), [OutSystems](https://www.outsystems.com/), [Appian](https://appian.com/), [Pega](https://www.pega.com/), [Camunda](https://camunda.com/), [UiPath](https://www.uipath.com/)
- Toca's side: [Toca and Power Platform](https://www.toca.io/power-platform), [the platform](https://www.toca.io/platform)
