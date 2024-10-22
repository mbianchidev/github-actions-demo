# github-actions-demo
GitHub actions demo!

For a guided experience you can just navigate to [this page](https://github.com/mbianchidev/github-actions-demo/actions/new) - also reachable from the actions tab when you don't have any wofklows set.

In our case, for educational purpose we are going for a good old fashioned fully manual setup!

Click on "Add file", then "create new file" and type `.github/workflows/demo-pipeline.yml`.

In the file, copy paste the following workflow:

```
name: Demo pipeline

on:
  push:
    branches: [ "main" ]
  pull_request:
    branches: [ "main" ]

jobs:
  demo-job:
    runs-on: ubuntu-latest
    steps:
    - name: Check Nodejs and NPM version
      run: |
        node --version 
        npm --version
```

Now you can check the actions tab and see if the piepline works!

The possibilities are infinite, check out [the reference docs](https://docs.github.com/en/actions/writing-workflows/workflow-syntax-for-github-actions#jobsjob_idneeds) for a complete overview of the workflows syntax.

Let's see something slightly more complex in this open source repo: [Example #2](https://github.com/mbianchidev/klab-cli/pull/232)
