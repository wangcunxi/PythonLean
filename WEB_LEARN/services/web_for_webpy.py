import web

urls = (
    '/index', 'Index',
    '/login', 'PostFormRespone',
    '/(.*)', 'TempleHtml'
)
app = web.application(urls, globals())

class TempleHtml:
    def GET(self, name):
        data = web.input()
        print('hello',data,name)
        return open(r'./template/index.html').read()

class Index:
    def GET(self):
        query = web.input()
        print('index query',query)
        return query

class PostFormRespone:
    def POST(self):
        data = web.input()
        print('blog data',data.id)
        web.header('Content-Type', 'text/html;charset=UTF-8')
        return data

if __name__ == "__main__":
    app.run()