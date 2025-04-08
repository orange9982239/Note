# subgit安裝準備
- [ ] Subgit [下載](https://subgit.com/download)
- [ ] openjdk 11 [下載](https://www.microsoft.com/openjdk)

# subgit安裝
- [ ] install openjdk 
- [ ] unzip Subgit to `C:\Subgit`
- [ ] add path
  - [ ] java   => C:\Program Files\Microsoft\jdk-11.0.15.10-hotspot\bin
  - [ ] subgit => C:\Subgit\bin


# subgit轉換指令

## format
```ps
# 設定
subgit import --non-interactive --username <<SvnAccount>> --password <<SvnPassword>> --svn-url <<SvnUrl>>
subgit configure --layout directory <<SvnUrl>> <<GitRepoName>>.git

# 使用vscod設定svn密碼，讓subgit可以登入svn
code <<GitRepoName>>.git\subgit\passwd

# 轉換
subgit install <<GitRepoName>>.git

cd <<GitRepoName>>.git/

# 先去GitServer建立儲存庫

# 把轉換內容推送至<<GitUrl>>
git remote add orign <<GitUrl>>
git push orign --all --follow-tags
```

## example
```ps
subgit import --non-interactive --username <<SvnAccount>> --password <<SvnPassword>> --svn-url https://svn.domin.com/MyProject 

subgit configure --layout directory https://svn.domin.com/MyProject MyProject.git

code C:\MyProject\MyProject.git\subgit\passwd

subgit install MyProject.git

cd MyProject.git/

git remote add orign https://git.domin.com/RepoOwner/MyProject
git push orign --all --follow-tags
```
