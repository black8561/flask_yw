from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from moudle import DICT, Task, db, TaskNode
from nowtime import nowtime, weekcycletime,monthcycletime
from emailsend import onlinesignmail
from sqlalchemy import desc, and_

task = Blueprint('task', __name__)


@task.route('/adder', methods=['GET', 'POST'])
@login_required
def task_adder():
    # 发布任务的视图函数
    if request.method == 'POST':
        TASK_SYSTEM = request.values.get('TASK_SYSTEM')
        TASK_TITLE = request.values.get('TASK_TITLE')
        TASK_SOURCE = request.values.get('TASK_SOURCE')
        TASK_DETAIL = request.values.get('TASK_DETAIL')
        TASK_STARTTIME = request.values.get('TASK_STARTTIME')
        TASK_ENDTIME = request.values.get('TASK_ENDTIME')
        TASK_STATE = request.values.get('TASK_STATE')
        if TASK_STATE == '2':
            TASK_SCHEDULE = 100
        else:
            TASK_SCHEDULE = 0
        TASK_USERNAME = current_user.LOGIN_NAME
        TASK_CREATETIME = nowtime()
        Taskadder = Task(TASK_SYSTEM=TASK_SYSTEM,
                         TASK_TITLE=TASK_TITLE,
                         TASK_SOURCE=TASK_SOURCE,
                         TASK_DETAIL=TASK_DETAIL,
                         TASK_STARTTIME=TASK_STARTTIME,
                         TASK_ENDTIME=TASK_ENDTIME,
                         TASK_STATE=TASK_STATE,
                         TASK_SCHEDULE=TASK_SCHEDULE,
                         TASK_USERNAME=TASK_USERNAME,
                         TASK_CREATETIME=TASK_CREATETIME)
        try:
            db.session.add(Taskadder)
            db.session.commit()
            onlinesignmail()
            flash('保存成功', 'task_keepsusscess')
            return redirect(url_for('task.task_adder'))
        except:
            flash('保存失败', 'task_keepfail')
            return redirect(url_for('task.task_adder'))
    else:
        system_name = DICT.query.filter_by(TYPE='系统').all()
        task_resource = DICT.query.filter_by(TYPE='任务来源').all()
        return render_template('tasks_adder.html',
                               system_name=system_name,
                               task_resource=task_resource)


@task.route('/all', methods=['GET', 'POST'])
@login_required
def task_all():
    # 任务一览，目前未设置时间参数，显示的是全部任务数据
    if request.method == 'POST':
        pass
    else:
        cycle = request.args.get("cycle")
        state = request.args.get("state")
        if state==None:
            if cycle == "week":
                task_all = Task.query.filter(and_(Task.TASK_USERNAME == current_user.LOGIN_NAME),
                    and_(Task.TASK_STARTTIME <= weekcycletime()[0]),
                    and_(Task.TASK_ENDTIME >= weekcycletime()[1])).order_by(desc(Task.TASK_CREATETIME))
            if cycle == "month":
                task_all = Task.query.filter(and_(Task.TASK_USERNAME == current_user.LOGIN_NAME),
                    and_(Task.TASK_STARTTIME <= monthcycletime()[0]),
                    and_(Task.TASK_ENDTIME >= monthcycletime()[1])).order_by(desc(Task.TASK_CREATETIME))
            if cycle == "all":
                task_all = Task.query.filter_by(TASK_USERNAME=current_user.LOGIN_NAME
                    ).order_by(desc(Task.TASK_CREATETIME))
            active='1'
        elif state=='2':
            task_all = Task.query.filter_by(TASK_USERNAME=current_user.LOGIN_NAME,TASK_STATE='2'
                                            ).order_by(desc(Task.TASK_CREATETIME))
            active='4'
        else:
            task_all = Task.query.filter(and_(Task.TASK_USERNAME == current_user.LOGIN_NAME),
                                         and_(Task.TASK_STATE != '2'),
                                            ).order_by(desc(Task.TASK_CREATETIME))
            active='3'
        return render_template('tasks_all.html',
                               task_all=task_all,state=state,active=active)


@task.route('/nodeadder', methods=['GET', 'POST'])
@login_required
def task_nodeadder():
    # 增加任务节点
    if request.method == 'POST':
        SYS_TASK_ID = request.args.get('id')
        NODE_SCHEDULE = request.values.get('NODE_SCHEDULE')
        NODE_SCHEDULE_DETAILE = request.values.get('NODE_SCHEDULE_DETAILE')
        NODE_SCHEDULE_REST = request.values.get('NODE_SCHEDULE_REST')
        NODE_CREATETIME = nowtime()
        TaskNodeAdder = TaskNode(SYS_TASK_ID=SYS_TASK_ID,
                                 NODE_SCHEDULE=NODE_SCHEDULE,
                                 NODE_SCHEDULE_DETAILE=NODE_SCHEDULE_DETAILE,
                                 NODE_SCHEDULE_REST=NODE_SCHEDULE_REST,
                                 NODE_CREATETIME=NODE_CREATETIME)
        # 添加节点进度比例为100时，同步更新任务表内任务状态值为2，非100时更新为1
        if NODE_SCHEDULE == '100':
            result = Task.query.filter_by(id=SYS_TASK_ID).first()
            result.TASK_STATE = '2'
            result.TASK_SCHEDULE = '100'
            db.session.commit()  # 更新状态和进度

            db.session.add(TaskNodeAdder)
            db.session.commit()
            flash('保存成功', 'task_keepsusscess')
            return redirect(url_for('task.task_nodeadder', id=SYS_TASK_ID))
        else:
            try:
                result = Task.query.filter_by(id=SYS_TASK_ID).first()
                result.TASK_STATE = '1'
                result.TASK_SCHEDULE = NODE_SCHEDULE
                db.session.commit()

                db.session.add(TaskNodeAdder)
                db.session.commit()
                flash('保存成功', 'task_keepsusscess')
                return redirect(url_for('task.task_nodeadder', id=SYS_TASK_ID))
            except:
                flash('保存失败', 'task_keepfail')
                return redirect(url_for('task.task_nodeadder', id=SYS_TASK_ID))
    else:
        taskid = request.args.get('id')
        task_detail = Task.query.filter_by(id=taskid).all()
        task_node_detail = TaskNode.query.filter_by(SYS_TASK_ID=taskid).all()
        return render_template('tasks_node_adder.html',
                               task_detail=task_detail,
                               task_node_detail=task_node_detail)


@task.route('/nodequery', methods=['GET', 'POST'])
@login_required
def task_nodequery():
    # 增加任务节点
    if request.method == 'POST':
        pass
    else:
        taskid = request.args.get('id')
        task_detail = Task.query.filter_by(id=taskid).all()
        task_node_detail = TaskNode.query.filter_by(SYS_TASK_ID=taskid).all()
        return render_template('tasks_node_query.html',
                               task_detail=task_detail,
                               task_node_detail=task_node_detail)
