# Report Creator - 技术调研报告撰写工具

一个用于 Kimi Code CLI 的 Skill，帮助用户完成从技术主题搜索到演示文档生成的完整技术调研报告撰写流程。

## 功能概述

- **深度调研**：搜索技术博客、科技网站、学术论文、社交媒体等多渠道信息
- **结构分析**：按技术发展历史、竞品对比、关键技术、未来趋势等维度整理信息
- **Markdown 报告**：生成结构化的技术调研报告
- **演示文档**：使用 LaTeX Beamer 生成专业的中文演示文稿（PDF）

## 适用场景

- 技术调研报告撰写
- 技术趋势分析
- 领域综述报告
- 技术分享演示文稿

## 文件结构

```
report-creator/
├── SKILL.md                     # Skill 主文档（Kimi CLI 使用）
├── README.md                    # 本文件
├── assets/
│   └── beamer-template.tex      # LaTeX Beamer 中文演示模板
├── scripts/
│   └── compile_beamer.py        # LaTeX 自动编译脚本
└── references/
    └── report-structure.md      # 报告结构详细指南
```

## 使用方法

### 1. 安装 Skill

将本仓库克隆到 Kimi CLI 的 skills 目录：

```bash
cd ~/.kimi/skills
git clone https://github.com/leochencn/report-creator.git
```

### 2. 使用 Skill

在 Kimi CLI 中输入：

```
使用 report-creator skill，帮我撰写关于 [技术主题] 的技术调研报告
```

或简写为：

```
/report-creator [技术主题]
```

### 3. 报告生成流程

1. **信息搜集**：搜索相关技术资料
2. **信息整理**：按维度分析整理
3. **Markdown 报告**：生成结构化文档
4. **演示文稿**：生成 LaTeX Beamer 幻灯片
5. **PDF 编译**：输出最终演示文档

## 依赖要求

- **LaTeX 发行版**：TeX Live 或 MiKTeX（用于编译 PDF）
- **中文字体**：确保系统安装了支持中文的字体（如 SimSun、SimHei）
- **Python 3**：用于运行编译脚本

### 安装依赖

**Windows:**
```bash
# 安装 TeX Live（推荐）或 MiKTeX
# 确保 xelatex 命令可用
xelatex --version
```

**macOS:**
```bash
brew install --cask mactex
```

**Linux:**
```bash
sudo apt-get install texlive-xetex texlive-lang-chinese
```

## 报告结构

生成的技术调研报告包含以下章节：

1. **摘要** - 研究背景、主要发现、核心结论
2. **引言** - 研究背景、范围与方法
3. **技术发展历史** - 起源、里程碑、发展阶段
4. **市场现状与竞品分析** - 主要参与者、产品对比、市场份额
5. **关键技术解析** - 技术原理、架构分析、核心挑战
6. **未来发展趋势** - 技术演进、应用前景、风险挑战
7. **总结与建议** - 核心发现、战略建议

## 输出示例

- **Markdown 报告**: `{主题}_技术调研报告.md`
- **LaTeX 源文件**: `{主题}_技术调研报告.tex`
- **演示文稿 PDF**: `{主题}_技术调研报告.pdf`

## 贡献

欢迎提交 Issue 和 Pull Request！

## 许可证

MIT License

## 作者

- **GitHub**: [@leochencn](https://github.com/leochencn)
