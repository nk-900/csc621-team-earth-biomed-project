# csc621-team-earth-biomed-project
A biomedical imaging analysis software developed by a team of 3 university students.


## Development Guidelines for team members
```md
1. Never commit directly to `main`.
2. Never force-push to `main`.
3. Pull/fetch before starting new work.
4. Sync with `main` again before opening a PR.
5. Keep branches focused on one task.
6. Do not commit `.venv`, CT datasets, generated results, or IDE cache files.
7. Test before requesting a merge.
8. At least one teammate reviews each PR.
9. Delete merged branches.
10. Use Git tags only for stable milestones.
```
### Detailed instructions for working with Git are below.
#### 1. Update local `main`
```bash
git checkout main
git fetch origin main
git pull origin main
```

#### 2. Create a new branch
`git checkout -b feature/your-feature-name`

Examples:
```
feature/segmentation
fix/fourier-transform-logic
docs/README-update
experiment/parameter-tuning
```

#### 3. Do your thing

Don't forget to use `git status` to enure you're working on the correct branch

#### 4. Pre-commit checks

```bash
git status
git diff
```

#### 5. Stage and commit

```bash
git add <the files you changed>
git commit -m "Tuned parameters for better segmentation"
git fetch origin
git merge origin/main
```
Fix any conflicts locally, test, and commit merge if needed.

#### 6. Pre-push test

```bash
python src/environment_test.py
python <any code related to your feature or fix>
```

#### 7. Push and Pull Request

The first time around for a branch, use
`git push -u origin <your-branch-name>`.

Then use `git push` for subsequent pushes.

When you make the Pull request, let the team know so one of us double check that everything is A-OK.

#### 8. Merging

If everything is good, merge branch into main. 
Then do
```bash
git checkout main
git pull origin main
git branch -d <merged-branch-name>
```

### Tags
Use tags only for milestones, like completing a major feature and adding a v0.x plus title or something. We can chat about this later.

```bash
git checkout main
git pull origin main

git tag -a v1.0 -m "CSC621 final project submission"
git push origin v1.0
```