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
**The short answer.** A community trust can see where its nurses' days actually go without asking them to record anything. An Android app on the trust-issued phone reports its location in the background, Toca receives each reading through a secure API and loads it into the trust's own data warehouse, and there the readings are matched to patient addresses to show which visits happened, when, and how much travelling sat between them. Toca designed this for an NHS community trust with 600 to 700 community nurses, as a first project scoped at five days of professional services.

## The situation

A community trust runs on visits. Several hundred nurses see patients at home, each working through a list, and the trust's systems hold the plan: who is to be seen, by whom and roughly when. This trust wanted less paper, safer staff and fewer administrative tasks for the front line, and it chose to start with visits.

## The complication

The plan is recorded. The day is not. The order the visits were really made in, the time spent driving between them and how long each one took are known only if a nurse writes them down afterwards. Asking nurses to log every arrival and departure would add exactly the administration the trust set out to remove.

## The question

How does a trust get a reliable record of the working day without asking its nurses for anything?

## The answer: use the phone the nurse already carries

The nurse's phone knows where it is. The design has three parts: an app on the phone, Toca in the middle, and the trust's data warehouse at the end.

| Step | What happens | Where |
|---|---|---|
| Capture | The app records the phone's GPS position in the background | The nurse's Android phone |
| Send | Each reading goes over HTTPS with the handset and SIM identifiers | Phone to a secure API on Toca |
| Store | Toca checks the device and loads the reading | The trust's data warehouse |
| Geocode | Each patient address is converted, once, to a latitude and longitude | The warehouse |
| Match | A reading within a set distance of an address counts as being there | The warehouse |
| Resolve | Where two addresses are close together, the time of the reading decides which visit it was | The warehouse |

### The app

A small Android app with nothing to fill in and nothing to tap. It runs in the background during working hours and sends the phone's position with the handset and SIM identifiers, so every reading belongs to a device the trust issued and nobody signs in. It is packaged as an APK, and the trust's IT team installs and updates it on every phone through Microsoft Intune.

![Mock-up of the Android app: a status screen, a what is recorded screen and the lock screen notification](2026-11-20-community-visits-app.svg){: .screen }

Mock-up. The status screen, the staff notice inside the app, and the standing notification.
{: .under }

### The platform

Each phone calls a secure API on Toca over HTTPS. A workflow receives the reading, checks that it came from a phone the trust issued and loads it into the data warehouse the trust prefers. The backend is sized for 600 to 700 phones reporting through the working day, and the platform can be hosted in the trust's own environment.

![Mock-up of the workflow on Toca: a reading arrives at the API, the device is checked, the reading is loaded to the warehouse and matched to an address](2026-11-20-community-visits-workflow.svg){: .screen }

Mock-up. One reading passing through the workflow, with the data each phone sends.
{: .under }

### The result: coordinates become visits

A reading is a latitude and a longitude, and a patient record holds an address, so each address is geocoded once in advance. The two never match exactly, because the phone may be in a car three doors down. The haversine formula gives the distance in metres between a reading and an address, and a reading inside a radius the trust chooses counts as the nurse being there. Where two patients live within the same radius, the time of each reading tells the visits apart.

![Mock-up of the service dashboard: a map of one nurse's morning with each address and its match radius, and the visits and travel worked out from the readings](2026-11-20-community-visits-dashboard.svg){: .screen }

Mock-up with illustrative data. One nurse's morning: each address with its match radius, and the visits and travel worked out from the readings.
{: .under }

## The projected impact

These are projections. The trust could not say how much of a nurse's day is travel, because nobody had measured it, so the first result is the baseline itself. From it the trust expected:

- **Visibility.** An accurate account of routes, visit patterns and response times.
- **Shorter routes.** Avoidable journeys show up once the journeys are visible, which cuts travel time and cost.
- **A complete record.** The app runs with no manual step, so the data has no gaps left by memory.
- **A quick rollout.** Intune puts the app on every phone and keeps it up to date.

## Before the first phone reports

This is location data about staff, so settle the governance before the build. Carry out a data protection impact assessment, tell staff plainly what is collected, when and why, and record during working hours only. Decide whether the data is for planning the service or for managing individuals, say which, and hold to it.

To see how this would work with your devices and your warehouse, [talk to Toca Health](https://www.toca.io/health/contact).

## Questions

### Does the nurse have to do anything?

No. The app has nothing to fill in. The trust's IT team installs it through Microsoft Intune and it runs in the background during the working day.

### How is a GPS reading matched to a patient's address?

Each address is geocoded to a latitude and longitude in advance. The haversine formula gives the distance between a reading and an address, and a reading within a set number of metres counts as a visit. Where two addresses fall within the same radius, the time of each reading tells the visits apart.

### Where is the location data held?

In the trust's own data warehouse. Readings travel from the phone to Toca over HTTPS, and Toca's platform can be hosted in the trust's own environment.

### Does a trust need a data protection impact assessment for this?

It should do one before building. The ICO lists tracking an individual's geolocation among the processing that calls for a DPIA when combined with other risk factors, and says workers must be told about monitoring.

## Sources

- Toca's solution design for an NHS community trust with 600 to 700 community nurses. The trust is not named here.
- Information Commissioner's Office, [When do we need to do a DPIA?](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/accountability-and-governance/data-protection-impact-assessments-dpias/when-do-we-need-to-do-a-dpia/)
- Information Commissioner's Office, [Employment practices and data protection: monitoring workers](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/employment/monitoring-workers/). The ICO notes that this guidance is under review following the Data (Use and Access) Act.
- Microsoft, [Add an Android line-of-business app to Microsoft Intune](https://learn.microsoft.com/en-us/intune/app-management/deployment/add-lob-android).
- Wikipedia, [Haversine formula](https://en.wikipedia.org/wiki/Haversine_formula).
