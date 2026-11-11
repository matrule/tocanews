---
title: "UK-hosted low-code platforms compared (2026)"
subtitle: "What \"UK-hosted\" can mean, which low-code and integration platforms offer it, and how to check before you buy."
date: 2026-11-11
updated: 2026-11-11
author: "Mat Rule"
author_role: "Founder and CEO, Toca"
tag: "Blog"
sites: ["io", "health", "legal"]
image: ""
---
**The short answer.** "UK-hosted" means one of three things, and they are not the same. A global platform running in its **UK cloud region** keeps your data in the UK but runs on the vendor's terms. A **UK vendor hosting in UK data centres** adds a UK company answering for it. A platform you can **run in your own tenancy or on your own servers** keeps everything inside your boundary. Power Platform offers the first; Netcall and Responsiv the second; n8n and Responsiv's self-hosted product the third; Toca offers all three, its UK cloud, your tenancy or your own servers, air-gapped if you need it. Decide which one your data actually needs, then check the vendor's G-Cloud listing or contract, not just its website. Toca is ours, so read this with that in mind.

## The three kinds of UK hosting

| Kind | What you get | What to check | Fits |
|---|---|---|---|
| A global cloud's UK region | Data stored and processed in the UK, on the vendor's global platform | Which features or AI services can move data outside the UK, and who can switch them on | Most commercial work where UK residency is enough |
| A UK vendor in UK data centres | UK residency, plus a UK company running the service | The data centres' certification, the sub-processors, and whether you can choose location | Public sector and regulated work that wants a UK supplier |
| Your own tenancy or servers | Nothing leaves your boundary; you control the infrastructure | Which product and plan allow self-managed deployment, and who patches it | Health, legal and financial work where data cannot leave the building |

## The platforms

These are the platforms that come up when UK buyers ask, described from each vendor's own published information or G-Cloud listing on 11 November 2026. Check the current terms before you shortlist; hosting options often depend on the plan.

| Platform | What it is | UK hosting, as published | Choose it when |
|---|---|---|---|
| **Microsoft Power Platform** | Low-code apps, automation and RPA in Microsoft 365 | Microsoft's cloud in the region you choose, the UK included; on-premises systems reached through a gateway | You are on Microsoft 365 and the work is team-level |
| **Netcall Liberty Create** | UK low-code platform for public sector, health and utilities | UK hosting on AWS; storage and processing in the United Kingdom (G-Cloud listing) | UK public sector or NHS portals and case management, bought through G-Cloud |
| **Responsiv** | UK integration and automation platform | Responsiv Cloud in ISO 27001 certified UK data centres; Responsiv Unity self-hosted | Integration-led work where you want a UK specialist, managed or self-hosted |
| **n8n** | Workflow automation with an open, self-hostable core | Self-host it anywhere, including your own UK infrastructure; or its cloud | Your technical team wants to run and extend workflow automation itself |
| **Mendix, OutSystems** | Enterprise low-code application platforms | Vendor clouds, or self-managed on the products and plans that allow it | You are building a portfolio of complex applications with your own developers |
| **Toca** | UK-hosted low-code automation, integration, apps and document AI (Spectral) | Toca's UK cloud, your own tenancy, or your own servers, air-gapped if needed | Regulated, high-volume processes across several systems, with documents read and a person deciding |

## What to ask every vendor

1. **Where exactly is my data stored and processed?** In the UK, and can I choose? Netcall's G-Cloud listing, for example, states United Kingdom and that users cannot change it, which is clear either way.
2. **Can any feature move data outside the UK?** AI features are the usual exception. Microsoft, for instance, says some generative AI features can process UK data outside the UK once an administrator allows it.
3. **Can it run in my own tenancy or on my own servers, and on which plan?** "Self-managed is available" often means a particular product or tier.
4. **Who are the sub-processors?** A UK data centre run under a non-UK parent may still matter to your DPIA.
5. **What is certified?** ISO 27001 for the service, Cyber Essentials Plus, and for health, DSPT and the clinical safety standards. For AI, ISO 42001.
6. **How does it reach systems with no API?** Regulated work usually involves at least one: an old case management system, a portal, a desktop application. Ask whether it is API, RPA or code, and who maintains it.
7. **What does it cost at your volume?** Per user, per bot, per app or per workflow: model three years at your real numbers.

## How Toca does it

Toca is a UK company. The platform runs in Toca's UK cloud, in your own cloud tenancy, or on your own servers, air-gapped if the data cannot leave the building, and you choose for each deployment. It brings apps and portals, automation, integration (APIs where they exist, RPA where they don't, C# when neither is enough) and Spectral, which reads documents with more than one model and sends any disagreement to a person. Toca holds ISO/IEC 27001, ISO/IEC 42001 and Cyber Essentials Plus, and Spectral is UKCA-marked as a Class I medical device. It runs eTriage across NHS trusts, claims work for UK volume law firms, and payroll for around 1,750 schools at EPM. See [the platform](https://www.toca.io/platform) and [certifications](https://www.toca.io/company#trust).

## When to choose something else

- **Power Platform**, if UK residency in Microsoft's cloud is enough and your people already have the licences.
- **Netcall**, if you are a council or NHS body buying a portal or case management product through G-Cloud and want a supplier with that track record.
- **Responsiv**, if the job is mainly integration and you want a UK specialist.
- **n8n**, if your engineers want to self-host and extend workflow automation themselves.
- **Mendix or OutSystems**, if you are building many complex applications with a large development team.

## Questions

### What does UK-hosted mean for a low-code platform?

That your data is stored and processed in the UK. It can mean a global cloud's UK region, a UK vendor's UK data centres, or the platform running in your own tenancy or servers. Ask which, and whether any feature can move data elsewhere.

### Which low-code platforms can run on our own servers?

Several offer self-managed deployment, often on particular products or plans, including Mendix, OutSystems, n8n, Responsiv Unity and Toca. Check which features run self-managed, not only that it is possible.

### Is Power Platform UK-hosted?

It can run in Microsoft's UK region. Systems on your own network are reached through the on-premises data gateway, and some generative AI features can process data outside the UK if an administrator allows it.

### What should a DPIA check about a low-code platform?

Where data is stored and processed, the sub-processors, which features can move data, certifications, and who can access production. G-Cloud listings state several of these in a standard form.

### Are there UK low-code platforms on G-Cloud?

Yes. Netcall Liberty Create, Responsiv and Toca all list services on G-Cloud; search the Digital Marketplace for "low-code platform" to see the current list.

## Sources

- Netcall, [Liberty Create on G-Cloud](https://www.applytosupply.digitalmarketplace.service.gov.uk/g-cloud/services/647914775105348) (hosting and data location)
- Responsiv, [Cloud solutions](https://responsiv.co.uk/cloud-solutions/) and [Responsiv Unity](https://responsiv.co.uk/products-hub/responsiv-unity/)
- Microsoft, [Power Platform regions overview](https://learn.microsoft.com/en-us/power-platform/admin/regions-overview), checked 10 November 2026
- [n8n](https://n8n.io/), [Mendix](https://www.mendix.com/), [OutSystems](https://www.outsystems.com/): each vendor's site for current deployment options
- Toca on G-Cloud 15: [the platform](https://www.applytosupply.digitalmarketplace.service.gov.uk/g-cloud-15/services/242159311913983), [Spectral](https://www.applytosupply.digitalmarketplace.service.gov.uk/g-cloud-15/services/424712051726736)
