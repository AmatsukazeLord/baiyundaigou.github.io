import web

urls = (
    '/wx', 'Handle',
)


class Handle(object):

    def GET(self):
        getRealIP = web.ctx.env.get('HTTP_X_REAL_IP')

        # getIp = web.ctx.ip

        getAll = web.ctx.env

        return getAll, getRealIP
        # return "hello, this is handle view"


if __name__ == '__main__':
    app = web.application(urls, globals())
    app.run()
