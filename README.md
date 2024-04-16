# gitlab-pull-mirror

Docker container for automaticly pull mirror repos in projects for GitLab CE.

## How to use

1. Create a new project in the mirror group and specify the source git repository in the description.
2. ....
3. Profit!

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
3. Create CI/CD Variable `GITLAB_API_TOKEN` in [this page](https://gitlab.com/-/user_settings/personal_access_tokens)
4. Create schedule for pipeline: `Build` -> `Pipeline schedules` -> `New schedule`
5. Optional: Setup `SSH_KEY_PRIVATE` in CI/CD Variable
