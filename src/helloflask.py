"""所有的flask程序都必须创建一个程序实例
    The flask object implements a WSGI application and acts as the central
    object.  It is passed the name of the module or package of the
    application.  Once it is created it will act as a central registry for
    the view functions, the URL rules, template configuration and much more.

    The name of the package is used to resolve resources from inside the
    package or the folder the module is contained in depending on if the
    package parameter resolves to an actual python package (a folder with
    an `__init__.py` file inside) or a standard module (just a `.py` file).

    For more information about resource loading, see :func:`open_resource`.

    Usually you create a :class:`Flask` instance in your main module or
    in the `__init__.py` file of your package like this::

        from flask import Flask
        app = Flask(__name__)

    .. admonition:: About the First Parameter

        The idea of the first parameter is to give Flask an idea what
        belongs to your application.  This name is used to find resources
        on the file system, can be used by extensions to improve debugging
        information and a lot more.

        So it's important what you provide there.  If you are using a single
        module, `__name__` is always the correct value.  If you however are
        using a package, it's usually recommended to hardcode the name of
        your package there.

        For example if your application is defined in `yourapplication/app.py`
        you should create it with one of the two versions below::

            app = Flask('yourapplication')
            app = Flask(__name__.split('.')[0])

        Why is that?  The application will work even with `__name__`, thanks
        to how resources are looked up.  However it will make debugging more
        painful.  Certain extensions can make assumptions based on the
        import name of your application.  For example the Flask-SQLAlchemy
        extension will look for the code in your application that triggered
        an SQL query in debug mode.  If the import name is not properly set
        up, that debugging information is lost.  (For example it would only
        pick up SQL queries in `yourapplication.app` and not
        `yourapplication.views.frontend`)
"""
from flask.ext.script import Manager
from flask import Flask
app = Flask(__name__)

""""    处理url和函数之间的关系的程序称为路由，定义路由最简单的方式为app.route修饰器
        A decorator that is used to register a view function for a
        given URL rule.  This does the same thing as :meth:`add_url_rule`
        but is intended for decorator usage::

            @app.route('/')
            def index():
                return 'Hello World'
"""


@app.route('/')
def index():
    return '<h1>Hello LiuJun!</h1>'

# 比如/user/<int:id>，支持int，float，path类型，默认为字符串
@app.route('/user/<name>')
def user(name):
    return '<h1>Hello %s!</h1>' % name
# 处理url动态，用<>把动态部分括起来，flask会把动态部分作为参数传递给函数，动态部分支持类型定义，


manager =Manager(app)

#启动服务器，使用run方法
if __name__ == '__main__':
    manager.run()





