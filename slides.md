---
marp: true
theme: default
size: 16:9
title: You received a leak, now what?
description: A hands-on OPSEC simulation covering the full lifecycle of a leak
author: |
  Alex Pyrigiotis, Freedom of the Press Foundation
  Kolja Weber, FlokiNet
---

<style>
/* ===== Custom Journalist Theme ===== */
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Inter:wght@400;600;700&display=swap');

section {
  --navy: #0c2340;
  --red: #b52a1e;
  --gold: #b8860b;
  --cream: #faf6f0;
  --slate: #1e2a3a;
  --light: #ecf0f1;
  font-family: 'Inter', 'Helvetica Neue', sans-serif;
  background: var(--cream);
  color: var(--slate);
  padding: 60px;
}

h1 {
  font-family: 'Playfair Display', 'Georgia', serif;
  font-weight: 900;
  font-size: 2.8em;
  color: var(--navy);
  letter-spacing: -0.03em;
  line-height: 1.1;
}

h2 {
  font-family: 'Playfair Display', 'Georgia', serif;
  font-weight: 700;
  font-size: 1.8em;
  color: var(--navy);
  border-bottom: 3px solid var(--red);
  padding-bottom: 0.25em;
  margin-bottom: 0.6em;
}

h3 {
  font-weight: 700;
  color: var(--red);
  font-size: 1.2em;
}

strong { color: var(--red); }
section.lead strong { color: white; }

a { color: var(--red); text-decoration: underline; }

blockquote {
  border-left: 4px solid var(--red);
  padding-left: 1em;
  margin: 1em 0;
  font-style: italic;
  color: var(--slate);
  background: rgba(181, 42, 30, 0.08);
  padding: 0.8em 1em;
  border-radius: 0 8px 8px 0;
}

table {
  width: 100%;
  border-collapse: collapse;
  font-size: 0.85em;
  margin: 0.5em 0;
}
th {
  background: var(--navy);
  color: white;
  padding: 8px 12px;
  text-align: left;
}
td {
  padding: 8px 12px;
  border-bottom: 1px solid #ddd;
}
tr:nth-child(even) td {
  background: rgba(12, 35, 64, 0.06);
}

code {
  background: rgba(12, 35, 64, 0.12);
  padding: 0.15em 0.4em;
  border-radius: 4px;
  font-size: 0.85em;
  font-family: 'JetBrains Mono', 'Fira Code', monospace;
}

/* --- Lead/Title slide --- */
section.lead {
  background: linear-gradient(135deg, var(--navy) 0%, #162d50 100%);
  color: white;
  text-align: center;
  justify-content: center;
  align-items: center;
  display: flex;
  flex-direction: column;
}
section.lead h1 {
  color: white;
  font-size: 3em;
  margin-bottom: 0.2em;
}
section.lead h1::after {
  content: '';
  display: block;
  width: 80px;
  height: 3px;
  background: var(--red);
  margin: 0.4em auto;
}
section.lead p {
  font-size: 1.2em;
  opacity: 0.9;
  margin: 0.2em 0;
}
section.lead small {
  opacity: 0.7;
  margin-top: 1.5em;
  font-size: 0.5em;
}

/* --- Section divider slides --- */
section.section {
  background: linear-gradient(135deg, #0c2340 0%, #1a3a5c 100%);
  color: white;
  justify-content: center;
  padding: 80px;
}
section.section h2 {
  color: white;
  border: none;
  font-size: 2.5em;
  margin-bottom: 0.2em;
}
section.section h2::before {
  content: '';
  display: block;
  width: 60px;
  height: 4px;
  background: var(--red);
  margin-bottom: 0.3em;
}
section.section p {
  font-size: 1.1em;
  opacity: 0.8;
}

/* --- Image backgrounds for section dividers --- */
section.section-bg {
  justify-content: center;
  padding: 80px;
  color: white;
}
section.section-bg h1 {
  color: white;
  font-size: 1.1em;
  font-weight: 600;
  font-family: 'Inter', sans-serif;
  letter-spacing: 0.05em;
  text-transform: uppercase;
  opacity: 0.9;
  text-shadow: 0 2px 15px rgba(0,0,0,0.6);
  margin: 0 0 0.2em 0;
}
section.section-bg h2 {
  font-size: 2.5em;
  color: white;
  border: none;
  text-shadow: 0 3px 25px rgba(0,0,0,0.7);
}
section.section-bg h2::before {
  content: '';
  display: block;
  width: 60px;
  height: 4px;
  background: var(--red);
  margin-bottom: 0.3em;
}
section.section-bg p {
  color: white;
  font-size: 1.1em;
  text-shadow: 0 2px 15px rgba(0,0,0,0.6);
}

/* --- Story slide --- */
section.story {
  padding: 60px;
}
section.story h2 {
  font-size: 1.6em;
}
section.story .citation {
  font-size: 0.5em;
  color: #666;
  margin-top: 1.5em;
  border-top: 1px solid #ddd;
  padding-top: 0.8em;
}
section.story .excerpt {
  background: rgba(12, 35, 64, 0.04);
  border-left: 3px solid var(--gold);
  padding: 0.6em 1em;
  margin: 0.8em 0;
  font-style: italic;
  font-size: 0.75em;
}
section.story small {
  margin-top: 1.5em;
  font-size: 0.7em;
}


/* --- Footer --- */
section::after {
  content: attr(data-marpit-pagination) ' / ' attr(data-marpit-pagination-total);
  font-size: 0.75em;
  color: rgba(12, 35, 64, 0.65);
  bottom: 20px;
  right: 30px;
  position: absolute;
}

/* --- Lists --- */
ul { line-height: 1.6; margin: 0.3em 0; }
li { margin-bottom: 0.3em; }

/* --- Columns via flex --- */
.columns {
  display: flex;
  gap: 2em;
}
.columns > div {
  flex: 1;
}

</style>

<!-- ===== TITLE SLIDE ===== -->

<!-- _class: lead -->
![bg right:45%](images/wish_you_were_here.png)

# You received a leak, now what?

**A hands-on OPSEC simulation**

<small>
<div class="columns">
<div>
Alex Pyrgiotis<br>
Freedom of the Press Foundation
</div>
<div>
Kolja Weber<br>
FlokiNet
</div>
</div>
</small>

---

## Aspects of a tip

<div class="columns">
<div>

### 1. First contact
How sources learn where to send tips.

### 2. GrapheneOS + Signal = ❤️
Hardening the mobile tipline

### 3. Perimeter security
Walls have ears, we have gears.

</div>
<div>

### 4. QubesOS + SecureDrop = ❤️
Compartmentalization as a defense.

### 5. Post-handling
Store it, share it, publish it, without burning your source.

</div>
</div>

---

<!-- _class: section-bg -->
![bg brightness:0.6](images/bench.jpg)

# Part I

## The first-contact problem
*How sources learn where to send tips.*

---

<!-- _class: story -->
## The tipline situation in 2013

In 2013, an anonymous user contacted Micah Lee, then staff technologist at EFF
and CTO at Freedom of the Press Foundation:

<div class="excerpt">

From: anon108@■■■■■■■■■
To: Micah Lee
Date: Fri, 11 Jan 2013

Micah,

I’m a friend. I need to get information securely to **Laura Poitras** and her alone, but I can’t find an email/**gpg** key for her.

Can you help?

</div>


<div class="citation">

Source: [The Intercept —  Ed Snowden Taught Me To Smuggle Secrets Past Incredible Danger. Now I Teach You. ](https://theintercept.com/2014/10/28/smuggling-snowden-secrets/)

</div>

---

<!-- _class: story -->
## The tipline situation in 2013

That person was paranoid enough about security that even though they acquired
Laura's PGP key, they proposed Micah to tweet it, just to be sure.

<div class="excerpt">

From: 303@riseup.net
To: Micah Lee
Date: Mon, 28 Jan 2013

Hey Micah,
This is **Laura Poitras**.
Someone is trying to verify my fingerprint to this email. The person has proposed you **tweet the fingerprint**. Would you be able to tweet this to your acct:
**1EBF 5F15 850C 540B 3142 F158 4BDD 496D 4C6C 5F25**
Let me know if possible.
Thanks,
Laura

</div>

---

![fg width:1200px](https://theintercept.com/wp-content/uploads/2014/10/micah_tweet.png?w=540)

---

<!-- _class: story -->
## The tipline situation in 2013

(maybe skip this)

<div class="excerpt">

From: **Laura Poitras**
To: Micah Lee
Date: Thu, 9 May 2013

I’m working on something with **Glenn** and I really need to get him on a secure (preferably **Tails**) system. He does not have the technical skills to set this up himself, and I’m trying to keep things compartmentalized, so I don’t want to email him about this topic directly on a non-secure channel.

</div>

---

<!-- _class: lead -->
![bg brightness:0.95](https://www.franceinfo.fr/pictures/4DVmuRcH08VuGZhDpYOeWUNrbCw/0x0:1920x1080/1024x576/filters:format(avif):quality(50)/2016/08/23/citizen1.jpg)

# Black swans exist

---

<!-- _class: story -->
## Tiplines must be advertised to everyone

### Washington Post - Blended with the news articles

![fg](https://docs.securedrop.org/en/stable/_images/how_to_share_a_tip_securely.png)

<div class="citation">

Source: [Promoting Your SecureDrop Instance](https://docs.securedrop.org/en/stable/admin/deployment/getting_the_most_out_of_securedrop.html)

</div>

---

<!-- _class: story -->

![bg right:40%](https://docs.securedrop.org/en/stable/_images/nytimes_tweet.png)

<br>
<br>
<br>
Yes, even in print.
<br>
<br>
<br>
<br>
<br>
<br>
<br>
<br>

<div class="citation">

Source: [Promoting Your SecureDrop Instance](https://docs.securedrop.org/en/stable/admin/deployment/getting_the_most_out_of_securedrop.html)

</div>

---

## The tipline landing page

What IT should know:

- **No subdomains:** use `newsroom.org/tips` not `tips.newsroom.org`
- **No analytics:** no trackers, zero logs
- **Tor-friendly** no captchas, no Javascript
- **Trustworthy hosting provider:** censorship-resistant, zero logs

---

## The tipline landing page

What sources should know:

- **Not from work:** no corporate devices, no corporate network
- **Public spaces:** cafes, libraries, anywhere not associated with you
- **Files have fingerprints:** leaked files may get traced back to you
- **Instructions:** how to securely use Signal/SecureDrop/etc.
- **Loose lips sink ships:** never discuss whistleblowing activities

---

<!-- _class: story -->
![bg right:30%](images/chelsea.png)

## Chelsea Manning: what can go wrong

In 2010, Chelsea Manning was leaking classified documents. She felt isolated and confided in Adrian Lamo, a former "grey hat" hacker, via encrypted chat.

<div class="excerpt">
Manning wrote: "but im not a source for you ... im talking to you as someone who needs moral and emotional fucking support", and Lamo replied: "i told you, none of this is for print."
</div>

Spoiler alert: it was.

<div class="citation">

Source: [Wikipedia — Chelsea Manning](https://en.wikipedia.org/wiki/Chelsea_Manning#Manning_and_Adrian_Lamo)

</div>

---

<!-- _class: story -->
![bg right:30%](images/slide.webp)

## Where do we go from here?

A lot of things can go wrong. A lot of things can go right, as we learned from the now distant 2013.

In 2026, we have new tools and more experience.

Let's go **deeper**.

---

<!-- _class: section-bg -->
![bg brightness:0.35](images/grapheneos.webp)

# Part II

## GrapheneOS + Signal
*Your phone as a tipline.*

---

## Harden Signal. Now.

| Setting | Why it matters |
|---------|----------------|
| **Sealed sender** | Signal itself can't see who's talking to whom |
| **Disable link previews** | Previews = IP leak to the server behind the link |
| **Registration lock** | Blocks SIM-swap hijacking |
| **No notification content** | Prevents lock-screen metadata leaks |
| **No SIM card** | SMS/MMS = attack surface; 0-days love SMS |

---

**Thank you**

Questions? OPSEC war stories?
