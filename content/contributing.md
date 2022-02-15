---
title: Contributing
nav_order: 98
layout: default
---

# Contributing to ARENA

Thanks for your willingness to help improve our flexible, programmatic, mixed-reality platform! ARENA is a project led by <a href='https://wise.ece.cmu.edu/'>Carnegie Mellon University</a>, under the [CONIX Research Center](https://conix.io/), a collaboration between six US-based universities. This guide will help you find the right path to contribute. Feel free to join the [ARENA CONIX slack](https://join.slack.com/t/arena-conix/shared_invite/zt-oq8fmgdc-QWZ414mJdfOaWfb_p2lPRg) and ask us questions.

## The Team

ARENA development is lead by a team from <a href='https://wise.ece.cmu.edu/'>Carnegie Mellon University</a>. Our team is composed of faculty, staff and several students and in continuously being strenghtned. See our [GitHub](https://github.com/conix-center/) for the list of contributors in each [repository](/content/source).

## Research Platform

The ARENA may be deployed by you or us in many different locations. We maintain a production ARENA Server instance at [arenaxr.org](https://arenaxr.org).

## Proposing New Features

If you want to work on something that there is no GitHub issue for, it's best to document your plan before working on a Pull Request. To do so, follow these steps:

1\. Create a new GitHub issue associated with the relevant repository and propose your change there with:

- Why is the change needed?
- How will it be implemented?

2\. An ARENA team member will respond and let you know if the Issue is acceptable to work on or if some implementation modification is needed.

3\. If you have questions or are not sure about the feature, please do ask us questions in our [ARENA CONIX slack](https://join.slack.com/t/arena-conix/shared_invite/zt-oq8fmgdc-QWZ414mJdfOaWfb_p2lPRg) Slack #questions channel.

## Issue Reporting

- There are 2 basic things that will help us greatly for any issue you report:

  - Is it reproducible and what are the steps to reproduce the problem?
  - Where was the issue? Which hostname and the version in use?

- Deployed web server issues please include version here from the commit history at <https://github.com/conix-center/arena-services-docker>

- Python client issues please include the version here from `pip show arena-py`.

## Pull Requests and Code Review

Some changes will require internal discussion to see if the needs of the project are still being met which can change from time to time. A list of which repo to use are listed at the end of this guide.

- A great way to start is to try development of a scene using the [Python](/content/overview/dev-guide.html) and [scene builder](/content/overview/build.html) tutorials.
- Once familiar, good first issues to help with are labeled with `help wanted` and `good first issue`.

## Process for Pull Requests

1. Create your own fork of the appropriate repository and clone it and any submodules.
2. Create your own branch with the name of your change, and do not use master or main branches for your change.
3. Create a draft PR for your changes.
4. Push changes to your PR/branch often.
5. Submit your PR and request a code review from us.
6. After all rounds of review feedback are addressed we will manage merging the PR.

## Language Style Guides

We use a number of languages and technologies to run the ARENA. You may need to have at least a basic familiarity with JavaScript, Python, and CSS/HTML. As such, we have some guidance for maintaining some style standards in each repo.

<!-- (move to CONTRIBUTING.md in each repo with links to linter guides) -->

## Which Issue Tracker?

The ARENA is composed from a number of repositories. That can be confusing. We recommend searching for an existing issue from our list first and familiarizing yourself with this basic map:

- ARENA Client Website: [conix-center/ARENA-core/issues](https://github.com/conix-center/ARENA-core/issues)
- ARENA Python client: [conix-center/ARENA-py/issues](https://github.com/conix-center/ARENA-py/issues)
- ARENA Unity client: [conix-center/ARENA-unity/issues](https://github.com/conix-center/ARENA-unity/issues)
- ARENA Docs Website: [conix-center/ARENA/issues](https://github.com/conix-center/ARENA/issues)

Server components:

- ATLAS Server: [conix-center/ATLAS/issues](https://github.com/conix-center/ATLAS/issues)
- ARENA MQTT Broker: [conix-center/ARENA-broker/issues](https://github.com/conix-center/ARENA-broker/issues)
- ARENA Runtime Supervisor: [conix-center/arts/issues](https://github.com/conix-center/arts/issues)
- ARENA User Account DB: [conix-center/arena-account/issues](https://github.com/conix-center/arena-account/issues)
- ARENA User Scene Persistence DB: [conix-center/arena-persist/issues](https://github.com/conix-center/arena-persist/issues)
- ARENA User File Manager: [conix-center/arena-store/issues](https://github.com/conix-center/arena-store/issues)

## Code of Conduct

We adhere to the Contributor Covenant Code of Conduct: <https://www.contributor-covenant.org/version/2/0/code_of_conduct/code_of_conduct.md>
