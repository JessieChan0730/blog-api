system_role_prompt = '''
用户将提供一篇博客文本（只需要关注其中文本内容即可），请尝试找出博客中可以改进的内容或者表达错误的地方，并且解析出 "type", "original", "suggest"，并且以JSON形式输出。其中 "type" 分为两个等级，"warning","error"
其中"warning"代表文章中存在可以改进的内容，"error"代表文章中存在的错误。

输入示例:
标题：<h1>Python基础知识</h1>
内容：Python是诞生于2000年2月20日的欧洲......

输出示例:
"results": [
    {
        "type": "error"
        "original": "Python是诞生于2000年2月20日的欧洲",
        "suggest": "Python是诞生于1991年2月20日"
    },
    {
        "type": "warning"
        "original": "Python是诞生于2000年2月20日的欧洲",
        "suggest": "Python于1991年2月20日诞生在荷兰"
    }
]
'''


def user_role_content(title: str, content: str):
    return f'''
       标题：{title}\n
       内容：{content}    
    '''
