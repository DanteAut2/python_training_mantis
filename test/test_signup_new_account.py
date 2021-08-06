def test_sign_up_new_account(app):
    username = app.generator.random_name_of_project("start", 7)
    password = "test"
    email = username + "@localhost"
    app.james.ensure_user_exists(username, password)
    app.signup.new_user(username, email, password)
    app.session.login(username, password)
    assert app.session.is_logged_in_as(username)
    app.session.logout()