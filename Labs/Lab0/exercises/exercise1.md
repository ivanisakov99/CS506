# Workflow 1: Create and Update My Repo

#### This is your checklist:

- [ ] Create a repo on GitHub (GH)
- [ ] Clone a repo
- [ ] Look at remotes
- [ ] Create a branch
- [ ] Switch to another branch
- [ ] Push changes to GH from terminal
- [ ] Submit a pull request (PR) on GH
- [ ] Merge the pull request (PR) on GH
- [ ] Pull changes locally
- [ ] Recover a deleted file

---

## Step 1:  create a repo (on GitHub)

The following steps create a GitHub Repository.

- Click on `+` next to your profile picture
- Select `New Repository`
- Repository name:  `gitclass`
- Description (optional):  `test project for git`
- Repo type
	- `Public` repos:  everyone can view, good for sharing work   
	- `Private` repos:  [unlimited, no charge, with up to 3 collaborators](https://techcrunch.com/2019/01/07/github-free-users-now-get-unlimited-private-repositories/) )
- Check box for `Initialize this repository with a README`
- Select green button `Create repository`

## Step 2: `clone` the repo from GitHub to our terminal

### Copy URL for cloning

Click on the green button for your GitHub repo, and ensure it is showing the url for **"Clone with SSH"** - for this, you must have followed optional setup step 2). Please do that now if you have not already. Then copy that URL.
 
<img src="../images/github_clone_button.png" align="left" height="40" width="180" >   <br> <br>

## Step 3: go to working directory (your local terminal)

Go to your working directory  

```bash
cd ~/Desktop/my/favorite/path
```

## Step 4: clone the repo

<kbd> git clone <url_name> </kbd> 

With SSH, it should be:
```
git clone git@github.com:gallettilance/CS506-Spring2022.git
git@github.com:gallettilance/CS506-Spring2022.git
Cloning into 'CS506-Spring2022'...
remote: Enumerating objects: 93, done.
remote: Counting objects: 100% (93/93), done.
remote: Compressing objects: 100% (87/87), done.
remote: Total 93 (delta 8), reused 84 (delta 4), pack-reused 0
Receiving objects: 100% (93/93), 2.17 MiB | 6.12 MiB/s, done.
Resolving deltas: 100% (8/8), done.	
```
## Step 5:  `cd` into the repo

<kbd> cd <repo_name> </kbd>

```bash
cd CS506-Spring2022 
```

## Step 6: look at remotes

**Remotes** are copies of a repo on another computer **(or on a service like GitHub)**

```bash
git remote -v
origin	git@github.com:gallettilance/CS506-Spring2022.git (fetch)
origin	git@github.com:gallettilance/CS506-Spring2022.git (push)
```

## Step 7: create a branch

- Branching means you diverge from the main line of development and continue to do work without changing the main line, like "scratch paper" but for online coding.  
- Can work on different parts in the codebase, or "features" or "web page updates"
    - create a separate *history* for each new *feature*
- More details can be found here:  [branches](../git_6_branches.md)

To list all your branches:

```git
git branch
* main
```

To create a working branch

<kbd> git branch <branch_name> </kbd>

Verify the branch was created by listing the branches using the above command.

<kbd> git branch </kbd> 

Do not forget to switch to the new branch you just created.    

<kbd> git checkout <branch_name> </kbd>

## Step 8:  create a file

```bash
> touch my-new-file.md
> ls
  README.md
  my-new-file.md
```

## Step 9: add content to this file

Add some content to this file using your editor of choice.

## Step 10: registering your changes

### Git Flow 

| #     | Command                   | Step  | Description      |
|-------|---------------------------| -----|------------------|
|  1    | `git add <filename>`      | begin tracking a file | adds a change in the working directory to the staging area; tells Git that you want to include updates to a particular file in the next commit.  |    
|  2    | `git commit -m "message"` | log the change | changes are recorded in Git (interaction is with local repo) |  
|  3    | `git push`                | finalize the change | changes are pushed from Git (local, terminal) to GitHub (browser account, remote) | 
 
**Note:**  Good practice is to have 1 commit per feature/component.

<p>
<img src="../images/git_shopping_cart.jpg" width="99%" height="99%" />
</p>

### Step 10.1: get status of repo

<kbd> git status </kbd>

Let's you see what files git is aware of / tracking.
    
### Step 10.2:  add/stage a file

```bash
git add my-new-file.md 
```

**Note:**  to `add` a file is to begin tracking it:  
- adds a change in the working directory to the staging area
- tells Git that you want to include updates to a particular file in the next commit

### Step 10.3: get status of repo

<kbd> git status </kbd>

Ensure that the file is now tracked by git.

### Step 10.4: commit the file

<kbd> git commit -m 'message' </kbd>  

**Note:**  to `commit` a file is to "log the change":  
- changes are recorded in Git (interaction is with local repo)

### Step 10.5:  get status of repo

<kbd> git status </kbd>  

Ensure the file does not appear.

### Step 10.6: push changes

<kbd> git push origin \<my new branch\> </kbd>  

**Note:**  to `push` a changes is to push from Git (local, terminal) to GitHub (browser account, remote)

Due to the deprecation of password authentication on Github, you need to set up token to connect Github when using HTTPS protocol. Further guidance are available [here](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token). 
	
On the other hand, you can also use SSH protocol to connect without typing username and passcode anymore. 

## Step 11: look at files on working branch (on GitHub)

**Note:**  we are on GitHub in browser
- go to repo
- may want to toggle "Branch"
	
## Step 12: submit pull request (on GitHub)

Still on GitHub, select the green button "Compare and pull request"

<img src="../images/pull_request_button.png" align="left" height="40" width="180" >   <br> <br>

## Step 13: merge the pull request (on GitHub)

Select the green button "Merge pull request".

Notice that the changes from your branch are now in the `main` branch on GitHub. Notice that these changes are not on you local directory.

## Step 14: pull these changes locally

<kbd> git checkout main </kbd>  
<kbd> git pull origin main </kbd>

## Step 15: delete the file

```bash
rm my-new-file.md 
```

## Step 16: recover the file

<kbd> git status </kbd>  

Notice that git sees the file was deleted. Undo the change to this file (the change being the deletion)

```bash
git checkout my-new-file.md
```

Notice that the file has been recovered.