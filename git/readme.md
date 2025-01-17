```
Git Template
Author: Brendan O'Connor 
Date: January 2025

The purpose of this program is to provide enough of a starting point 
to write bash (sh) scrtipts without needing to do too much research
on syntax.
``` 

# Getting Started
- Download and install Git 
- Run `git config user.name = "Firstname Lastname"`
- Run `git config user.email = "email@provider.com"`
- Run `git config init.defaultbranch = main`

# Remove a Commit Locally
Use this if one of your commits failed and you need to remove it. This command will "undo" the last commit. Run as many times as needed to get back to a good state. 
`git reset --soft HEAD~`

# Pull from a specific branch
A "pull" means to synch your local copy with the known good state on GitHub. 
`git pull origin branchname`

# Push to a specific branch
A "push" means to synch changes from your local copy to an outdated state on GitHub.
`git push origin branchname`