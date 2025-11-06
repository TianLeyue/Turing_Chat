FROM node:20-alpine

WORKDIR /app

# 复制依赖清单
COPY package.json /app/package.json
RUN npm install

# 复制源码
COPY . /app

EXPOSE 5173

CMD ["npm", "run", "dev"]

