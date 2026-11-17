---
title: "Data sovereignty for law firms: a practical framework (2026)"
subtitle: "What control of your systems and client data means for a law firm, what the SRA expects, what happens when it goes wrong, and how to keep control of your own work."
date: 2026-11-16
updated: 2026-11-17
author: "Keith Sutton"
author_role: "Sales Director, Toca"
tag: "Guides"
section: learn
sites: ["io", "legal"]
image: ""
---

For most law firms, moving to cloud computing has been a sensible decision. Email, documents, case management and communications are handled by specialist providers rather than a server in a cupboard, and the services are generally better maintained, more secure and easier to manage.

But putting so much of the firm's operation in somebody else's hands raises two questions. What happens when that provider has a problem? And who actually controls the information the firm holds for its clients?

The Microsoft 365 outage on 12 and 13 November 2026 answered the first bluntly: email, Teams, SharePoint and other services were disrupted across more than seventy countries. The second is less visible. A provider can store information in a UK data centre while remaining subject to the laws of another country, so choosing a UK region does not necessarily put client data beyond the reach of foreign authorities.

Neither problem means abandoning the cloud. Both lead to the question at the heart of data sovereignty: how much control does a law firm actually have over its own data and the systems it depends on? The SRA expects firms to consider it, even though it does not say where their data must be stored.

The answer is not to bring everything back in-house. It is to separate the systems that need to stay under your control from those better left to specialist providers. That is the approach we have taken in building Toca, a UK platform for applications, automation and AI that can run in Toca's UK cloud, a customer's own cloud or on their own servers. I'll come back to how that works later.

## The strongroom has moved, but who holds the keys?

For most of the profession's history, client information lived in the strongroom, the archive and, later, a server somewhere in the office. Now email, documents, telephones, messaging and increasingly case management sit in somebody else's data centre, and for many UK firms that somebody is Microsoft.

There were good reasons for the move. The security, expertise and economies of scale of the major providers are hard for any individual firm to match. The downside is that when something goes wrong, everybody connected to the same service is affected at once. In November, an issue introduced during an infrastructure upgrade disrupted Exchange Online, Teams and SharePoint, and customers had no control over the change and no way of preventing it.

Control has a legal side too. In June 2025, Microsoft's director of public and legal affairs in France told a French Senate inquiry that he could not guarantee French customer data would never be passed to US authorities without French agreement. Around the same time, the Associated Press reported that the chief prosecutor of the International Criminal Court had lost access to his Microsoft email after US sanctions; Microsoft disputed that it had stopped providing services to the court. Neither involved a law firm, but both show that a provider's legal obligations do not always align with its customers' expectations.

So the question is not whether to use the cloud. It is whether the firm understands who controls the services it uses, what happens when they fail and how much independence it keeps over its own work.

## Data residency and data sovereignty are not the same thing

**Data residency** describes where information is physically stored, and Microsoft, Amazon and Google all offer UK regions. **Data sovereignty** is broader: which laws govern the information, who controls the service and whether the firm can keep working when something goes wrong.

| Question | Does UK residency answer it? | What sovereignty requires |
|---|---|---|
| Where is the data stored? | Yes, subject to configuration | Known locations for primary data and backups |
| Which country's laws can reach it? | No | Understanding provider ownership and legal obligations |
| Who can suspend the service? | No | Understanding provider powers and having alternatives |
| Can the firm work during an outage? | No | Independent continuity arrangements |
| Can the firm leave the provider? | No | Contractual exit rights and usable data exports |

Under the US CLOUD Act of 2018, US authorities can use valid legal process to require a US-based provider to produce information in its possession, custody or control, wherever that information is stored. Putting client information in a UK region of a US-owned cloud does not, by itself, take it out of reach of US law. That does not mean US authorities can browse a UK firm's files, since legal procedures apply, but the location of the data centre is not the whole story. Nor is a UK provider beyond the reach of government: it is subject to UK law, including UK investigatory powers. The aim is to understand jurisdiction, not to escape it.

Residency does nothing for resilience either. A UK data centre can be running perfectly well while the systems needed to reach it are down.

## What does the SRA actually expect?

The SRA does not require firms to store client information in the UK, nor does it prohibit international cloud providers. It requires them to remain accountable for their obligations, whoever provides their technology. These parts of the Code of Conduct for Firms are the most relevant.

| Code provision | Requirement | Practical implication |
|---|---|---|
| 2.1 | Effective governance, systems and controls | Somebody must own the firm's approach to data and suppliers |
| 2.2 | Records demonstrating regulatory compliance | Maintain a register of systems, providers and decisions |
| 2.3 | Accountability for work carried out through others | Outsourcing IT does not outsource responsibility |
| 2.5 | Management of material business risks | Provider failure and supplier lock-in belong on the risk register |
| 3.3(b) | Access to relevant information held by third parties carrying out critical functions | Supplier contracts must support SRA inspection |
| 3.5 | Honesty and openness with clients when things go wrong | Have a plan for explaining and addressing incidents |
| 3.9 and 3.10 | Reporting serious breaches and other relevant matters | Assess incidents and record reporting decisions |
| 6.3 | Confidentiality of current and former clients' affairs | This applies to information held by third parties too |
| 9.1 | COLP responsibility for compliance | The COLP needs visibility of technology risks |

Paragraph 2.3 means a firm cannot assume its managed service provider has everything covered, and under paragraph 2.5 depending on one provider for email, documents, case management and automation is plainly a material risk. The SRA's guidance on confidentiality of client information, updated in June 2022, addresses cloud storage directly: information may be held by third parties, possibly in another jurisdiction, and firms should consider the security arrangements and explain them to clients.

The SRA's own research into cybercrime found that three quarters of the firms it visited used third-party IT providers, and that more than half of those with a disaster recovery plan kept it on their own systems. The plan for recovering from a system failure was stored on the system that had failed.

UK GDPR adds another layer. Article 28 requires a written contract with each processor, Article 32 requires security appropriate to the risk, including the ability to restore access to personal data in a timely manner, and Article 33 requires certain breaches to be reported to the ICO within 72 hours, where feasible. A loss of availability can itself be a personal data breach, and medical and criminal records bring the stricter rules for special category and criminal offence data.

## What happens when a law firm's technology fails?

| Incident | What happened | The lesson |
|---|---|---|
| CTS, 2023 | Around 80 law firms affected by an attack on a UK managed IT provider | One supplier can become a point of failure for many firms |
| Tuckers Solicitors, 2020 | Ransomware affected the firm's systems and court bundles were published online | In-house infrastructure is not automatically secure |
| Legal Aid Agency, 2025 | Cyber attack exposed applicant data and disrupted services | Firms depend on external systems they cannot control |
| Microsoft 365, 2026 | Global infrastructure fault disrupted email and other services | Shared infrastructure creates concentration risk |

**CTS** is the example closest to home for conveyancing and volume firms. When the UK managed IT provider suffered a cyber incident in November 2023, around 80 firms were affected. Some lost email, telephones and case management, completions were disrupted, and work done by hand had to be re-entered when systems returned. A UK provider is not automatically a resilient one, and putting everything with one supplier creates the same concentration risk as a global cloud.

**Tuckers Solicitors** is the counterpoint. In 2020 ransomware encrypted nearly a million of the criminal law firm's files, and court bundles were later published on the dark web. The ICO fined the firm £98,000 in 2022, citing the absence of multi-factor authentication on remote access and a critical vulnerability left unpatched for five months after an NCSC alert. Bringing IT in-house only helps if you have the people and processes to run it properly. A poorly maintained server in your own office can be a far greater risk than a professionally managed cloud service.

**The Legal Aid Agency** attack in 2025 shows the limits of control. Attackers had been inside its systems since December 2024, data on applicants going back to 2010 was taken, including criminal records, and online services were offline for weeks. No firm can guarantee that the government systems and portals it relies on will stay available. What it can do is design its own processes so that work is held safely, queued and resumed when they return.

**Outages are not always attacks.** The November Microsoft outage was not an isolated event, and earlier failures at Microsoft and AWS disrupted services worldwide with no attacker involved. A perfectly secure system can still be unavailable because somebody made a change that did not work as intended.

That is why sovereignty and continuity are connected. Email, calendars, documents and sign-in may all depend on Microsoft, and automation and AI are increasingly being added to the same environment through Power Automate and Copilot. Each decision makes sense on its own; together they can let one provider's outage stop almost everything. The aim is not to abandon Microsoft, but to make sure the work that cannot stop, such as intake, evidence gathering, case updates and portal submissions in a volume firm, does not depend entirely on it.

Some Toca customers on our UK cloud have recorded 100% uptime over the past two years, including the periods when Microsoft and AWS had the outages described above. No provider is infallible, but separating critical work from shared dependencies makes a real difference.

## A practical framework for data sovereignty

The starting point is not another platform or a different cloud. It is understanding what the firm already has and deciding how much control each part needs. I would approach it in six steps.

**1. Map your systems and their dependencies.** List every system that holds client information or that the firm's work depends on: case and document management, email and telephony, finance, client and claims portals, automation and integration platforms, AI tools used by teams, and anything staff have built themselves. For each, record where the data and backups are stored, who operates it, who owns that provider, which laws apply, how people sign in and what depends on it. A system that everybody reaches through Microsoft's sign-in is not independent when that sign-in fails.

**2. Classify the data and the work.** A holiday rota and privileged client documents need different protection, and a reporting dashboard matters less than the system that submits a claim before a limitation deadline. In a high-volume firm the critical work usually includes intake, evidence gathering, portal submissions, client communications and anything tied to a limitation date or completion.

**3. Decide how much control each system needs.** Most firms will end up with a mix.

| Hosting arrangement | What it means | Typical use |
|---|---|---|
| Global software service | Supplier operates the application and decides where its infrastructure runs | Low-risk tools that are easy to replace |
| UK region of a global cloud | Data stored in a UK region, but the provider remains subject to its home jurisdiction | Email and collaboration |
| UK provider under UK law | UK-owned provider operates the service in UK infrastructure | Case work, portals and automation |
| Inside the firm's own boundary | Firm operates its own servers or dedicated environment | Particularly sensitive information and critical applications |

Platforms such as Toca support this mix: applications and automation can run in a UK-hosted environment, a customer's own cloud tenancy or on-premise, chosen by the sensitivity of the data and the importance of the process. Two qualifications apply. A UK tenancy in a US-owned cloud remains subject to that provider's wider legal arrangements, and holding your own encryption keys does nothing about its outages. And a UK provider is not automatically more secure or resilient, so assess its security, resilience and exit terms separately.

**4. Design for the day something fails.** For each critical process, ask what happens if a supporting system is down for a day, then for a week. Work should queue and catch up rather than stop, staff need another way in if the main identity provider fails, and there should be a way to reach colleagues and clients that does not run through the email platform that has just gone offline. Keep the contingency plan somewhere independent of the systems it is meant to recover, and test your backups: taking one is not the same as proving you can restore from it.

**5. Contract for inspection and exit.** Contracts with critical suppliers should cover where data and backups are held, notice of changes to locations and sub-processors, the ultimate parent company, security and incident notification, the SRA's access under paragraph 3.3, business continuity, and how, in what format and how quickly your data comes back when the contract ends. A contractual right to leave is useful. A tested ability to leave is considerably more useful.

**6. Give somebody responsibility for it.** In most firms that means the COLP working with whoever runs IT and information security, with the partners seeing the material risks. Review the register at least annually and whenever a system changes, and include the tools staff build themselves. A system should not escape scrutiny because somebody built it rather than bought it.

## Particular considerations for high-volume law firms

In personal injury, credit hire, conveyancing and other areas where thousands of matters move through a process each month, a short outage can leave a long backlog. Five points deserve particular care.

**Do not replace one concentration risk with another.** Moving everything from a global provider to a single UK supplier leaves the same concentration in place. No single provider should be able to halt the whole operation.

**External portals are not yours.** The Claims Portal, Official Injury Claim, MedCo, HM Land Registry and Legal Aid Agency systems are outside the firm's control, so processes need to hold work, queue submissions and resume when those services return.

**Look for hidden dependencies.** An independent platform can still be locked if it signs people in through Microsoft, and an automated process that reads and sends through Exchange Online stops when Exchange does. Keep alternative access and know which processes depend on email.

**Know where AI sends client information.** A firm can get everything else right and still send client documents to a model in another country because somebody switched on an AI feature in software it already uses. Know where each feature processes data, which model it uses and who can enable it.

**Treat migration as a major risk.** Moving live matters, years of documents and their integrations is harder than setting up the new system. Move in stages, run old and new side by side until they reconcile, and do not switch off the old environment until the new one has proved itself.

None of this means leaving Microsoft 365 because of an outage. It remains a capable platform, and replacing it would be expensive and disruptive for little benefit. Sovereignty is about making sure the firm's most important work and information do not depend unnecessarily on any single supplier.

## What data sovereignty makes possible

There are commercial opportunities too. AI is the obvious one: firms can see the potential of generative AI on client documents, but risk and compliance teams rightly want to know where those documents go and which models process them. When AI runs inside the firm's own environment, or with a UK provider under UK law, the debate moves from whether the firm can use AI to how to use it properly.

Then there is the firm's own data. A firm whose information is spread across a dozen software services relies on each supplier's reports to understand its own operation. Bring case management, finance, portal and document information together under the firm's control, and it becomes much easier to see which work types are profitable, which files are drifting towards trouble, where the delays are and which sources produce the cases that settle well.

It helps win work, too. Insurers, corporate clients and public bodies increasingly ask about data locations, sub-processors, security and continuity, and a firm that can answer from a documented register and tested arrangements is better placed than one that has to ask its IT supplier every time a questionnaire arrives. And a firm with a tested alternative negotiates from strength. Having control does not necessarily mean changing providers. Sometimes it simply means having the option.

## Where Toca fits

Toca is our platform, built for regulated, high-volume work of the sort discussed here. We are a UK company, and the platform runs in Toca's UK cloud, in a customer's own cloud tenancy or on its own servers, air-gapped if information cannot leave the organisation, so a firm can keep its most sensitive applications inside its own environment and run the rest in Toca's UK cloud. Agent bots inside the customer's network connect outbound to the Toca server, so processes in Toca's cloud can still work with a case management system the firm hosts itself. Spectral, our document AI, can run its models inside the customer's boundary, and client documents are not used to train them.

Toca holds ISO/IEC 27001, ISO/IEC 42001 and Cyber Essentials Plus, both the platform and Spectral are listed on G-Cloud 15, and the platform runs around 276,000 workflows a day across our customers, including claims processes for UK volume law firms.

Toca is not a replacement for Microsoft 365. It handles the high-volume work around the case management system, such as intake, evidence gathering, chasing, checking and portal submissions, so that a bad day at Microsoft does not have to stop every process in the firm.

If you want to see how your own systems fit together, [talk to us](https://www.toca.io/contact). We will spend twenty minutes on what you use, what depends on what and which processes would stop if one system failed, then show you a process running end to end with the audit trail in view. There is more on [the Toca platform](https://www.toca.io/platform).

## Frequently asked questions

### What is data sovereignty for a law firm?

It is a firm's ability to understand and control where client information is held, which laws can reach it, who can access or suspend the services holding it, and whether the firm can keep working if a provider fails. Data residency, by contrast, describes only where the information is stored.

### Is client data in a UK region of Microsoft or AWS sovereign?

It is UK-resident, but not sovereign in the full sense. The US parent companies remain subject to US law, including the CLOUD Act, and their UK services depend on shared global infrastructure. That may be reasonable for email and collaboration. For sensitive information and critical work, consider a UK-owned provider or your own boundary.

### Does the SRA require law firms to keep client data in the UK?

No. But the Code of Conduct for Firms requires effective systems and controls (2.1), accountability for work done through others (2.3), management of material risks (2.5), SRA access to information held by critical third parties (3.3) and client confidentiality (6.3). UK GDPR also governs international transfers of personal data.

### What should a law firm's cloud contract include?

Where data and backups are held, the sub-processors and ultimate parent company, security obligations, incident notification timescales, business continuity commitments, the SRA access required by paragraph 3.3, and how, in what format and how quickly data is returned at the end. Article 28 of UK GDPR sets out what any processor contract must contain.

### Does a law firm have to report a cloud outage or cyber attack to the SRA?

It depends on the circumstances. Paragraphs 3.9 and 3.10 of the Code cover serious breaches and other matters the SRA should know about, so assess each incident and record the decision. Separately, a personal data breach likely to result in a risk to individuals must be reported to the ICO within 72 hours, where feasible.

### Should a law firm move away from Microsoft 365?

Usually not, and certainly not because of one outage. The better approach is to identify the work that cannot stop and make sure it does not depend entirely on Microsoft or any other single provider.

### Where should a law firm start with data sovereignty?

Map the firm's systems: where information is stored, who operates each service, which laws apply, how people sign in and what depends on what. Then take the most critical piece of work and work out how the firm would carry on if its main provider were unavailable for a day.

## Sources

- Solicitors Regulation Authority, [Code of Conduct for Firms](https://www.sra.org.uk/solicitors/standards-regulations/code-conduct-firms/), [Confidentiality of client information](https://www.sra.org.uk/solicitors/guidance/confidentiality-client-information/) (updated 30 June 2022) and [How to reduce the risk of being affected by cybercrime](https://www.sra.org.uk/solicitors/resources/cybercrime/cybersecurity-advice/) (23 November 2020).
- [UK GDPR](https://www.legislation.gov.uk/eur/2016/679/contents), Articles 28, 32 and 33; National Cyber Security Centre, [Cloud security guidance](https://www.ncsc.gov.uk/collection/cloud); US Department of Justice, [CLOUD Act resources](https://www.justice.gov/criminal/cloud-act-resources).
- The Register, [Microsoft admits it 'cannot guarantee' data sovereignty](https://www.theregister.com/2025/07/25/microsoft_admits_it_cannot_guarantee/), 25 July 2025; PBS NewsHour (Associated Press), [Trump's sanctions on ICC's chief prosecutor have halted tribunal's work](https://www.pbs.org/newshour/world/trumps-sanctions-on-iccs-chief-prosecutor-have-halted-tribunals-work), 15 May 2025.
- BleepingComputer, [Massive Microsoft 365 outage disrupts Outlook, Teams, Copilot worldwide](https://www.bleepingcomputer.com/news/microsoft/massive-microsoft-365-outage-disrupts-outlook-teams-copilot-worldwide/), and Sky News, [Microsoft outage: 'Underlying issue' explained](https://news.sky.com/story/microsoft-outage-latest-hundreds-of-thousands-of-users-affected-as-fix-not-going-as-expected-13611764), 12 and 13 November 2026; The Register on the [January 2026 Microsoft 365 outage](https://www.theregister.com/2026/01/23/microsoft_365_outage/) and the [October 2025 AWS outage](https://www.theregister.com/2025/10/20/amazon_aws_outage/).
- Law Gazette, [Dozens of conveyancing firms paralysed by cyber attack](https://lawgazette.co.uk/news/dozens-of-conveyancing-firms-paralysed-by-cyber-attack/5118045.article), November 2023; Legal Futures, [Top criminal law firm fined £98,000 for cyber-security "negligence"](https://www.legalfutures.co.uk/latest-news/top-criminal-law-firm-fined-98000-for-cyber-security-negligence), March 2022; The Law Society, [Legal Aid Agency data breach](https://www.lawsociety.org.uk/topics/legal-aid/legal-aid-agency-data-breach).
