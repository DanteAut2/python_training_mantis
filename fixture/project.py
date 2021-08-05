class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def adding_project(self):
        wd = self.app.wd
        self.open_all_projects()
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys("abyrvalg")
        wd.find_element_by_css_selector("input.button").click()

    def open_all_projects(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
        if not len(wd.find_elements_by_xpath("//input[@value='Create New Project']")) > 0:
            wd.find_element_by_link_text("Manage Projects").click()

    def deleting_project(self):
        wd = self.app.wd
        self.open_all_projects()
        wd.find_element_by_link_text("abyrvalg").click()
        wd.find_element_by_css_selector("form > input.button").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_css_selector("input.button").click()