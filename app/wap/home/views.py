# -*- coding: utf-8 -*-
__author__ = 'liuxu'
__date__ = '2019/5/27 9:40'
from  flask import render_template, request
from . import home
from app.models.product_models import Classification,Products,Orders


@home.route('/')
@home.route('/<int:page>')
def index(page=1):
        # 分类数据提取
        classification = Classification.query.all()
        # 商品数据提取
        goods = Products.query.paginate(page, per_page=page*10)
        return render_template('wap/wap_home.html', classification=classification, goods=goods)


@home.route('/detail/<id>')
def detail(id=0):
        return render_template('wap/wap_detail.html')


@home.route('/category/<int:id>')
def category(id):
        return render_template('wap/wap_category.html')


@home.route('/local')
def local(id):
        return '本地页面'


@home.route('/Personal')
def Personal(id):
        return '个人中心页'