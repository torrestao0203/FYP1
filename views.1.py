from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import Employee,Department, Function, EmployeeHistory, Benefit, MenuItem, MenuCategory, News, NewsCategory
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app import appbuilder, db
from flask_appbuilder.baseviews import expose, BaseView
from flask import Flask, render_template, redirect, request, flash
from flask_appbuilder import AppBuilder, BaseView, expose, has_access
from flask_appbuilder.models.sqla.interface import SQLAInterface
from flask_appbuilder.security.decorators import has_access



def department_query():
    return db.session.query(Department)


class EmployeeHistoryView(ModelView):
    datamodel = SQLAInterface(EmployeeHistory)
    #base_permissions = ['can_add', 'can_show']
    list_columns = ['department', 'begin_date', 'end_date']


class EmployeeView(ModelView):
    datamodel = SQLAInterface(Employee)

    list_columns = ['full_name', 'department.name', 'employee_number']
    edit_form_extra_fields = {'department':  QuerySelectField('Department',
                                query_factory=department_query,
                                widget=Select2Widget(extra_classes="readonly"))}


    related_views = [EmployeeHistoryView]
    show_template = 'appbuilder/general/model/show_cascade.html'


class FunctionView(ModelView):
    datamodel = SQLAInterface(Function)
    related_views = [EmployeeView]


class DepartmentView(ModelView):
    datamodel = SQLAInterface(Department)
    related_views = [EmployeeView]


class BenefitView(ModelView):
    datamodel = SQLAInterface(Benefit)
    add_columns = ['name']
    edit_columns = ['name']
    show_columns = ['name']
    list_columns = ['name']

class MenuItemView(ModelView):
    datamodel = SQLAInterface(MenuItem)
    list_columns = ['id', 'name', 'link', 'menu_category_id']

class MenuCategoryView(ModelView):
    datamodel = SQLAInterface(MenuCategory)
    list_columns = ['id', 'name']

class NewsView(ModelView):
    datamodel = SQLAInterface(News)
    list_columns = ['id', 'title', 'content', 'date', 'newsCat_id']

class NewsCategoryView(ModelView):
    datamodel = SQLAInterface(NewsCategory)
    list_columns = ['id', 'name']

class NewsPageView(BaseView):
    default_view = 'local_news'

    @expose('/local_news/')
    def local_news(self):
        param1 = 'Local News'
        self.update_redirect()
        return self.render_template('news.html', param1 = param1)

    @expose('/global_news/')
    def global_news(self):
        param1 = 'Global News'
        self.update_redirect()
        return self.render_template('news.html', param1=param1)
        
    @expose('/zsam/')
    def zsam(self):
        param1 = 'Global News'
        self.update_redirect()
        return self.render_template('zsam.html', param1=param1)
        
    @expose('/myye/')
    def myye(self):
        param1 = 'Global News'
        self.update_redirect()
        return self.render_template('myye.html', param1=param1)
        
        
    @expose('/cwyp/')
    def cwyp(self):
        param1 = 'Global News'
        self.update_redirect()
        return self.render_template('cwyp.html', param1=param1)
    


db.create_all()

""" Page View """
appbuilder.add_view(NewsPageView, 'Local News', category="超級市場")
appbuilder.add_link("Global News", href="/newspageview/hlpk/", category="護理保健")
appbuilder.add_link("Global NewsTEST", href="/newspageview/hffc/", category="護膚化妝")
appbuilder.add_link("時尚服飾", href="/newspageview/zsam/", category="直送澳門")
appbuilder.add_link("玩具圖書", href="/newspageview/zsam/", category="直送澳門")
appbuilder.add_link("超級市場", href="/newspageview/zsam/", category="直送澳門")
appbuilder.add_link("嬰兒奶粉", href="/newspageview/myye/", category="母嬰育兒")
appbuilder.add_link("身體清潔", href="/newspageview/myye/", category="母嬰育兒")
appbuilder.add_link("奶樽", href="/newspageview/myye/", category="母嬰育兒")
appbuilder.add_link("母乳餵哺用品", href="/newspageview/myye/", category="母嬰育兒")
appbuilder.add_link("嬰兒醫療", href="/newspageview/myye/", category="母嬰育兒")
appbuilder.add_link("狗狗專區", href="/newspageview/cwyp/", category="寵物用品")
appbuilder.add_link("貓貓專區", href="/newspageview/cwyp/", category="寵物用品")
appbuilder.add_link("其他寵物專區", href="/newspageview/cwyp/", category="寵物用品")
appbuilder.add_link("水族用品", href="/newspageview/cwyp/", category="寵物用品")
appbuilder.add_link("寵物家居清潔", href="/newspageview/cwyp/", category="寵物用品")

appbuilder.add_link("Global NewsTEST", href="/newspageview/tnc/", category="大腦場")
appbuilder.add_link("Local NewsTEST", href="/newspageview/kkdk/", category="家居電器")
appbuilder.add_link("Local NewsTEST", href="/newspageview/kpks/", category="家品傢俬")

appbuilder.add_link("必嚐美食", href="/newspageview/foodanddrink/", category="吃喝玩樂")
appbuilder.add_link("美容及健康服務", href="/newspageview/foodanddrink/", category="吃喝玩樂")
appbuilder.add_link("旅遊住宿", href="/newspageview/foodanddrink/", category="吃喝玩樂")
appbuilder.add_link("旅行用品", href="/newspageview/travel/", category="運動旅行")
appbuilder.add_link("行山裝備", href="/newspageview/travel/", category="運動旅行")
appbuilder.add_link("健身產品", href="/newspageview/travel/", category="運動旅行")
appbuilder.add_link("迪士尼", href="/newspageview/toy/", category="玩具圖書")
appbuilder.add_link("漫威", href="/newspageview/toy/", category="玩具圖書")
appbuilder.add_link("教科書", href="/newspageview/toy/", category="玩具圖書")



""" Custom Views """
appbuilder.add_view(MenuItemView, "MenuItem", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(MenuCategoryView, "MenuCategory", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsView, "News", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsCategoryView, "NewsCategory", icon="fa-folder-open-o", category="Admin")

