---
title: "Data sovereignty for law firms: a practical framework (2026)"
subtitle: "What control of your systems and client data means for a law firm, what the SRA expects, what happens when it goes wrong, and how to keep control of your own work."
date: 2026-11-16
updated: 2026-11-16
author: "Keith Sutton"
author_role: "Sales Director, Toca"
tag: "Guides"
section: learn
sites: ["io", "legal"]
image: ""
---

For most law firms, the move to cloud computing has been a sensible one. Email, documents, case management and communications are now handled by specialist providers, rather than by servers sitting in a cupboard somewhere in the office. The systems are generally better maintained, more secure and considerably easier to manage.

But there is a consequence to putting so much of the firm's operation in somebody else's hands. What happens when that provider has a problem? And perhaps more importantly, who actually has control of the information the firm holds on behalf of its clients?

The Microsoft 365 outage on 12 and 13 November 2026 brought the first question into sharp focus. Email, Teams, SharePoint and other services were unavailable or disrupted across more than seventy countries. Some organisations struggled to operate for much of the following day. For law firms, where a missed email or an inaccessible case file can have consequences well beyond a day's lost productivity, this is a rather important consideration.

There is another issue. A provider can store information in a UK data centre while remaining subject to the laws of another country. Choosing a UK region does not necessarily mean that your data is beyond the reach of foreign authorities.

Neither problem means that law firms should abandon the cloud. But they do raise a question that deserves more attention: **how much control does a law firm actually have over its own data and the systems it depends on?**

That is what data sovereignty is about. It is also something the SRA expects firms to consider, even though it does not prescribe where their data must be stored.

## The strongroom has moved, but who holds the keys?

For most of the profession's history, looking after client information was relatively straightforward. Deeds and wills went into the strongroom, completed files went into storage and, when computers arrived, the firm's server lived in a cupboard that somebody in the office had a key to.

If a client asked where their papers were, a partner could point to them.

That arrangement has changed considerably over the last fifteen years. Email, documents, telephones, messaging and increasingly the case management system itself now sit in somebody else's data centre. For many UK firms, that somebody is Microsoft.

There were good reasons for making the move. In *The Big Switch*, published in 2008, Nicholas Carr argued that computing would follow the same path as electricity: businesses would stop generating it themselves and buy it as a utility from a small number of large suppliers.

He was largely right. Most firms are better off buying managed services than trying to maintain their own infrastructure. The security updates, specialist expertise and economies of scale available from the major providers are difficult for an individual firm to match.

But utilities have a property we tend to forget until something goes wrong. When they fail, everybody connected to them can fail at the same time.

The Microsoft outage in November was a good example. An issue introduced during an earlier network capacity upgrade surfaced after a subsequent network change. The resulting disruption affected Exchange Online and a wider range of Microsoft 365 services, including Teams, SharePoint, Copilot and Defender. Microsoft reported that the incident was resolved at 16:10 on 13 November, although recovery and the processing of delayed messages took longer.

The important point is that this was not a cyber attack. Microsoft had made a change to its own infrastructure and something went wrong. Customers had no control over the change and no practical way of preventing the resulting outage.

For some organisations, the consequences were more than an inconvenience. NHS staff reportedly returned to paper records, while businesses found themselves unable to access the systems they used to communicate and carry out their work. Some of the law firms we work with faced the familiar problem of having staff who could not access Outlook or Teams.

There is a second issue, which has been developing rather more quietly.

In June 2025, Microsoft's director of public and legal affairs in France was questioned by a French Senate inquiry about whether he could guarantee that French customers' data would never be passed to US authorities without French agreement. He said he could not give that guarantee.

Around the same time, the Associated Press reported that the chief prosecutor of the International Criminal Court had lost access to his Microsoft email account following US sanctions, and had moved to a Swiss provider. Microsoft disputed the suggestion that it had stopped providing services to the court.

Neither incident involved a law firm, but both illustrate an uncomfortable reality. A technology provider has obligations to the country in which it operates, and those obligations do not necessarily align with the expectations of its customers.

So the question is not whether a law firm should use cloud computing. That argument is largely settled. The question is whether the firm understands who controls the services it uses, what happens when those services fail, and how much independence it retains over its own work.

## Data residency and data sovereignty are not the same thing

The distinction is worth understanding because the two terms are often used interchangeably.

Data residency simply describes where information is physically stored. Microsoft, Amazon and Google all offer UK data regions, allowing customers to specify where particular workloads and information are held.

Data sovereignty is a broader question. It concerns the legal jurisdiction governing the information, who can access it, who controls the service and whether the organisation using it can continue to operate independently when something goes wrong.

Consider the difference:

| Question | Does UK data residency answer it? | What sovereignty requires |
|---|---|---|
| Where is the data physically stored? | Yes, subject to the service and configuration | Known locations for primary data and backups |
| Which country's laws can reach the data? | No | Understanding the provider's corporate ownership and legal obligations |
| Who can suspend or restrict the service? | No | Understanding the provider's powers and having alternatives |
| Can the firm continue working during an outage? | No | Independent continuity arrangements |
| Can the firm leave the provider? | No | Contractual exit rights and a tested, usable data export |

The legal jurisdiction question is particularly important.

Under the US CLOUD Act of 2018, US authorities can use valid legal process to require a US-based service provider to produce information within its possession, custody or control, regardless of where that information is physically stored.

In other words, putting client information in a UK region of a US-owned cloud does not, by itself, remove the provider from the reach of US law.

This does not mean that US authorities can simply browse through the files of a UK law firm. There are legal requirements and procedures involved, and the circumstances matter. But it does mean that the location of the data centre is not the whole story.

The provider may also be subject to restrictions on notifying its customer about certain legal demands.

The large cloud providers have responded to these concerns with products marketed as sovereign cloud services. These are worth examining, but firms should look beyond the product name and understand exactly what control has been transferred, retained or delegated.

There is no such thing as a provider that is beyond the reach of every government. A UK company is subject to UK law, including UK investigatory powers. The point is not to eliminate legal jurisdiction. It is to understand it and make an informed decision about where client information should be held.

There is another distinction worth making. Even if the firm is entirely comfortable with the legal arrangements, UK residency does nothing to protect it from a failure in the provider's global infrastructure.

The Microsoft outage demonstrated that quite clearly. A UK data centre can be operating perfectly well while the systems needed to access it are unavailable.

Residency and resilience are two different things.

## What does the SRA actually expect?

The SRA does not require law firms to store client information in the UK, nor does it prohibit the use of international cloud providers.

What it does require is that firms remain accountable for their regulatory obligations, regardless of who provides their technology.

That distinction is important. A firm can outsource its IT, but it cannot outsource its responsibility for looking after client information or ensuring that its services continue to operate properly.

Several parts of the SRA Code of Conduct for Firms are particularly relevant.

| Code provision | What it requires | Practical implication |
|---|---|---|
| 2.1 | Effective governance structures, systems and controls | Somebody must own the firm's approach to data, suppliers and continuity |
| 2.2 | Records demonstrating regulatory compliance | The firm should maintain a register of its systems, providers and decisions |
| 2.3 | Accountability for work carried out through others | Outsourcing IT does not outsource regulatory responsibility |
| 2.5 | Identification, monitoring and management of material business risks | Provider failure, foreign access and supplier lock-in belong on the risk register |
| 3.3(b) | Relevant information held by third parties carrying out critical functions must be available for SRA inspection | Contracts with critical providers must support this requirement |
| 3.5 | Honesty and openness with clients when things go wrong | The firm needs a plan for explaining incidents and putting matters right |
| 3.9 and 3.10 | Reporting serious breaches and other matters that should be brought to the SRA's attention | Incidents need to be assessed and the reporting decision recorded |
| 6.3 | Confidentiality of current and former clients' affairs | The obligation applies to information held by third-party providers too |
| 9.1 | The COLP must take all reasonable steps to ensure compliance | The COLP needs visibility of the firm's technology risks |

Two provisions deserve particular attention.

Paragraph 2.3 makes clear that a firm remains accountable when work is carried out through somebody else. It is not enough to assume that a managed service provider or cloud supplier has everything covered.

Paragraph 2.5 requires firms to identify, monitor and manage all material risks to their business. If a firm depends on one provider for email, documents, case management and the automation that moves work between them, the possibility of that provider becoming unavailable is plainly relevant.

The confidentiality requirement in paragraph 6.3 is equally important. It does not stop applying simply because client information has moved outside the firm's own infrastructure.

The SRA's guidance on confidentiality of client information, updated in June 2022, specifically addresses cloud storage. It recognises that outsourcing includes arrangements for storing data with third parties through cloud services, and that clients may not realise their information is being held by an unregulated third party, potentially in another jurisdiction.

The guidance suggests that firms should explain these arrangements through their terms of engagement and consider the security of the cloud provider. It also points to the National Cyber Security Centre's cloud security guidance.

There is a useful lesson in the SRA's own research.

In a report published in November 2020, the regulator examined how law firms were managing cybercrime risks. Three quarters of the firms it visited used third-party IT providers. The SRA was clear that firms remained responsible for overseeing their cybersecurity, and identified cases where attacks had succeeded because of shortcomings at the IT provider.

Perhaps more concerning was the approach to disaster recovery. More than half of the firms that had a disaster recovery or contingency plan kept it on their own systems.

In other words, the plan for recovering from a system failure was stored on the system that had failed.

That is not much of a contingency plan.

### UK GDPR adds another layer

The SRA is not the only regulator firms need to consider.

UK GDPR places specific obligations on organisations using third-party data processors.

Article 28 requires a written contract containing the appropriate processor obligations. Article 32 requires security measures appropriate to the risk, including the ability to restore access to personal data in a timely manner following an incident.

Article 33 requires a personal data breach that is likely to result in a risk to individuals to be reported to the ICO within 72 hours of the controller becoming aware of it, where feasible.

A loss of availability can itself constitute a personal data breach. It is not necessary for somebody to have stolen or viewed the information.

For firms handling medical records, criminal records and other sensitive client information, the additional requirements around special category and criminal offence data also need to be considered.

The practical point is straightforward. A firm needs to understand where its data goes, who handles it and what happens when something goes wrong. That is not just good IT management. It is part of managing the firm's regulatory obligations.

## What happens when a law firm's technology fails?

The risks are not theoretical. There have been several significant incidents involving law firms and the systems they depend on.

They are worth looking at because each illustrates a slightly different problem.

| Incident | What happened | The lesson |
|---|---|---|
| CTS cyber attack, 2023 | Around 80 law firms were affected by an attack on a UK managed IT provider | A single supplier can become a point of failure for an entire group of firms |
| Tuckers Solicitors, 2020 | Ransomware affected the firm's own systems and court bundles were published online | Running your own infrastructure does not automatically make it secure |
| Legal Aid Agency, 2025 | A cyber attack exposed applicants' data and disrupted online services | Firms depend on external systems they cannot control |
| Microsoft 365, November 2026 | A global infrastructure fault disrupted email and other services | Concentrating too much work with one provider creates operational risk |
| Microsoft and the ICC, 2025 | Questions arose over access to a sanctioned official's Microsoft email account | Corporate and legal obligations can cross national boundaries |

### CTS: when one provider becomes everybody's problem

The CTS cyber incident in November 2023 is probably the most relevant example for UK conveyancing and volume law firms.

CTS was a managed IT provider serving a significant number of legal practices. Following a cyber incident, around 80 firms were reported to have been affected, with some early reports suggesting the number could have been higher.

The extent of the disruption varied between firms, depending on how much of their infrastructure they had placed with CTS.

For some, the consequences were severe. Email, telephones and case management systems were unavailable, and firms had to find alternative ways of communicating and progressing work.

Property completions were disrupted. Some firms reportedly faced questions from lenders about whether they had been affected, including potential implications for their panel status.

The incident was widely reported to have involved exploitation of a Citrix vulnerability, although CTS did not publicly confirm the precise cause. The company's managed systems were not fully restored until late December.

When systems eventually came back, some firms had to re-enter work that had been carried out manually during the outage.

There are two lessons here. First, a UK provider is not automatically a resilient provider. Second, putting everything with one supplier can create exactly the same concentration risk as relying on a global cloud provider.

### Tuckers: bringing IT in-house is not the answer on its own

The Tuckers Solicitors attack provides an important counterpoint.

In 2020, the criminal law firm suffered a ransomware attack that encrypted nearly a million files. Court bundles were subsequently published on the dark web.

The ICO fined the firm £98,000 in 2022, citing shortcomings including the absence of multi-factor authentication on remote access and a critical vulnerability that had remained unpatched for five months after an NCSC alert.

This matters because it would be easy to draw the wrong conclusion from the CTS incident and decide that the answer is to bring everything back in-house.

It isn't.

Control only provides an advantage if you have the people, processes and security measures to exercise it properly. A poorly maintained server in your own office can be a much greater risk than a professionally managed cloud service.

### The Legal Aid Agency: some systems will always be outside your control

The Legal Aid Agency attack in 2025 demonstrates another problem.

The Ministry of Justice detected the incident in April 2025 and subsequently established that attackers had been inside its systems since December 2024.

Data relating to legal aid applicants going back to 2010 was taken, including sensitive personal information and criminal records. The Agency's online services were taken offline for weeks.

Firms carrying out legal aid work were left having to manage without systems used to submit applications and administer cases.

There is no way for a law firm to guarantee that every external system it depends on will remain available. Some of those systems belong to government departments, regulators, portals or other organisations.

The answer is to design the firm's own processes so that work can be held safely, queued and resumed when the external service returns.

### Microsoft and AWS: outages are not always cyber attacks

The November 2026 Microsoft outage was not an isolated event.

In January 2026, another fault in Microsoft's North American infrastructure disrupted Outlook, Teams and other Microsoft 365 services for nearly ten hours.

In October 2025, a configuration change to Azure Front Door caused errors across Azure and Microsoft 365. During the same month, a DNS fault in Amazon Web Services' US East region disrupted services around the world. UK customers of Lloyds, Halifax and Bank of Scotland reported problems accessing their banking services.

None of these incidents required an attacker. They were failures inside the providers' own infrastructure.

That is an important distinction. Cybersecurity is essential, but it is only one part of resilience. A perfectly secure system can still be unavailable because somebody made a change that did not work as intended.

## Why outages are also a question of sovereignty

It is tempting to treat data sovereignty and business continuity as separate subjects. One belongs to the IT department, perhaps, and the other to the risk committee.

In practice, they are closely connected.

Think about how much of a typical law firm's operation now sits behind a single front door. Email, calendars, chat, documents and sign-in are likely to depend on Microsoft. Increasingly, automation and AI are being added to the same environment through Power Automate and Copilot.

Each decision makes sense on its own. Together, however, they can create a situation where a single provider's outage prevents the firm from doing almost anything.

Go back to Nicholas Carr's electricity analogy. Nobody would suggest that a hospital should generate all its own electricity. But hospitals have backup generators for critical areas because some work cannot stop when the grid goes down.

The same principle applies to a law firm.

The objective is not to abandon Microsoft or build a completely independent technology estate. It is to identify the work that cannot stop and make sure that it does not depend entirely on one provider being available.

For a volume law firm, that might mean ensuring that intake, evidence gathering, case updates and portal submissions can continue even if the main email and collaboration environment is unavailable.

The firm might not be able to send an email or access every document, but it should not necessarily have to stop processing every case.

This is where a more independent automation and application layer can make a difference. It can connect the firm's case management system, portals and other services without making all of that work dependent on the same environment as email and chat.

It can also provide a degree of separation between the firm's operational systems and the infrastructure used for general office productivity.

Some of our customers using Toca's own UK cloud have recorded 100% uptime over the past two years, including periods when Microsoft and AWS experienced the outages described above.

That is not an argument that one provider is infallible and another is not. It is an illustration of what separating critical work from a shared dependency can achieve.

## A practical framework for data sovereignty

So what should a law firm actually do?

The starting point is not to buy another platform or move everything to a different cloud provider. It is to understand what the firm already has and decide how much control each part of the operation needs.

I would approach it in six steps.

### 1. Map your systems and their dependencies

Start by listing every system that holds client information or that the firm depends on to carry out its work.

That will normally include:

- Case management and document management.
- Email, telephony and messaging.
- Finance and accounts.
- Client portals and online applications.
- Claims and regulatory portals.
- Automation and integration platforms.
- AI tools used by individual teams.
- Systems built internally by staff.

For each system, record where the data is stored, including backups, who operates it, which company owns that provider and which country's laws may apply.

Also record how people sign in and which other systems depend on it.

That last point is particularly important. A system may appear to be independent, but if everybody accesses it through Microsoft's identity service, it is not independent when that service fails.

### 2. Classify the data and the work

Not every system needs the same level of protection.

A holiday rota and a set of privileged client documents do not have the same requirements. Nor does an internal reporting dashboard have the same operational importance as a system used to submit a claim before a limitation deadline.

Separate the information according to its sensitivity and the work according to its importance.

For a high-volume firm, critical activities are likely to include new matter intake, evidence gathering, portal submissions, client communications and anything connected to a limitation date or property completion.

The SRA's reference to third parties carrying out functions critical to the delivery of legal services in paragraph 3.3 is useful here. It encourages firms to think about which external services are genuinely essential to their ability to deliver legal work.

### 3. Decide how much control each system needs

Once you understand the systems and the information they hold, you can decide what sort of hosting arrangement is appropriate.

Most firms will end up with a mixture. There is little reason to insist that every application runs inside the firm's own infrastructure, but equally there is no reason to assume that a standard global cloud service is suitable for everything.

A useful way of looking at the options is:

| Hosting arrangement | What it means | Typical use |
|---|---|---|
| Global software service | A supplier operates the application and determines where its infrastructure runs | Low-risk tools that are easy to replace |
| UK region of a global cloud | Data is stored in a UK region, but the wider provider remains subject to its home jurisdiction | Email, collaboration and general productivity |
| UK provider under UK law | A UK-owned provider operates the service in UK infrastructure | Case work, client portals, automation and document processing |
| Inside the firm's own boundary | The firm operates its own servers or a dedicated environment under its control | Particularly sensitive information and critical applications |

There are some important qualifications.

A UK tenancy in a US-owned cloud remains subject to the wider legal and corporate arrangements of that provider. Holding your own encryption keys can help control who reads the data, but it does not prevent the provider from experiencing an outage.

Equally, a UK provider is not automatically more secure or more resilient. The CTS incident demonstrates that rather well.

The benefit of using a UK-owned provider is primarily about legal jurisdiction and corporate control. Its security, operational resilience and exit arrangements still need to be assessed separately.

### 4. Design for the day something fails

This is where the exercise becomes practical.

For each critical process, ask what happens if one of its supporting systems is unavailable for a day. Then ask what happens if it is unavailable for a week.

The answers should lead to a few straightforward design decisions.

Work should be able to queue and catch up rather than simply stop. Staff should have an alternative way of accessing essential systems if the main identity provider fails. There should be a way to contact colleagues and clients that does not depend entirely on the email and messaging platform that has just gone offline.

The contingency plan itself should be stored somewhere independent of the systems it is intended to recover.

And backups should be tested. Taking a backup is not the same as proving that you can restore a working system from it.

A backup that has never been restored successfully is rather like a spare tyre that has never been checked. It might be fine, but you probably don't want to discover otherwise on the motorway.

### 5. Contract for inspection and exit

The firm's contracts with critical suppliers deserve more attention than they often receive.

They should cover:

- The locations where client data is stored, including backups.
- Notification before changes to data locations or important sub-processors.
- The identity of sub-processors and the ultimate parent company.
- Security obligations and incident notification timescales.
- The SRA's access to relevant information under paragraph 3.3.
- Business continuity and disaster recovery commitments.
- Data return and deletion when the contract ends.
- The format and timescale for exporting information.

Article 28 of UK GDPR sets out the requirements for processor contracts. But firms should also think about what happens when the relationship ends.

Can you actually get your data back? Is it in a format that another system can use? How long will the supplier take to provide it? What happens to the integrations and historical records?

A contractual right to leave is useful. A tested ability to leave is considerably more useful.

### 6. Give somebody responsibility for it

Finally, the register and the decisions need an owner.

In most firms, this should involve the COLP working alongside whoever is responsible for IT and information security. The partners should have visibility of the material risks and understand the decisions being made on their behalf.

Review the register at least annually and whenever a new system is introduced or an existing one changes materially.

This should include tools that employees build themselves, particularly as AI makes it increasingly easy for people to create applications without going through a traditional IT procurement process.

We covered this issue in [Shadow AI apps: how to stop AI-built tools becoming shadow IT](https://www.toca.io/news/learn/shadow-ai-apps-shadow-it/).

The important thing is to make sure that the firm has a consistent approach. A system should not escape scrutiny simply because somebody built it rather than bought it.

## A set of rules to keep the firm in control

A framework is useful for carrying out an assessment, but it is not necessarily something people will remember when a new supplier comes along or a department wants to switch on another AI feature.

For that reason, I would also suggest having a short set of principles that the partners agree to and that can be applied to every new system.

The following is a starting point.

1. **We know where every copy of our clients' data is held**, including backups, and whose laws can reach it.

2. **We judge providers by who controls them, not simply where their servers are.** UK residency is not the same as sovereignty.

3. **No critical client work depends on a single provider without a tested way to continue.**

4. **We can leave any supplier with our data in a usable format**, and we know how long that process takes.

5. **Our contingency plan does not live on the systems it is designed to recover.**

6. **Nobody is locked out of everything because one sign-in service is unavailable.**

7. **Our AI processes client information in an environment we understand and control.** We know where documents are sent and which models process them.

8. **Every new system is checked before it is bought, built or switched on**, including tools created by our own employees.

9. **We test failure, not just backups.** We carry out restores, test alternative access and practise operating without email.

10. **One named person owns the process**, reports to the partners and has the authority to challenge a decision that creates unnecessary risk.

These are not particularly complicated rules. The difficulty is making sure they are followed consistently.

## Particular considerations for high-volume law firms

The principles above apply to any legal practice, but high-volume firms have some additional considerations.

In personal injury, credit hire, conveyancing and other areas where thousands of matters move through a process each month, a relatively short outage can create a surprisingly large amount of work.

There are several things worth considering.

**Do not replace one concentration risk with another.**

The CTS incident showed what can happen when a large proportion of a firm's IT is placed with one provider. Moving everything to another UK supplier does not solve the underlying problem if the same concentration remains.

The objective should be to make sure that no single provider can bring the entire operation to a halt.

**Control brings responsibility.**

Tuckers is a useful reminder that operating your own infrastructure is not automatically safer. If you bring systems inside your own boundary, you also take responsibility for patching, monitoring, access control and incident response.

If the firm does not have the people to manage those responsibilities, a properly managed external provider may be the better option.

**The portals are not yours.**

The Claims Portal, Official Injury Claim, MedCo, HM Land Registry and Legal Aid Agency systems are outside the firm's control.

Even the most independent law firm will have to wait when one of these services is unavailable.

The important thing is to design processes that can hold work safely, queue submissions and resume when the service returns. Staff also need to understand the manual fallback arrangements and how deadlines are treated during an outage.

**Volume turns an hour into a backlog.**

A firm handling a few dozen new matters each week might lose a day during an outage. A firm opening thousands of matters each month can lose a day and then spend another week catching up.

Portal timetables, limitation dates and completion dates do not necessarily move simply because a supplier has experienced a technical problem.

The CTS incident showed that firms working on paper during an outage can face a substantial amount of re-keying when their systems return.

Planning the recovery is just as important as planning for the outage itself.

**Identity and email are hidden dependencies.**

A supposedly independent platform can still be inaccessible if it relies on Microsoft's identity service for sign-in.

Similarly, an automated process that reads and sends messages through Exchange Online will stop working when Exchange is unavailable.

Firms need to understand these dependencies, maintain break-glass access and identify which automated processes depend on email.

**AI can move data without anybody noticing.**

A firm can do almost everything else correctly and still send client documents to a model in another country because somebody has enabled an AI feature inside software the firm already uses.

The question is not simply whether the firm has approved the application. It needs to understand where each AI feature processes information, which model it uses and who can enable it.

We discussed some of the considerations around UK-hosted platforms in [UK-hosted low-code platforms compared](https://www.toca.io/news/learn/uk-hosted-low-code-platforms-compared/).

**Migration is where the risk concentrates.**

Moving live matters, years of documents and the integrations around them is considerably more difficult than setting up a new system.

Move in stages. Start with the work that matters most, run old and new systems alongside one another for long enough to reconcile the information, and do not switch off the old environment until you have demonstrated that the new one works.

**Do not leave Microsoft 365 simply because of an outage.**

Microsoft 365 is a capable platform for email, documents and collaboration. Replacing it would be expensive and disruptive, and there may be very little benefit in doing so.

Sovereignty is not about choosing one particular supplier over another. It is about making sure the firm's most important work and information are not unnecessarily dependent on any single supplier.

## What data sovereignty makes possible

So far, much of the discussion has been about avoiding problems. But there is another side to this.

Having greater control over systems and information can create opportunities that are difficult to realise when everything is spread across separate software services.

AI is an obvious example.

Many law firms have spent the last couple of years debating how they can use generative AI on client documents. The commercial teams can see the potential, while risk and compliance teams quite reasonably want to know where those documents are going and which models are processing them.

When AI can run inside the firm's own environment, or through a UK provider under UK law, the discussion changes. Rather than spending months debating whether the firm can use AI at all, it becomes possible to focus on the applications, supervision and controls required to use it properly.

That does not remove the need for oversight. We have covered some of those considerations in [Supervising AI on volume files after Mazur](https://www.toca.io/news/learn/supervising-ai-on-volume-files-after-mazur/). But it does remove one of the practical obstacles that often prevents projects from getting started.

There is also an opportunity in the firm's own data.

A law firm whose information is spread across a dozen different software services often has to rely on each supplier's reporting tools to understand its own operation.

If case management, finance, portal and document information can be brought together under the firm's control, it becomes much easier to ask meaningful questions about the business.

Which work types are profitable? Which files are drifting towards trouble? Which sources produce the cases that settle well? Where are the delays occurring?

These are commercial questions, not just IT questions. Better access to the firm's own information can improve how it manages its work and makes decisions.

There is also a question of winning and retaining business. Insurers, corporate clients and public bodies increasingly ask suppliers about data locations, sub-processors, cybersecurity and business continuity.

A firm that can answer those questions clearly, with a documented register and tested arrangements behind the answers, is in a better position than one that has to go back to its IT supplier every time a questionnaire arrives.

Finally, there is the question of cost and negotiating power.

Microsoft increased the list prices of its commercial Microsoft 365 suites from 1 July 2026. That is a commercial decision for Microsoft, and customers can decide whether the additional value justifies the price.

But a customer that cannot realistically leave a supplier is always in a weaker negotiating position than one with a tested alternative.

Having control does not necessarily mean changing providers. Sometimes it simply means having the option.

## Where Toca fits

Toca is our platform, and it was built for the sort of regulated, high-volume work discussed in this guide.

We are a UK company, and the platform can run in Toca's own UK cloud, in a customer's own cloud tenancy or on the customer's own servers. It can also be deployed in an air-gapped environment where information cannot leave the organisation.

The deployment is chosen to suit the firm's requirements. That means a firm can keep particularly sensitive applications and information inside its own environment while running other parts of its operation in Toca's UK cloud.

Toca's agent bots sit inside the customer's network and connect outbound to the Toca server. They need internet access and an entry on the customer's allow-list, allowing a process running in Toca's UK cloud to work with a case management system hosted within the firm's own infrastructure.

Spectral, our document AI platform, can run its models inside the customer's boundary. Client documents are not used to train the models.

Toca holds ISO/IEC 27001, ISO/IEC 42001 and Cyber Essentials Plus certifications, and both the platform and Spectral are listed on G-Cloud 15. Across our customers, the platform runs around 276,000 workflows a day, including claims processes for UK volume law firms.

Toca is not intended to replace Microsoft 365. It is designed to take the high-volume operational work around the case management system, including intake, evidence gathering, chasing, checking and portal submissions, and make that work less dependent on the same systems used for email and general collaboration.

That separation matters. If Microsoft has a bad day, it should not automatically mean that every process in the firm has to stop.

If you want to look at how your own systems fit together, [talk to us](https://www.toca.io/contact). We can spend twenty minutes looking at what you use, what depends on what and which processes would stop if one of those systems became unavailable. We can then show you a process running end to end, with the audit trail in view.

There is more information on [the Toca platform](https://www.toca.io/platform).

## Where should a law firm start?

Data sovereignty can sound like a substantial technology programme, and for a large firm it may eventually become one.

But the first step is relatively straightforward.

Make a list of the systems the firm uses, where they hold information, who operates them, which laws apply, how people access them and what other services depend on them.

That list will probably reveal more than a few things that nobody had previously considered. It will also provide a useful starting point for the SRA's expectations around governance, records and risk management.

Then choose the one piece of work that would cause the most damage if it stopped tomorrow. Work out what would happen if its main provider became unavailable for a day, and put a practical alternative in place.

The cloud is not going anywhere, and nor should it. The major providers offer services that most firms would struggle to replicate economically.

But there is a difference between using a service and being entirely dependent on it.

A law firm should know where its clients' information is held, understand who can reach it and have a realistic plan for continuing its work when an external provider fails.

Ultimately, the question is quite simple: when the next outage comes, who decides whether your firm can carry on working?

That decision should not belong entirely to somebody else's IT department.

## Frequently asked questions

### What is data sovereignty for a law firm?

Data sovereignty is a firm's ability to understand and control where client information is held, which laws can reach it, who can access or suspend the services holding it, and whether the firm can continue working if a provider fails.

It goes further than data residency, which describes only the physical location of the information.

### Is client data stored in a UK region of Microsoft or AWS sovereign?

It is UK-resident, but that does not necessarily make it sovereign in the full sense.

The US parent companies remain subject to US law, including the CLOUD Act, and their UK services can depend on shared global infrastructure. This means that a UK region does not, by itself, remove foreign legal jurisdiction or protect against a wider provider outage.

For general email and collaboration, this may be an entirely reasonable arrangement. For particularly sensitive information and critical operational work, firms may wish to consider a UK-owned provider or infrastructure within their own boundary.

### Does the SRA require law firms to keep client data in the UK?

No. The SRA does not prescribe where law firms must store their data.

However, the Code of Conduct for Firms requires effective systems and controls (paragraph 2.1), accountability for work carried out through others (2.3), management of material business risks (2.5), access for SRA inspection to relevant information held by critical third parties (3.3) and confidentiality of client information (6.3).

Where data is held and which laws can reach it are relevant considerations when demonstrating compliance. UK GDPR also imposes requirements on international transfers of personal data.

### What should a law firm's cloud contract include?

A cloud contract should identify where data is held, including backups, and list the relevant sub-processors and corporate ownership arrangements.

It should include appropriate security obligations, incident notification timescales, business continuity commitments and the access to information required by paragraph 3.3 of the SRA Code for Firms.

It should also explain how information is returned when the contract ends, including the export format and timescale. Article 28 of UK GDPR sets out the requirements for contracts with data processors.

### Does a law firm have to report a cloud outage or cyber attack to the SRA?

It depends on the circumstances.

Paragraph 3.9 of the Code requires firms to report promptly facts or matters they reasonably believe are capable of amounting to a serious breach of regulatory requirements. Paragraph 3.10 requires firms to bring other relevant matters to the SRA's attention where they reasonably believe it should know about them.

The SRA's cybersecurity guidance also discusses reporting cyber attacks. Firms should assess each incident and record the decision about whether regulatory reporting is required.

Separately, a personal data breach likely to result in a risk to individuals must be reported to the ICO within 72 hours, where feasible. A provider outage that causes no personal data breach may not require an ICO notification, but the circumstances should still be assessed.

### Should a law firm move away from Microsoft 365?

Usually not, and certainly not simply because of an outage.

Microsoft 365 is a capable platform for email, documents and collaboration. Replacing it would be expensive and disruptive, and may offer little practical benefit.

The more useful approach is to identify the work that cannot stop and ensure it does not depend entirely on Microsoft or any other single provider.

### Where should a law firm start with data sovereignty?

Start by mapping the firm's systems. Record where information is stored, who operates each service, which laws may apply, how people sign in and what other systems depend on it.

Then identify the most critical piece of work and establish how the firm would continue if its main provider became unavailable for a day.

That gives the firm a practical starting point without requiring a wholesale change to its technology.

## Sources

- Solicitors Regulation Authority, [Code of Conduct for Firms](https://www.sra.org.uk/solicitors/standards-regulations/code-conduct-firms/) and [SRA Principles](https://www.sra.org.uk/solicitors/standards-regulations/principles/).
- Solicitors Regulation Authority, [Confidentiality of client information](https://www.sra.org.uk/solicitors/guidance/confidentiality-client-information/), updated 30 June 2022.
- Solicitors Regulation Authority, [How to reduce the risk of being affected by cybercrime](https://www.sra.org.uk/solicitors/resources/cybercrime/cybersecurity-advice/), 23 November 2020.
- [UK GDPR](https://www.legislation.gov.uk/eur/2016/679/contents), Articles 28, 32 and 33.
- National Cyber Security Centre, [Cloud security guidance](https://www.ncsc.gov.uk/collection/cloud).
- US Department of Justice, [CLOUD Act resources](https://www.justice.gov/criminal/cloud-act-resources).
- The Register, [Microsoft admits it 'cannot guarantee' data sovereignty](https://www.theregister.com/2025/07/25/microsoft_admits_it_cannot_guarantee/), 25 July 2025.
- PBS NewsHour (Associated Press), [Trump's sanctions on ICC's chief prosecutor have halted tribunal's work](https://www.pbs.org/newshour/world/trumps-sanctions-on-iccs-chief-prosecutor-have-halted-tribunals-work), 15 May 2025; heise online, [Microsoft denies mail blockade at the International Criminal Court](https://heise.de/-10429628).
- BleepingComputer, [Massive Microsoft 365 outage disrupts Outlook, Teams, Copilot worldwide](https://www.bleepingcomputer.com/news/microsoft/massive-microsoft-365-outage-disrupts-outlook-teams-copilot-worldwide/), 12 and 13 November 2026; Sky News, [Microsoft outage: 'Underlying issue' explained](https://news.sky.com/story/microsoft-outage-latest-hundreds-of-thousands-of-users-affected-as-fix-not-going-as-expected-13611764), 13 November 2026; Microsoft service incident reports.
- The Register, [Microsoft 365 outage drags on for nearly 10 hours](https://www.theregister.com/2026/01/23/microsoft_365_outage/), 23 January 2026.
- Microsoft, [Azure status history](https://azure.status.microsoft/en-gb/status/history/), including the Azure Front Door incident of 29 October 2025.
- The Register, [Major AWS outage across US-East region breaks half the internet](https://www.theregister.com/2025/10/20/amazon_aws_outage/), 20 October 2025.
- Law Gazette, [Dozens of conveyancing firms paralysed by cyber attack](https://lawgazette.co.uk/news/dozens-of-conveyancing-firms-paralysed-by-cyber-attack/5118045.article), November 2023; Today's Conveyancer, [Cyber incident affects c.80 conveyancing firms](https://todaysconveyancer.co.uk/cyber-incident-affects-c-80-conveyancing-firms/); TechCrunch, [CTS cyberattack](https://techcrunch.com/2023/11/27/cyberattack-cts-sprout-citrixbleed-data-breach), 27 November 2023; Estate Agent Today, [CTS restores systems following cyber incident](https://www.estateagenttoday.co.uk/breaking-news/2024/1/cts-restores-systems-following-cyber-incident), January 2024.
- Legal Futures, [Top criminal law firm fined £98,000 for cyber-security "negligence"](https://www.legalfutures.co.uk/latest-news/top-criminal-law-firm-fined-98000-for-cyber-security-negligence), March 2022.
- The Law Society, [Legal Aid Agency data breach](https://www.lawsociety.org.uk/topics/legal-aid/legal-aid-agency-data-breach).
- Microsoft, [2026 Microsoft 365 packaging and pricing updates FAQ](https://www.microsoft.com/licensing/news/2026-M365-Packaging-Pricing-Updates-FAQ).
- Nicholas Carr, *The Big Switch: Rebuilding the World, from Edison to Google*, W. W. Norton, 2008.
