from suds.client import Client
from suds import WebFault
from model.project import Project

class SoapHelper:
    def __init__(self, app):
        self.app = app

    def can_login(self, username, password):
        client = Client(self.app.baseUrl + "/api/soap/mantisconnect.php?wsdl")
        try:
            client.service.mc_login(username, password)
            return True
        except WebFault:
            return False

    def get_list_of_projects(self, username, password):
        list_of_projects = []
        client = Client(self.app.baseUrl + "/api/soap/mantisconnect.php?wsdl")
        try:
            projects = client.service.mc_projects_get_user_accessible(username, password)
            for prj in projects:
                list_of_projects.append(Project(name=prj.name))
            return list_of_projects
        except WebFault:
            return False