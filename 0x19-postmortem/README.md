-- Postmortem example --

![alt text](https://github.com/MohamedAdel89/alx-system_engineering-devops/blob/master/0x19-postmortem/postmortem.jpg)

## Date

Nov 11th, 2023

## Authors

* Mohamed Elsayed

## Status

Complete

## Summary

The event started at 16:51 UTC and ends at 18:30 UTC afecting 100% of the service.

## Impact

Estimated 1500 queries lost, no revenue impact.

## Root Causes

The load balancer went down due to a combination of exceptionally high load and a fan failure which end up overheating the server.

![alt text](https://github.com/MohamedAdel89/alx-system_engineering-devops/blob/master/0x19-postmortem/meme-it-is-fine.jpg)

## Trigger

A sudden increase in traffic when a user promotes the website on Reddit.

## Resolution

At the begging, the load balancer was eliminated from the architecture and it was necessary to set up a pass-through configuration, where the requests were served directly by the web-servers. After that, a new balancer was set up and put in the system.

## Detection

The monitor system installed on the servers sent an email.

## Corrective and preventative measures
Lessons Learned

 	Single points of failure are the biggest risk

* Monitoring quickly alerted us to a high rate (reaching ~100%) of HTTP 500s
* Rapidly was set up a temporary configuration
