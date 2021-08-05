def test_adding_project(app):
    app.session.login("administrator", "root")
    app.project.manage_click()
    app.project.open_all_projects()
    app.project.adding_project()

