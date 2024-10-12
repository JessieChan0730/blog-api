<p align="center">
	<img src="https://img.shields.io/badge/python-3.12.0-red">
    <img src="https://img.shields.io/badge/DRF-3.15.1-red">
	<img src="https://img.shields.io/badge/Django-5.0.6-brightgreen">
	<img src="https://img.shields.io/badge/simplejwt-2.8.0-brightgreen">
	<img src="https://img.shields.io/badge/simplejwt-1.21.7-brightgreen">
	<img src="https://img.shields.io/badge/license-MIT-blue">
</p>

![](https://foruda.gitee.com/images/1708618984641188532/a7cca095_716974.png "rainbow.png")

## 🙂 简介

基于Django5开发的博客系统，此仓库为「博客系统的后端接口」，目前博客处于起步阶段，很多功能暂未开发，当然此项目会持续维护，大部分功能会在后续版本中更新，如果喜欢的话不妨点个start支持

前台仓库：https://github.com/JessieChan0730/blog-view  
后台仓库：https://github.com/JessieChan0730/blog-admin

## 🔨 相关库与框架

1. 核心框架：[Django](https://github.com/django/django)
2. Token库：[django-rest-framework-simplejwt](https://github.com/jazzband/djangorestframework-simplejwt)
3. RestApi：[django-rest-framework](https://github.com/encode/django-rest-framework/tree/master)
4. Api文档：[drf-yasg](https://github.com/axnsan12/drf-yasg)

## 🚀 服务启动

1. 安装依赖 `pip install -r requirements.txt`
2. 在 dev.py 中配置好您的数据库信息(`DATABASES`中)，并且执行 `python manage.py migrate` 迁移到您的数据库；
3. 在dev.py 配置博客的相关配置(`BLOG_SETTINGS`中)，如果无其他需求，此配置默认即可，随后执行 `python manage.py init_blog`
4. 创建用户，执行 `python manage.py createsuperuser`，输入用户名，密码邮箱等，即可创建唯一的管理员用户，随后后台使用此用户名，密码登录即可。

## ⚙ 相关配置

配置文件由Django原本项目的单文件，拆分为了两个文件，`dev.py` `prod.py`，其中 `BLOG_SETTINGS` `SUPER_USER_SETTINGS`
为此blog项目自定义配置，其余都为Django框架本身的配置。

1. BLOG_SETTINGS

> 在此闭包下有分为三大闭包分别为：`FRONT_SETTING` `ADMIN_SETTING` `COMMON_SETTING`
> ，分别用于控制客户端，后台以及通用的行为。在三大闭包下面又分为：`BLOG`，`CATEGORY`
> 等等，这些闭包代表了不同模块，例如`CATEGORY`
> 中其实就是配置了分类模块的行为。闭包下大概分为下几种配置：

- `WEBSITE_TITLE`：网站的标题信息
- `WEBSITE_COVER`：客户端网页封面，如需配置，请将图片放入到`media`文件夹下，并且值设置为为`/media/图片全称`
- `WEBSITE_LOGO`：后台网站Logo信息，如需配置，请按照`WEBSITE_COVER`一样的方式配置
- `RECORD_INFO`：网站备案信息
- `COPYRIGHT`：网站版权信息
- `PAGE_SIZE`：分页每页展示的数量
- `MAX_PAGE_SIZE`：分页每页最大展示数量
- `VISIBLE_MAX_NUM`：最多可显示数量
- `QUOTE_MAX_NUM`：最多可引用数量
- `RECOMMEND_MAX_NUM`：最多可推荐数量

> 当使用`python manage.py init_blog`命令时，这些配置的数据会被写入到数据库。

2. SUPER_USER_SETTINGS

> 此配置用于配置博客管理员相关信息

- `nickname`：用于指定管理员昵称信息
- `signature`：用于指定管理员个性签名信息
- `avatar`：用于指定管理员头像信息，操作同`WEBSITE_COVER`配置一样
- `hobby`：用于指定管理员爱好信息，分为 `name` 爱好名称，`detail` 爱好详情
- `media`：用于指定管理员相关社区媒体的信息，指定相关链接即可

> 当使用 `python manage.py createsuperuser`时，以上配置的数据会被写入到数据库中。

3. EMAIL

> 此项目具有`服务异常通知`，`友链审核通过通知的功能`，这些功能需要邮箱来支持，在dev中，请配置如下内容

```python
EMAIL_HOST = 'smtp.qq.com'  # 邮箱服务器地址，这里为QQ邮箱
EMAIL_PORT = 465  # SMTP服务端口号
EMAIL_HOST_USER = '您的邮箱(xxxxx@qq.com)'  # 发送者邮箱号，最好与管理员（superuser）注册时邮箱不同
EMAIL_HOST_PASSWORD = 'qq邮箱授权码'  # 邮箱授权码
DEFAULT_FROM_EMAIL = 'xxxxx@qq.com'  # 邮箱显示的发送者邮箱
EMAIL_USE_SSL = True  # 是否启用SSL
```

> 具体邮箱授权码获取规则请查看此博客：[查看邮箱授权码](https://blog.csdn.net/KaiSarH/article/details/116724290)

## 💡 注意事项

- MySQL
  确保数据库字符集为utf8mb4,否则在后端插入emoji表情时，会产生数据库的插入数据的错误，具体设置请查看：[解决方案](https://blog.csdn.net/weixin_37989267/article/details/89019647)
- 确保当前依赖版本不会改变，请勿升级或者降低依赖库版本
- 自定义设置如果没有需求可以无需更改，在后台中可以通过设置界面进行更改
- prod.py是用于生产环境，当修改了dev.py文件时，请自行同步的此文件内容

## 📈 下一步计划

- [ ] 评论功能
- [ ] 系统日志

## 🌹 致谢

感谢提供支持的相关开源库和框架，也感谢您对此项目的支持。如果您对此项目还满意，不妨点一个Star，这对我来说很重要。

## 📑 LICENSE

[MIT](https://github.com/JessieChan0730/blog-api/blob/main/LICENSE)