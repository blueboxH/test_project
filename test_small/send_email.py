import smtplib
from email.header import Header
from email.mime.text import MIMEText
from email.utils import formataddr, parseaddr


def send_email(message, Subject:'邮件主题' ='GBI爬虫出现必须需主动处理的bug', receiver:'可以多个收件人'={'18570367466@163.com': '何涛', '17705592986@163.com': 'copy'},
               sender={'robothetao@sina.com': 'GBI爬虫'}, password='123456987', smtp_server='smtp.sina.com', ):
    if not (isinstance(receiver, dict) and isinstance(sender, dict)):
        print('receiver and sender must be dict')
        return

    def _format_addr(s, only_addr = False):
        datas = []
        if only_addr:
            datas = list(s.keys())
        else:
            for k, v in s.items():
                name, addr = parseaddr('{} <{}>'.format(v, k))
                datas.append(formataddr((Header(name, 'utf-8').encode(), addr)))
            datas = ','.join(datas)

        if len(datas) == 1:
            return datas[0]
        else:
            return datas

    try:
        msg = MIMEText(message, 'plain', 'utf-8')
        msg['From'] = _format_addr(sender)
        msg['to'] = _format_addr(receiver)
        msg['Subject'] = Header(Subject, 'utf-8').encode()

        server = smtplib.SMTP(smtp_server, 25)
        # 日志
        # server.set_debuglevel(1)
        server.login(_format_addr(sender, True), password)
        server.sendmail(_format_addr(sender, True), _format_addr(
            receiver, True), msg.as_string())
        server.quit()
    except Exception as err:
        print('send_email failed')


send_email('1')
