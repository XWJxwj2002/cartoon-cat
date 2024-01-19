#-*- coding: utf-8 -*-

import cartoon_cat as cc

if __name__ == '__main__':

    # 一拳超人
    site = 'https://rouman5.com/books/55a4a769-296a-457c-b718-d9e47a107a38/126'

    crawler = cc.CartoonCat(
        site=site,                                  # 漫画首页
        begin=0,                                    # 起始章节
        end=-1,                                     # 结束章节
        save_folder='./download',                   # 保存路径，不存在会自动创建
        browser=cc.BrowserType.CHROME,              # 浏览器类型：FIREFOX，CHROME，SAFARI，IE，PHANTOMJS
        driver='./chromedriver.exe'                 # 驱动程序路径，firefox不需要
    )
    crawler.start()

