from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_login import UserMixin

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SECRET_KEY'] = 'hard to guess string'
app.config['SQLALCHEMY_DATABASE_URI'] = \
    'mysql+pymysql://root:yunwei159@cd-cdb-cph00878.sql.tencentcdb.com:63811/ly?charset=utf8'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(UserMixin, db.Model):  # 定义用户登录表
    __tablename__ = 'SYS_USERLOGIN'

    id = db.Column(db.Integer, primary_key=True)
    # fid主键
    LOGIN_NAME = db.Column(db.String(20), unique=False, nullable=True)
    # 登录名
    PASSWORD = db.Column(db.String(20), unique=False, nullable=True)
    # 密码
    USERNAME = db.Column(db.String(20), unique=False, nullable=True)
    # 姓名
    LAST_LOGIN_TIME = db.Column(db.DateTime, unique=True, nullable=True)
    # 最后一次登录时间
    ROLEID = db.Column(db.Integer, unique=False, nullable=True)
    # 角色id
    LOGIN_COUNT = db.Column(db.Integer, unique=True, nullable=True)
    # 登录次数
    DEPARTMENTID = db.Column(db.Integer, unique=True, nullable=True)
    # 所属部门
    REMARK = db.Column(db.String(100), unique=False, nullable=True)

    # 备注

    def __repr__(self):
        return '<User %r>' % self.LOGIN_NAME

    def is_active(self):
        return True


class DICT(db.Model):
    __tablename__ = 'DICT'
    id = db.Column(db.Integer, primary_key=True)
    # fid主键
    NAME = db.Column(db.String(50), unique=False, nullable=True)
    # ID
    TYPE = db.Column(db.String(50), unique=False, nullable=True)
    # 类型


# 以下为task蓝图的处理模块
# 处理任务
class Task(db.Model):
    __tablename__ = 'SYS_TASK'
    id = db.Column(db.Integer, primary_key=True)
    # fid主键
    TASK_SYSTEM = db.Column(db.String(50), unique=False, nullable=True)
    # ID
    TASK_TITLE = db.Column(db.String(200), unique=False, nullable=True)
    # 类型
    TASK_SOURCE = db.Column(db.String(50), unique=False, nullable=True)
    # ID
    TASK_DETAIL = db.Column(db.String(1000), unique=False, nullable=True)
    # 类型
    TASK_STARTTIME = db.Column(db.String(16), unique=False, nullable=True)
    # 类型
    TASK_ENDTIME = db.Column(db.String(16), unique=False, nullable=True)
    # ID
    TASK_SCHEDULE = db.Column(db.Integer, unique=False, nullable=True)
    # 类型
    TASK_SCHEDULE_DETAILE = db.Column(db.String(1000), unique=False, nullable=True)
    # ID
    TASK_USERNAME = db.Column(db.String(50), unique=False, nullable=True)
    # 类型
    TASK_CREATETIME = db.Column(db.DateTime(50), unique=False, nullable=True)
    # ID
    TASK_STATE = db.Column(db.String(1), unique=False, nullable=True)
    # ID
    TASK_TRANSLATE = db.Column(db.String(50), unique=False, nullable=True)
    # 类型


# 处理任务节点
class TaskNode(db.Model):
    __tablename__ = 'SYS_TASK_NODE'
    id = db.Column(db.Integer, primary_key=True)
    # fid主键
    SYS_TASK_ID = db.Column(db.Integer, unique=False, nullable=True)
    NODE_SCHEDULE = db.Column(db.Integer, unique=False, nullable=True)
    NODE_SCHEDULE_DETAILE = db.Column(db.String(1000), unique=False, nullable=True)
    NODE_SCHEDULE_REST = db.Column(db.String(1000), unique=False, nullable=True)
    NODE_CREATETIME = db.Column(db.DateTime(50), unique=False, nullable=True)


# 以下为onlinesign蓝图的处理模块
# 处理网签日报
class OnlineSignReprot(db.Model):
    __tablename__ = 'REPORT_ONLINESIGN'
    id = db.Column(db.Integer, primary_key=True)
    # 主键
    CYCEL = db.Column(db.String(10), unique=False, nullable=True)
    # 周期，区别日报周报月报
    CHECKTIME = db.Column(db.DateTime, unique=False, nullable=True)
    # 检查时间
    PROTJECT_1 = db.Column(db.String(200), unique=False, nullable=True)
    # 检查商品房网签系统(http://wq.cq315house.com/bdckfs/)是否可以正常访问；
    PROTJECT_2 = db.Column(db.String(200), unique=False, nullable=True)
    # 登录存量房网签系统(http://esfwq.cq315house.com/bdckfs/)是否可以正常访问；
    PROTJECT_3 = db.Column(db.String(200), unique=False, nullable=True)
    # 检查系统(10.0.145.50:7001/cqgtfw_access_web/user/login)是否可以正常访问、登录；
    PROTJECT_4 = db.Column(db.String(200), unique=False, nullable=True)
    # 检查系统菜单是否空白、功能模块是否正常记载；
    PROTJECT_5 = db.Column(db.String(200), unique=False, nullable=True)
    # 随机抽检系统功能是否正常，本次抽查认购信息表中的条件检索功能；
    PROTJECT_6 = db.Column(db.String(200), unique=False, nullable=True)
    # 检查系统数据是否正常加载、实时更新；
    PROTJECT_7 = db.Column(db.String(200), unique=False, nullable=True)
    # 检查系统历史登录记录(IP、时间)是否异常；
    PROTJECT_8 = db.Column(db.String(200), unique=False, nullable=True)
    # 检查对账差错信息表中是否有差错账记录
    PROTJECT_9 = db.Column(db.String(200), unique=False, nullable=True)
    # 检查10.0.145.51服务器磁盘是否足够
    PROTJECT_10 = db.Column(db.String(200), unique=False, nullable=True)
    # 检查10.0.145.50服务器磁盘是否足够
    PROTJECT_11 = db.Column(db.String(200), unique=False, nullable=True)
    # 暂时未使用
    EMAIL_STATE = db.Column(db.String(1), unique=False, nullable=True)

    USERNAME = db.Column(db.String(200), unique=False, nullable=True)
    # 创建人


# 以下为邮件收件人地址的处理模块
class MailTo(db.Model):
    __tablename__ = 'MAIL_TO'
    id = db.Column(db.Integer, primary_key=True)
    # fid主键
    MAIL_ADDR = db.Column(db.String(50), unique=False, nullable=True)
    MAIL_TONAME = db.Column(db.String(50), unique=False, nullable=True)
    MAIL_TYPE = db.Column(db.DateTime(50), unique=False, nullable=True)
