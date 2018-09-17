from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from moudle import DICT, Task, db,TaskNode
from nowtime import nowtime,weekcycletime,monthcycletime
from emailsend import onlinesignmail
from sqlalchemy import desc,and_
task_all = Task.query.filter(
                and_(Task.TASK_STARTTIME <= monthcycletime()[0]),
                and_(Task.TASK_ENDTIME >= monthcycletime()[1])).order_by(desc(Task.TASK_CREATETIME))

print(task_all)