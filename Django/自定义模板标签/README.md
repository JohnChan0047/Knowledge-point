# 自定义模板标签例子
整理来自[https://www.zmrenwu.com/post/12/](https://www.zmrenwu.com/post/12/)
## 模板标签目录结构
首先在我们的 blog 应用下创建一个 templatetags 文件夹。然后在这个文件夹下创建一个 __init__.py 文件，使这个文件夹成为一个 Python 包，之后在 templatetags\ 目录下创建一个 blog_tags.py 文件，这个文件存放自定义的模板标签代码。  
  
  此时你的目录结构应该是这样的：
```
blog\
    __init__.py
    admin.py
    apps.py
    migrations\
        __init__.py
    models.py
    static\
    templatetags\
        __init__.py
        blog_tags.py
    tests.py
    views.py
```
## 编写模板标签代码
接下来就是编写各个模板标签的代码了，自定义模板标签代码写在 blog_tags.py 文件中。其实模板标签本质上就是一个 Python 函数，因此按照 Python 函数的思路来编写模板标签的代码就可以了，并没有任何新奇的东西或者需要新学习的知识在里面。
```
from django import template
from ..models import Post

register = template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return Post.objects.all().order_by('-created_time')[:num]
```
## 使用自定义的模板标签
打开 base.html，为了使用模板标签，我们首先需要在模板中导入存放这些模板标签的模块，这里是 blog_tags.py 模块。当时我们为了使用 static 模板标签时曾经导入过 {% load staticfiles %}，这次在 {% load staticfiles %} 下再导入 blog_tags：
```
templates/base.html

{% load staticfiles %}
{% load blog_tags %}
<!DOCTYPE html>
<html>
...
</html>
```
然后找到最新文章列表处，把里面的列表修改一下：
```
templates/base.html

<div class="widget widget-recent-posts">
  <h3 class="widget-title">最新文章</h3>
  {% get_recent_posts as recent_post_list %}
  <ul>
    {% for post in recent_post_list %}
    <li>
      <a href="{{ post.get_absolute_url }}">{{ post.title }}</a>
    </li>
    {% empty %}
    暂无文章！
    {% endfor %}
  </ul>
</div>
```
## 注意
如果你按照教程的步骤做完后发现报错，请按以下顺序检查
1. 检查目录结构是否正确。确保 templatetags\ 位于 blog\ 目录下，且目录名必须为 templatetags。具体请对照上文给出的目录结构。
1. 确保 templatetags\ 目录下有 __init__.py 文件。
1. 确保使用的 Django 版本不小于 1.9。
1. 确保通过 register = template.Library() 和 @register.simple_tag 装饰器将函数装饰为一个模板标签。
1. 确保在使用模板标签以前导入了 blog_tags，即 {% load blog_tags %}。注意要在使用任何 blog_tags 下的模板标签以前导入它。
1. 确保模板标签的语法使用正确，即 {% load blog_tags %}，注意 { 和 % 以及 % 和 } 之间没有任何空格