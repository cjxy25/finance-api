"""应用配置 — 数据库连接、JWT 密钥等"""

DATABASE_URL = "mysql+pymysql://root:18717890819Asd@localhost:3306/financial_db"

JWT_SECRET_KEY = "a0b8c7d6e5f4g3h2i1j0k9l8m7n6o5p4"
JWT_ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24  # 24小时
