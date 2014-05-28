StateGov
========
This is still a development version. The production version can be found at http://maythirtysecond.com/billcount/legi/

<h2>Behind the Scense:</h2>

The BaseCommand file <a href="https://github.com/drewablo/StateGov/blob/master/legi/management/commands/ilgaLegislation.py">(ilgaLegislation.py)</a> is doing the lion's share of the work. It, in combination with a cron job, is going through www.ilga.gov every 5 minutes and either a) creating a new record in the database when a new bill is introduced b) updating a record when it's last action is different that what exists in the database for a specific bill c) doing nothing because there has been no changes since the last time the application ran. 

<h2>Front end:</h2>

The simple stuff. Through the legi app, project is requesting bills who's last action date is the current date, the bills whose last action was "Passed Both Houses", bills whose last action was "Sent to the Governor" and bills that are in the House Rules committee, and Senate Assignments committee, collectively "Legislative Purgatory".

I'm sure this isn't best practices, but much of the resources for the html template are refrenced from outside the project (they already exist for the other page on maythirtysecond.com)
