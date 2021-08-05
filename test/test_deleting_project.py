def test_deleting_project(app):
    app.session.login("administrator", "root")
    app.project.manage_click()
    app.project.open_all_projects()
    if len(app.project.list_of_projects()) == 0:
        app.project.adding_project()
    app.project.deleting_project()
