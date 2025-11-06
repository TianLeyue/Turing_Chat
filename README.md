#🧠 Turing Chat — 本地智能对话系统
一个基于 FastAPI + Vue/React + Docker + Ollama (Qwen3:8B) 的端到端私有化 AI 聊天应用。无需联网、不依赖 OpenAI，所有数据与模型运行在本地，保护隐私，支持多轮对话、流式响应、文件分析与知识库问答（RAG）。

[![License](https://img.shields.io/badge/license-MIT-blue.svg)](LICENSE)
(可选：后续加上 demo 链接、GitHub Actions 状态等)

✨ 核心特性
🔒 完全本地运行：模型（Qwen3:8B）通过 Ollama 在本地加载，无外部 API 调用
💬 多轮对话记忆：自动维护上下文，支持连贯交互
⚡ 流式输出：文字逐字生成，体验接近 ChatGPT
📄 文档理解：支持上传 PDF/TXT 文件，AI 自动解析内容并回答问题
🧠 RAG 知识库：基于 ChromaDB 实现私有文档语义检索增强
🌗 现代化 UI：Markdown 渲染、暗黑模式、自动滚动、对话持久化
🐳 一键部署：Docker Compose 三服务编排（前端 + 后端 + Nginx）

🛠 技术栈

层级 技术
------ ------
前端 Vue 3 / React + Vite + Tailwind CSS + vue3-markdown-it
后端 FastAPI + Pydantic + HTTPX
AI 引擎 Ollama + Qwen3:8B（GGUF 量化版）
向量库 ChromaDB（轻量、嵌入式）
部署 Docker + Docker Compose + Nginx

🚀 快速开始
前置条件
已安装 [Docker](https://www.docker.com/) 和 [Docker Compose](https://docs.docker.com/compose/)
本地已拉取 Qwen3:8B 模型：
bash
ollama pull qwen3:8b

启动项目
bash
git clone https://github.com/yourname/turing-chat.git
cd turing-chat
构建并启动（自动构建前端 + 启动后端 + Nginx 反代）
docker-compose up --build
访问
前端：http://localhost
API：http://localhost/api/chat
💡 首次启动可能较慢（需加载 8B 模型），请耐心等待。

📂 项目结构

turing-chat/
├── backend/ # FastAPI 后端
│ ├── main.py # 入口
│ ├── api/
│ │ └── chat.py # 聊天、流式、文件上传接口
│ └── rag/
│ └── chroma_client.py
├── frontend/ # Vue/React 前端
│ ├── src/
│ │ ├── components/
│ │ └── App.vue
│ └── vite.config.js
├── nginx/
│ └── default.conf # 反向代理配置
├── docker-compose.yml
├── Dockerfile.backend
├── Dockerfile.frontend # （可选，也可合并构建）
└── README.md

🖼 功能预览（可选）
（建议后续添加 1–2 张截图：聊天界面 + RAG 问答效果）

🧩 后续计划
🔹 核心体验完善
 多轮对话增强：支持上下文自动摘要，避免长对话超限
 流式响应优化：前端 SSE 稳定性提升 + 打字机动画
 角色预设系统：内置“编程助手”“学术顾问”等 persona，支持自定义 system prompt
🔹 知识与文件理解
 文件智能分析：支持 PDF / DOCX / TXT 上传，自动提取文本并问答
 本地 RAG 引擎：基于 ChromaDB 构建私有知识库，实现文档语义检索增强生成
🔹 行动能力扩展
 插件系统（Function Calling）：模型可调用工具（如查天气、执行 Python 代码、搜索网络）
 动态工具注册：开发者可轻松添加新插件，无需修改核心逻辑
🔹 长期探索
 语音交互：集成 Whisper（语音转文字） + 开源 TTS（文字转语音），支持语音聊天
 多模态支持：接入 Qwen-VL 等视觉语言模型，实现图文混合输入
 对话数据沉淀：匿名化保存高质量对话，用于小模型微调或评估


💡 致谢
[Ollama](https://ollama.com/) – 本地大模型运行引擎
[Qwen](https://qwenlm.github.io/) – 千问系列开源模型
[ChromaDB](https://www.trychroma.com/) – 轻量向量数据库
