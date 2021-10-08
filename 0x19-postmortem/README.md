# 0x19. Postmortem
![alt text](https://arevtech.com/wp-content/uploads/2016/11/dreamstime_l_27442026-Server-Problem.jpg)
The following notice is to report the incident presented on October 4, 2021 at 10:25 in the morning. Where the great impact on each of our staff and users is evidenced.
As a consequence, there is a great loss since the activities on our page are completely stopped, as a first step it was taken to review the generated status code, which is 500 corresponding to Internal Server Error. Where we go in to talk with the development team to validate what happened.
## The following events took place October 4, 2021:
- 10:35 a.m: Restart servers and validate status code again.
- 10:45 a.m: Review all lastest changes on a production branch.
- 10:55 a.m: Asign to developer corresponding of that issue.
- 1:20 p.m: The developer pushed their changes
- 1:30 p.m: Validate their changes with tester team.
- 2:00 p.m: The changes are approved with tester team
- 2:10 p.m: The changes are merged with a production branch.
- 2:25 p.m: Restart the service and show a correct status code.

## Aparent reason
An incompatibility of versions with respect to the production environment, not presented in the tests previously carried out, which causes a failure in each request.

## Resolution and recovery
The developer had to adapt some imports to the version present in the production environment in such a way that they could be tested in the QA environment.

## Corrective and preventive measures
To avoid future similar cases, we are talking with the infrastructure area, with the aim of adjusting a day where the necessary components are updated and thus avoiding any incompatibility, which will previously notify the public of this adjustment in the service to the destined date.

## Author
Cristian Pinzon: Cohort 14 - Bogotá.
