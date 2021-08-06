def test_sign_up_new_account(app):
    username = app.generator.random_name_of_project("start", 7)
    password = "test"
    app.james.ensure_user_exists(username, password)