
import jenkinsapi

class JenkinsApi:

    def __init__(self):
        self.jenkins_url = "http://localhost:8080"
        self.username = "xxx"
        self.password = "xxx"
        self.jsever = jenkinsapi.api

    def get_build(self,jobname):
        return self.jsever.get_latest_build(self.jenkins_url, jobname, username=self.username, password=self.password)

    # todo 获取Jenkinsjob最新的noid
    def get_last_build_no(self,jobname):
        return self.get_build(jobname).buildno

    # todo 获取Jenkinsjob最新的状态
    def get_last_build_status(self,jobname):
        return self.get_build(jobname).get_status()

if __name__ == '__main__':
    J = JenkinsApi()
    print(J.get_last_build_no("apitest"))
    print(J.get_last_build_status("apitest"))







