
DROP TABLE IF EXISTS `product`;
CREATE TABLE IF NOT EXISTS `product` (
  `product_id` int(10) NOT NULL auto_increment COMMENT '产品id',
  `source_product_id` varchar(64) NOT NULL COMMENT '来源网站的product id',
  `source_website` varchar(64) NOT NULL COMMENT '来源网站',
  `brand_id` int(10) unsigned NOT NULL COMMENT '品牌id，关联brand数据表',
  `category_id` int(10) unsigned COMMENT '分类id,关联category数据表',
  `product_name` varchar(256) NOT NULL COMMENT '展示名称',
  `product_name_ch` varchar(256) NOT NULL COMMENT '展示中文名称',
  `gender` varchar(64) NOT NULL COMMENT 'boy,girl,baby 可以有多个属性，json',
  `pic_list` mediumtext COMMENT '图片列表，json',
  `source_original_price` float NOT NULL COMMENT '原网站原价',
  `source_selling_price` float NOT NULL COMMENT '原网站销售价',
  `source_currency` varchar(16) NOT NULL COMMENT '原网站货币',
  `product_detail` mediumtext COMMENT '产品描述',
  `product_type` mediumtext COMMENT '产品类型',
  `product_tag` mediumtext COMMENT '产品标签',
  `bbt_original_price` float COMMENT '棒棒糖原价',
  `bbt_selling_price` float COMMENT '棒棒糖销售价',
  `color_list` mediumtext COMMENT '颜色列表，关联color数据表，颜色名称、颜色图片，json',
  `size_list` mediumtext COMMENT '尺寸列表，关联size数据表，尺码、年龄、网站，json',
  `sku_list` mediumtext COMMENT 'sku列表，关联sku数据表，json',
  `supplier` varchar(64) default NULL  COMMENT '供应商',
  `ext_info` mediumtext COMMENT '保留字段',
  `version_id` int(10) unsigned COMMENT '版本号',
  `create_time` timestamp NOT NULL default '0000-00-00 00:00:00' COMMENT '创建时间',
  `update_time` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY  (`product_id`),
  UNIQUE KEY `product_index` (`product_id`,`version_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=100000 ;

DROP TABLE IF EXISTS `sku`;
CREATE TABLE IF NOT EXISTS `sku` (
  `sku_id` int(10) NOT NULL auto_increment COMMENT 'sku ID',
  `product_id` int(10) unsigned  NOT NULL COMMENT '产品id，关联product数据表',
  `source_sku_id` varchar(64) NOT NULL COMMENT '来源网站的sku id',
  `size_id` int(10) unsigned NOT NULL COMMENT '尺码id，关联size数据表',
  `color_id` int(10) unsigned NOT NULL COMMENT '颜色id,关联color数据表',
  `source_original_price` float NOT NULL COMMENT '原网站原价',
  `source_selling_price` float NOT NULL COMMENT '原网站销售价',
  `source_currency` varchar(16) NOT NULL COMMENT '原网站货币',
  `bbt_original_price` float COMMENT '棒棒糖原价',
  `bbt_selling_price` float COMMENT '棒棒糖销售价',
  `available_stock` int(5) unsigned COMMENT '可用库存数量',
  `real_stock` int(5) unsigned COMMENT '实际库存数量',
  `pipeline_stock` int(5) unsigned COMMENT '在途库存数量',
  `virtual_stock` int(5) unsigned COMMENT '虚库存数量',
  `detail` mediumtext COMMENT '商品描述',
  `tag` varchar(128) default NULL  COMMENT '标签',
  `weight` int(5) unsigned COMMENT '估计重量(克)',
  `ext_info` mediumtext COMMENT '保留字段',
  `version_id` int(10) unsigned COMMENT '版本号',
  `create_time` timestamp NOT NULL default '0000-00-00 00:00:00' COMMENT '创建时间',
  `update_time` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY  (`sku_id`),
  UNIQUE KEY `sku_index` (`source_sku_id`,`version_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=100000 ;

DROP TABLE IF EXISTS `sku_color`;
CREATE TABLE IF NOT EXISTS `sku_color` (
  `color_id` int(10) NOT NULL auto_increment COMMENT '颜色ID',
  `color_name` varchar(128) NOT NULL COMMENT '颜色名',
  `color_url` varchar(256) default NULL  COMMENT '颜色url',
  `ext_info` mediumtext COMMENT '保留字段',
  `version_id` int(10) unsigned COMMENT '版本号',
  `create_time` timestamp NOT NULL default '0000-00-00 00:00:00' COMMENT '创建时间',
  `update_time` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY  (`color_id`),
  UNIQUE KEY `sku_color_index` (`color_name`,`version_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=100000 ;

DROP TABLE IF EXISTS `sku_size`;
CREATE TABLE IF NOT EXISTS `sku_size` (
  `size_id` int(10) NOT NULL auto_increment COMMENT '尺寸ID',
  `size_name` varchar(64) NOT NULL COMMENT '尺寸名',
  `size_detail` varchar(128) default NULL  COMMENT '尺寸详情',
  `age` varchar(64) default NULL COMMENT '年龄',
  `ext_info` mediumtext COMMENT '保留字段',
  `version_id` int(10) unsigned COMMENT '版本号',
  `create_time` timestamp NOT NULL default '0000-00-00 00:00:00' COMMENT '创建时间',
  `update_time` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY  (`size_id`),
  UNIQUE KEY `sku_size_index` (`size_name`,`version_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=100000 ;


DROP TABLE IF EXISTS `brand`;
CREATE TABLE IF NOT EXISTS `brand` (
  `brand_id` int(10) NOT NULL auto_increment COMMENT '品牌ID',
  `brand_name` varchar(64) NOT NULL COMMENT '品牌名',
  `brand_name_ch` varchar(64) default NULL  COMMENT '品牌中文名',
  `source_website` varchar(128) default NULL COMMENT '源网站',
  `source_website_brand_url` varchar(128) default NULL COMMENT '源网站品牌首页',
  `ext_info` mediumtext COMMENT '保留字段',
  `version_id` int(10) unsigned COMMENT '版本号',
  `create_time` timestamp NOT NULL default '0000-00-00 00:00:00' COMMENT '创建时间',
  `update_time` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY  (`brand_id`),
  UNIQUE KEY `brand_index` (`brand_name`,`version_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=100000 ;

DROP TABLE IF EXISTS `category`;

CREATE TABLE IF NOT EXISTS `category` (
  `category_id` int(10) NOT NULL auto_increment COMMENT '分类ID',
  `category_name` varchar(64) NOT NULL COMMENT '分类名',
  `category_name_ch` varchar(64) default NULL COMMENT '分类中文名',
  `source_website` varchar(128) default NULL COMMENT '源网站',
  `category_level1` varchar(64) default NULL COMMENT '源网站的分类1',
  `category_level2` varchar(64) default NULL COMMENT '源网站的分类2',
  `ext_info` mediumtext COMMENT '保留字段',
  `version_id` int(10) unsigned COMMENT '版本号',
  `create_time` timestamp NOT NULL default '0000-00-00 00:00:00' COMMENT '创建时间',
  `update_time` timestamp NOT NULL default CURRENT_TIMESTAMP on update CURRENT_TIMESTAMP COMMENT '更新时间',
  PRIMARY KEY  (`category_id`),
  UNIQUE KEY `category_index` (`category_level1`,`category_level2`,`version_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=100000 ;

