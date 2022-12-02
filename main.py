import git

# repo = git.Repo('/Users/macbookpro/PycharmProjects/testfork/cvelist')
repo = git.Repo('cvelist')
o = repo.remotes.origin
o.pull()