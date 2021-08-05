def test_deleting_project(app):
    app.session.login("administrator", "root")
    app.project.open_all_projects()
    app.project.deleting_project()
