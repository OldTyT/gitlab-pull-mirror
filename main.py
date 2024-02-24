import gitlab
import git
import os

GITLAB_API_URL = os.getenv('GITLAB_API_URL')
GITLAB_API_TOKEN = os.getenv('GITLAB_API_TOKEN')
GITLAB_GROUP = os.getenv('GITLAB_GROUP')

if GITLAB_GROUP is None:
    print("env GITLAB_GROUP not set.")
    os._exit(1)

if GITLAB_API_URL is None:
    print("env GITLAB_API_URL not set.")
    os._exit(1)

if GITLAB_API_TOKEN is None:
    print("env GITLAB_API_TOKEN not set.")
    os._exit(1)

gl = gitlab.Gitlab(GITLAB_API_URL, private_token=GITLAB_API_TOKEN)

gl.groups.list(search=GITLAB_GROUP)

group = gl.groups.list(search=GITLAB_GROUP)[0]

for project in group.projects.list(all=True):
    if project.description is None:
        print(f"Skip project {project.name} from pull mirroring.")
        continue
    description = project.description
    if description.find(".git") != -1:
        try:
            repo = git.Repo.clone_from(description, 'tmp_repo', mirror=True)
            origin = repo.create_remote('gitlab', url=project.ssh_url_to_repo)
            repo.git.push('--mirror', 'gitlab')
            print(f"Repo {project.name} mirrored successfully!")
        except Exception as e:
            print(f"Failed to mirror {project.name}: {e}")
        finally:
            if os.path.isdir('tmp_repo'):
                git.Repo('tmp_repo').close()
                git.rmtree('tmp_repo')
