import smtplib
import ssl

from django.core.mail.backends.smtp import EmailBackend as DjangoEmailBackend

'''
自定义邮箱后端
'''


class CustomEmailBackend(DjangoEmailBackend):
    def open(self):
        # 创建一个 SSL 上下文，并加载自定义的 CA 证书文件
        context = ssl.create_default_context(cafile='/etc/ssl/certs/ca-certificates.crt')
        # 注意：这里我们并没有指定客户端证书，因为 SMTP 客户端通常不需要证书来验证自己
        # 如果你的服务器要求客户端证书，那么这是一个更复杂的情况，通常需要使用其他库或方法

        # 创建一个 SMTP_SSL 对象，使用自定义的 SSL 上下文
        self.connection = smtplib.SMTP_SSL(self.host, self.port, context=context)
        # 如果需要，可以在这里添加登录代码（通常是在 open() 方法的后面部分）
        self.connection.login(self.username, self.password)
        return self.connection

    # 你可能还需要重写其他方法，比如 close()，但这取决于你的具体需求
