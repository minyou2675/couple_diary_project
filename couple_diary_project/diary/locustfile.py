from locust import HttpUser, task, between, TaskSet
from requests.auth import HTTPBasicAuth


#유저 객체 생성
class WebsiteTestUser(HttpUser):
    wait_time = between(1, 2.5) 
    def on_start(self):
        return self.login()
    
    def login(self):
        self.client.post("/user/login/",{'username':'kym2675','password':'dbals3319','test-mode' : 'locust-test'})
    
         
    @task
    def dailyQuestion(self):
        self.client.get("/dailyquestion/")
    
    @task
    def my_task(self):
        self.client.get("/questionlist/1")   

        
