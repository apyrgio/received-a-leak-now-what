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
  position: relative;
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
  position: absolute;
  bottom: 20px;
  left: 60px;
  right: 60px;
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

.text-center {
  text-align: center;
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

### 5. Post-verification
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

<!--[> _class: story <]-->
<!--## The tipline situation in 2013-->

<!--(maybe skip this)-->

<!--<div class="excerpt">-->

<!--From: **Laura Poitras**-->
<!--To: Micah Lee-->
<!--Date: Thu, 9 May 2013-->

<!--I’m working on something with **Glenn** and I really need to get him on a secure (preferably **Tails**) system. He does not have the technical skills to set this up himself, and I’m trying to keep things compartmentalized, so I don’t want to email him about this topic directly on a non-secure channel.-->

<!--</div>-->

<!------->

<!-- _class: lead -->
![bg opacity blur](https://www.franceinfo.fr/pictures/4DVmuRcH08VuGZhDpYOeWUNrbCw/0x0:1920x1080/1024x576/filters:format(avif):quality(50)/2016/08/23/citizen1.jpg)

Would you go through those hoops?

---

<!-- _class: lead -->
![bg brightness:0.95](https://www.franceinfo.fr/pictures/4DVmuRcH08VuGZhDpYOeWUNrbCw/0x0:1920x1080/1024x576/filters:format(avif):quality(50)/2016/08/23/citizen1.jpg)

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

## GrapheneOS + Signal = ❤️
*Hardening the mobile tipline*

---

## What Signal knows about you

- **Phone number:** Used to fight spam, switch devices, contact discovery
- **IP address:** The IP address of your device
- **Ephemeral keys:** Identifiers of your device and the devices you send messages to
- **Registration PIN:** If you have enabled registration lock

If Signal (or AWS) was malicious, it would theoretically track who's talking
with who, based on IPs and ephemeral keys.

---

## Quick Signal wins

| Setting | Why it matters |
|---------|----------------|
| **Sealed sender** | Harder for Signal/AWS to track who talks with whom |
| **Disable link previews** | Previews = IP leak to the server behind the link |
| **Registration lock** | Blocks SIM-swap hijacking |
| **No notification content (iOS-only)** | Do not store incoming messages to device |

---

## Registration lock

- Signal numbers can switch to a different device (think lost/broken phones).
- Sole requirement is to have ownership of phone number (but law enforcement also can).
- Registration lock means that you can't do it, unless you remember a PIN.
- Prevents recent phishing attacks against journalists:


<div class="citation">

Source: [Netzpolitik — Phishing](https://netzpolitik.org/2026/phishing-attack-numerous-journalists-targeted-in-attack-via-signal-messenger/)

</div>

---


## iOS notifications

- iOS stores all your notifications locally, with no way to disable it.
- FBI used this avenue to partially restore Signal messages (even deleted ones).

<div class="citation">

Source: [Forbes — FBI](https://netzpolitik.org/2026/phishing-attack-numerous-journalists-targeted-in-attack-via-signal-messenger/)

</div>

---

## FBI doesn't always win


<div class="excerpt">

(something about not getting round the phone)

</div>


<div class="citation">

Source: [404 Media— Lockdown]()

</div>

---

## How Cellebrite works

(image of Cellebrite device on the right)

Important terms:
- **BFU:** "Before First unlock", i.e., device powered off or just booted
- **AFU:** "After First unlock", i.e., device has been unlocked at least once
- **TPM:** "Trusted Platform Module", an onboard-chip that prevents PIN guessing
  - Available on iOS and certain Android devices.

(show image of TPM)

---

(full picture of device that Cellebrite can unlock)

---

## Quick phone wins

| Setting | Why it matters |
|---------|----------------|
| **Lockdown mode (iOS)** | Protection against device seizures/spyware |
| **Advanced Protection (Android)** | Protection against device seizures/spyware |
| **No SIM card (newsroom devices)** | lots of 0-days target SMS/MMS |

---

## GrapheneOS

| Setting | Why it matters |
|---------|----------------|
| **Auto-reboot** | Brings device to BFU if not unlocked for `N` hours |
| **Disable USB port on lock screen** | Prevents software bugs |
| **No/sandboxed Google Play** | Makes Google integration smaller |
| **User profiles** | Compartmentalization as a defense |
| **Hardware attestation** | Protection against evil-maid attacks |
| **Duress password** | Wipe device in case of physical intimidation |

---

## Live demo: GrapheneOS + Signal

- Simple installation
- User profiles (personal, tips, vaults)
- Receiving a tip via Signal
- Device VPN (Orbot)
- Secure PDF viewer / browser

---

# Part III

## Perimeter security
*Walls have ears, we have gears.*

---

# Part IV

## QubesOS + SecureDrop = ❤️
*Compartmentalization as a defense.*

---

## Remember that WaPo reporter?

- Mention that Macbook of WaPo reporter was compromised.
- Signal can be subpoenaed to reveal phone numbers
- Opening files with attachments can be very dangerous.

---

## Fake whistleblowers

(mention ICIJ story)

---

## SecureDrop overview - Sources

- Sources visit Tor site, receive a long codename
- Sources can send messages, attachments
- Sources can learn about replies only if they visit again

(add picture of Tor landing page)

---

## SecureDrop overview - Journalists


- Journalists have two laptops and four USB keys.
- Download submissions over Tor from one laptop.
- Decrypt submissions in other offline laptop.
- Reply back to the user from original laptop.

(add picture of two laptop airgap)

---

## SecureDrop woes

- Upfront money investment (NUCs, laptops, router, USBs, IT person, physical space)
  - The newsroom is getting more virtual by the day.
- Journalist time investment: lots of passwords and keys to juggle, lots of
  spam, infrequent communication
- Freedom of the Press Foundation is working hard on fixing these problems:
  - Ditch NUCs in favor of end-to-end encrypted protocol with centralized server.
  - Ditch multiple laptops and Tails keys in favor of a single laptop.

---

## Qubes OS

- Linux
- Targeted at technical users
- Everything is a VM
- Compartmentat


---

## Live Demo: QubesOS + SecureDrop

- Compartmentalization
- Safe file viewing and printing
- Search messages, export transcripts

---

<!-- _class: section-bg -->
![bg brightness:0.5](images/handle_with_care1.jpg)

# Part V

## Post-verification
*Store it, share it, publish it, without burning your source.*

---

<!-- _class: story -->

![bg right:25%](images/its_happening2.png)

## Post-verification

You have verified in a secure fashion that the material is important.

Possible scenarios:
- **Store it**
- **Share it privately**
- **Go public**

---

<!-- _class: story -->

## Store it offline

<div class="columns">
<div>

Use [Veracrypt](https://veracrypt.io) on any USB drive!

- Available on Windows/macOS
- Third-party support on Android/iOS
- Open-source
- Offers plausible deniability

</div>
<div>

![fg height:200px](https://www.premiumusb.com/content/images/sitepremium/customer-help/resource-center/flash-drive.jpg)

</div>
</div>

---

<!-- _class: story -->

## Plausible deniability

<div class="columns">
<div>

A Veracrypt drive can consist of two volumes:
- **Outer volume:** Place decoy files in there (tax / health records, previous
  investigations).
- **Inner (hidden) volume:** Place sensitive files in there.

In duress, offer the password of the **outer volume**.

</div>
<div>

![fg](https://veracrypt.io/en/Beginner's%20Tutorial_Image_024.gif)

</div>
</div>

---

<!-- _class: story -->

## Making it tamper-evident

<div class="columns">
<div>

In cases of:
- Shipping USB drive to someone
- Crossing borders
- Long-term storage

<div class="citation">

Source: [dys2p.com — Random Mosaic – Detecting unauthorized physical access with beans, lentils and colored rice](https://dys2p.com/en/2021-12-tamper-evident-protection.html#manipulation-auf-dem-versandweg)

</div>

</div>
<div>

![fg](https://dys2p.com/assets/images/tamper-evident-protection/nsa-pwn-cisco.jpg)

</div>
</div>

---

<!-- _class: section-bg -->
![bg brightness:0.1](https://theintercept.com/wp-content/uploads/2014/10/fedex_redacted3.png?w=1024)

#### Here's Micah's "flash drive gift" to Glenn Greenwald.

<div class="citation">

Source: [The Intercept —  Ed Snowden Taught Me To Smuggle Secrets Past Incredible Danger. Now I Teach You. ](https://theintercept.com/2014/10/28/smuggling-snowden-secrets/)

</div>

---

<!-- _class: section-bg -->
![bg](https://theintercept.com/wp-content/uploads/2014/10/fedex_redacted3.png?w=1024)

---

## Making it tamper-evident (the boring way)

<div class="columns">
<div>

One way is to buy tamper evident bags...

</div>
<div>

![fg](https://hsasecurity.net/wp-content/uploads/2020/11/HSA-Security-TAMPER-EVIDENT-BAG-WITH-VOIDOPEN-Message-2.jpg)

</div>
</div>

---

<!-- _class: story -->

![bg right:40%](images/tamper_fail.png)

... but if your threat model is law enforcement, assume that they have ways around it.

<small>

_(here, it's just a syringe with acetone)_

</small>

<div class="citation">

Source: [DEF CON 30 - Tamper Evident Village ](https://www.youtube.com/watch?v=slhdowWjSuU)

</div>

---

<!-- _class: story -->

## Making it tamper-evident (the fun way)

<div class="columns">
<div>

1. Grab a bean mix
2. Wrap the USB drive with plastic wrap
3. Put the beans and the USB drive in a vacuum bag
3. Seal it with a vacuum sealer
4. Take a picture of it from both sides
5. Verify the mosaic with [BlinkComparison](https://play.google.com/store/apps/details?id=org.proninyaroslav.blink_comparison) (Android-only)

<div class="citation">

Source: [dys2p.com — Random Mosaic – Detecting unauthorized physical access with beans, lentils and colored rice](https://dys2p.com/en/2021-12-tamper-evident-protection.html#manipulation-auf-dem-versandweg)

</div>


</div>
<div>

![fg](https://dys2p.com/assets/images/tamper-evident-protection/blink.webp)

<small>

_Showcase of how blink comparison works_

</small>

</div>
</div>

---

![bg right:50%](https://pmecdn.protonweb.com/image-transformation/?s=a&image=Keep_your_files_safe_and_private_1d23c0a646.png&width=1920&height=1014)

## Store it online

- [Proton Drive](https://proton.me/drive) offers end-to-end encryption.
- For the paranoid, you can even create an anonymous account using Tor.

---

## Going public

The material may have de-anonymization vectors that point back to the source.

Let's see some prominent examples.

---

<!-- _class: story -->
## Exhibit A - Simple metadata (multimedia)

<div class="columns">
<div>

![fg](images/exhibit_a.png)

</div>
<div>

![fg](images/exhibit_a_headline.png)

</div>
</div>

<div class="text-center">

⚠Photos may contain location and author info

</div>

<div class="citation">

Source: [Wired — Oops! Did Vice Just Give Away John McAfee's Location With Photo Metadata?](https://www.wired.com/2012/12/oops-did-vice-just-give-away-john-mcafees-location-with-this-photo/)

</div>

---

<!-- _class: story -->
## Exhibit B - Complex metadata (PDF, MS Office)

<div class="columns">
<div>

![fg](images/exhibit_b.png)

</div>
<div>

![fg](images/exhibit_b_headline.png)

</div>
</div>

<div class="text-center">

⚠ PDFs and office documents may contain nested metadata.
Think embedded photos, Word’s tracking changes feature.

</div>

<div class="citation">

Source: [The Register — Metadata ruins Google's anonymous eBay Australia protest](https://www.theregister.com/on-prem/2008/05/30/metadata-ruins-googles-anonymous-ebay-australia-protest/1285606)

</div>

---

<!-- _class: story -->
## Exhibit C - Redactions

<div class="columns">
<div>

![fg](images/exhibit_c.png)

</div>
<div>

![fg](images/exhibit_c_headline.png)

</div>
</div>

<div class="text-center">

⚠ Redactions do not work if in a layer or not opaque

</div>

<div class="citation">

Source: [The Verge — Sony’s confidential PlayStation secrets just spilled because of a Sharpie](https://www.theverge.com/2023/6/28/23777298/sony-ftc-microsoft-confidential-documents-marker-pen-scanner-oops)

</div>

---

<!-- _class: story -->
## Exhibit D - Physical watermarks

<div class="columns">
<div>

![fg](images/exhibit_d.png)

</div>
<div>

![fg](images/exhibit_d_headline.png)

</div>
</div>

<div class="text-center">

⚠ Printed documents may contain tracking dots

</div>

<div class="citation">

Source: [The Atlantic — The Mysterious Printer Code That Could Have Led the FBI to Reality Winner](https://www.theatlantic.com/technology/archive/2017/06/the-mysterious-printer-code-that-could-have-led-the-fbi-to-reality-winner/529350/)

</div>

---

<!-- _class: story -->
## Exhibit E - Digital watermarks

<div class="columns">
<div>

![fg height:370px](images/exhibit_e.png)

</div>
<div>

![fg](images/exhibit_e_headline.png)

</div>
</div>

<div class="text-center">

⚠ Digital material accessible only to you may have invisible watermarks

</div>

<div class="citation">

Source: [The Intercept — How Elon Musk Says He Catches Leakers at His Companies](https://theintercept.com/2022/12/15/elon-musk-leaks-twitter/)

</div>

---

<!-- _class: story -->
## Exhibit F - Canary tokens

<div class="columns">
<div>

![fg](images/exhibit_f.png)

</div>
<div>

- Most sane document viewers block them silently.
- Microsoft Office asks to enable macros.
- Adobe Acrobat asks if it's ok to connect to site.
- Deanonymization is a click away.

</div>
</div>

<div class="text-center">

⚠ Trapped documents may phone home in major viewers

</div>

<div class="citation">

Source: [Austin Martin — Canary Tokens](https://blog.amartinsec.com/blog/canary/)

</div>

---

<!-- _class: story -->
## Exhibit G - Fingerprinting

<div class="columns">
<div>

![fg](images/exhibit_g.png)

</div>
<div>

- Cameras, mics are subject to fingerprinting
- Your way of writing is a fingerprint (stylometry)
- Unlike watermarking, fingerprinting is useful only with a second match (much like human fingerprints)

</div>
</div>

<div class="text-center">

⚠ A/V equipment and writing style can be fingerprinted

</div>

<div class="citation">

Source: [Digital Image Forensics: Camera Fingerprint and its Robustness](https://www.slideshare.net/slideshow/digital-image-forensics-camera-fingerprint-and-its-robustness/15069696)

</div>

---

<!-- _class: story -->
## Exhibit H - Environment

<div class="columns">
<div>

![fg](images/exhibit_h.png)

</div>
<div>

![fg](images/exhibit_h_headline.png)

</div>
</div>

<div class="text-center">

⚠ Cameras, microphones capture the surrounding environment

</div>

<div class="citation">

Source: [Koreaboo — Japanese “Sasaeng” Tracked down a Female Idol’s Home by Zooming in on the Reflection in Her Eyes](https://www.koreaboo.com/stories/matsuoka-ena-sasaeng-obsessed-fan-idol-stalker-photo-eyes-reflection/)

</div>

---

## Going public

Practical advice:
- Ensure that the source used **disposable equipment** not tied to them.
- Ensure that the documents were **not directed** to the source.
- Sanitize documents before publication:
  - [Dangerzone](https://dangerzone.rocks/) (GUI)
  - [MAT2](https://github.com/jvoisin/mat2) (CLI-only)

---

<!-- _class: story -->
![bg right:30%](https://oxfordwaveresearch.com/wp-content/uploads/2017/09/Spectrogram12.9-768x1024.png)

## OPSEC works!

[KRIK](https://www.krik.rs) protected their source by not providing the prosecutors office with the original recording of an incriminating discussion.

<div class="excerpt">

In its latest letter to KRIK, the prosecutor’s office claims the recording is needed for forensic examination and insists it is not asking the newsroom to reveal its source, only to **provide the recording itself — either the original, its “closest copy,” or the device on which it was recorded.** The letter again threatens journalists with a **fine if they fail to comply**.

</div>

<div class="citation">

Source: [OCCRP —  Serbian Prosecutors Threaten KRIK with Fine if it Fails to Submit Recording of a Conversation ]()

</div>

---

<!-- _class: story -->
![bg right:30%](images/document_forensics.jpg)

## OPSEC works!

[Radio New Zealand](https://www.rnz.co.nz) protected their source by not disclosing the document format that the source provided to them.

<div class="excerpt">

[...] the investigator interviewed more than **40 people** including those who accessed the Budget report **"via SharePoint"**, received a copy of the report as an **email attachment**, or **had printed it**. [...] It was unclear which version the reporter had seen.

The Investigator asked to speak to the RNZ reporter [...] to discuss matters such as **the file format and version of the Budget Report disclosed to him**. The reporter and Radio New Zealand via its legal representation declined to do so.

</div>

<div class="citation">

Source: [Radio New Zealand — Ministry of Education's $20,000 inquiry fails to find Budget leak to RNZ](https://www.rnz.co.nz/news/national/574602/ministry-of-education-s-20-000-inquiry-fails-to-find-budget-leak-to-rnz)

</div>

---

**Thank you**

Questions? OPSEC war stories?
