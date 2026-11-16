---
title: "Shadow AI apps: how to stop AI-built tools becoming shadow IT (2026)"
subtitle: "Why staff are building their own apps with AI, where the risks really sit, and how to give them somewhere governed to build."
date: 2026-11-16
updated: 2026-11-16
author: "Mat Rule"
author_role: "Founder and CEO, Toca"
tag: "Guides"
section: learn
sites: ["io", "health", "legal"]
image: ""
---
**The short answer.** Staff can now describe an app to an AI tool and have it running the same day, and each one is a small system that nobody in IT chose, secured or agreed to maintain. A ban does not stop it. Sort the apps by what they touch: let the harmless ones run on a simple register, and move anything that holds personal data, writes to a core system or acts on its own onto a governed platform that already provides sign-in, permissions, integration, versions and an audit trail.

## The problem with letting everyone build their own software

For years, businesses have been trying to give employees the technology they need to do their jobs more effectively. The problem is that the systems they use don't always provide everything they need.

A finance team might have an accounting system that works perfectly well, but still need a separate tool to manage an approval process. A legal team might have a case management system, but need another application to track a particular stage of a claim. And someone in an operations department might spend hours every week moving information between two systems that were never designed to talk to each other.

These are relatively small problems individually, but they add up. Traditionally, fixing them meant asking IT for help, finding a developer, getting a budget approved and waiting for the work to be done. Often, the problem was small enough that nobody thought it was worth the investment.

AI has changed that equation.

Today, almost anyone can describe an application to an AI coding tool and have something working a few hours later. A tracker, a form connected to a spreadsheet, a script that reads an inbox or even an application that drafts replies to customers. What once required a developer can now be built by the person who actually needs it.

And why wouldn't they? If you've spent years waiting for IT to fix a problem that you can now solve yourself in an afternoon, the temptation is obvious.

But there is a catch. These applications are often being built without anyone considering where the data goes, who can access it, how it connects to other systems or who is responsible for maintaining it.

This is the latest version of an old problem: shadow IT. Only this time, the technology is moving considerably faster than the people responsible for governing it.

So should businesses stop employees from building their own applications with AI? Probably not. The more useful question is how to give people the freedom to solve their own problems without creating a collection of unmanaged systems that nobody knows about.

## What exactly is a shadow AI app?

Shadow AI is generally used to describe employees using AI tools that their organisation hasn't approved. A familiar example would be someone pasting a customer contract or patient record into a public AI chatbot to help summarise it.

A shadow AI app takes things a step further.

Rather than simply using an AI tool, an employee uses an AI coding assistant or application builder to create something that actually runs. It might store information, connect to other systems, process documents or perform tasks automatically.

The practice of building applications in this way is often called *vibe coding*. The UK's National Cyber Security Centre (NCSC) describes it as giving an AI agent a high-level prompt and allowing it to build an application with significant autonomy.

There is an important distinction here. Pasting a document into an unapproved chatbot creates a potential data exposure. Building an application creates something that can continue to access, process and store information long after the original interaction has finished.

The application might contain passwords, API keys and connections to business systems. It might also become something that other employees rely on every day.

The Cloud Security Alliance (CSA) has started referring to this as "shadow operations". Its research describes employees deploying applications that process business data independently, without IT or security teams being involved.

Perhaps more concerningly, this can happen using platforms that the organisation has already approved. An employee might be using an AI builder included in software the company already pays for. From an IT perspective, the platform is perfectly legitimate. The application being built inside it might not be.

This makes traditional approaches to detecting shadow IT considerably less effective.

## Why is this happening now?

The need for employees to build their own tools is nothing new.

Some years ago, before the arrival of modern language models, we published a paper called *How to Achieve Frictionless Business*. The central argument was that much of the inefficiency in modern organisations sits between their existing systems.

Businesses invest heavily in major applications such as SAP, Oracle and other enterprise platforms. These systems are generally very good at what they were designed to do. But they don't necessarily cover every process that happens around them.

The result is that employees spend time moving information between systems, maintaining spreadsheets and finding their own ways to fill the gaps.

We described this as the iceberg problem. The costs that businesses can easily identify sit above the waterline. The wasted time, manual processes and inefficiency underneath are much harder to see, even though they can represent a considerable expense.

Our argument was that businesses needed to give the people doing the work more control over improving their own processes, rather than relying entirely on central IT departments to solve every problem.

That argument still holds true. What's changed is the technology available to do it.

Previously, building an application to solve one of these problems required a developer, a platform and some investment. Today, it might require little more than a description of what you want.

The barrier to building software has fallen dramatically, but the responsibilities that come with running software haven't disappeared.

This is why shadow AI is becoming such a difficult issue for organisations. The people building these applications are often doing something perfectly sensible from their own perspective. They have identified a problem and found a way to fix it.

Unfortunately, they might also have created a new security, compliance and maintenance problem in the process.

The available research suggests this is already happening at scale, although much of it comes from security vendors and should be considered in that context.

A 1Password survey of more than 5,000 knowledge workers and IT and security professionals, published in October 2025, found that 27% of employees had worked on AI-based applications that their employer had not approved.

BlackFog's survey of 2,000 employees at larger UK and US companies, reported in January 2026, found that 51% had connected AI tools to other work systems or applications without IT approval or oversight.

The NCSC has also observed larger, traditionally risk-averse organisations building tools for individual employees or teams that would previously have been features in commercially purchased software.

In other words, this isn't just a problem with people experimenting with AI at home. It is already happening inside established businesses.

## Where does the real risk sit?

The interesting thing about shadow AI applications is that the biggest risk isn't necessarily that they don't work.

In fact, the opposite can be true. They work well enough that people start relying on them, even though they haven't been built or tested to the same standards as the systems they are replacing or supplementing.

Consider what happens when an employee builds a simple application to manage customer information. It might work perfectly well for the person who created it. But where is the information stored? Can other people access it? What happens when the employee leaves? Is there a record of changes? And what happens if the application is suddenly unavailable?

These are questions that would normally be considered when developing business software. With AI-built applications, they are often overlooked.

There are several recurring problems:

| What goes wrong | Why it happens | What it can mean |
|---|---|---|
| Data is stored somewhere unknown | The AI builder uses whatever storage is easiest to configure | Client or patient records end up in personal accounts or unregistered databases |
| Passwords and API keys are exposed | Generated code can place secrets somewhere accessible to the browser | Other people can potentially use those credentials to access business systems |
| Access controls are missing | The application works for its creator, but nobody tests other user permissions | Private information becomes accessible to people who shouldn't see it |
| Nobody owns the application | There was no formal development project or handover | The original builder leaves and the application continues running without supervision |
| There is no audit trail | The application wasn't designed to record individual actions | The organisation cannot demonstrate who accessed or changed information |
| Integrations are fragile | The application relies on screen scraping or exported files rather than supported connections | A routine change to another system breaks the application |

These aren't just theoretical problems.

In February 2026, security researchers at Wiz reported finding serious security exposures in Moltbook, an AI social network built using AI-assisted development. The exposed database contained approximately 1.5 million API tokens and 35,000 email addresses. The issue included an API key exposed in the application's page source.

There has also been the CVE-2025-48757 vulnerability, involving database access rules in applications generated by an AI builder that could allow unauthorised access to private information.

The wider impact is beginning to show up in breach reporting too. IBM's 2026 Cost of a Data Breach Report, as summarised by Baker Donelson, found that incidents involving employees' shadow AI had more than doubled in a year, from 20% to 43%. Among organisations experiencing an AI-related incident, 92% lacked proper AI access controls and 68% had no AI governance policy.

There is another important point here. None of these problems changes the organisation's legal responsibilities.

Under UK GDPR, the organisation remains responsible for personal data it processes as a data controller, regardless of whether an employee used an approved application or built something themselves with AI.

You cannot simply explain to a regulator that nobody in IT knew the application existed.

## What does the NCSC recommend?

The NCSC has taken a particularly interesting position on AI-assisted software development.

On 24 March 2026, it warned that AI-generated code currently poses intolerable risks for many organisations, while also recognising that the potential business benefits will make the technology difficult to resist.

Its subsequent guidance, published on 18 June 2026, is more practical. Rather than treating all AI-assisted development as equally dangerous, it describes a spectrum of uses and recommends applying safeguards according to the risks involved.

The NCSC puts it rather well:

"The risk isn't in using AI. The risk is not applying the right safeguards when the stakes are high."

For example, using AI to create a prototype or a simple internal tool with no sensitive information involved is very different from using it to build an application that manages customer records or controls access to a financial system.

The NCSC is relatively comfortable with AI doing much of the work in low-risk situations. But it expects considerably more human oversight when applications handle authentication, permissions, sensitive personal information, credentials or safety-critical processes.

This is a sensible approach, but it raises another problem.

The NCSC guidance assumes that somebody can recognise where an application sits on that risk spectrum. With shadow AI, the person building the application might not have the technical knowledge to make that assessment.

Something that starts as a simple demonstration on Monday could be holding live customer information by Friday. An application that was originally intended for one person might suddenly become essential to an entire department.

Somebody needs to be able to see when that happens.

## Why banning AI-built applications won't work

The obvious response might be to prohibit employees from building their own applications.

Unfortunately, this is unlikely to solve the problem.

The BlackFog research found that 63% of respondents considered it acceptable to use AI tools without IT oversight when no approved alternative was available, and 60% agreed that unsanctioned tools were worth the security risk if they helped people work faster or meet a deadline.

The figures are revealing because they show that employees aren't necessarily ignoring security for the sake of experimenting with technology. They are trying to get their jobs done.

Anyone who has worked in IT for long enough will recognise this pattern. We have been through it with spreadsheets, Microsoft Access databases and unsanctioned cloud applications.

When a business doesn't provide people with the tools they need, they find their own. A policy might discourage them from doing so openly, but it doesn't remove the underlying problem.

The more successful approach has generally been to provide a sanctioned alternative that is almost as easy to use as the unofficial one.

This is where businesses need to think differently about AI governance. Instead of trying to prevent employees from building applications, they need to establish where those applications can be built and what safeguards apply.

## How to bring shadow AI applications under control

The first step is to find out what already exists.

This sounds straightforward, but it is important to create an environment where employees feel comfortable admitting what they have built. If the first response is to ban everything or start looking for someone to blame, people will simply stop telling you.

Ask departments what they have created, look at the AI builders already available inside licensed platforms and check network activity for connections to external AI services.

Once you have an idea of what exists, the next step is to understand what each application actually does.

The Cloud Security Alliance proposes a three-tier approach to managing these applications. The following is a practical interpretation of that model.

| Tier | Type of application | Recommended approach |
|---|---|---|
| 1. Low risk | Uses no personal, client or patient data, serves one person or team and doesn't change anything in a core system | Allow it to run, but register it and identify an owner |
| 2. Moderate risk | Holds personal, client or patient data, or is relied upon by people beyond the original team | Rebuild it on a governed platform with proper sign-in, permissions and ownership |
| 3. High risk | Writes to a system of record, influences decisions about individuals or includes an AI agent that acts autonomously | Treat it as a governed business process, with controlled permissions, human approval where appropriate and a complete audit trail |

The distinction is important.

Not every application needs to go through an enterprise software development process. If someone has built a simple tool to organise their own work, there may be very little reason to interfere.

But when an application starts processing personal information or interacting with important business systems, the situation changes.

At that point, it needs to be treated as business software, regardless of how it was created.

Registration should be quick and straightforward. You want employees to tell you what they have built, not feel that they are reporting a security incident every time they create a spreadsheet replacement.

Most of what you find will probably be relatively harmless. Being able to demonstrate that you recognise this is important if you want people to be honest about the applications that carry more risk.

## Fix the foundations before building more applications

There is another way to look at this problem.

In *How to Achieve Frictionless Business*, we used the analogy of an inherited house with a cracked roof and subsiding foundations.

You could spend all your time repairing the roof, replacing windows and fixing the cracks in the walls. But if the foundations are still moving, those problems will keep returning.

The better approach is to fix the foundations first.

The same principle applies to AI-built applications.

If every employee has to work out how to manage user accounts, permissions, integrations, version control and audit logging every time they build something, you are simply creating the same problems repeatedly.

These are things that should be provided once, as part of the underlying platform.

There are six areas worth considering:

**Identity**

Employees should sign in using accounts that the organisation already manages. When someone leaves, their access should be removed without having to track down every application they have ever created.

**Permissions**

Applications need to recognise what different people are allowed to see and do. Permissions should be managed consistently rather than relying on individual application builders to get everything right.

**Integration**

Core business systems should be connected through supported interfaces wherever possible. If an application needs information from an ERP, case management or patient administration system, it should reuse an established connection rather than inventing its own.

**Versions and environments**

There should be a record of who changed an application and when. Changes need to be tested somewhere other than the live production environment, with a way to roll back if something goes wrong.

**Audit trails**

It should be possible to establish what an application has done, who initiated an action and whether somebody approved it. This is particularly important when applications are processing sensitive information or making decisions that affect customers, patients or clients.

**Hosting**

The organisation needs to know where information is stored and processed. For some businesses, particularly those working in regulated industries, the ability to choose the hosting environment is an important requirement.

Once these foundations are in place, building the next application becomes much easier. The employee can concentrate on solving the actual business problem rather than recreating the infrastructure that every application needs.

This is also particularly important when introducing AI agents.

An AI agent given direct access to a database can potentially do anything that the database permissions allow. An agent that has to call a governed business process can only perform the actions that process permits. The workflow can also require human approval at the appropriate points and record what happened.

In other words, the important thing isn't just controlling the AI model. It is controlling what the AI is allowed to do.

## What about regulated industries?

For businesses operating in regulated environments, the consequences of unmanaged applications can be considerably more serious.

In the NHS, DCB0160 places clinical risk management responsibilities on the organisation deploying and using a health IT system. If an application built by an employee starts influencing patient care, the organisation should establish with its Clinical Safety Officer whether it falls within the scope of that standard.

In legal services, the authorised person remains responsible for work undertaken with the assistance of AI. The Solicitors Regulation Authority expects firms to maintain appropriate supervision and accountability.

Imagine an application that drafts correspondence, checks documents or files information on a client matter. If nobody can establish who approved its output, what information it used or whether anyone checked the result, the firm has a problem.

We have explored this issue in more detail in [Supervising AI on volume files after Mazur](https://www.toca.io/news/learn/supervising-ai-on-volume-files-after-mazur/).

The important distinction is that the regulatory responsibilities don't disappear just because an application was built using AI. If anything, the ease with which people can now create applications makes proper governance more important.

## How Toca approaches the problem

Toca is a UK-hosted low-code platform designed for regulated, high-volume business processes.

The idea is to provide the foundations that individual application builders shouldn't have to recreate every time they want to solve a problem.

Teams can build applications, portals and automations that connect to the systems they already use. Where APIs are available, integrations can use those. Where they aren't, RPA can be used to interact with existing systems.

Once a system has been connected, that integration can be reused by other applications rather than being rebuilt each time.

Users can sign in through single sign-on or passkeys, while roles distinguish between people building applications and those administering the platform. Workspaces are versioned using Git, giving changes an author, a history and a way back. Applications can be developed and tested in one environment before being moved into production.

The platform also records the actions taken by workflows in an audit trail.

AI is treated in much the same way. Copilot Studio agents can use Toca workflows as tools over MCP, allowing them to interact with business processes through defined interfaces rather than having unrestricted access to underlying systems.

Toca's document AI platform, Spectral, takes a different approach to document analysis. It uses more than one AI model to examine findings and sends disagreements between models to a person for review.

Hosting is available in Toca's UK cloud, the customer's own cloud or on-premises servers, depending on the requirements of the organisation.

Toca holds ISO/IEC 27001, ISO/IEC 42001 and Cyber Essentials Plus certifications and is listed on G-Cloud 15.

The platform currently runs around 276,000 workflows a day. These include eTriage across NHS trusts, claims processing for UK volume law firms and payroll services for approximately 1,750 schools through EPM.

The point isn't that every AI-built application needs to become a Toca project. If an employee has built a harmless little tool that saves them ten minutes a day, there may be no reason to change it.

But if that application starts holding personal information, connecting to core business systems or performing work that other people rely on, it needs a more substantial foundation.

If your staff have already built something that concerns you, [get in touch with us](https://www.toca.io/contact). We can spend twenty minutes looking at what it does and what systems it touches, then demonstrate how one part of it could run on Toca, including the permissions, approvals and audit trail.

You can also find out more about [the Toca platform](https://www.toca.io/platform).

## When you don't need a low-code platform

It is worth making one final point.

Not every application built with AI needs an enterprise platform behind it. If the application is only used by one person, contains no sensitive information and doesn't interact with important business systems, a simple registration process and a named owner might be all that is required.

The NCSC's guidance supports this distinction. Low-risk experimentation should be encouraged, not buried under unnecessary processes.

A platform starts to make sense when applications become business-critical, when they handle personal information, when several applications need to connect to the same systems or when AI agents are being given the ability to take actions.

The objective isn't to turn every small application into a major IT project. It is to make sure that the applications that matter are built on foundations that can support them.

## Questions

### What is a shadow AI app?

A shadow AI app is an application, automation or AI agent that an employee has built using AI tools and put into use without appropriate IT or security oversight. Unlike ordinary shadow AI, which usually involves using unapproved AI services, these applications can continue running, storing data and connecting to other business systems.

### Is vibe coding the same as shadow IT?

No. Vibe coding is a way of building software by describing what you want to an AI tool and allowing it to generate the code. Professional developers can use it as part of a properly managed development process. It becomes shadow IT when the resulting application is put into business use without appropriate ownership, review or governance.

### Should businesses ban employees from building applications with AI?

Generally, no. Banning the practice is unlikely to remove the underlying demand. Employees will often find another way to solve the same problems, potentially making the applications harder to identify. A better approach is to allow low-risk applications and provide a governed environment for anything that handles sensitive data or interacts with core systems.

### Who is responsible for an application built by an employee using AI?

Ultimately, the organisation remains responsible for the business activities and personal data it processes. Data protection, clinical safety and professional conduct obligations do not change depending on how the software was created. Every application should have a named owner responsible for its ongoing use.

### How can an organisation find existing shadow AI applications?

Start by asking employees and departments what they have built. Make it clear that the purpose is to understand and manage the applications, not punish people for solving problems. IT teams can also examine AI builders included in existing software licences and look for outbound connections to external AI services.

### Can AI agents safely interact with core business systems?

Yes, provided they are given controlled access and operate within appropriate safeguards. One approach is to have agents call governed workflows rather than giving them direct access to databases or systems of record. These workflows can enforce permissions, require human approval for important actions and record what the agent has done.

## Sources

- NCSC, [The 'vibe coding spectrum' approach to AI-assisted software development](https://www.ncsc.gov.uk/blogs/the-vibe-coding-spectrum-approach-to-ai-assisted-software-development), 18 June 2026.
- NCSC, [Vibe check: AI may replace SaaS (but not for a while)](https://www.ncsc.gov.uk/blogs/vibe-check-ai-may-replace-saas-but-not-for-a-while), 24 March 2026, and [NCSC CEO: Seize 'disruptive' vibe coding opportunity to make software more secure](https://www.ncsc.gov.uk/news/ncsc-ceo-seize-disruptive-vibe-coding-opportunity-to-make-software-more-secure).
- Cloud Security Alliance, [The Vibe Coding Governance Gap](https://labs.cloudsecurityalliance.org/research/csa-research-note-vibe-coding-ai-governance-gap-20260602-csa/), 2 June 2026.
- Cloud Security Alliance, [Shadow AI Apps: The Enterprise Attack Surface That Outpaces Monitoring](https://labs.cloudsecurityalliance.org/research/csa-research-note-shadow-ai-apps-enterprise-20260530/), 30 May 2026.
- 1Password, [The enterprise AI crisis: unsanctioned tools and unenforced policies](https://1password.com/blog/the-enterprise-ai-crisis-unsanctioned-tools-and-unenforced-policies), 30 October 2025.
- SecurityBrief UK, [Shadow AI use surges as staff trade security for speed](https://securitybrief.co.uk/story/shadow-ai-use-surges-as-staff-trade-security-for-speed), 29 January 2026, reporting BlackFog's survey.
- Baker Donelson, [Ten takeaways from IBM's 2026 Cost of a Data Breach Report](https://www.bakerdonelson.com/ten-takeaways-from-ibms-2026-cost-of-a-data-breach-report), 2026.
- Wiz, [Hacking Moltbook: AI social network reveals 1.5M API keys](https://www.wiz.io/blog/exposed-moltbook-database-reveals-millions-of-api-keys), 2 February 2026.
- Matt Palmer, [CVE-2025-48757](https://mattpalmer.io/posts/2025/05/CVE-2025-48757/), 29 May 2025.
- NHS England, [DCB0160: Clinical Risk Management: its Application in the Deployment and Use of Health IT Systems](https://digital.nhs.uk/data-and-information/information-standards/governance/latest-activity/standards-and-collections/dcb0160-clinical-risk-management-its-application-in-the-deployment-and-use-of-health-it-systems).
