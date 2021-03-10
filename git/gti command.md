# git remote set-url 원격저장소 URL 변경하기

```
$ git remote -v  # View existing remotes
origin  https://github.com/username/repository.git (fetch)
origin  https://github.com/username/repository.git (push)

#Change existing remotes to new url
$ git remote set-url origin https://github.com/username/newrepository.git
```

# Branch

```

$ git checkout `branch name` # move branch

#create branch
$ git branch <branch name>
$ git checkout -b <branch name> 
$ git checkout -b <sub branch name> <branch name> #create sub branch 

#delete branch
$ git branch -d <branch>
```