<p align="center">
    <img alt="Watcher Logo" src="/Watcher/static/watcher-logo-readme.png" height="250" width="250">
</p>

===

[![Documentation](/Watcher/static/documentation-Yes-brightgreen.svg)](https://felix83000.github.io/Watcher/)
[![LICENSE](https://img.shields.io/github/license/Felix83000/Watcher?logo=github&style=flat-square)](/LICENSE)
[![Docker Build Status](https://img.shields.io/docker/build/felix83000/watcher?logo=docker&style=flat-square)](https://hub.docker.com/repository/docker/felix83000/watcher)

Watcher is a Django & React JS automated platform for discovering new potentially cybersecurity threats targeting your organisation. 

It should be used on webservers and available on Docker.

## Watcher capabilities

- Detect emerging vulnerability, malware using social network & other RSS sources (www.cert.ssi.gouv.fr, cert.europa.eu, www.us-cert.gov, www.cyber.gov.au...). 
- Detect Keywords in pastebin & other it exchange websites (stackoverflow, github, gitlab, bitbucket, apkmirror, npm...).
- Monitor malicious domain names (IP, mail/MX record, html content using [TLSH](https://github.com/trendmicro/tlsh)).
- Detect potentially malicious domain names targeting your organisation, using [dnstwist](https://github.com/elceef/dnstwist). 

Useful as a bundle regrouping threat hunting/intelligence automated features.

## Additional features

- Integrated IOCs export to [TheHive](https://thehive-project.org/) and [MISP](https://www.misp-project.org/).
- LDAP & Local Authentication.
- Email notifications.
- Ticketing system feeding.
- Admin interface.
- Advance users permissions & groups.

## Involved dependencies

- [RSS-Bridge](https://github.com/RSS-Bridge/rss-bridge)
- [dnstwist](https://github.com/elceef/dnstwist)
- [Searx](https://searx.github.io/searx/)
- [pymisp](https://github.com/MISP/PyMISP)
- [thehive4py](https://github.com/TheHive-Project/TheHive4py)
- [TLSH](https://github.com/trendmicro/tlsh)
- [shadow-useragent](https://github.com/lobstrio/shadow-useragent)
- [NLTK](https://www.nltk.org/)

## Screenshots
Watcher provides a powerful user interface for data visualization and analysis. This interface can also be used to manage Watcher usage and to monitor its status.

**Threats detection**

<p align="center">
    <img alt="Watcher Logo" src="/Watcher/static/Watcher-threats-detection.png">
</p>

**Keywords detection**

**Malicious domain names monitoring**

<p align="center">
    <img alt="Watcher Logo" src="/Watcher/static/Watcher-malicious-domain-names-monitoring.png">
</p>

**Potentially malicious domain names detection**

Django provides a ready-to-use user interface for administrative activities. We all know how an admin interface is important for a web project: Users management, user group management, Watcher configuration, usage logs...  

**Admin interface**

<p align="center">
    <img alt="Watcher Logo" src="/Watcher/static/Watcher-admin-interface.png">
</p>

## Installation

Create a new Watcher instance in ten minutes using Docker (see [Installation Guide](https://felix83000.github.io/Watcher/README.html))

## Pastebin compliant
In order to use Watcher pastebin API feature, you need to subscribe to a pastebin pro account and whitelist Watcher public IP (see https://pastebin.com/doc_scraping_api).


---
Thanks to [**ISEN-Toulon Engineering School**](https://www.isen-mediterranee.fr/) and to [**Thales Group**](https://www.thalesgroup.com/) CERT (THA-CERT) for allowing me to carry out this project.