# 个人财务管理 API

FastAPI + MySQL + SQLAlchemy 构建的个人财务管理后端接口。

## 功能

- 用户注册/登录（密码哈希 + JWT）
- 账单管理：创建、查询（分页+筛选）、删除
- 分类管理：创建、删除、查询
- 金额/时间筛选，月度汇总

## 技术栈

| 层级 | 技术 |
|------|------|
| 框架 | FastAPI |
| 数据库 | MySQL 8.0 |
| ORM | SQLAlchemy 2.0 |
| 鉴权 | JWT (python-jose) + bcrypt |
| 运行 | uvicorn |

## 快速启动

### 1. 准备环境

```bash
# 安装依赖
pip install -r requirements.txt
```

### 2. 配置数据库

确保 MySQL 已运行，修改 `app/config.py` 中的数据库连接信息：

```python
DATABASE_URL = "mysql+pymysql://root:你的密码@localhost:3306/financial_db"
```

### 3. 创建数据库

在 MySQL 中执行：

```sql
CREATE DATABASE financial_db CHARACTER SET utf8mb4;
```

### 4. 启动服务

```bash
uvicorn app.main:app --reload
```

访问 `http://localhost:8000/docs` 查看自动生成的 API 文档。

## API 接口

### 用户

| 方法 | 路径 | 说明 |
|------|------|------|
| POST | `/register` | 注册 `{name, password}` |
| POST | `/login` | 登录 `{name, password}` → `{token}` |

### 账单

| 方法 | 路径 | 说明 |
|------|------|------|
| POST | `/bills` | 创建账单 `{money, place, bill_time, category_id, remark}` |
| GET  | `/bills` | 查询账单列表（支持 year/month/day/amount_op/amount_value/category_id 筛选） |
| DELETE | `/bills/{id}` | 删除账单 |

### 分类

| 方法 | 路径 | 说明 |
|------|------|------|
| GET  | `/categories` | 获取所有分类 |
| POST | `/categories` | 创建分类 `{category_name}` |
| DELETE | `/categories/{id}` | 删除分类 |

## 项目结构

```
finance-api/
├── app/
│   ├── main.py              # 入口
│   ├── config.py             # 数据库/密钥配置
│   ├── database.py           # SQLAlchemy 引擎
│   ├── routers/
│   │   ├── auth.py           # 注册/登录
│   │   ├── bill.py           # 账单 CRUD
│   │   └── category.py       # 分类 CRUD
│   ├── models/
│   │   ├── user.py
│   │   ├── bill.py
│   │   └── category.py
│   └── utils/
│       └── security.py       # JWT + 密码哈希
├── requirements.txt
└── README.md
```
