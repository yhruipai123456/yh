# 阶段一：构建前端产物
FROM node:20-alpine AS build

WORKDIR /app

# 先复制依赖清单，利用 Docker 层缓存
COPY package*.json ./
RUN npm ci

# 复制源码并构建
COPY . .
RUN npm run build

# 阶段二：用 nginx 托管静态文件
FROM nginx:alpine

# 新版 nginx:alpine 默认以非 root 运行，会因无法写入 /run/nginx.pid 而崩溃，这里改回 root
USER root

# 覆盖默认 nginx 配置（SPA 路由回退 + /api 反向代理）
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist /usr/share/nginx/html

EXPOSE 80

CMD ["nginx", "-g", "daemon off; pid /tmp/nginx.pid;"]
