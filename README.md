# Quick Start

To view the web site, visit [this page](http://veasy.org.test.arq.s3-website.eu-west-2.amazonaws.com/index.html).

Changes to the displayed text can be made by updating a database record, avoiding the need to redeploy the site.

# Architectural Overview

In summary, the application is deployed to **AWS** and uses the following services:

* DynamoDB - used to store the configurable text.
* Lambda - reads the text from the DynamoDB.
* AWS API Gateway - defines the configuration for the API 'message' endpoint, including the proxy lambda that actually returns the response - both content and HTTP headers.

For the frontend, (no surprises), the follow have been used:

* HTML / Javascript

In addition:

* GitHub Actions - release branches provide control over code/configurtion changes; the Actions automates deploying new releases to production from new release branches.
* CDK - has been chosen over Terraform as the IAC tool and integrated into the GitHub action as deployment steps.
* Slack - not specified as a requirement, however adding Slack notifications is so useful, not only for team awareness of deployments, but also or myself as a confirmation of deployment status.

# Architectual Choices

* AWS - I already have experience with AWS so this was a natural choice for the Cloud provider.
* DynamoDB - cheap, scalable and integrates well with the other AWS services.
* Lambda - implemented using Python for simplicity of this mini project.
* AWS API Gateway - for ease in exposing the lambda function via an HTTP endpoint, but also supports a multitude of features such as throttling, monitoring, lifecycle management.

# Future Improvements

In no particular order - would need to be prioritised in conjunction with business needs and future enhancements.

* Logging - some basic logging has been included but should be reviewed and possibly extended to ensure sufficient monitoring is available in production.
* Testing - currently the GitHub action assumes deployment directly from 'dev' to 'prod'.  Separate deployment configuration could be included for 'stage' to allow a more controlled testing environment before promoting to 'prod'.
* Scalability - unlikely to be an issue at present with such a trivial app, however, as the app becomes more complex, consider using a AWS Edge Locations / Cloundfront to minimise network latency on static content, configuring endpoint caching in AWS API Gateway, backend data layer caching.
* (done) API usage limiting - generally good practice to include some rate limiting on services that could potentially result in costs.  Better to set a very high limit that no limit whatsoever.
* API versioning - the endpoint should be versioned - I would favour versioning via the URL path, eg. /api/v1/message
* CSS - the &lt;h1&gt; tag should be moved to a separate styling CSS file.
* text updates - could be facilitated by extending the API endpoint to support the PUT HTTP method, to support a simple 'Content Management' application.  Naturally this would need to be secured, possibly by a simple login that generates a JWT token that could be included in API requests to update the text.
* (done) Deployment simplications - Avoid hardcoding the API URL in the javascript.