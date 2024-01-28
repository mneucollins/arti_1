# ARTI_1
Actionable Real Time Intelligence-- Medical Outcomes System

## Purpose:
With the great majority of my 40-some years of professional experience having been devoted to developing software systems to collect and manage Patient Medical Outcomes data, I have decided to try to distill this experience into a program that leverages cutting edge contemporary software tools to generate real-time actionable information from Patient Self-Reported Outcomes Measures.

### Noted:
- This is a ground-up development effort, not a reworking of an existing system.
- It will leverage a state-of-the-art stable infrastructure including:
  - Python
  - Django
  - PostgreSQL
  - NGINX
  - R (Posit)
  - Plumber API
- And utilize software tools, patterns and practices that will facilitate clear and rapid understanding of the code base by external sources
- A Test-Driven Development model will be followed, with the goal of 100% test coverage

### Security:
- Since this program will be handling Protected Health Information under the HIPPA definition, verifiable security and protected confidentiallity of all data collected will be a ground rule.


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
