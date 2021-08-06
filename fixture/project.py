from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def adding_project(self, very_new_project):
        wd = self.app.wd
        wd.find_element_by_xpath("//input[@value='Create New Project']").click()
        wd.find_element_by_name("name").click()
        wd.find_element_by_name("name").clear()
        wd.find_element_by_name("name").send_keys(very_new_project)
        wd.find_element_by_css_selector("input.button").click()

    def open_all_projects(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage Projects").click()

    def deleting_project(self, project):
        wd = self.app.wd
        wd.find_element_by_xpath("//a[contains(text(),'" + project + "')]")
        wd.find_element_by_css_selector("form > input.button").click()
        wd.find_element_by_xpath("//input[@value='Delete Project']").click()
        wd.find_element_by_css_selector("input.button").click()

    def list_of_projects(self):
        wd = self.app.wd
        self.projects_list = []
        elements = wd.find_elements_by_xpath("/html/body/table[3]/tbody/tr")
        for element in elements:
            if element.get_attribute("class") not in ('', 'row-category'):
                cells = element.find_elements_by_tag_name("td")
                name = cells[0].text
                self.projects_list.append(Project(name=name))
        return list(filter(None, self.projects_list))

    def manage_click(self):
        wd = self.app.wd
        wd.find_element_by_link_text("Manage").click()
