# MaxKB 部署记录

## 1. 项目目标

使用 Docker Desktop 在 Windows 本地启动 MaxKB，为后续知识库配置、API 调用、LangChain Tool 封装和 LangGraph 编排做准备。

## 2. 本地环境

- 操作系统：Windows
- 终端：PowerShell
- 容器工具：Docker Desktop
- 项目目录：E:\From_Beginner_To_Expert\From_Beginner_to_Expert\MaxKB+Langchain
- 手动挂载目录：C:\maxkb
- 访问端口：8080

## 3. 启动命令

```powershell
docker run -d --name=maxkb `
  --restart=always `
  -p 8080:8080 `
  -v C:/maxkb:/opt/maxkb `
  registry.fit2cloud.com/maxkb/maxkb
```

## 4. 检查命令

```powershell
docker ps -a
docker logs --tail 100 maxkb
```

## 5. 当前容器状态

- 容器名：maxkb
- 镜像：registry.fit2cloud.com/maxkb/maxkb
- 状态：Up
- 端口映射：0.0.0.0:8080->8080/tcp
- 手动挂载：C:\maxkb -> /opt/maxkb
- 数据库挂载：Docker 自动 volume -> /var/lib/postgresql/data

当前完整挂载信息：

```text
bind   | C:/maxkb | /opt/maxkb
volume | Docker volume | /var/lib/postgresql/data
```

## 6. 访问地址

```text
http://localhost:8080
```

## 7. 登录验证

- 默认用户名：admin
- 默认密码：MaxKB@123..
- 当前状态：网页登录成功
