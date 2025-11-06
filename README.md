## 🧠 Turing Chat：本地智能对话系统
> FastAPI + Vue3 + Docker + Ollama (Qwen3:8B)

> **🚧 项目声明**  
> 本项目是作者学习 **大模型课程-FastAPI** 阶段的练手作品，当前仅实现「接入本地模型 + 前端基础对话」功能，代码与文档均处于课程实验状态。  
> 下文所列的「RAG、插件系统、多模态、语音交互」等特性均为课程结业后的**远期探索目标**，尚未落地。
> 部署项目时请参考下方文件结构，由于上传时为一次性上传，故项目文件目录与实际目录不符，后续再调整。
> 若你期待完整功能，请关注作者结课后的后续更新！


---

## 📑 目录
- [✨ 核心特性](#-核心特性)
- [🛠 技术栈](#-技术栈)
- [🚀 快速开始](#-快速开始)
- [📂 项目结构](#-项目结构)
- [🖼 功能预览](#-功能预览)
- [🧩 后续计划](#-后续计划)
- [🤝 贡献指南](#-贡献指南)
- [💡 致谢](#-致谢)

---

## ✨ 核心特性

| 特性 | 说明 |
|---|---|
| 🔒 **完全本地运行** | 模型（Qwen3:8B）通过 Ollama 加载，零外部 API 调用 |
| 💬 **多轮对话记忆** | 自动维护上下文，支持连贯交互 |
| ⚡ **流式输出** | SSE 逐字生成，体验接近 ChatGPT |
| 📄 **文档理解** | 上传 PDF / TXT，自动解析并问答 |
| 🧠 **RAG 知识库** | 基于 ChromaDB 实现私有文档语义检索增强 |
| 🌗 **现代化 UI** | Markdown 渲染、暗黑模式、自动滚动、对话持久化 |
| 🐳 **一键部署** | Docker Compose 三服务编排（前端 + 后端 + Nginx） |

---

## 🛠 技术栈

| 层级 | 技术 |
|---|---|
| 前端 | Vue 3 + Vite + Tailwind CSS + vue3-markdown-it |
| 后端 | FastAPI + Pydantic + HTTPX |
| AI 引擎 | Ollama + Qwen3:8B（GGUF 量化版） |
| 向量库 | ChromaDB（轻量、嵌入式） |
| 部署 | Docker + Docker Compose + Nginx |

---

## 🚀 快速开始

### 前置条件
1. 已安装 **Docker** 与 **Docker Compose**
2. 本地已拉取 Qwen3:8B 模型  
   ```bash
   ollama pull qwen3:8b
   ```

### 一键启动
```bash
git clone https://github.com/yourname/turing-chat.git
cd turing-chat
# 自动构建前端、启动后端、Nginx 反代
docker-compose up --build
```

### 访问服务
- 前端：http://localhost  
- API：http://localhost/api/chat  

> 首次启动需加载 8B 模型，耐心等待 30-60s 即可。

---

## 📂 项目结构

```
turing-chat/
├── backend/                 # FastAPI 后端
│   ├── main.py
│   ├── api/
│   │   └── chat.py         # 聊天 / 流式 / 文件上传
│   └── rag/
│       └── chroma_client.py
├── frontend/                # Vue3 前端
│   ├── src/
│   │   ├── components/
│   │   └── App.vue
│   └── vite.config.js
├── nginx/
│   └── default.conf        # 反向代理
├── docker-compose.yml
├── Dockerfile.backend
├── Dockerfile.frontend
└── README.md
```

---

## 🖼 功能预览

| 聊天界面 | RAG 问答 |
|---|---|
| ![chat](docs/chat.png) | ![rag](docs/rag.png) |

> 截图后续补充，现为占位。

---

## 🧩 后续计划

| 方向 | 详情 |
|---|---|
| 🔹 **核心体验** | 多轮摘要 · SSE 优化 · 角色预设 |
| 🔹 **知识增强** | DOCX 支持 · 分段策略 · 检索重排序 |
| 🔹 **插件系统** | Function Calling · 动态注册 · 沙箱执行 |
| 🔹 **多模态** | Whisper + TTS · Qwen-VL 图文对话 |
| 🔹 **数据沉淀** | 匿名化对话保存 · 小模型微调 |

---

## 🤝 贡献指南

欢迎提 Issue / PR！  
请遵守 [Conventional Commits](https://www.conventionalcommits.org/) 规范，并在 PR 内描述测试场景。

---

## 💡 致谢

- [Ollama](https://ollama.ai) – 本地大模型运行引擎  
- [Qwen](https://github.com/QwenLM) – 千问系列开源模型  
- [ChromaDB](https://www.trychroma.com) – 轻量向量数据库  

---

