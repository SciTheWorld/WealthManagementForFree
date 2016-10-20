WealthManagementForFree
======

Roboadvisors aim at democratizing the access to advanced advisory services of wealth management. We think that if it is not open sourced it is not democratic enough hence... here we go (!). If you want to learn about big data and finance and gain credibility in the FinTech space, just join us.

You need to download all Docker containers

[OPEN SOURCE DISCLAIMER] This product is intended to be free for independent individuals. Cannot be used for commercial purposes.

[FINANCIAL DISCLAIMER] This product is open source. SciTheWorld nor any of the contributors are responsible for its well functioning, the signals and messages conveyed through it nor any loss derived from its advices, whether its usage is direct or indirect. We are simply democratizing what we would use for ourselves (whether that is right or wrong).


Folders
======
**RA**  main app directory
>** Settings.py ** App Configuration
>**urls.py**  Main urls

**Dashboard** django app when you are logged
**static** Static files
**templates** Templates of all applications
**web** Landing page for users without login
**ngRobo** Dashboard for logged users



Docker
======

>**Stop:** docker-compose down
>**Build:** docker-compose build
>**Start:** docker-compose up -d
>**State:** docker-compose ps


Run app
http://0.0.0.0:50002
User: admin/adminadmin
