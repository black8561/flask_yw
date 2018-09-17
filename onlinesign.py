# 网签相关功能

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from nowtime import nowtime, nowdaystr,nowday
from moudle import OnlineSignReprot, db,MailTo
from emailsend import onlinesignmail

onlinesign = Blueprint('onlinesign', __name__)


@onlinesign.route('/reportday', methods=['GET', 'POST'])
@login_required
def onlinesign_reportday():
    if request.method == 'POST':
        PROTJECT = list(range(10))
        PROTJECT[0] = request.values.get('PROTJECT_1')
        PROTJECT[1] = request.values.get('PROTJECT_2')
        PROTJECT[2] = request.values.get('PROTJECT_3')
        PROTJECT[3] = request.values.get('PROTJECT_4')
        PROTJECT[4] = request.values.get('PROTJECT_5')
        PROTJECT[5] = request.values.get('PROTJECT_6')
        PROTJECT[6] = request.values.get('PROTJECT_7')
        PROTJECT[7] = request.values.get('PROTJECT_8')
        PROTJECT[8] = request.values.get('PROTJECT_9')
        PROTJECT[9] = request.values.get('PROTJECT_10')
        CHECKTIME = nowtime()
        CYCEL = 'day'
        OnlineSignReprotday = OnlineSignReprot(PROTJECT_1=PROTJECT[0],
                                               PROTJECT_2=PROTJECT[1],
                                               PROTJECT_3=PROTJECT[2],
                                               PROTJECT_4=PROTJECT[3],
                                               PROTJECT_5=PROTJECT[4],
                                               PROTJECT_6=PROTJECT[5],
                                               PROTJECT_7=PROTJECT[6],
                                               PROTJECT_8=PROTJECT[7],
                                               PROTJECT_9=PROTJECT[8],
                                               PROTJECT_10=PROTJECT[9],
                                               PROTJECT_11='',
                                               CHECKTIME=CHECKTIME,
                                               CYCEL=CYCEL,
                                               EMAIL_STATE='0',
                                               USERNAME=current_user.USERNAME
                                               )
        try:
            db.session.add(OnlineSignReprotday)
            db.session.commit()
            try:
                info = list(range(2))
                info[0] = current_user.USERNAME
                info[1] = nowdaystr()
                to=MailTo.query.filter_by(MAIL_TYPE='网签日报').all()
                to_list = [to[i].MAIL_ADDR for i in range(len(to))]
                subject='网签运维日报'+nowday()
                #onlinesignmail(subject,to_list, PROTJECT, info)
                flash('邮件发送成功', 'task_keepsusscess')
                return redirect(url_for('onlinesign.onlinesign_reportday'))
            except (NameError, IndexError) as e:
                print(e)
                flash('保存成功发送失败', 'task_sendfail')
                return redirect(url_for('onlinesign.onlinesign_reportday'))
        except (NameError, IndexError) as e:
            print(e)
            flash('保存失败', 'task_keepfail')
            return redirect(url_for('onlinesign.onlinesign_reportday'))
    else:
        return render_template('onlinesign_reportday.html')
