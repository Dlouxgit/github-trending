# GitHub Trending 数据抓取

这是一个自动抓取 GitHub Trending 页面数据的工具。它会每天自动运行并保存 GitHub 趋势项目的相关信息。

## 功能特点

- 🔄 每天自动更新（北京时间早上 8:00）
- 📊 抓取 GitHub Trending 页面的热门仓库信息
- 💾 将数据以 JSON 格式保存
- 🔍 包含以下数据：
  - 仓库标题
  - 仓库链接
  - 项目描述
  - star 数量
  - fork 数量

## 技术实现

- Python 3.9
- GitHub Actions 自动化运行
- 主要依赖：
  - requests
  - beautifulsoup4

## 数据格式

每日数据保存为 JSON 文件，格式如下：

```json
[
    {
        "title": "用户名/仓库名",
        "link": "https://github.com/用户名/仓库名",
        "description": "项目描述",
        "stars": "星标数",
        "forks": "分支数"
    }
]
```

## 本地运行

1. 克隆仓库：
```bash
git clone [仓库地址]
```

2. 安装依赖：
```bash
pip install requests beautifulsoup4
```

3. 运行脚本：
```bash
python fetch_trending.py
```

## 自定义配置

你可以通过修改 `fetch_trending.py` 中的参数来自定义数据抓取：

```python
# 指定编程语言
trending_data = fetch_trending(language='python')

# 指定时间范围：daily（每日）、weekly（每周）、monthly（每月）
trending_data = fetch_trending(since='weekly')
```

## GitHub Actions 自动运行

本项目使用 GitHub Actions 实现自动化运行：

- 定时任务：每天 UTC 时间 00:00（北京时间早上 8:00）运行
- 支持手动触发运行
- 自动提交更新的数据文件

## 许可证

MIT License

## 贡献指南

欢迎提交 Issue 和 Pull Request！
