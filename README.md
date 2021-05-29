# color-change-webapp
A simple containerized Flask webapp which dynamically serves a webpage with a random colored background. The information displayed also includes the HOSTNAME or NAME variable.

The background may be set manually by passing the color as a parameter when creating the container, or by setting the APP_COLOR env variable. 

It may be one of 9 colors:
* gray
* red
* yellow
* green
* blue
* indigo
* purple
* pink

Technologies used:
* Docker
* Python
* Flask
* Jinja
* TailwindCSS
