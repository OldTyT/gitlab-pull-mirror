# gitlab-pull-mirror

Docker container designed to create a pipeline that automatically pulls mirror repositories into projects for GitLab CE.

## How to use

1. In the mirror group, create a new project and specify the source git repository's URL in its description.
2. ...
3. Enjoy the benefits!

## Prepare

1. Create group in gitlab for mirrored repos.
2. Create a repository with a pipeline:
```yaml
#.gitlab-ci.yml
---
stages:
  - mirror

mirror_repositories:
  stage: mirror
  image:
    name: ghcr.io/oldtyt/gitlab-pull-mirror
    entrypoint: [""]
  variables:
    GITLAB_API_URL: "https://gitlab.com/"
    GIT_STRATEGY: none
    GITLAB_GROUP: MY_MIRRORED_GITLAB_GROUP
  script:
    - /app/entrypoint.sh
```
3. Generate a CI/CD variable named `GITLAB_API_TOKEN `by visiting [this page](https://gitlab.com/-/user_settings/personal_access_tokens).
4. Set up a pipeline schedule by navigating to: CI/CD -> Pipeline schedules -> New schedule.
5. Optional: Add your `SSH_KEY_PRIVATE` as a CI/CD variable.
