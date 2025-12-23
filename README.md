# OK 小助手

简洁单页应用，包含首页、门店地址页、商品列表页、线上购卡页、使用说明页与使用场景页。

## 本地运行（FastAPI）

```bash
uvicorn main:app --reload
```

路由：

- `/` 首页：四宫格卡片，促销图点击进入商品列表；“哪里买”切换线上/线下购卡卡片。
- `/address`：门店地址，数据来自 `static/data/addresses.json`。
- `/items`：商品/票券列表，数据来自 `static/data/items.json`，双列展示。
- `/buy-online`：线上购卡页（背景 + 中心图）。
- `/how-to-use`：使用说明页，顶部标签切换“电子卡 / 实体卡”，展示对应示意图。
- `/where-use`：使用场景页，两列同时展示线上/线下分类列表。

## GitHub Pages 静态托管

项目自带导出脚本，会把可直接托管的静态站点放到 `docs/`，并复制 `static/` 资源：

```bash
python tools/export_static.py
```

然后提交代码，GitHub Pages 设置：

1. 打开仓库 Settings → Pages。
2. Source 选择 `Deploy from a branch`。
3. Branch 选 `main`，目录选择 `/docs`，保存。

上线后访问：`https://<your-user>.github.io/<repo>/`。

注意：导出的静态版使用相对路径（如 `items.html`、`address.html` 等），适合 GitHub Pages。若更新模板或静态资源，重新运行导出脚本并提交即可。

## 目录说明

- `main.py`：FastAPI 入口。
- `templates/`：运行时模板。
- `static/`：样式、图片、数据等静态资源。
- `docs/`：执行导出脚本后生成的静态站点（供 GitHub Pages 使用）。
- `tools/export_static.py`：导出静态站点脚本。
