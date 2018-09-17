import smtplib
from email.mime.text import MIMEText
from email.header import Header

def onlinesignmail(subject,to,project,info):
    HOST="smtp.qq.com"
    SUBJECT=subject
    TO=to
    FROM="3364343840@qq.com"
    htmltext="""
               <style>
    table {
        border-collapse: collapse;
    }
    
    table, td, th {
        border: 1px solid black;
    }
    </style>
    
    <table style="word-wrap:break-word; word-break:break-all;">
    
      <tr>
        <th>序号</th>
        <th>检查内容</th>
        <th width="200px">检查结果</th>
      </tr>
        <tr>
        <th colspan="3">网签系统可访问性检查</th>
      </tr>
      <tr>
        <td>1</td>
        <td>检查商品房网签系统(http://wq.cq315house.com/bdckfs/)是否可以正常访问；</td>
        <td>"""+project[0]+"""</td>
      </tr>
      <tr>
        <td>2</td>
        <td>登录存量房网签系统(http://esfwq.cq315house.com/bdckfs/)是否可以正常访问；</td>
        <td>"""+project[1]+"""</td>
      </tr>
        </tr>
        <tr>
        <th colspan="3">重庆市商品房交易监管金融接入平台管理系统检查</th>
      </tr>
        <tr>
        <td>3</td>
        <td>检查系统(10.0.145.50:7001/cqgtfw_access_web/user/login)是否可以正常访问、登录；</td>
        <td>"""+project[2]+"""</td>
      </tr>
        <tr>
        <td>4</td>
        <td>检查系统菜单是否空白、功能模块是否正常记载；</td>
        <td>"""+project[3]+"""</td>
      </tr>
        <tr>
        <td>5</td>
        <td>随机抽检系统功能是否正常，本次抽查认购信息表中的条件检索功能；</td>
        <td>"""+project[4]+"""</td>
      </tr>
        <tr>
        <td>6</td>
        <td>检查系统数据是否正常加载、实时更新；</td>
        <td>"""+project[5]+"""</td>
      </tr>
        <tr>
        <td>7</td>
        <td>检查系统历史登录记录(IP、时间)是否异常；</td>
        <td>"""+project[6]+"""</td>
      </tr>
        <tr>
        <td>8</td>
        <td>检查对账差错信息表中是否有差错账记录;</td>
        <td>"""+project[7]+"""</td>
      </tr>
         <tr>
        <td>9</td>
        <td>检查10.0.145.51服务器磁盘是否足够;</td>
        <td>"""+project[8]+"""</td>
      </tr>
         <tr>
        <td>10</td>
        <td>检查10.0.145.50服务器磁盘是否足够</td>
        <td>"""+project[9]+"""</td>
      </tr>
    </table>
     <div>
     <p style="line-height:50%">巡查时间：每天早上8：45-8：50</p>
     <p style="line-height:50%">巡检人："""+info[0]+"""</p>
     <p style="line-height:50%">检查时间："""+info[1]+"""</p>
 </div>
    
    """

    msg=MIMEText(htmltext,
                 "html","utf-8")
    msg['Subject']=SUBJECT
    msg['From']=FROM
    msg['TO']=','.join(to)


    server=smtplib.SMTP()
    server.connect(HOST,"25")
    server.starttls()
    server.login("3364343840@qq.com","ueynlpctsyxtciaa")
    server.sendmail(FROM,TO,msg.as_string())
    server.quit()
    print("发送成功")

#yrowjjjvcoglbhhf 78845906
#ueynlpctsyxtciaa 3364343840