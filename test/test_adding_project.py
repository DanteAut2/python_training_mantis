from model.project import Project
import time

def test_adding_project(app):
    very_new_project = Project(name=app.generator.random_name_of_project("start", 7))
    app.session.login("administrator", "root")
    app.project.manage_click()
    app.project.open_all_projects()
    old_projects = app.soap.get_list_of_projects("administrator", "root")
    app.project.adding_project(very_new_project.name)
    time.sleep(3)
    new_projects = app.soap.get_list_of_projects("administrator", "root")
    old_projects.append(very_new_project)
    assert sorted(old_projects, key=Project.sorted_name) == sorted(new_projects, key=Project.sorted_name)

