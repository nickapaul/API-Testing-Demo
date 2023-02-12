# Python API Test Demo

## What Is This?
This is a demo of a typical API automation testing pipeline. I am using a test API to be the "app" we are testing, then I am using GitHub Actions to execute the pipeline in an automated fashion. This serves as a proof of concept for an automated test pipeline. To begin, however, we may need to get into a little test theory.

QA has a nebulous meaning and really is a much bigger topic than its given credit for. In my life, as a QA I started where most do manual testing and booking bugs. However, soon I realized that the amount of regression ran was taking longer and longer. Our 1 or 2 day test swarms were taking 2-3 or 4 days long and it really kept us from deploying more than 1 or twice a month. Big fat deploys are hard to plan for, let alone execute. So, a few of us started looking into automation. Having the ability to run 100s if not 1000s of tests in the time it would take to run a fraction of the manual tests really opened our eyes...push button, get results.

The next progression took me from a dev (in my head a dev is anybody who writes code) to more of a QaOps (SRE) role. Eliminating the manual touches while speeding up the feedback loop through automation was presented to me as the concept of shifting left, and that always resonated with me. 

Anyways that was all to say that this a proof of concept that with a little setup, a fleshed-out testing suite complete with configured testing pipeline is easy to set up and maintain.

## The Pipeline
The pipeline is designed to execute on merge request to master. I know that in this example I’m just running the test itself, so you would think I ran my test before I checked it in (looking at you "works on my machine" guys). Just imagine that in most build and deploy tools you can chain pipelines or call pipelines from other pipelines. So, if your tests are fast enough, you can gate merges from dev to QA with the regression tests.

This desgin goes as follows:
- Pull Source
- Set Up Python
- Install Dependencies
- Run Test
- Create HTML Report

This is all configured from the python-app.yml in the .github/workflows folder. Every check-in to master will kick off a build and keep the merge from happening if the build fails.

## Installation
1. Install Python (3.10.10)
2. In ther terminal, run: python3 --version and confirm python is installed
3. run: pip install -r requirements.txt
4. run: nose2