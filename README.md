# ARTI_1
Actionable Real Time Intelligence-- Medical Outcomes System

## Purpose:
With the great majority of my 40-some years of professional experience having been devoted to developing software systems to collect and manage Patient Medical Outcomes data, I have decided to try to distill this experience into a program that leverages cutting edge contemporary software tools to generate real-time actionable information from Patient Self-Reported Outcomes Measures (PROMS).
The program will follow a mobile-first strategy for collecting outcomes information, with an eye toward leveraging future developments in wearable technology.

### Noted:
- While this flows naturally from my long experience in developing outcomes collection systems, this is a ground-up development effort, not a reworking of any existing system.
- It will utilize state-of-the-art stable infrastructure including:
  - Python
  - Django
  - PostgreSQL
  - NGINX
  - R (Posit)
  - Plumber API
- And utilize software tools, patterns and practices that will:
  - facilitate clear and rapid understanding of the code base by external resources
  - future proof the code base to the extent possible.
- A Test-Driven Development model will be followed, with the goal of provably correct code, and 100% test coverage

### Data Security and Quality
- Since it anticipated that this program will be handling Protected Health Information under the HIPPA definition, verifiable security and protected confidentiallity of all data collected will be a ground rule.
- It is expected that this program will live or die based upon the  quality of the data collected, hence best-of-class data quality standards will be followed and data quality certifications will be sought.


#### development notes
Notes on NGINX installed using brew

Docroot is: /opt/homebrew/var/www

The default port has been set in /opt/homebrew/etc/nginx/nginx.conf to 8080 so that
nginx can run without sudo.

nginx will load all files in /opt/homebrew/etc/nginx/servers/.

To start nginx now and restart at login:
  brew services start nginx
Or, if you don't want/need a background service you can just run:
  /opt/homebrew/opt/nginx/bin/nginx -g daemon\ off\;
