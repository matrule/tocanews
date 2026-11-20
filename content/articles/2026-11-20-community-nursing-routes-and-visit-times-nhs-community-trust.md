---
title: "NHS community trust use case: nurse routes and visit times, without asking nurses to record them"
subtitle: "A community trust knows which visits were planned. How does it find out what the day actually looked like, without adding to the nurse's paperwork?"
seo_title: "NHS community trust use case: community nursing routes and visit times from GPS"
seo_description: "How an NHS community trust can see community nursing routes and visit times: a background Android app, a secure API on Toca's low-code platform, the trust's own data warehouse, and the projected impact."
date: 2026-11-20
updated: 2026-11-20
author: "Mat Rule"
author_role: "Founder and CEO, Toca"
tag: "Guides"
section: learn
sites: ["health"]
image: ""
draft: true
---
**The short answer.** A community trust can learn where its nurses' days actually go without asking them to record anything. A small Android app on the trust-issued phone reports its location in the background, Toca receives those readings through a secure API and loads them into the trust's own data warehouse, and there they are matched against patient addresses to show which visits happened, when, and how much travelling sat between them. Toca designed this for an NHS community trust with 600 to 700 community nurses, as a first project on its low-code platform scoped at five days of professional services. The projected impact is a picture of routes and visit times the trust has never had, and from it shorter routes, less time and money spent on travel, and no new task for the nurse.

## The plan is recorded, the day is not

A community trust runs on visits. Several hundred nurses see patients in their own homes, each working through a list, and the trust's systems hold the plan for all of it: who is to be seen, by whom, and roughly when. What those systems do not hold is the day as it turned out. In what order were the visits really made? How much of the shift was spent driving between them? How long did a visit take compared with the time allowed for it? Where the trust has answers, it is because a nurse wrote them down afterwards, and information recalled at the end of a shift is the least reliable kind there is.

The trust in this case had three aims that will be familiar to any community provider: less paper, safer staff, and fewer administrative tasks for the people on the front line. It chose to begin with visits, because almost every other question about a community service depends on knowing how the working day is spent. You cannot plan routes, size a team or judge whether a locality is short of staff from the schedule alone, any more than a haulier could run a fleet from the delivery notes.

That comparison is worth a moment. Logistics firms have had this information for years because their vehicles report it. A community nurse usually drives their own car, so there is no vehicle to instrument, and the obvious alternative is to ask the nurse to log arrivals and departures. But that creates exactly the administration the trust set out to remove, and it turns a clinician into a data entry clerk for a few minutes of every visit. So the real question is a narrower one: how does a trust get a reliable record of the working day without asking its nurses for anything at all?

## How Toca was used

The answer starts with something the nurse already carries. The trust's community nurses carry Android phones that the trust issues and manages, and a phone knows where it is. The design has three parts: an app on the phone, Toca in the middle, and the trust's data warehouse at the end.

The app is deliberately small. It has no screens to fill in and nothing to tap. It runs persistently in the background, captures the phone's GPS position, and sends each reading with the identifiers of the handset and SIM, so that every reading can be tied to a device the trust issued without anyone signing in. It is packaged as an APK and distributed through Microsoft Intune, the device management service the trust already uses, which means the trust's own IT team installs it and updates it on every phone from one place. The nurse does not download anything or change how they work.

Toca's platform does the connecting. It provides the secure API endpoints that the phones call over HTTPS, a backend sized for the volume that 600 to 700 phones produce across a working day, and the integration that loads the readings into the data warehouse the trust prefers. The platform can be hosted in the trust's own environment, so the location data stays under the trust's control from the moment it leaves the phone. Because the endpoints and the integration are configured on a low-code platform, the build is short, and it can be changed when the trust decides it wants something different from the data.

| Step | What happens | Where |
|---|---|---|
| Capture | The app records the phone's GPS position in the background | The nurse's trust-issued Android phone |
| Send | Each reading goes over HTTPS with the handset and SIM identifiers | Phone to a secure API on Toca |
| Store | Toca loads the readings into the warehouse | The trust's data warehouse |
| Geocode | Each patient address is converted, once, to a latitude and longitude | The warehouse, before any analysis |
| Match | A reading within a set distance of an address counts as being there | The warehouse |
| Resolve | Where two addresses are close together, the time of the reading decides which visit it was | The warehouse |

## Turning coordinates into visits

Collecting the readings is the easy half. A GPS reading is a pair of numbers, a latitude and a longitude, and a patient record holds an address, so nothing lines up until the two are expressed in the same terms. The first job is therefore geocoding: working out the coordinates of each patient address ahead of time, as a preparation step in the warehouse, so that the analysis has something to compare the readings with.

Even then the two will never match exactly. The phone may be in a bag in the hallway or in a car parked three doors down, and GPS itself drifts by a few metres. What the analysis needs is not equality but nearness, and for that Toca proposed the haversine formula, a piece of navigators' trigonometry that gives the distance between two points on a sphere from their latitudes and longitudes. The term was coined in 1835, long before anyone had a satellite to feed it. A reading that falls within a defined number of metres of a geocoded address is treated as the nurse being at that address. The radius is a setting, and choosing it is a judgement the trust makes about its own patch: too tight and a visit is missed because the nurse parked up the road, too loose and neighbouring houses merge into one.

Which raises the awkward case. What happens when two patients live in the same block, or next door to each other? Both addresses fall inside the radius and one stop looks like two visits. Here the timestamps do the work. Each reading carries the time it was taken, so overlapping matches can be separated by when they happened and counted once, which keeps the record of visits accurate where the geography alone cannot.

## The projected impact

These are projections, and it is worth being plain about why. The trust could not say, before a project like this, how much of a community nurse's day is spent travelling, because nobody had measured it. The first thing the project delivers is therefore the baseline itself.

From that baseline the trust expected four things. The first is operational visibility: an accurate account of the routes nurses take, and with it an understanding of visit patterns and response times that had only ever been estimated. The second is route optimisation, because once the journeys are visible, the avoidable ones are too: the doubling back, the two nurses crossing the same estate an hour apart. Shorter routes mean less travel time and lower travel cost, and time taken out of the car can go back to patients. The third is continuity. An app that runs unobtrusively in the background, with no manual step, produces a complete record, where anything that depends on people remembering produces a record with holes in it. The fourth is ease of rollout: because the app is managed centrally through Intune, it reaches every device quickly and stays up to date without visits to a desk.

Staff safety was one of the trust's three aims, and location data is the raw material for it. But this first project is analysis after the fact, in a data warehouse. A lone worker alert that someone watches in real time is a different design with different safeguards, and it should be scoped as its own piece of work.

## What to settle before the first phone reports

None of this is technically exotic, and that is rather the point: the difficult questions are not about software. This is location data about staff, and a trust should approach it as that from the first conversation.

Do the data protection impact assessment before anything is built. The Information Commissioner's Office lists tracking an individual's geolocation among the kinds of processing that call for one, and notes that employees may count as vulnerable because of the imbalance of power with their employer. Tell staff plainly what is collected, when and why; the ICO's guidance on monitoring workers says they must be told in a way that is accessible and easy to understand. Involve staff side early. Decide whether the data is for planning the service or for managing individuals, say which, and hold to it, because a project sold as route planning and then used in a disciplinary hearing will not survive its first month. Collect during working hours on trust devices only, and keep the raw readings no longer than it takes to turn them into visits.

There are practical checks too. Android is designed to stop apps running in the background in order to save battery, so a persistent app has to be granted the right permissions through device management and tested on the handsets the trust actually issues. And the patient addresses that make the matching possible are patient data, which is one more reason for the work to happen in the trust's own warehouse and not somewhere else.

## Where this fits, and where it does not

A trust whose scheduling system already records arrival and departure from the nurse's device may not need any of this, and should use what it has. The case for building it is strongest where the trust has phones in every bag, a data warehouse it trusts, and no reliable record connecting the two.

It is also a sensible first project for a platform. Nothing here is a product that a trust buys and leaves alone. It is three things the trust already owns, phones, device management and a warehouse, with the missing connections made between them, and the next request will come as soon as the first results are on a screen. A platform built for connecting systems lets the trust answer that request with a change and not a procurement.

If you run community services and want to see how this would work with your devices and your warehouse, [talk to Toca Health](https://www.toca.io/health/contact).

## Questions

### Can an NHS community trust record community nursing visits automatically?

Yes. A background app on the nurse's trust-issued Android phone can report its GPS position, and those readings can be matched against patient addresses in the trust's data warehouse to show which visits took place and when. The nurse records nothing.

### Does the nurse have to do anything?

No. The app has no screens to complete. It is installed and updated by the trust's IT team through Microsoft Intune and runs in the background during the working day.

### How is a GPS reading matched to a patient's address?

Each patient address is geocoded to a latitude and longitude in advance. The haversine formula then gives the distance between a reading and an address, and a reading within a set number of metres counts as a visit. Where two addresses fall within the same radius, the time of each reading is used to tell the visits apart.

### What is the projected impact?

Visibility of nurse routes and visit times that the trust did not have before, and from that the opportunity to shorten routes and reduce travel time and cost. The first result is a baseline: a measured account of how the working day is spent.

### Where is the location data held?

In the trust's own data warehouse. Readings travel from the phone to Toca over HTTPS, and Toca's platform can be hosted in the trust's own environment.

### Does a trust need a data protection impact assessment for this?

It should do one before building. The ICO lists tracking an individual's geolocation among the processing that calls for a DPIA when combined with other risk factors, and treats employees as a group that may be vulnerable. Staff must also be told what is collected and why.

### How long does it take to build?

For the trust described here, Toca scoped the work at five days of professional services on its low-code platform, as part of its standard onboarding. The trust's own preparation, the impact assessment and the geocoding of addresses, runs alongside.

## Sources

- Toca's solution design for an NHS community trust with 600 to 700 community nurses. The trust is not named here.
- Information Commissioner's Office, [When do we need to do a DPIA?](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/data-protection-impact-assessments-dpias/when-do-we-need-to-do-a-dpia/)
- Information Commissioner's Office, [Employment practices and data protection: monitoring workers](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/employment/monitoring-workers/). The ICO notes that this guidance is under review following the Data (Use and Access) Act.
- Microsoft, [Add an Android line-of-business app to Microsoft Intune](https://learn.microsoft.com/en-us/intune/app-management/deployment/add-lob-android).
- Wikipedia, [Haversine formula](https://en.wikipedia.org/wiki/Haversine_formula).
