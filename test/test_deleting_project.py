import time
import random
from model.project import Project

def test_deleting_project(app):
    very_new_project = Project(name=app.generator.random_name_of_project("start", 7))
    app.session.login("administrator", "root")
    app.project.manage_click()
    app.project.open_all_projects()
    if len(app.project.list_of_projects()) == 0:
        app.project.adding_project(very_new_project.name)
    time.sleep(3)
    old_projects = app.soap.get_list_of_projects(app.config["webadmin"]["username"], app.config["webadmin"]["password"])
    project = random.choice(old_projects)
    app.project.deleting_project(project.name)
    new_projects = app.soap.get_list_of_projects(app.config["webadmin"]["username"], app.config["webadmin"]["password"])
    old_projects.remove(project)
    assert old_projects == new_projects
