We use Continuous Integration and Delivery/Deployment (CICD) for this project.

> Before using CICD for your project, there are some one-time setup steps for establishing CICD for your project via our Jenkins server.
> Those setup steps are outlined at the end of this document.

Simply complete the 'Deployment Checklist' to deploy your project to its Python Package Index.
The checklist, which includes the 'Deployment Workflow', 
It is really quite a simple workflow!

## Deployment Checklist

Before delivering a new version of this package, these are key steps.

- [ ] Update declared dependencies, if needed.
- [ ] Ensure all existing automated tests pass.
    - [ ] **BONUS POINTS**: Ensure code coverage of any new code.
        * E.g. `hatch run dev:coveragee` will produce "htmlcov/index.html" report.
- [ ] Ensure any production functionality has not regressed (best effort).
- [ ] Update the version, following [Semantic Versioning](http://semver.org).
    * E.g. `hatch version patch|minor|major`
- [ ] Update Release Notes, to include the new version.
- [ ] Update the User Guide with any relevant changes.
- [ ] Complete the [Deployment Workflow](#deployment-workflow)
- [ ] Once the package is in PyPI, ensure you can download and install the new package version successfully.

## Deployment Workflow

Our Continuous Integration and Delivery (CICD) are triggered by Pull Requests.
The workflow to trigger a new deployment is the very simple pull request workflow (annotated with CICD steps):

1. **`git push`** your new branch to the Source Control Management (SCM) server.
2. Log in to the SCM server and **create a pull request**.
    * CI runs at this point (running all automated tests).
3. Once Jenkins has completed its CI run, **merge** the pull request
    * CD runs at this point (deploying to the appropriate Python Package Index)

## Initial, One-Time Setup Steps

There are a few pieces that we need to establish the first time deploying this tool.
These include updating this project's Jenkinsfile and updating Bitbucket to trigger Jenkins webhooks.
In short, you will have to do the following, discussed in detail below:

1. Decide which Python Package index to use (via Jenkinsfile).
2. Set up the "Parameterized Build for Jenkins" plugin in your Bitbucket repo.

### Which Python Package Index?

> If using pypi.uoregon.edu, there are some [additional one-time setup instructions for your package (internal docs)](https://confluence.uoregon.edu/display/NTS/Deploy+to+pypi.uoregon.edu)

First, you must decide whether you will be publishing to pypi.org or our private pypi.uoregon.edu server.

1. Simply update the `packageIndex:` in [Jenkinsfile](../Jenkinsfile) to either of:
    * 'pypi.org' or, 
    * 'pypi.uoregon.edu'

### Establish Bitbucket Hook

Follow our [instructions to "Enable Default Settings for my repo" (internal docs)](https://confluence.uoregon.edu/pages/viewpage.action?pageId=458892621#NTSJenkinsBitbucketIntegration-EnableDefaultSettingsformyrepo)
