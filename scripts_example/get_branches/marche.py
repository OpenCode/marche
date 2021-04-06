# Copyright 2021 Francesco Apruzzese <cescoap@gmail.com>
# License GPL-3.0 or later (http://www.gnu.org/licenses/gpl-3.0.html).


def marche(repo, *args, **kwargs):
    repo.log_info(f'Repo: {repo.name}')
    branches = list(repo.repo.get_branches())
    repo.log_info(f'    Branches')
    branches_name = [b.name for b in branches]
    for branch_name in branches_name:
        repo.log_info(f'    - {branch_name}')
