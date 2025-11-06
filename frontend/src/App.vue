<template>
  <div class="chat-container">
    <h2 class="chat-title">Turing Chat (qwen3:8b via Ollama)</h2>

    <!-- 聊天消息区域 -->
    <div class="chat-box">
      <div
        v-for="(m, i) in messages"
        :key="i"
        :class="['message', m.role]"
      >
        <div class="bubble" v-html="formatText(m.text)"></div>
      </div>

      <!-- “思考中...” 动画 -->
      <div v-if="loading" class="message assistant">
        <div class="bubble thinking">
          <span class="dot"></span>
          <span class="dot"></span>
          <span class="dot"></span>
        </div>
      </div>
    </div>

    <!-- 输入框 -->
    <div class="input-area">
      <input
        v-model="prompt"
        @keyup.enter="send"
        placeholder="输入消息后回车"
        class="input-box"
      />
      <button @click="send" class="send-btn">发送</button>
    </div>
  </div>
</template>

<script>
import axios from "axios";

export default {
  data() {
    return {
      prompt: "",
      messages: [],
      loading: false,
    };
  },
  methods: {
    async send() {
      const text = this.prompt.trim();
      if (!text) return;
      this.messages.push({ role: "user", text });
      this.prompt = "";
      this.loading = true;

      try {
        const res = await axios.post("http://localhost:8000/api/chat", {
          prompt: text,
        });
        const reply = res.data?.reply || "(no reply)";
        this.messages.push({ role: "assistant", text: reply });
      } catch (e) {
        console.error(e);
        this.messages.push({
          role: "assistant",
          text: "❌ 网络错误，请稍后再试。",
        });
      } finally {
        this.loading = false;
      }
    },

    // 文本格式化（去除 Markdown、添加换行）
    formatText(text) {
      if (!text) return "";
      // 转义 HTML
      const safe = text
        .replace(/&/g, "&amp;")
        .replace(/</g, "&lt;")
        .replace(/>/g, "&gt;");
      // 去掉 **、---、### 等 Markdown 格式
      return safe
        .replace(/\*\*(.*?)\*\*/g, "$1")
        .replace(/---+/g, "")
        .replace(/^#+\s*/gm, "")
        .replace(/\n/g, "<br>");
    },
  },
};
</script>

<style scoped>
.chat-container {
  max-width: 800px;
  margin: 40px auto;
  font-family: "Segoe UI", Arial, sans-serif;
  display: flex;
  flex-direction: column;
  height: 90vh;
}

.chat-title {
  text-align: center;
  margin-bottom: 16px;
}

.chat-box {
  flex: 1;
  overflow-y: auto;
  padding: 12px;
  border: 1px solid #ddd;
  border-radius: 10px;
  background: #fafafa;
}

.message {
  display: flex;
  margin-bottom: 12px;
}

.message.user {
  justify-content: flex-end;
}

.message.assistant {
  justify-content: flex-start;
}

.bubble {
  padding: 10px 14px;
  border-radius: 10px;
  max-width: 75%;
  white-space: pre-wrap;
  word-break: break-word;
  line-height: 1.5;
}

.user .bubble {
  background: #d1ecff;
}

.assistant .bubble {
  background: #f1f1f1;
}

/* “思考中...” 动画 */
.thinking {
  display: flex;
  align-items: center;
  gap: 4px;
}

.dot {
  width: 8px;
  height: 8px;
  background-color: #888;
  border-radius: 50%;
  animation: blink 1.4s infinite both;
}

.dot:nth-child(2) {
  animation-delay: 0.2s;
}
.dot:nth-child(3) {
  animation-delay: 0.4s;
}

@keyframes blink {
  0%, 80%, 100% {
    opacity: 0;
  }
  40% {
    opacity: 1;
  }
}

.input-area {
  display: flex;
  gap: 8px;
  margin-top: 12px;
}

.input-box {
  flex: 1;
  padding: 10px;
  border: 1px solid #ddd;
  border-radius: 8px;
  font-size: 15px;
}

.send-btn {
  padding: 10px 16px;
  border: none;
  background-color: #007bff;
  color: white;
  border-radius: 8px;
  cursor: pointer;
}

.send-btn:hover {
  background-color: #0056b3;
}
</style>
