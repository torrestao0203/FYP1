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


class SupermarketView(BaseView):
    default_view = 'supermarket'

    @expose('/supermarket/')
    def supermarket(self):
        return self.render_template('supermarket.html')
    
appbuilder.add_view_no_menu(SupermarketView())

class NursingCareView(BaseView):
    default_view = 'NursingCare'

    @expose('/NursingCare/')
    def NursingCare(self):
        return self.render_template('NursingCare.html')
    
appbuilder.add_view_no_menu(NursingCareView())

class SkinView(BaseView):
    default_view = 'Skin'

    @expose('/Skin/')
    def Skin(self):
        return self.render_template('Skin.html')
    
appbuilder.add_view_no_menu(SkinView())


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
    
    @expose('/DNF/')
    def DNF(self):
        param1 = 'Global News'
        self.update_redirect()
        return self.render_template('DNF.html', param1=param1)
    
    @expose('/SkinCare/')
    def SkinCare(self):
        param1 = 'Global News'
        self.update_redirect()
        return self.render_template('SkinCare.html', param1=param1)
    
    @expose('/Nursing/')
    def Nursing(self):
        param1 = 'Global News'
        self.update_redirect()
        return self.render_template('Nursing.html', param1=param1)
    
    @expose('/foodanddrink/')
    def foodanddrink(self):
        param1 = 'Global News'
        self.update_redirect()
        return self.render_template('foodanddrink.html', param1=param1)
    
    @expose('/toy/')
    def toy(self):
        param1 = 'Global News'
        self.update_redirect()
        return self.render_template('toy.html', param1=param1)
    
    @expose('/travel/')
    def travel(self):
        param1 = 'Global News'
        self.update_redirect()
        return self.render_template('travel.html', param1=param1)
    
    @expose('/furniture/')
    def furniture(self):
        param1 = 'Global News'
        self.update_redirect()
        return self.render_template('furniture.html', param1=param1)
    
    @expose('/computer/')
    def computer(self):
        param1 = 'Global News'
        self.update_redirect()
        return self.render_template('computer.html', param1=param1)

    @expose('/homeEL/')
    def homeEL(self):
        param1 = 'Global News'
        self.update_redirect()
        return self.render_template('homeEL.html', param1=param1)


    
db.create_all()

""" Page View """
appbuilder.add_view(NewsPageView, '零食甜品', href="/newspageview/DNF/", category="超級市場")
appbuilder.add_link('飲品', href="/newspageview/DNF/", category="超級市場")
appbuilder.add_link('水果蔬菜',href="/newspageview/DNF/", category="超級市場")

appbuilder.add_link("護膚用品", href="/newspageview/Nursing/", category="護理保健")
appbuilder.add_link("保健產品", href="/newspageview/Nursing/", category="護理保健")
appbuilder.add_link("化妝品", href="/newspageview/Nursing/", category="護理保健")

appbuilder.add_link("卸妝", href="/newspageview/SkinCare/", category="護膚化妝")
appbuilder.add_link("美甲護具", href="/newspageview/SkinCare/", category="護膚化妝")
appbuilder.add_link("男士專區", href="/newspageview/SkinCare/", category="護膚化妝")

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

appbuilder.add_link("洗衣機 雪櫃 冷氣機", href="/newspageview/computer/", category="大腦場")
appbuilder.add_link("美容儀器", href="/newspageview/computer/", category="大腦場")
appbuilder.add_link("智能家居設備", href="/newspageview/computer/", category="大腦場")


appbuilder.add_link("儲物收納", href="/newspageview/homeEL/", category="家居電器")
appbuilder.add_link("家居清潔", href="/newspageview/homeEL/", category="家居電器")
appbuilder.add_link("睡房", href="/newspageview/homeEL/", category="家居電器")

appbuilder.add_link("浴室", href="/newspageview/furniture/", category="家品傢俬")
appbuilder.add_link("廚具", href="/newspageview/furniture/", category="家品傢俬")
appbuilder.add_link("睡房", href="/newspageview/furniture/", category="家品傢俬")

appbuilder.add_link("必嚐美食", href="/newspageview/foodanddrink/", category="吃喝玩樂")
appbuilder.add_link("美容及健康服務", href="/newspageview/foodanddrink/", category="吃喝玩樂")
appbuilder.add_link("旅遊住宿", href="/newspageview/foodanddrink/", category="吃喝玩樂")

appbuilder.add_link("旅行用品", href="/newspageview/travel/", category="運動旅行")
appbuilder.add_link("行山裝備", href="/newspageview/travel/", category="運動旅行")
appbuilder.add_link("健身產品", href="/newspageview/travel/", category="運動旅行")

appbuilder.add_link("迪士尼", href="/newspageview/toy/", category="玩具圖書")
appbuilder.add_link("漫威", href="/newspageview/toy/", category="玩具圖書")
appbuilder.add_link("文具", href="/newspageview/toy/", category="玩具圖書")



""" Custom Views """
appbuilder.add_view(MenuItemView, "MenuItem", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(MenuCategoryView, "MenuCategory", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsView, "News", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsCategoryView, "NewsCategory", icon="fa-folder-open-o", category="Admin")

