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
# 固定版本：nginx:alpine 现在已到 1.31.8（Alpine 3.23），在 CentOS 7 的 3.10 内核上会报 pwrite EPERM，回退到稳定版
FROM nginx:1.26-alpine

# 以 root 运行，确保主进程能写 pid 文件
USER root

# 覆盖默认 nginx 配置（SPA 路由回退 + /api 反向代理）
COPY nginx.conf /etc/nginx/conf.d/default.conf
COPY --from=build /app/dist /usr/share/nginx/html

# 主配置里的 pid 指向 /run，改为 /tmp 确保可写（-g 参数会被主配置覆盖，所以直接改主配置）
RUN sed -i -E 's@^pid[[:space:]]+.*;@pid /tmp/nginx.pid;@' /etc/nginx/nginx.conf

EXPOSE 80

CMD ["nginx", "-g", "daemon off;"]
