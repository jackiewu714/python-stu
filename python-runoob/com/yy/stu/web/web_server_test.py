#_*_ coding:utf-8 _*_
import os, subprocess;
import types;
from http.server import BaseHTTPRequestHandler, HTTPServer;

#-----------------------------------------------------------------------------------
class ServerException(Exception):
    "服务器内部错误"
    pass;

#-----------------------------------------------------------------------------------
class BaseCase(object):
    "条件处理基类"
    def handle_file(self, handler, fullPath):
        try:
            with open(fullPath, "rb") as reader:
                content = reader.read();
            handler.send_content(content);
        except IOError as msg:
            msg = "'{0}' can't be read: {1}".format(fullPath, msg);
            handler.handle_error(msg);

    def index_path(self, handler):
        return os.path.join(handler.fullPath, "index.html");

    def test(self, handler):
        assert False, 'Not implementd method test(...)';

    def act(self, handler):
        assert False, 'Not implementd method act(...)';

#-----------------------------------------------------------------------------------
class CaseNoFile(BaseCase):
    "文件或者目录不存在"
    def test(self, handler):
        return not os.path.exists(handler.fullPath);

    def act(self, handler):
        raise ServerException("'{0}' not found".format(handler.path));

#-----------------------------------------------------------------------------------
class CaseCgiFile(BaseCase):
    "可执行脚本"
    def run_cgi(self, handler):
        data = subprocess.check_output(["python", handler.fullPath]);
        handler.send_content(data);

    def test(self, handler):
        return os.path.isfile(handler.fullPath) and handler.fullPath.endswith(".py");

    def act(self, handler):
        self.run_cgi(handler);

#-----------------------------------------------------------------------------------
class CaseExistingFile(BaseCase):
    "文件存在的情况"
    def test(self, handler):
        return os.path.isfile(handler.fullPath);

    def act(self, handler):
        self.handle_file(handler, handler.fullPath);

#-----------------------------------------------------------------------------------
class CaseDirectoryIndexFile(BaseCase):
    "在根路径下返回主页文件"
    def test(self, handler):
        return os.path.isdir(handler.fullPath) and os.path.isfile(self.index_path(handler));

    def act(self, handler):
        self.handle_file(handler, self.index_path(handler));

#-----------------------------------------------------------------------------------
class CaseAlwaysFail(BaseCase):
    "默认处理"
    def test(self, handler):
        return True;

    def act(self, handler):
        raise ServerException("Unknow object '{0}'".format(handler.path));

#-----------------------------------------------------------------------------------
class RequestHandler(BaseHTTPRequestHandler):
    "处理请求并返回页面(请求路径合法则返回相应处理，否则返回错误页面)"
    caseList = [CaseNoFile(),
             CaseCgiFile(),
             CaseExistingFile(),
             CaseDirectoryIndexFile(),
             CaseAlwaysFail()];

    # Page = '''<html><body><p>Hello, web!</p></body></html>''';
    Page = '''\
    <html>
    <body>
    <table>
    <tr>  <td>Header</td>         <td>Value</td>          </tr>
    <tr>  <td>Date and time</td>  <td>{date_time}</td>    </tr>
    <tr>  <td>Client host</td>    <td>{client_host}</td>  </tr>
    <tr>  <td>Client port</td>    <td>{client_port}</td> </tr>
    <tr>  <td>Command</td>        <td>{command}</td>      </tr>
    <tr>  <td>Path</td>           <td>{path}</td>         </tr>
    </table>
    </body>
    </html>
    ''';

    #错误页面模板
    errorPage = """
        <html>
            <body>
                <h1>Error accessing {path}</h1>
                <p>{msg}</p>
            </body>
        </html>
    """;


    # 处理一个GET请求
    def do_GET(self):
        print("request path: ", self.path);
        try:
            #得到完整的请求路径
            self.fullPath = os.getcwd() + self.path;

            for case in self.caseList:
                if case.test(self):
                    case.act(self);
                    break;
        #处理异常
        except Exception as msg:
            print("Exception, msg:", msg);
            self.handle_error(msg);

    def create_page(self):
        "待实现"
        values = {
            'date_time' : self.date_time_string(),
            'client_host' : self.client_address[0],
            'client_port' : self.client_address[1],
            'command' : self.command,
            'path' : self.path
        }
        page = self.Page.format(**values);
        return page;

    def handle_error(self, msg):
        content = self.errorPage.format(path=self.path, msg=msg);
        self.send_content(content, 404);

    def send_content(self, content, status=200):
        print("contentType={1}, content: {0}".format(content, type(content)));
        self.send_response(status);
        self.send_header("Content-Type", "text/html");
        self.send_header("Content-Length", str(len(content)));
        self.end_headers();

        if isinstance(content, str):    # 判断内容若为字符串
            self.wfile.write(content.encode("utf-8"));
        elif type(content) is bytes:    # 判断内容若为字节
            self.wfile.write(content);
        else:
            self.wfile.write("Error content type.")


if __name__ == '__main__':
    serverAddress = ('localhost', 8080);
    print("start up http server: ", serverAddress);
    server = HTTPServer(serverAddress, RequestHandler);
    server.serve_forever();



