# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topecs/items.html

import scrapy


# 商品级别的信息 
class ProductInfo(scrapy.Item):
    itemType = scrapy.Field()
    sourceItemId = scrapy.Field()
    sourceWebsite = scrapy.Field()
    sourceItemVersion = scrapy.Field()
    sourceUrl = scrapy.Field()
    brandName = scrapy.Field()
    categoryLevel1 = scrapy.Field()
    categoryLevel2 = scrapy.Field()
    itemName = scrapy.Field()
    gender = scrapy.Field()
    picList = scrapy.Field()
    sourceOriginalPrice = scrapy.Field()
    sourceSellingPrice = scrapy.Field()
    sourceCurrency = scrapy.Field()
    itemDetail = scrapy.Field()
    itemPicList = scrapy.Field()
    itemType = scrapy.Field()
    itemTag = scrapy.Field()


# sku级别信息 1个型号1个sku 
class SkuInfo(scrapy.Item):
    itemType = scrapy.Field()
    sourceSkuId = scrapy.Field()
    # 关联product 
    sourceItemId = scrapy.Field()
    sourceWebsite = scrapy.Field()
    sourceItemVersion = scrapy.Field()
    sourceUrl = scrapy.Field()
    # 品牌名
    brandName = scrapy.Field()
    # 原价 
    sourceOriginalPrice = scrapy.Field()
    # 现价 
    sourceSellingPrice = scrapy.Field()
    # 货币 
    sourceCurrency = scrapy.Field()
    # 库存
    sourceStock = scrapy.Field()
    ########### 属性 
    # 商品型号 xl xxl
    size = scrapy.Field()
    # 颜色
    color = scrapy.Field()
    colorPic = scrapy.Field()
    # 图片
    picList = scrapy.Field()

class ImageInfo(scrapy.Item):
    itemType = scrapy.Field()
    image_urls = scrapy.Field()
    image_paths = scrapy.Field()
    picType = scrapy.Field()
    sourceItemId = scrapy.Field()
    sourceWebsite = scrapy.Field()

# 性别信息 
class GenderInfo(scrapy.Item):
    # define the fields for your item here like:
    # 详情url 
    itemType = scrapy.Field()
    product_url = scrapy.Field()
    # 性别 男童 女童 baby 
    product_gender = scrapy.Field()


# url信息 
class UrlInfo(scrapy.Item):
    itemType = scrapy.Field()
    url = scrapy.Field()
    taskId = scrapy.Field()
    parentUrl = scrapy.Field()
    urlLevel = scrapy.Field()
    expectCnt = scrapy.Field()
    actualCnt = scrapy.Field()
    urlStatus = scrapy.Field()

# 日志信息 
class logInfo(scrapy.Item):
    itemType = scrapy.Field()
    logDetail = scrapy.Field()
    taskId = scrapy.Field()
    level = scrapy.Field()
    ip = scrapy.Field()
    url = scrapy.Field()
    urlId = scrapy.Field()
    sourceWebsite = scrapy.Field()


# 日志信息 
class stockInfo(scrapy.Item):
    itemType = scrapy.Field()
    code = scrapy.Field()
    day = scrapy.Field()
    query = scrapy.Field()
    value = scrapy.Field()
    openPrice = scrapy.Field()
    closePrice = scrapy.Field()
    maxPrice = scrapy.Field()
    minPrice = scrapy.Field()
    amount = scrapy.Field()


