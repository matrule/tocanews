---
title: "Elective SPoA software: what a Trust needs beyond e-RS (2026)"
subtitle: "Does a Trust simply need to manage referrals in e-RS, or does it need something that connects the referral decision to the rest of its hospital systems?"
seo_description: "Elective single point of access (SPoA) software for NHS Trusts: what NHS England requires, why e-RS alone may not be enough, and how eTriage, EPR modules, Consultant Connect, Strata Health, Novari Health and Synergos compare."
date: 2026-11-17
updated: 2026-11-17
author: "Mat Rule"
author_role: "Founder and CEO, Toca"
tag: "Comparisons"
section: learn
sites: ["health"]
image: ""
---
**The short answer.** An elective single point of access runs through NHS e-RS, which gives every specialty one digital front door for referrals and Advice and Guidance. What e-RS does not do is carry the consultant's decision into the Trust's own systems: the EPR, the document store and the services that arrange tests. For a small specialty e-RS may be enough. Where it isn't, the Trust needs software that connects the referral decision to the rest of the hospital, and that is what eTriage by Toca Health does.

## What is an elective single point of access?

The NHS uses "single point of access" for two quite different models. An urgent care SPoA is a coordination service for patients who might otherwise be taken to hospital: ambulance crews, GPs, care homes and community teams contact it for an assessment, and patients are directed to urgent community response, virtual wards or same day emergency care where appropriate. An elective SPoA concerns planned outpatient referrals and Advice and Guidance between primary and secondary care.

NHS England's technical guidance, published on 12 October 2026, describes a model in which Advice and Guidance requests and urgent and routine elective referrals, other than urgent suspected cancer, are directed into one digital entry point at specialty or sub-specialty level. A specialist reviews each request and decides the next step: advice that lets the GP manage the patient, a request for more information, a straight to test pathway, redirection to another service, or acceptance onto a consultant-led pathway.

Trusts were expected to implement the model by the beginning of October 2026 in the ten specialties they had prioritised for Advice and Guidance, with the broadest feasible coverage by March 2027. Once a specialty's SPoA is operating, its directly bookable services, Referral Assessment Services and Clinical Assessment Services stop receiving referrals, and everything comes through the single entry point.

## What NHS England expects Trusts to deliver

Dr Amanda Doyle's letter to GPs of 22 April 2026 (PRN02476) sets out how quickly requests should be handled, and NHS England's technical guidance repeats it.

| Request | Required response |
|---|---|
| Advice and Guidance | Within 5 working days of receipt |
| Routine referral | Next step actioned within 5 working days |
| Urgent referral | Next step actioned within 2 working days |

Every response must come from a named consultant, or from a local model with clear accountability to one, and the next step must be clear: an outpatient appointment, a diagnostic pathway organised by the Trust, or specific advice the GP can act on. NHS England has not set a national target for diverting a fixed proportion of referrals, and the clinical threshold for referral is unchanged.

Some practical requirements are easy to overlook. Consultants need triage time in their job plans, and Trusts need enough administrative support to prepare requests and move them on. A referral can be redirected to another specialty's SPoA without going back to the GP, which makes sense clinically but means the software has to support more than accept or reject.

Then there is the technology. NHS England says specialist review should take place within e-RS or a digital solution integrated with it, and that third-party solutions must be integrated as soon as reasonably practicable once the relevant APIs are available, or be decommissioned unless NHS England agrees an exception. The first e-RS API changes for SPoA reached production on 9 October 2026: SPoA services can now be identified in the Directory of Services, and Advice and Guidance requests carry a mandatory clinical intent from four national categories. Further changes are planned during 2026/27, including two-way conversations for triage services and reporting against the processing standards. For a Trust choosing software now, e-RS integration is not something to leave until later.

## Why e-RS alone may not be enough

e-RS is the national referral service and an essential part of the model. GPs submit requests through it, hospital clinicians review them in it, and it supports Advice and Guidance responses, referral conversion and comments returned to the GP. For a smaller specialty with straightforward needs, its worklist may be perfectly adequate.

But consider what happens when a consultant starts reviewing a referral. The request is in e-RS, the patient's history is in the Trust's electronic patient record (EPR), supporting documents may have to be downloaded separately, and the decision has to be recorded in the EPR and filed in the document management system. The consultant is working across several systems to deal with one patient.

That is not a failing of e-RS, which was designed as a national referral service, not a replacement for every Trust's own EPR, document store and integration engine. But if the outcome still has to be entered into two or three other systems, the administrative work has not disappeared; it has moved further along. Against the five and two working-day standards, a referral that is still waiting for someone to update the EPR or arrange a test has not really moved forward.

## What eTriage adds

eTriage by Toca Health is designed for that work. It works alongside e-RS rather than replacing it, so GPs carry on submitting referrals and Advice and Guidance through e-RS exactly as they do today. On the hospital side, each specialty has one worklist, with the patient's hospital record and supporting documents beside each request, and each case is assigned to the consultant reviewing it, so responsibility is clear and nothing is triaged twice.

More importantly, the decision is carried into the Trust's other systems. If a consultant decides a patient needs a diagnostic investigation before an outpatient appointment, they select straight to test, and the decision is written to e-RS, the EPR and the document store in the same action. The same applies to answering Advice and Guidance, converting advice into a referral, accepting a patient to the right clinic, asking for more information, redirecting a referral to another specialty or returning it with comments.

Many Trusts are also waiting on their EPR supplier for an interface, while the SPoA deadlines have already arrived. eTriage uses the EPR's APIs and the Trust's integration engine wherever they exist; where they don't, it uses automation under a service account whose permissions the Trust controls, with an audit trail, and moves onto the interface when it arrives. A Trust can get its first specialties running without waiting for every piece of integration.

It also handles referrals that don't yet arrive through e-RS: referrals by email, tertiary referrals from other hospitals, consultant-to-consultant referrals, and requests from optometrists and dentists without an e-RS login. NHS England expects these routes to join the national SPoA model progressively; in the meantime, eTriage puts them in the same specialty worklist rather than separate inboxes. The administrative team sees what is waiting, who is responsible and what has happened to each request, and messages between the GP and the hospital stay with the referral. e-RS remains the front door, and the Trust's booking team and PAS continue to manage appointments.

## e-RS alone versus e-RS with eTriage

| Requirement | e-RS alone | e-RS with eTriage |
|---|---|---|
| Single referral entry point | Yes | Yes, using the same e-RS entry point |
| Patient record | Viewed separately in the EPR | Available alongside the referral |
| Supporting documents | Downloaded separately | Presented with the case |
| Clinical decisions | Advice, referral conversion and comments | Advice, acceptance, straight to test, redirection and further information |
| EPR updates | Through local integration or manual entry | Written as part of the decision |
| Document filing | Separate Trust process | Written as part of the decision |
| EPR integration gaps | Dependent on supplier interfaces | APIs where available, automation where they aren't |
| Referrals outside e-RS | Managed separately | Can be included in the same specialty worklist |
| Case ownership | Managed through e-RS processes | Cases assigned to the reviewing consultant |

For some Trusts e-RS will be sufficient; for others, keeping the EPR and document store up to date makes a dedicated triage layer worthwhile.

## What other elective SPoA software is available?

eTriage is not the only option, and the others are built for different jobs. The comparison below is based on supplier information, G-Cloud 15 listings and NHS England's published material, reviewed on 17 November 2026.

| Product | Main purpose | Best suited to |
|---|---|---|
| **e-RS** | National referral and Advice and Guidance service | Trusts with straightforward requirements or existing integration |
| **eTriage (Toca Health)** | Consultant triage worklists integrated with the EPR and document store | Trusts needing to manage the complete referral decision |
| **EPR referral modules** | Referral management within the hospital's existing EPR | Trusts whose supplier can deliver the required functionality and integration |
| **Consultant Connect e-RS Connect** | Improved e-RS worklists and access to remote consultants | Trusts with a shortage of consultant capacity |
| **Strata Health** | Referral and care coordination across health and social care | Systems managing transfers of care, discharge and wider service access |
| **Novari Health** | Central intake, referral and waiting list management | Organisations managing referrals and requests across multiple services |
| **Synergos referapatient** | Structured referral and advice services for clinicians | Referrals from clinicians and hospitals outside the standard e-RS route |

**Consultant Connect**'s e-RS Connect gives clinicians a faster interface over their existing e-RS worklists, and its National Consultant Network can supply remote consultants to clear backlogs, which suits a Trust whose real shortage is clinical capacity. It describes EPR integration as available for uploading cases automatically, but its published information does not describe the same breadth of EPR and document-store write-back as eTriage.

**Strata Health**'s Strata PathWays brings together referrals from e-RS and other sources and moves patients between health, social care and voluntary sector services, including discharge and transfers of care. That is a different proposition from a consultant worklist for elective referrals and Advice and Guidance.

**Novari Health**'s Novari eRequest provides central intake that can be configured for many kinds of request, from specialist referrals to imaging requisitions and surgical waiting lists. Its G-Cloud price list prices the NHS e-RS interface and other integrations separately, so compare the total cost rather than the platform licence.

**Synergos**, from Bloomsbury Health, and its referapatient service focus on structured referrals and advice from referring clinicians, which helps where requests originate outside e-RS, including urgent referrals between hospitals: Barking, Havering and Redbridge University Hospitals publishes referapatient as its route for emergency neurosurgery referrals. Its published technical information lists ETL, HL7, FHIR and RESTful API capabilities, but not which hospital systems it writes to.

**EPR suppliers** offer referral management modules too, and Dedalus, Epic, IMS Maxims, InterSystems, Nervecentre and Oracle Health are on NHS England's e-RS API partner list. If your supplier can deliver the full SPoA functionality, including e-RS integration and write-back, this may be the most straightforward route.

These are not direct substitutes: a Trust might need extra consultants, a discharge platform and an elective triage system, each for a different part of the problem.

## Choosing the right software for your Trust

Before comparing demonstrations or prices, work out where the work is actually getting stuck. Four questions narrow the options.

**1. Does the supplier integrate with e-RS?** NHS England's guidance is clear that third-party solutions must integrate with e-RS once the relevant APIs are available, unless an exception is agreed. Ask whether the integration is two-way, whether it uses the official e-RS API and whether the supplier is on NHS England's accredited partner list. Toca is on that list, and eTriage uses the e-RS API.

**2. What happens after the consultant makes a decision?** This is the most important question. Take a straight to test referral and follow it through: does the decision update e-RS, the EPR and the document management system, or does someone still enter the same information elsewhere?

**3. How does the software connect to your existing systems?** Ask whether the supplier uses your EPR interfaces and integration engine, and what happens where those interfaces don't exist. Waiting for an EPR supplier can hold up an otherwise straightforward project, and any alternative needs to be secure, auditable and acceptable to the Trust's technical and information governance teams.

**4. How long will it take, and what will it cost?** Include implementation, integrations, support and any additional charges, model the total over three years at your expected referral volumes, and ask when the first specialties can realistically go live. eTriage's first specialties are typically live within weeks of contract, at typically £1 per referral in NHS acute and general hospitals with no other costs, and it is available through G-Cloud.

## Making the elective SPoA work in practice

Getting referrals into one digital entry point is only part of the job; the real work happens after the request arrives. The best way to assess any of these products is to follow a real referral from arrival to outcome and count how much is still done by hand, how many systems are involved and how long the patient waits for the next step. That will tell you far more than a demonstration of a tidy worklist.

If you are implementing an elective SPoA, [book a demonstration with Toca Health](https://www.toca.io/health/contact?topic=etriage). We will take one of your specialties and show how a referral arrives from e-RS, how the consultant reviews it and how the decision reaches your EPR and document store. For the wider market, see [NHS referral triage software compared](https://www.toca.io/news/learn/nhs-referral-triage-software-compared/), or visit [Toca Health eTriage](https://www.toca.io/health/etriage).

## Frequently asked questions

### What software can an NHS Trust use to run an elective single point of access?

Trusts can use NHS e-RS directly, an existing EPR referral module or a specialist platform such as eTriage by Toca Health. Other products include Consultant Connect e-RS Connect, Strata Health, Novari Health and Synergos. The right choice depends on whether the Trust needs basic referral management, additional consultant capacity or integration with its own hospital systems.

### Can an elective SPoA run on e-RS alone?

Yes. e-RS provides the national entry point and supports specialist review, but it does not update each Trust's EPR or document management system. Those outcomes have to be carried across by local integration or entered by hand.

### What are the NHS response standards for elective SPoA?

Advice and Guidance within five working days, routine referrals actioned within five working days and urgent referrals within two, with every response from a named consultant or an accountable local model.

### Does elective SPoA software have to integrate with e-RS?

Yes. NHS England's technical guidance requires specialist review within e-RS or a digital solution integrated with it. Third-party solutions must integrate as soon as reasonably practicable once the relevant APIs are available, or be decommissioned unless an exception is agreed.

### What is the difference between elective SPoA and urgent care SPoA?

An urgent care SPoA coordinates care for patients who might otherwise be taken to hospital, directing them to community or urgent services. An elective SPoA brings Advice and Guidance and planned referrals into each specialty through a single digital entry point.

### Does elective SPoA aim to reduce hospital referrals?

Not through a target. NHS England has said there is no national target for diverting a fixed proportion of referrals. The aim is the most appropriate next step for each patient, and the clinical threshold for referral is unchanged.

### How much does elective SPoA software cost?

It depends on the supplier, the functionality and the integrations. eTriage is typically £1 per referral in NHS acute and general hospitals, with no other costs. Other platforms may charge separately for interfaces, modules and implementation, so compare the full cost over the contract period.

## Sources

- NHS England, [Specialist advice and elective single point of access: what this means for you and your patients](https://www.england.nhs.uk/long-read/letter-specialist-advice-elective-single-point-of-access/), Dr Amanda Doyle, 22 April 2026, PRN02476.
- NHS England, [Elective Single Point of Access: technical guidance](https://www.england.nhs.uk/long-read/elective-single-point-of-access-technical-guidance/), 12 October 2026, PRN02321.
- NHS England Digital, [e-RS API roadmap: specialist advice and single points of access](https://digital.nhs.uk/services/e-referral-service/api/updates-and-releases/roadmap/spoa).
- NHS England Digital, [e-RS API: current integrated partner list](https://digital.nhs.uk/services/e-referral-service/api/benefits).
- NHS England, [Single point of access (SPoA)](https://www.england.nhs.uk/long-read/single-point-of-access-spoa/).
- Consultant Connect, [e-RS Connect](https://www.consultantconnect.org.uk/what-we-do/e-rs-connect/).
- Strata Health, [Navigation and single eReferral system](https://stratahealth.com/uk/solutions/navigation-single-ereferral-system/) and [G-Cloud 15 listing](https://www.applytosupply.digitalmarketplace.service.gov.uk/g-cloud/services/714630161103857).
- Novari Health, [G-Cloud 15 listing](https://www.applytosupply.digitalmarketplace.service.gov.uk/g-cloud/services/399130345636589).
- Bloomsbury Health, [Synergos](https://www.bloomsburyhealth.org/synergos) and [referapatient](https://www.referapatient.org/).
- Barking, Havering and Redbridge University Hospitals, [Emergency neuro referrals](https://www.bhrhospitals.nhs.uk/emergency-neuro-referrals/).
- Toca Health, [eTriage](https://www.toca.io/health/etriage), [governance](https://www.toca.io/health/governance) and [Royal Berkshire, in its own words](https://www.toca.io/news/articles/royal-berkshire-e-triage-in-its-own-words/).
