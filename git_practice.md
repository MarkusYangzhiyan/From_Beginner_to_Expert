# Git 分支与团队协作速查

## 1. 查看当前状态和分支

```powershell
# 查看当前分支和文件状态
git status

# 只显示当前分支名称
git branch --show-current

# 查看所有分支
git branch -all
```

## 2. 创建和切换分支

创建分支前，先切换到作为起点的共享开发分支，并同步远程代码：

```powershell
git switch dev_yzy
git pull --ff-only origin dev_yzy
```

创建并立即进入新分支：

```powershell
git switch -c feature/example
```

切换到已经存在的分支：

```powershell
git switch feature/example
```

## 3. 在指定分支提交代码

查看修改、暂存并提交：

```powershell
# 查看尚未暂存的修改
git diff

# 暂存指定文件
git add 文件名

# 查看已经暂存、即将提交的修改
git diff --staged

# 创建提交
git commit -m "提交说明"
```

第一次推送新分支：

```powershell
git push -u origin feature/example
```

`-u` 会让本地分支跟踪对应的远程分支。建立跟踪关系后，可以直接使用：

```powershell
git push
git pull
```

## 4. 查看代码差异和提交历史

```powershell
# 查看工作区与暂存区的差异
git diff

# 查看暂存区与最近提交的差异
git diff --staged

# 比较两个分支从共同祖先开始产生的差异
git diff dev_yzy...feature/example

# 查看最近一次提交的详细修改
git show HEAD

# 查看指定提交
git show 提交哈希

# 查看简洁提交历史和分支图
git log --oneline --graph --decorate --all -10
```

在 GitHub Pull Request 中，可以通过 `Files changed` 检查：

1. 修改了哪些文件。
2. 绿色行表示新增内容，红色行表示删除内容。
3. 是否包含与本次任务无关的修改。
4. PR 标题、描述和实际代码修改是否一致。

## 5. 本地合并分支

合并时，先切换到接收修改的目标分支：

```powershell
git switch dev_yzy
git pull --ff-only origin dev_yzy
```

把功能分支合并进当前的 `dev_yzy`：

```powershell
git merge feature/example
```

需要明确保留 Merge Commit 时：

```powershell
git merge --no-ff feature/example -m "merge: feature example"
```

合并方向可以理解为：

```text
git switch 目标分支
git merge 来源分支
```

## 6. 使用 Pull Request 合并

1. 在功能分支完成修改、测试、提交和 Push。
2. 在 GitHub 创建 Pull Request。
3. 设置 `base` 为接收修改的分支，例如 `dev_yzy`。
4. 设置 `compare` 为功能分支，例如 `feature/example`。
5. 在 `Files changed` 中检查差异。
6. 确认测试结果、Review 意见和合并冲突。
7. 选择 `Create a merge commit`、`Squash and merge` 或团队规定的方式合并。
8. 合并成功后删除远程功能分支。

GitHub 合并后，同步本地目标分支：

```powershell
git switch dev_yzy
git pull --ff-only origin dev_yzy
```

删除本地功能分支：

```powershell
git branch -d feature/example
```

## 7. 回退单个提交

先通过日志找到需要回退的提交哈希：

```powershell
git log --oneline
git show 提交哈希
```

创建一个新的反向提交，撤销指定提交造成的修改：

```powershell
git revert --no-edit 5c2d37a
```

命令含义：

- `git revert`：创建一个新提交，反向撤销目标提交。
- `--no-edit`：不打开编辑器，使用 Git 自动生成的提交说明。
- `5c2d37a`：需要回退的目标提交哈希。

原提交不会消失，提交历史中会同时保留原提交和 Revert Commit。这种方式适合已经 Push 或合并到共享分支的提交。

回退后检查并推送：

```powershell
git show HEAD
git status
git push
```

## 8. 使用 Git Tag 标记项目版本

Git Tag 用于给某个提交添加固定的版本名称。提交保存了当时所有受 Git 管理文件的完整快照，因此标签可以代表整个项目在该提交时的版本。

例如：

```text
提交 A -> 提交 B -> 提交 C
                      ^
                    v0.1.0
```

`v0.1.0` 指向提交 C，但不会修改仓库名称，也不会随着分支继续移动。

### 创建标签前检查

发布版本前，应切换并同步准备发布的分支，然后确认工作区干净、测试通过：

只有已经提交的文件会进入版本快照。未提交修改、未跟踪文件和被 `.gitignore` 忽略的文件不会包含在标签版本中。

### 创建带说明的标签

给当前提交 `HEAD` 创建 `v0.1.0` 标签：

```powershell
git tag -a v0.1.0 -m "Product Manager CLI v0.1.0"
```

参数含义：

- `git tag`：管理 Git 标签。
- `-a v0.1.0`：创建名为 `v0.1.0` 的附注标签。
- `-m`：设置标签说明。
- 未指定提交哈希时，标签默认指向当前 `HEAD`。

给指定历史提交创建标签：

```powershell
git tag -a v0.1.0 提交哈希 -m "Product Manager CLI v0.1.0"
```

### 查看标签

```powershell
# 查看所有标签
git tag --list

# 查看标签指向的提交和详细信息
git show v0.1.0
```

版本号通常采用：

```text
v主版本.次版本.修复版本
v0.1.0
```

`v0.1.0` 通常表示项目处于早期开发阶段，但已经形成第一个完整、可运行和可测试的版本。

### 推送标签到远程仓库

普通 `git push` 默认不会推送标签，需要单独执行：

```powershell
git push origin v0.1.0
```

### 删除错误标签

标签尚未发布或确认创建错误时，可以删除本地和远程标签：

```powershell
# 删除本地标签
git tag -d v0.1.0

# 删除远程标签
git push origin --delete v0.1.0
```

已经正式发布并被其他人使用的标签不应随意移动或删除，通常应发布新的修复版本，例如 `v0.1.1`。

## 9. 完整团队协作流程

```text
同步共享分支
-> 创建功能分支
-> 修改并测试
-> 查看差异
-> git add 和 git commit
-> Push 远程功能分支
-> 创建 Pull Request
-> Review 和自动化测试
-> 合并 Pull Request
-> 本地拉取最新目标分支
-> 删除已合并的功能分支
-> 创建并推送版本标签（发布版本时）
```
