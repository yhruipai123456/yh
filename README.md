# 亿鸿皮具 / 瑞牌企业官网

项目分为前端和后端：

- `frontend/`：Vue 3、TypeScript、Vite、Tailwind CSS 前端
- `backend/`：FastAPI 后端，提供文章和管理员接口

## 前端启动

```bash
cd frontend
npm install
npm run dev
```

# 终端1：后端
cd backend
py -m uvicorn app.main:app --reload --host 0.0.0.0 --port 8000

# 终端2：前端
npm run dev

开发服务器默认使用 5173 端口，并将 `/api` 请求代理到 `http://127.0.0.1:8000`。后端启动方式见 [backend/README.md](backend/README.md)。

## 前端构建

```bash
cd frontend
npm run build
npm run preview
```

构建产物位于 `frontend/dist/`。正式图片请放在 `frontend/public/images/`，文件名参考该目录下的 README。

上线前请核对企业资料、荣誉及合作品牌授权，并补全企业官方联系方式。
