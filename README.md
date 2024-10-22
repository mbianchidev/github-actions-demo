# github-actions-demo
GitHub actions demo!

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

Now let's see something slightly more complex: [Example #2](https://github.com/mbianchidev/klab-cli/pull/232)
