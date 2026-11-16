---
title: "Power Automate or a specialist? Choosing the right automation approach for personal injury and credit hire claims"
subtitle: "Power Automate, an in-house build, your case management system's own workflow or a specialist: what each one does with high-volume personal injury and credit hire claims, and where each one runs out."
date: 2026-11-16
updated: 2026-11-16
author: "James Swash"
author_role: "CTO, Toca"
tag: "Comparisons"
section: learn
sites: ["io", "legal"]
image: ""
---
**The short answer:** For high-volume personal injury and credit hire claims, a specialist automation platform is likely to be the better choice. Power Automate is useful for smaller jobs inside Microsoft 365, an in-house build gives you control but leaves you responsible for maintaining the software, and the workflow inside your case management system often stops at the edge of the case record.

The problem is that claims work rarely stays in one place. It moves between the MOJ Portal, the OIC portal, medical agencies, bank statements, repair invoices and the finance ledger. Each of these steps creates work for someone, and each one introduces another opportunity for delay, error or unnecessary cost.

So, what is the best way to automate that work? And more importantly, how do you avoid spending more on the technology than you save in the process?

## Understanding your options

When a claimant firm sets out to automate its claims processes, there are usually five routes to consider.

The first is the one it is already using: handlers doing the work manually, or a back-office team doing it on their behalf, sometimes through an outsourced service.

The second is Microsoft Power Automate. It is an obvious starting point because most firms already use Microsoft 365, and the tools are readily available.

The third is to build something in-house, using your own developers or an external consultancy.

The fourth is to use the workflow capabilities already provided by the case management system.

And finally, there is the option of using a specialist automation platform designed to work across the systems, applications and documents involved in a claim.

Each approach has its merits. The important thing is understanding where each one works well, and where it starts to become difficult or expensive.

| Approach | Good at | Where it runs out on claims work | Who maintains it? | How the cost grows |
|---|---|---|---|---|
| Manual or outsourced | No technology project required | Every additional file still requires people to do the work | Your team or the outsourcer | With headcount or volume |
| Power Automate | Approvals, reminders and simple Microsoft 365 tasks | Complex applications, portal connections and high-volume unattended processing | Whoever built it, often one person | Per user and per bot |
| In-house development | Building exactly what you specify | Every integration, document process and audit control has to be developed and maintained | Your developers | With every change and update |
| Case management workflow | Tasks and processes within the case record | Work that crosses into other systems and applications | Your software vendor | With change requests |
| Specialist platform | High-volume work across systems, portals, documents and the ledger | More than you need for simple approvals and reminders | The platform provider, with your own team able to make changes | Per workflow, not per seat |

Let's look at each in a little more detail.

## Doing nothing is a decision too

The way you work today can look like the cheapest option because the cost is already buried in your staffing budget. But in a high-volume practice, every manual step has a cost, and that cost increases with every additional claim.

Consider the work involved in establishing an impecuniosity position from a claimant's bank statements. One UK personal injury firm, with a team of around 70 people, was spending three to four hours of a handler's time on each claim building that position.

With the help of Spectral, Toca's document AI, the same work can now be completed in seconds. The system extracts the relevant information, ties each finding back to the page it came from and presents the result for a lawyer to review.

That is a substantial amount of time returned to the people who should be dealing with the actual claim, rather than reading through pages of bank statements.

Winn Group has also reported that it can now handle four times the number of leads with a team of the same size.

Of course, some firms try to reduce these costs by outsourcing the work. This can lower the cost of each individual task, but it doesn't necessarily make the process more efficient. You are still paying someone to do the work, and the work itself is still taking place outside your own operation.

There is also the question of supervision. Following the Court of Appeal's ruling in *Mazur*, unauthorised staff may undertake legal work under the direction, control and responsibility of an authorised person. That makes it important to retain clear evidence of who has reviewed and approved work, and under whose supervision it has been completed.

Moving the work to an outsourced provider doesn't remove that responsibility. You still need to understand what has been done and be able to demonstrate the appropriate oversight.

We look at this in more detail in [Supervising AI on volume files after Mazur](https://www.toca.io/news/learn/supervising-ai-on-volume-files-after-mazur/).

## Power Automate: a good starting point, but is it enough?

Microsoft Power Automate is a very capable tool. If you want to save an email attachment into SharePoint, send an approval request through Teams or remind a handler about an upcoming date, it is an excellent place to start.

It is relatively easy to use, it integrates with the Microsoft environment and many organisations already have access to some of its capabilities through their existing licences.

But there is a difference between automating a simple office task and automating a substantial part of a personal injury or credit hire claims process.

A number of law firms have come to us after attempting to build claims applications on Power Platform. The issues they encountered tend to fall into four areas.

### 1. Maintenance and complexity

A simple flow is relatively straightforward to build. The difficulty comes when you start adding more rules, screens, connections and exceptions.

A personal injury claim can involve a considerable number of different systems and stages. Each one introduces more complexity, and every additional rule makes the application harder to change and maintain.

Over time, the knowledge of how everything fits together often ends up sitting with the person who originally built it. If that person leaves, or moves on to another project, the firm can find itself with an increasingly important application that very few people understand.

This is one of the reasons we designed Toca to bring the entire process together in a single workflow. Whether a step involves an API connection, an RPA bot or a piece of custom code, it remains part of the same process.

In Toca 10, Git is built into every workspace, allowing changes to be branched, committed and rolled back. This gives development teams a much more structured way of managing changes to business-critical automation.

### 2. Volume and processing capacity

The second issue is volume.

Microsoft's licensing model for unattended desktop automation is based around bots. An unattended bot runs one desktop flow at a time, so if you need multiple desktop flows to run concurrently, you need sufficient bot capacity.

Cloud flows also have their own service limits and request allocations. If those limits are exceeded, flows can be throttled, and consistently throttled flows can be turned off.

There is also a practical consideration when dealing with claims that remain active for months or even years. A Power Automate flow run has a maximum duration of 30 days. That means the state of a longer-running claim has to be stored and managed separately, with the process picked up again through additional flows.

None of these limitations necessarily makes Power Automate unsuitable. They do, however, need to be considered when designing a system that is expected to process thousands of claims and operate reliably every day.

Toca currently runs around 276,000 workflows a day in production. We believe that much of this type of high-volume, multi-system work would be extremely difficult to deliver reliably using a collection of individual Power Automate flows.

### 3. The real cost of Power Automate

This is where things can become particularly interesting.

At first glance, Power Automate looks like the cheaper option. Microsoft's UK list price for Power Automate Premium is £11.50 per user per month. That sounds very reasonable, particularly when many firms already have Microsoft 365 in place.

But that is only part of the picture.

The standard Microsoft 365 connectors are included with eligible licences, but connecting to external systems, using premium connectors or building custom integrations can require additional licensing. Power Apps Premium is also £15.40 per user per month, while Power Automate Process, which provides unattended bot capacity, is £115.30 per month per bot. These prices are based on Microsoft's UK list price on 16 November 2026, paid annually and before VAT.

The important point is that the costs increase as the operation grows. More users can mean more licences, and more concurrent unattended processing means more bot capacity.

Consider a larger firm that needs 110 unattended bots running concurrently to handle its workload. At Microsoft's published price of £115.30 per bot per month, that would amount to £152,196 a year in bot licences alone.

That is already more than the upper end of Toca's typical annual price range, before considering the infrastructure needed to run those bots, or the developers required to build, maintain and support the applications.

Of course, not every firm will need 110 bots, and Power Automate can be considerably cheaper for smaller or simpler processes. But it illustrates how quickly the economics can change when you start automating a substantial part of a claims operation.

#### Work out your own Microsoft licence bill

The example is a firm with 500 people using ten claims applications, which between them connect to ten systems, among them Proclaim, the MOJ Portal, the OIC portal, MedCo and the finance ledger, with ten jobs running at once on each at the busiest times. The number of applications is not one of the questions, because a Power Apps Premium licence covers every application a person uses. Change the three numbers to match your own firm.

<div class="calc" data-calc>
<table class="calc-in">
<thead><tr><th>Your claims applications</th><th>Number</th></tr></thead>
<tbody>
<tr><td>People who use them<small>Handlers, supervisors and anyone else who opens any of the applications.</small></td><td class="q" data-in="users" data-label="People who use the applications">500</td></tr>
<tr><td>Systems they connect to<small>For example Proclaim, the MOJ Portal, the OIC portal, MedCo and the finance ledger.</small></td><td class="q" data-in="systems" data-label="Systems the applications connect to">10</td></tr>
<tr><td>Jobs running at once on each connection<small>At your busiest. One Process licence runs one unattended job at a time.</small></td><td class="q" data-in="atonce" data-label="Jobs running at once on each connection">10</td></tr>
</tbody>
</table>
<table class="calc-out">
<thead><tr><th>What Microsoft charges for</th><th>Licences</th><th>Each year</th></tr></thead>
<tbody>
<tr data-price="15.40" data-from="users"><td>Power Apps Premium<small>One for each person, covering every application they use. £15.40 per user per month.</small></td><td class="n">500</td><td class="y">£92,400</td></tr>
<tr data-price="115.30" data-from="systems*atonce"><td>Power Automate Process<small>One for each unattended job running at once on each connection. £115.30 per month.</small></td><td class="n">100</td><td class="y">£138,360</td></tr>
</tbody>
<tfoot>
<tr><th colspan="2">Each month</th><td data-total="m">£19,230</td></tr>
<tr><th colspan="2">Each year</th><td data-total="y">£230,760</td></tr>
<tr><th colspan="2">Over three years</th><td data-total="y3">£692,280</td></tr>
</tfoot>
</table>
<p class="calc-note">Microsoft's UK list prices on 16 November 2026, paid yearly and before VAT. It assumes each connection runs unattended in the background; a connection used only when a licensed person presses a button in an application needs no Process licence. This is the licences only. It leaves out extra database storage, AI credits, the machines the unattended jobs run on, the Microsoft 365 unattended licence they may need, and the people who build and maintain the applications.</p>
</div>

Does the bill go up with every new application? That depends on the licence. Power Apps Premium is charged per user and covers as many applications as that person needs, so a new application only costs more when it brings in people who are not yet licensed. Microsoft's per app plan, at $5 per user per app per month, did rise with every application, and Microsoft stopped selling it to new customers on 2 January 2026. What still grows application by application is everything around the user licence: each process that has to run unattended needs its own bot capacity, and each new application adds to the storage and the AI credits you buy.

Toca takes a different approach. Rather than charging for every user and every unattended bot, it is priced around the workflows being automated. As a guide, a law firm would typically pay between £30,000 and £70,000 a year, depending on the scale and complexity of the operation.

This provides a much clearer view of the annual cost as automation grows across the business. You are not continually adding another licence every time another person needs access or another process needs to run.

For a larger firm, the cost of the Microsoft licences alone can exceed the cost of a specialist platform. And that is before taking into account the development and maintenance effort required to keep everything working.

The sensible comparison is not the cost of one Power Automate licence against the cost of Toca. It is the total cost of delivering and running the same automation capability over three years.

You can read more about the technical and licensing differences in our [Toca and Power Platform comparison](https://www.toca.io/power-platform).

### 4. Document processing and AI

The final consideration is the nature of the work itself.

A lot of claims processing involves more than moving information from one system to another. Someone has to read and interpret documents, identify relevant information and make decisions based on what they contain.

Impecuniosity assessments, basic hire rate rebuttals and medical records are good examples. These are not simply data-entry tasks. They involve interpreting information that a lawyer may need to review and sign off.

With Power Automate, you can certainly build document-processing workflows, but you need to assemble the underlying capabilities yourself. You also need to consider how findings are checked, how disagreements are handled and how the audit trail is maintained.

This is where Spectral comes in.

Spectral is Toca's AI control plane for document processing. Multiple models can examine a document, compare their findings and identify disagreements for a person to resolve. Findings can be tied back to the original document, with the relevant passage available for review.

The result is not simply an automated answer. It is a process that records what the system found, where it found it, and who approved the result.

For legal work, that distinction matters.

## Building it in-house

Building your own solution can be an attractive option, particularly if you already have a development team and want complete control over the process.

You can build exactly what you need, integrate with the systems you use and retain ownership of the resulting software.

But the cost is not just the first version. It is every version that follows.

Take the Claims Portal, for example. It offers a REST API for software houses and in-house developers, but accessing it involves a letter of authorisation from your client, a signed development agreement and test credentials. You then need to maintain the integration as the portal changes.

The Official Injury Claim portal is another consideration. Its professional user pages do not provide equivalent integration documentation, which means a development team looking to automate the process may have to interact with the portal through its screens.

Add medical agencies, finance systems, case management software and the document-processing requirements, and the firm is effectively running a software product as well as a legal practice.

There is also the risk of relying on people. An in-house claims system often depends heavily on the developers who built it. When one of them leaves, some of the knowledge about how the system works can leave with them.

Toca takes much of that plumbing off your developers' hands. The connections to the MOJ Portal, the OIC portal and MedCo already exist. Agent bots inside your network can connect out to Toca with internet access and an allow-list entry, allowing a cloud deployment to work with older case management systems running on your own servers.

And you are not restricted to low-code. When a process needs something more specialised, your developers can write C# on .NET Core, React or Python in a browser-based IDE. That code can then become a reusable drag-and-drop block within the same workflow and audit trail.

The intellectual property remains yours. Your developers can concentrate on the things that are particular to your firm, rather than spending their time keeping portal connections alive.

## Surely our case management system can already do this?

Often, it can do part of it. Most case management systems designed for personal injury work have some form of workflow capability, and there is no reason not to use it for the things it does well.

Tasks, letters from templates and key dates within an individual case are all sensible examples.

But claims work doesn't stay inside the case record.

Bank statements come from the claimant. Repair invoices need to be processed and sent to the finance ledger. Medical reports arrive from external agencies. Claims are submitted and updated through portals. Each of these steps involves information moving between systems.

The work that often costs a firm the most is the work that takes place between those systems, and the documents that have to be read along the way.

Before relying on your case management vendor to automate the entire process, there are three questions worth asking:

1. **Which of these steps is already running at another firm, at our volume?** A demonstration using sample data is not the same as a live deployment processing thousands of claims.
2. **Who changes it when our process changes, and how long does that take?** If every change has to go into the vendor's development queue, your processes will move at the vendor's pace.
3. **What is recorded when a person signs off a finding from a document?** In a regulated legal environment, you need to be able to demonstrate what was reviewed, who approved it and what evidence they relied on.

Toca does not ask firms to choose between their case management system and another platform. It works alongside systems such as Proclaim, Visualfiles, ActionStep, Aderant and Clio, reading information from them and writing it back.

JMK Solicitors, Northern Ireland's number one personal injury firm, uses Toca to connect its case management system with medical agencies and the MOJ Portal. The firm reports 25% fewer files at risk of write-off.

The idea is not to replace the systems that already work. It is to automate the work that happens around them.

## What does a specialist automation platform actually deliver?

Ultimately, the technology is only useful if it delivers measurable improvements to the business.

Toca is already used by firms to automate parts of the personal injury and credit hire claims lifecycle. These are some examples of the results reported from live deployments.

| Firm | Work being automated | Result |
|---|---|---|
| Winn Group | Repair invoices and the claims lifecycle | More than 1,000 repair invoices processed automatically each month, claims lifecycle around 50% faster, and approximately 160 hours of staff time returned to billable work each month |
| Bond Turner | Basic hire rate rebuttal reports, drafted by Spectral for a lawyer to review and sign off | Up to 80% less than commissioning a report, with results in minutes rather than days |
| UK personal injury firm (anonymised) | Impecuniosity assessments from bank statements | Three to four hours of handler time per claim reduced to seconds |
| JMK Solicitors | Key dates across its case management system, medical agencies and the MOJ Portal | 25% fewer files at risk of write-off |

As Clint Milnes, Chief Information Officer at Winn Group, explains:

> We needed to reduce our case handling duration so that we could process more claims.

Winn Group has since extended its partnership with Toca for a further three years.

Toca holds ISO/IEC 27001, ISO/IEC 42001 and Cyber Essentials Plus certifications. It can run in Toca's UK cloud, in your own cloud tenancy or on your own servers.

For firms looking to understand the potential savings, our [credit hire cost calculator](https://www.toca.io/legal/cost/credit-hire) allows you to model individual processes using your own volumes and staff costs. The workings are visible, so you can see where the savings come from.

We also explain the different stages involved in [credit hire claims automation](https://www.toca.io/news/learn/credit-hire-claims-automation/).

## How do you decide which approach is right?

There isn't a single answer for every firm. A small practice looking to automate a few simple approvals may find that Power Automate is perfectly adequate. A larger firm looking to automate thousands of claims across multiple systems has a very different set of requirements.

There are five things worth considering before making a decision.

**1. Count the systems a claim touches.** Look at your case management system, the portals, medical agencies, finance ledger and documents. The more systems involved, the less likely it is that a tool operating inside just one of them will be sufficient.

**2. Calculate the cost over three years.** Include the licences, bots, development, infrastructure and ongoing maintenance. Count the people who need to approve work and the processing capacity required at your busiest periods. These costs are easy to overlook when comparing headline licence prices.

**3. Understand who maintains the solution.** Your processes will change, and external portals will change too. Find out who is responsible for making those changes, how long they take and what they cost.

**4. Look carefully at document processing.** How does the system show where a finding came from? What happens when it is unsure? Who reviews and approves the result? And can you demonstrate that process afterwards?

**5. Test it using your own claims.** A demonstration using a generic example is useful, but it won't tell you what the system can achieve with your documents, your processes and your case management system. Run a real example and measure the time saved, the accuracy of the results and where people still need to be involved.

## The right automation should make claims work easier

Automation is not simply about replacing a manual task with a computer program. It is about looking at the whole process and understanding where time, effort and money are being wasted.

Power Automate is a useful tool, and there are plenty of situations where it is exactly the right choice. Building in-house can also make sense where a firm has the resources and appetite to maintain its own software.

But personal injury and credit hire claims involve a complicated mix of systems, documents, decisions and regulatory responsibilities. Trying to automate all of that with a collection of disconnected tools can quickly become another problem to manage.

A specialist platform gives you a way to bring those processes together without replacing the systems you already rely on. It also gives you a clearer view of what the automation is doing, where information has come from and who has approved the work.

The real question is not whether you can automate a particular task. It is whether you can automate the process reliably, at scale, and at a cost that makes commercial sense.

If there is a claims process you want to take out of your handlers' hands, [talk to us](https://www.toca.io/contact). We can spend twenty minutes looking at where the time goes today, then show you one step running against a sample of your own documents, with the sign-off and audit trail visible.

## Questions

### Can we run claims workflow on Power Automate?

Yes, particularly for simpler tasks such as approvals, reminders and moving files between people who already use Microsoft 365. High-volume claims work is more complicated. Complex applications become harder to maintain as rules are added, unattended bots have licensing and concurrency limits, and long-running claims need additional state management. Document processing and legal sign-off controls also need to be built around the platform.

### Our case management system has workflow built in. Why add anything else?

Keep using it for the processes that live inside the case record. The work that often takes the most time in a personal injury or credit hire claim happens between systems: portals, medical agencies, finance ledgers and documents. Toca works alongside case management systems such as Proclaim, Visualfiles, ActionStep, Aderant and Clio, reading information from them and writing it back.

### Should we build claims automation in-house?

That depends on whether you want to maintain a software product as well as run a legal practice. An in-house solution needs portal connections, document processing, audit trails and ongoing maintenance as external systems change. A specialist platform provides much of that infrastructure already, while still allowing your developers to extend it with C#, React or Python where needed.

### Does Toca replace our case management system?

No. Toca works alongside your existing case management system, reading information from it and writing information back. Your case record stays where it is, and you can continue using your existing system for the work it already does well.

### Does Toca connect to the MOJ Portal and the OIC portal?

Yes. Toca connects to the MOJ Portal, the OIC portal and MedCo, as well as to case management systems and finance ledgers. JMK Solicitors, for example, uses Toca to connect its case management system with medical agencies and the MOJ Portal.

### How much does a specialist cost compared with Power Automate?

Toca is typically priced between £30,000 and £70,000 per year, depending on the scale and complexity of the operation. It is priced around the workflows being automated, rather than charging separately for every user and unattended bot.

Power Automate has a lower entry price, but the total cost grows as more users and processing capacity are needed. At Microsoft's UK list price on 16 November 2026, Power Automate Premium was £11.50 per user per month and Power Automate Process was £115.30 per month per unattended bot, paid annually and before VAT.

For example, 110 unattended bots running concurrently would cost £152,196 a year in bot licences alone. That is already above the upper end of Toca's typical annual price range, before infrastructure, development and maintenance costs are included.

Not every firm needs that level of processing capacity, of course. The right comparison is to model the actual users, workflows and concurrent processing requirements over three years, rather than comparing the price of one licence with the price of a complete platform.

## Sources

- Microsoft, [Power Automate pricing (UK)](https://www.microsoft.com/en-gb/power-platform/products/power-automate/pricing) and [Power Apps pricing (UK)](https://www.microsoft.com/en-gb/power-platform/products/power-apps/pricing), read 16 November 2026, including terms on unattended bots; [Copilot Studio pricing (UK)](https://www.microsoft.com/en-gb/microsoft-365-copilot/pricing/copilot-studio), read 16 November 2026.
- Microsoft Licensing, [Power Apps per app license sales end](https://www.microsoft.com/en-us/licensing/news/power-app-per-app-end-of-sale), 14 January 2026.
- Microsoft Learn, [Power Platform licensing FAQ](https://learn.microsoft.com/en-us/power-platform/admin/powerapps-flow-licensing-faq), [Limits of automated, scheduled and instant flows](https://learn.microsoft.com/en-us/power-automate/limits-and-config), [Requests limits and allocations](https://learn.microsoft.com/en-us/power-platform/admin/api-request-limits-allocations) and [Run unattended desktop flows](https://learn.microsoft.com/en-us/power-automate/desktop-flows/run-unattended-desktop-flows), checked 16 November 2026.
- Claims Portal, [For REST API developers](https://www.claimsportal.org.uk/developer/for-rest-api-developers/), and Official Injury Claim, [Professional users](https://www.officialinjuryclaim.org.uk/professional-users/), checked 16 November 2026.
- Winn Group, Bond Turner and the anonymised firm: [Toca legal customer evidence](https://www.toca.io/legal#evidence). Winn Group's figures are also reported in Legal IT Insider and Winn Group's press release.
- JMK Solicitors: [Northern Ireland's number one personal injury firm runs on Toca](https://www.toca.io/news/articles/jmk-solicitors-runs-on-toca/).
