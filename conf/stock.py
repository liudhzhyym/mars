#!/usr/bin/python
# -*- coding: utf-8 -*-

indicatorList = [
	# "KDJ金叉",
	# "KDJ二次金叉",
	# "KDJ低位金叉",
	# "KDJ买入信号",
	# "KDJ有效金叉",
	# "KDJ即将金叉",
	# "60分钟KDJ金叉",
	# "30分钟KDJ金叉",
	# "周KDJ金叉",
	# "月KDJ金叉",
	# "60分钟KDJ二次金叉",
	# "60分钟KDJ即将金叉",
	# "KDJ死叉",
	# "KDJ高位死叉",
	# "60分钟KDJ高位死叉",
	# "30分钟KDJ死叉",
	# "KDJ底背离",
	# "KDJ顶背离",
	# "60分钟KDJ底背离",
	# "周KDJ底背离",
	# "KDJ上移",
	# "KDJ下移",
	# "KDJ拐头向上",
	# "KDJ拐头向下",
	# "60分钟KDJ上移",
	# "60分钟KDJ拐头向上",
	# "60分钟KDJ拐头向下",
	# "30分钟KDJ拐头向上",
	# "KDJ小于0",
	# "KDJ中J大于0",
	# "J大于0，小于20",
	# "周KDJ大于0",
	# "60分钟KDJ中J大于0",
	# "周KDJ中J大于0金叉",
	# "MACD金叉",
	# "MACD二次金叉",
	# "MACD低位金叉",
	# "MACD低位二次金叉",
	# "MACD三次金叉",
	# "MACD零轴以上金叉",
	# "60分钟MACD金叉",
	# "30分钟MACD金叉",
	# "周MACD金叉",
	# "月MACD金叉",
	# "60分钟MACD二次金叉",
	# "60分钟MACD零轴上金叉",
	# "MACD死叉",
	# "MACD高位死叉",
	# "60分钟MACD高位死叉",
	# "30分钟MACD死叉",
	# "MACD底背离",
	# "MACD顶背离",
	# "60分钟MACD底背离",
	# "周MACD底背离",
	# "MACD上移",
	# "MACD下移",
	# "MACD拐头向上",
	# "MACD拐头向下",
	# "MACD走平",
	# "60分钟MACD上移",
	# "60分钟MACD拐头向上",
	# "30分钟MACD走平",
	# "30分钟MACD拐头向上",
	# "60分钟MACD拐头向下",
	# "MACD红柱缩短",
	# "MACD红柱放大",
	# "MACD绿柱缩短",
	# "MACD绿柱放大",
	# "30分钟MACD绿柱缩短",
	# "60分钟MACD红柱放大",
	# "60分钟MACD绿柱缩短",
	# "30分钟MACD红柱放大",
	# "MACD翻红",
	# "MACD上穿0轴",
	# "MACD红二波",
	# "MACD下穿0轴",
	# "30分钟MACD翻红",
	# "60分钟MACD红二波",
	# "30分钟MACD上穿0轴",
	# "60分钟MACD下穿0轴",
	# "MACD大于0",
	# "MACD中DIFF大于0，DEA大于0",
	# "DEA大于0，小于0.1",
	# "周MACD大于0",
	# "60分钟MACD中DIFF大于0",
	# "周MACD中DEA大于0金叉",
	# "日线OBV上移",
	# "周线OBV上移",
	# "60分钟OBV上移",
	# "日线OBV下移",
	# "60分钟OBV下移",
	# "日线OBV走平",
	# "60分钟OBV走平",
	# "OBV指标创新高",
	# "周线OBV指标创新高",
	# "60分钟OBV指标创新高",
	# "日线VR指标底背离",
	# "60分钟VR底背离",
	# "日线VR指标顶背离",
	# "60分钟VR顶背离",
	# "日线VR低位",
	# "60分钟VR低位",
	# "CCI买入信号",
	# "60分钟CCI买入信号",
	# "CCI卖出信号",
	# "60分钟CCI卖出信号",
	# "CCI上移",
	"CCI下移",
	"60分钟CCI上移",
	"60分钟CCI下移",
	"CCI大于+100",
	"CCI小于-100",
	"CCI指标创新高",
	"CCI指标创新低",
	"周CCI超买（高位）",
	"60分钟CCI超卖（低位）",
	"30分钟CCI指标创新高",
	"60分钟CCI指标创新低",
	"BOLL突破中轨",
	"BOLL突破上轨",
	"BOLL买入信号",
	"BOLL突破中轨",
	"BOLL二次突破中轨",
	"BOLL突破下轨",
	"60分钟BOLL突破中轨",
	"30分钟BOLL突破上轨",
	"周BOLL买入信号",
	"周BOLL突破下轨",
	"60分钟BOLL二次突破中轨",
	"30分钟BOLL突破下轨",
	"BOLL跌破上轨",
	"BOLL跌破中轨",
	"BOLL卖出信号",
	"60分钟BOLL跌破上轨",
	"30分钟BOLL跌破中轨",
	"周BOLL卖出信号",
	"BOLL上移",
	"BOLL下移",
	"BOLL中轨拐头向上",
	"BOLL开口张开",
	"30分钟BOLL上移",
	"60分钟BOLL下移",
	"周BOLL中轨拐头向上",
	"60分钟BOLL开口缩小",
	"BOLL中轨以下",
	"BOLL中轨以上",
	"BOLL中轨附件",
	"BOLL上轨附件",
	"BOLL下轨附近",
	"周BOLL中轨以下",
	"60分钟BOLL中轨附近",
	"30分钟BOLL下轨附近",
	"周BOLL上轨附近",
	"30分钟BOLL下轨附近",
	"SKDJ金叉",
	"SKDJ即将金叉",
	"SKDJ低位金叉",
	"60分钟SKDJ低位金叉",
	"30分钟SKDJ金叉",
	"周SKDJ金叉",
	"月SKDJ金叉",
	"SKDJ二次金叉",
	"SKDJ死叉",
	"SKDJ即将死叉",
	"SKDJ高位死叉",
	"60分钟SKDJ高位死叉",
	"30分钟SKDJ死叉",
	"周SKDJ死叉",
	"月SKDJ死叉",
	"SKDJ底背离",
	"SKDJ顶背离",
	"60分钟SKDJ底背离",
	"周SKDJ底背离",
	"月SKDJ底背离",
	"SKDJ超买",
	"日线SKDJ超买",
	"周线SKDJ超买",
	"月线SKDJ超买",
	"SKDJ超卖",
	"日线SKDJ超卖",
	"周线SKDJ超卖",
	"月线SKDJ超卖",
	"MTM金叉",
	"MTM买入信号",
	"MTM二次金叉",
	"60分钟MTM金叉",
	"周MTM买入信号",
	"30分钟MTM二次金叉",
	"MTM卖出信号",
	"MTM死叉",
	"60分钟MTM卖出信号",
	"周MTM死叉",
	"MTM大于0",
	"MTM小于0",
	"周MTM指标创新高",
	"60分钟MTM指标创新低",
	"WR金叉",
	"WR买入信号",
	"60分钟WR金叉",
	"周WR买入信号",
	"WR卖出信号",
	"60分钟WR卖出信号",
	"WR上移",
	"WR下移",
	"60分钟WR上移",
	"60分钟WR下移",
	"WR1大于80",
	"WR1小于20",
	"周WR超卖（高位）",
	"60分钟WR超买（低位）",
	"RSI金叉",
	"RSI三线金叉",
	"RSI低位金叉",
	"RSI即将金叉",
	"60分钟RSI金叉",
	"30分钟RSI金叉",
	"周RSI金叉",
	"60分钟RSI即将金叉",
	"RSI死叉",
	"30分钟RSI死叉",
	"RSI上移",
	"RSI下移",
	"RSI拐头向上",
	"RSI拐头向下",
	"60分钟RSI上移",
	"60分钟RSI拐头向上",
	"60分钟RSI拐头向下",
	"30分钟RSI拐头向上",
	"RSI小于20",
	"RSI大于80",
	"RSI1小于25",
	"周RSI大于80",
	"60分钟RSI中RSI1小于20",
	"周RSI中RSI1小于20",
	"量比小于0.5",
	"量比在1.5-2.5",
	"量比在2.5-5",
	"量比在5-10",
	"量比大于20",
	"BIAS金叉",
	"BIAS买入信号",
	"60分钟BIAS金叉",
	"周BIAS买入信号",
	"BIAS死叉",
	"30分钟BIAS死叉",
	"BIAS小于0",
	"BIAS小于-6",
	"BIAS1大于0",
	"周BIAS大于0",
	"BIAS1小于0",
	"周BIAS中BIAS1小于0",
]

timeList = [
	"20141203",
	"20141204",
	"20141205",
	"20141208",
	"20141209",
	"20141210",
	"20141211",
	"20141212",
	"20141215",
	"20141216",
	"20141217",
	"20141218",
	"20141219",
	"20141222",
	"20141223",
	"20141224",
	"20141225",
	"20141226",
	"20141229",
	"20141230",
	"20141231",
	"20150105",
	"20150106",
	"20150107",
	"20150108",
	"20150109",
	"20150112",
	"20150113",
	"20150114",
	"20150115",
	"20150116",
	"20150119",
	"20150120",
	"20150121",
	"20150122",
	"20150123",
	"20150126",
	"20150127",
	"20150128",
	"20150129",
	"20150130",
	"20150202",
	"20150203",
	"20150204",
	"20150205",
	"20150206",
	"20150209",
	"20150210",
	"20150211",
	"20150212",
	"20150213",
	"20150216",
	"20150217",
	"20150225",
	"20150226",
	"20150227",
	"20150302",
	"20150303",
	"20150304",
	"20150305",
	"20150306",
	"20150309",
	"20150310",
	"20150311",
	"20150312",
	"20150313",
	"20150316",
	"20150317",
	"20150318",
	"20150319",
	"20150320",
	"20150323",
	"20150324",
	"20150325",
	"20150326",
	"20150327",
	"20150330",
	"20150331",
	"20150401",
	"20150402",
	"20150403",
	"20150407",
	"20150408",
	"20150409",
	"20150410",
	"20150413",
	"20150414",
	"20150415",
	"20150416",
	"20150417",
	"20150420",
	"20150421",
	"20150422",
	"20150423",
	"20150424",
	"20150427",
	"20150428",
	"20150429",
	"20150430",
	"20150504",
	"20150505",
	"20150506",
	"20150507",
	"20150508",
	"20150511",
	"20150512",
	"20150513",
	"20150514",
	"20150515",
	"20150518",
	"20150519",
	"20150520",
	"20150521",
	"20150522",
	"20150525",
	"20150526",
	"20150527",
	"20150528",
	"20150529",
	"20150601",
	"20150602",
	"20150603",
	"20150604",
	"20150605",
	"20150608",
	"20150609",
	"20150610",
	"20150611",
	"20150612",
	"20150615",
	"20150616",
	"20150617",
	"20150618",
	"20150619",
	"20150623",
	"20150624",
	"20150625",
	"20150626",
	"20150629",
	"20150630",
	"20150701",
	"20150702",
	"20150703",
	"20150706",
	"20150707",
	"20150708",
	"20150709",
	"20150710",
	"20150713",
	"20150714",
	"20150715",
	"20150716",
	"20150717",
	"20150720",
	"20150721",
	"20150722",
	"20150723",
	"20150724",
	"20150727",
	"20150728",
	"20150729",
	"20150730",
	"20150731",
	"20150803",
	"20150804",
	"20150805",
	"20150806",
	"20150807",
	"20150810",
	"20150811",
	"20150812",
	"20150813",
	"20150814",
	"20150817",
	"20150818",
	"20150819",
	"20150820",
	"20150821",
	"20150824",
	"20150825",
	"20150826",
	"20150827",
	"20150828",
	"20150831",
	"20150901",
	"20150902",
	"20150907",
	"20150908",
	"20150909",
	"20150910",
	"20150911",
	"20150914",
	"20150915",
	"20150916",
	"20150917",
	"20150918",
	"20150921",
	"20150922",
	"20150923",
	"20150924",
	"20150925",
	"20150928",
	"20150929",
	"20150930",
	"20151008",
	"20151009",
	"20151012",
	"20151013",
	"20151014",
	"20151015",
	"20151016",
	"20151019",
	"20151020",
	"20151021",
	"20151022",
	"20151023",
	"20151026",
	"20151027",
	"20151028",
	"20151029",
	"20151030",
	"20151102",
	"20151103",
	"20151104",
	"20151105",
	"20151106",
	"20151109",
	"20151110",
	"20151111",
	"20151112",
	"20151113",
	"20151116",
	"20151117",
	"20151118",
	"20151119",
	"20151120",
	"20151123",
	"20151124",
	"20151125",
	"20151126",
	"20151127",
	"20151130",
	"20151201",
	"20151202",
	"20151203",
	"20151204",
	"20151207",
	"20151208",
	"20151209",
	"20151210",
	"20151211",
	"20151214",
	"20151215",
	"20151216",
	"20151217",
	"20151218",
	"20151221",
	"20151222",
	"20151223",
	"20151224",
	"20151225",
	"20151228",
	"20151229",
	"20151230",
	"20151231",
	"20160104",
	"20160105",
	"20160106",
	"20160107",
	"20160108",
	"20160111",
	"20160112",
	"20160113",
	"20160114",
	"20160115",
	"20160118",
	"20160119",
	"20160120",
	"20160121",
	"20160122",
	"20160125",
	"20160126",
	"20160127",
	"20160128",
	"20160129",
	"20160201",
	"20160202",
	"20160203",
	"20160204",
	"20160205",
	"20160215",
	"20160216",
	"20160217",
	"20160218",
	"20160219",
	"20160222",
	"20160223",
	"20160224",
	"20160225",
	"20160226",
	"20160229",
	"20160301",
	"20160302",
	"20160303",
	"20160304",
	"20160307",
	"20160308",
	"20160309",
	"20160310",
	"20160311",
	"20160314",
	"20160315",
	"20160316",
	"20160317",
	"20160318",
	"20160321",
	"20160322",
	"20160323",
	"20160324",
	"20160325",
	"20160326",
]


stockList = [
	"sh600761",
	"sh600502",
	"sh600643",
	"sh600336",
	"sh600298",
	"sh600000",
	"sh600004",
	"sh600005",
	"sh600006",
	"sh600007",
	"sh600008",
	"sh600009",
	"sh600010",
	"sh600011",
	"sh600012",
	"sh600015",
	"sh600016",
	"sh600017",
	"sh600018",
	"sh600019",
	"sh600020",
	"sh600021",
	"sh600022",
	"sh600026",
	"sh600027",
	"sh600028",
	"sh600029",
	"sh600030",
	"sh600031",
	"sh600033",
	"sh600035",
	"sh600036",
	"sh600037",
	"sh600038",
	"sh600039",
	"sh600048",
	"sh600050",
	"sh600051",
	"sh600052",
	"sh600053",
	"sh600054",
	"sh600055",
	"sh600056",
	"sh600058",
	"sh600059",
	"sh600060",
	"sh600061",
	"sh600062",
	"sh600063",
	"sh600064",
	"sh600066",
	"sh600067",
	"sh600068",
	"sh600069",
	"sh600070",
	"sh600071",
	"sh600072",
	"sh600073",
	"sh600074",
	"sh600075",
	"sh600076",
	"sh600077",
	"sh600078",
	"sh600079",
	"sh600080",
	"sh600081",
	"sh600082",
	"sh600083",
	"sh600084",
	"sh600085",
	"sh600086",
	"sh600087",
	"sh600088",
	"sh600089",
	"sh600090",
	"sh600091",
	"sh600093",
	"sh600095",
	"sh600096",
	"sh600097",
	"sh600098",
	"sh600099",
	"sh600100",
	"sh600101",
	"sh600102",
	"sh600103",
	"sh600104",
	"sh600105",
	"sh600106",
	"sh600107",
	"sh600108",
	"sh600109",
	"sh600110",
	"sh600111",
	"sh600112",
	"sh600113",
	"sh600114",
	"sh600115",
	"sh600116",
	"sh600117",
	"sh600118",
	"sh600119",
	"sh600120",
	"sh600121",
	"sh600122",
	"sh600123",
	"sh600125",
	"sh600126",
	"sh600127",
	"sh600128",
	"sh600129",
	"sh600130",
	"sh600131",
	"sh600132",
	"sh600133",
	"sh600135",
	"sh600136",
	"sh600137",
	"sh600138",
	"sh600139",
	"sh600141",
	"sh600143",
	"sh600145",
	"sh600146",
	"sh600148",
	"sh600149",
	"sh600150",
	"sh600151",
	"sh600152",
	"sh600153",
	"sh600155",
	"sh600156",
	"sh600157",
	"sh600158",
	"sh600159",
	"sh600160",
	"sh600161",
	"sh600162",
	"sh600163",
	"sh600165",
	"sh600166",
	"sh600167",
	"sh600168",
	"sh600169",
	"sh600170",
	"sh600171",
	"sh600172",
	"sh600173",
	"sh600175",
	"sh600176",
	"sh600177",
	"sh600178",
	"sh600179",
	"sh600180",
	"sh600182",
	"sh600183",
	"sh600184",
	"sh600185",
	"sh600186",
	"sh600187",
	"sh600188",
	"sh600189",
	"sh600190",
	"sh600191",
	"sh600192",
	"sh600193",
	"sh600195",
	"sh600196",
	"sh600197",
	"sh600198",
	"sh600199",
	"sh600200",
	"sh600201",
	"sh600202",
	"sh600203",
	"sh600206",
	"sh600207",
	"sh600208",
	"sh600209",
	"sh600210",
	"sh600211",
	"sh600212",
	"sh600213",
	"sh600215",
	"sh600216",
	"sh600217",
	"sh600218",
	"sh600219",
	"sh600220",
	"sh600221",
	"sh600222",
	"sh600223",
	"sh600225",
	"sh600226",
	"sh600227",
	"sh600228",
	"sh600229",
	"sh600230",
	"sh600231",
	"sh600232",
	"sh600233",
	"sh600234",
	"sh600235",
	"sh600236",
	"sh600237",
	"sh600238",
	"sh600239",
	"sh600240",
	"sh600241",
	"sh600242",
	"sh600243",
	"sh600246",
	"sh600247",
	"sh600248",
	"sh600249",
	"sh600250",
	"sh600251",
	"sh600252",
	"sh600253",
	"sh600255",
	"sh600256",
	"sh600257",
	"sh600258",
	"sh600259",
	"sh600260",
	"sh600261",
	"sh600262",
	"sh600263",
	"sh600265",
	"sh600266",
	"sh600267",
	"sh600268",
	"sh600269",
	"sh600270",
	"sh600271",
	"sh600272",
	"sh600273",
	"sh600275",
	"sh600276",
	"sh600277",
	"sh600278",
	"sh600279",
	"sh600280",
	"sh600281",
	"sh600282",
	"sh600283",
	"sh600284",
	"sh600285",
	"sh600287",
	"sh600288",
	"sh600289",
	"sh600290",
	"sh600291",
	"sh600292",
	"sh600293",
	"sh600295",
	"sh600297",
	"sh600298",
	"sh600299",
	"sh600300",
	"sh600301",
	"sh600302",
	"sh600303",
	"sh600305",
	"sh600306",
	"sh600307",
	"sh600308",
	"sh600309",
	"sh600310",
	"sh600311",
	"sh600312",
	"sh600315",
	"sh600316",
	"sh600317",
	"sh600318",
	"sh600319",
	"sh600320",
	"sh600321",
	"sh600322",
	"sh600323",
	"sh600325",
	"sh600326",
	"sh600327",
	"sh600328",
	"sh600329",
	"sh600330",
	"sh600331",
	"sh600332",
	"sh600333",
	"sh600335",
	"sh600336",
	"sh600337",
	"sh600338",
	"sh600339",
	"sh600340",
	"sh600343",
	"sh600345",
	"sh600346",
	"sh600348",
	"sh600350",
	"sh600351",
	"sh600352",
	"sh600353",
	"sh600354",
	"sh600355",
	"sh600356",
	"sh600358",
	"sh600359",
	"sh600360",
	"sh600361",
	"sh600362",
	"sh600363",
	"sh600365",
	"sh600366",
	"sh600367",
	"sh600368",
	"sh600369",
	"sh600370",
	"sh600371",
	"sh600372",
	"sh600373",
	"sh600375",
	"sh600376",
	"sh600377",
	"sh600378",
	"sh600379",
	"sh600380",
	"sh600381",
	"sh600382",
	"sh600383",
	"sh600385",
	"sh600386",
	"sh600387",
	"sh600388",
	"sh600389",
	"sh600390",
	"sh600391",
	"sh600392",
	"sh600393",
	"sh600395",
	"sh600396",
	"sh600397",
	"sh600398",
	"sh600399",
	"sh600400",
	"sh600403",
	"sh600405",
	"sh600406",
	"sh600408",
	"sh600409",
	"sh600410",
	"sh600415",
	"sh600416",
	"sh600418",
	"sh600419",
	"sh600420",
	"sh600421",
	"sh600422",
	"sh600423",
	"sh600425",
	"sh600426",
	"sh600428",
	"sh600429",
	"sh600432",
	"sh600433",
	"sh600435",
	"sh600436",
	"sh600438",
	"sh600439",
	"sh600444",
	"sh600446",
	"sh600448",
	"sh600449",
	"sh600452",
	"sh600455",
	"sh600456",
	"sh600458",
	"sh600459",
	"sh600460",
	"sh600461",
	"sh600462",
	"sh600463",
	"sh600466",
	"sh600467",
	"sh600468",
	"sh600469",
	"sh600470",
	"sh600475",
	"sh600476",
	"sh600477",
	"sh600478",
	"sh600479",
	"sh600480",
	"sh600481",
	"sh600482",
	"sh600483",
	"sh600485",
	"sh600486",
	"sh600487",
	"sh600488",
	"sh600489",
	"sh600490",
	"sh600491",
	"sh600493",
	"sh600495",
	"sh600496",
	"sh600497",
	"sh600498",
	"sh600499",
	"sh600500",
	"sh600501",
	"sh600502",
	"sh600503",
	"sh600505",
	"sh600506",
	"sh600507",
	"sh600508",
	"sh600509",
	"sh600510",
	"sh600511",
	"sh600512",
	"sh600513",
	"sh600515",
	"sh600516",
	"sh600517",
	"sh600518",
	"sh600519",
	"sh600520",
	"sh600521",
	"sh600522",
	"sh600523",
	"sh600525",
	"sh600526",
	"sh600527",
	"sh600528",
	"sh600529",
	"sh600530",
	"sh600531",
	"sh600532",
	"sh600533",
	"sh600535",
	"sh600536",
	"sh600537",
	"sh600538",
	"sh600539",
	"sh600540",
	"sh600543",
	"sh600545",
	"sh600546",
	"sh600547",
	"sh600548",
	"sh600549",
	"sh600550",
	"sh600551",
	"sh600552",
	"sh600555",
	"sh600557",
	"sh600558",
	"sh600559",
	"sh600560",
	"sh600561",
	"sh600562",
	"sh600563",
	"sh600565",
	"sh600566",
	"sh600567",
	"sh600568",
	"sh600569",
	"sh600570",
	"sh600571",
	"sh600572",
	"sh600573",
	"sh600575",
	"sh600576",
	"sh600577",
	"sh600578",
	"sh600579",
	"sh600580",
	"sh600581",
	"sh600582",
	"sh600583",
	"sh600584",
	"sh600585",
	"sh600586",
	"sh600587",
	"sh600588",
	"sh600589",
	"sh600590",
	"sh600592",
	"sh600593",
	"sh600594",
	"sh600595",
	"sh600596",
	"sh600597",
	"sh600598",
	"sh600599",
	"sh600600",
	"sh600601",
	"sh600602",
	"sh600603",
	"sh600604",
	"sh600605",
	"sh600606",
	"sh600608",
	"sh600609",
	"sh600610",
	"sh600611",
	"sh600612",
	"sh600613",
	"sh600614",
	"sh600615",
	"sh600616",
	"sh600617",
	"sh600618",
	"sh600619",
	"sh600620",
	"sh600621",
	"sh600622",
	"sh600623",
	"sh600624",
	"sh600626",
	"sh600628",
	"sh600629",
	"sh600630",
	"sh600631",
	"sh600634",
	"sh600635",
	"sh600636",
	"sh600637",
	"sh600638",
	"sh600639",
	"sh600640",
	"sh600641",
	"sh600642",
	"sh600643",
	"sh600644",
	"sh600645",
	"sh600647",
	"sh600648",
	"sh600649",
	"sh600650",
	"sh600651",
	"sh600652",
	"sh600653",
	"sh600654",
	"sh600655",
	"sh600656",
	"sh600657",
	"sh600658",
	"sh600660",
	"sh600661",
	"sh600662",
	"sh600663",
	"sh600664",
	"sh600665",
	"sh600666",
	"sh600667",
	"sh600668",
	"sh600671",
	"sh600673",
	"sh600674",
	"sh600675",
	"sh600676",
	"sh600677",
	"sh600678",
	"sh600679",
	"sh600680",
	"sh600682",
	"sh600683",
	"sh600684",
	"sh600685",
	"sh600686",
	"sh600687",
	"sh600688",
	"sh600689",
	"sh600690",
	"sh600691",
	"sh600692",
	"sh600693",
	"sh600694",
	"sh600695",
	"sh600696",
	"sh600697",
	"sh600698",
	"sh600699",
	"sh600701",
	"sh600702",
	"sh600703",
	"sh600704",
	"sh600706",
	"sh600707",
	"sh600708",
	"sh600710",
	"sh600711",
	"sh600712",
	"sh600713",
	"sh600714",
	"sh600715",
	"sh600716",
	"sh600717",
	"sh600718",
	"sh600719",
	"sh600720",
	"sh600721",
	"sh600722",
	"sh600723",
	"sh600724",
	"sh600725",
	"sh600726",
	"sh600728",
	"sh600729",
	"sh600730",
	"sh600731",
	"sh600732",
	"sh600733",
	"sh600734",
	"sh600735",
	"sh600736",
	"sh600737",
	"sh600738",
	"sh600739",
	"sh600740",
	"sh600741",
	"sh600742",
	"sh600743",
	"sh600744",
	"sh600745",
	"sh600746",
	"sh600747",
	"sh600748",
	"sh600749",
	"sh600750",
	"sh600751",
	"sh600753",
	"sh600754",
	"sh600755",
	"sh600756",
	"sh600757",
	"sh600758",
	"sh600759",
	"sh600760",
	"sh600761",
	"sh600763",
	"sh600764",
	"sh600765",
	"sh600766",
	"sh600767",
	"sh600768",
	"sh600769",
	"sh600770",
	"sh600771",
	"sh600773",
	"sh600774",
	"sh600775",
	"sh600776",
	"sh600777",
	"sh600778",
	"sh600779",
	"sh600780",
	"sh600781",
	"sh600782",
	"sh600783",
	"sh600784",
	"sh600785",
	"sh600787",
	"sh600789",
	"sh600790",
	"sh600791",
	"sh600792",
	"sh600793",
	"sh600794",
	"sh600795",
	"sh600796",
	"sh600797",
	"sh600798",
	"sh600800",
	"sh600801",
	"sh600802",
	"sh600803",
	"sh600804",
	"sh600805",
	"sh600806",
	"sh600807",
	"sh600808",
	"sh600809",
	"sh600810",
	"sh600811",
	"sh600812",
	"sh600814",
	"sh600815",
	"sh600816",
	"sh600818",
	"sh600819",
	"sh600820",
	"sh600821",
	"sh600822",
	"sh600823",
	"sh600824",
	"sh600825",
	"sh600826",
	"sh600827",
	"sh600828",
	"sh600829",
	"sh600830",
	"sh600831",
	"sh600832",
	"sh600833",
	"sh600834",
	"sh600835",
	"sh600836",
	"sh600837",
	"sh600838",
	"sh600839",
	"sh600841",
	"sh600843",
	"sh600844",
	"sh600845",
	"sh600846",
	"sh600847",
	"sh600848",
	"sh600850",
	"sh600851",
	"sh600853",
	"sh600854",
	"sh600855",
	"sh600856",
	"sh600857",
	"sh600858",
	"sh600859",
	"sh600860",
	"sh600861",
	"sh600862",
	"sh600863",
	"sh600864",
	"sh600865",
	"sh600866",
	"sh600867",
	"sh600868",
	"sh600869",
	"sh600870",
	"sh600871",
	"sh600872",
	"sh600873",
	"sh600874",
	"sh600875",
	"sh600876",
	"sh600877",
	"sh600879",
	"sh600880",
	"sh600881",
	"sh600882",
	"sh600883",
	"sh600884",
	"sh600885",
	"sh600886",
	"sh600887",
	"sh600888",
	"sh600889",
	"sh600890",
	"sh600891",
	"sh600892",
	"sh600893",
	"sh600894",
	"sh600895",
	"sh600896",
	"sh600897",
	"sh600900",
	"sh600960",
	"sh600961",
	"sh600962",
	"sh600963",
	"sh600965",
	"sh600966",
	"sh600967",
	"sh600969",
	"sh600970",
	"sh600971",
	"sh600973",
	"sh600975",
	"sh600976",
	"sh600978",
	"sh600979",
	"sh600980",
	"sh600981",
	"sh600982",
	"sh600983",
	"sh600984",
	"sh600985",
	"sh600986",
	"sh600987",
	"sh600988",
	"sh600990",
	"sh600991",
	"sh600992",
	"sh600993",
	"sh600995",
	"sh600997",
	"sh600998",
	"sh600999",
	"sh601000",
	"sh601001",
	"sh601002",
	"sh601003",
	"sh601005",
	"sh601006",
	"sh601007",
	"sh601008",
	"sh601009",
	"sh601011",
	"sh601018",
	"sh601088",
	"sh601098",
	"sh601099",
	"sh601101",
	"sh601106",
	"sh601107",
	"sh601111",
	"sh601116",
	"sh601117",
	"sh601118",
	"sh601126",
	"sh601137",
	"sh601139",
	"sh601158",
	"sh601166",
	"sh601168",
	"sh601169",
	"sh601177",
	"sh601179",
	"sh601186",
	"sh601188",
	"sh601216",
	"sh601268",
	"sh601288",
	"sh601299",
	"sh601318",
	"sh601328",
	"sh601333",
	"sh601369",
	"sh601377",
	"sh601390",
	"sh601398",
	"sh601518",
	"sh601519",
	"sh601558",
	"sh601588",
	"sh601600",
	"sh601601",
	"sh601607",
	"sh601616",
	"sh601618",
	"sh601628",
	"sh601666",
	"sh601668",
	"sh601678",
	"sh601688",
	"sh601699",
	"sh601700",
	"sh601717",
	"sh601718",
	"sh601727",
	"sh601766",
	"sh601777",
	"sh601788",
	"sh601799",
	"sh601801",
	"sh601808",
	"sh601818",
	"sh601857",
	"sh601866",
	"sh601872",
	"sh601877",
	"sh601880",
	"sh601888",
	"sh601890",
	"sh601898",
	"sh601899",
	"sh601918",
	"sh601919",
	"sh601933",
	"sh601939",
	"sh601958",
	"sh601988",
	"sh601989",
	"sh601991",
	"sh601992",
	"sh601998",
	"sh601999",
	"sh000001",
	"sh000002",
	"sz000001",
	"sz000002",
	"sz000004",
	"sz000005",
	"sz000006",
	"sz000007",
	"sz000008",
	"sz000009",
	"sz000010",
	"sz000011",
	"sz000012",
	"sz000014",
	"sz000016",
	"sz000017",
	"sz000018",
	"sz000019",
	"sz000020",
	"sz000021",
	"sz000022",
	"sz000023",
	"sz000024",
	"sz000025",
	"sz000026",
	"sz000027",
	"sz000028",
	"sz000029",
	"sz000030",
	"sz000031",
	"sz000032",
	"sz000033",
	"sz000034",
	"sz000035",
	"sz000036",
	"sz000037",
	"sz000039",
	"sz000040",
	"sz000042",
	"sz000043",
	"sz000045",
	"sz000046",
	"sz000048",
	"sz000049",
	"sz000050",
	"sz000055",
	"sz000056",
	"sz000058",
	"sz000059",
	"sz000060",
	"sz000061",
	"sz000062",
	"sz000063",
	"sz000065",
	"sz000066",
	"sz000068",
	"sz000069",
	"sz000070",
	"sz000078",
	"sz000088",
	"sz000089",
	"sz000090",
	"sz000096",
	"sz000099",
	"sz000100",
	"sz000150",
	"sz000151",
	"sz000153",
	"sz000155",
	"sz000157",
	"sz000158",
	"sz000159",
	"sz000301",
	"sz000338",
	"sz000400",
	"sz000401",
	"sz000402",
	"sz000404",
	"sz000407",
	"sz000408",
	"sz000409",
	"sz000410",
	"sz000411",
	"sz000413",
	"sz000415",
	"sz000416",
	"sz000417",
	"sz000418",
	"sz000419",
	"sz000420",
	"sz000421",
	"sz000422",
	"sz000423",
	"sz000425",
	"sz000426",
	"sz000428",
	"sz000429",
	"sz000430",
	"sz000488",
	"sz000501",
	"sz000502",
	"sz000503",
	"sz000504",
	"sz000505",
	"sz000506",
	"sz000507",
	"sz000509",
	"sz000510",
	"sz000511",
	"sz000513",
	"sz000514",
	"sz000516",
	"sz000517",
	"sz000518",
	"sz000519",
	"sz000520",
	"sz000521",
	"sz000522",
	"sz000523",
	"sz000524",
	"sz000525",
	"sz000526",
	"sz000527",
	"sz000528",
	"sz000529",
	"sz000530",
	"sz000531",
	"sz000532",
	"sz000533",
	"sz000534",
	"sz000536",
	"sz000537",
	"sz000538",
	"sz000539",
	"sz000540",
	"sz000541",
	"sz000543",
	"sz000544",
	"sz000545",
	"sz000546",
	"sz000547",
	"sz000548",
	"sz000550",
	"sz000551",
	"sz000552",
	"sz000553",
	"sz000554",
	"sz000555",
	"sz000557",
	"sz000558",
	"sz000559",
	"sz000560",
	"sz000561",
	"sz000562",
	"sz000563",
	"sz000564",
	"sz000565",
	"sz000566",
	"sz000567",
	"sz000568",
	"sz000570",
	"sz000571",
	"sz000572",
	"sz000573",
	"sz000576",
	"sz000578",
	"sz000581",
	"sz000582",
	"sz000584",
	"sz000585",
	"sz000586",
	"sz000587",
	"sz000589",
	"sz000590",
	"sz000591",
	"sz000592",
	"sz000593",
	"sz000594",
	"sz000595",
	"sz000596",
	"sz000597",
	"sz000598",
	"sz000599",
	"sz000600",
	"sz000601",
	"sz000602",
	"sz000603",
	"sz000605",
	"sz000606",
	"sz000607",
	"sz000608",
	"sz000609",
	"sz000610",
	"sz000611",
	"sz000612",
	"sz000613",
	"sz000615",
	"sz000616",
	"sz000617",
	"sz000619",
	"sz000623",
	"sz000625",
	"sz000626",
	"sz000627",
	"sz000628",
	"sz000629",
	"sz000630",
	"sz000631",
	"sz000632",
	"sz000633",
	"sz000635",
	"sz000636",
	"sz000637",
	"sz000638",
	"sz000639",
	"sz000650",
	"sz000651",
	"sz000652",
	"sz000655",
	"sz000656",
	"sz000659",
	"sz000661",
	"sz000662",
	"sz000663",
	"sz000665",
	"sz000666",
	"sz000667",
	"sz000668",
	"sz000669",
	"sz000671",
	"sz000673",
	"sz000676",
	"sz000677",
	"sz000678",
	"sz000679",
	"sz000680",
	"sz000682",
	"sz000683",
	"sz000685",
	"sz000686",
	"sz000687",
	"sz000690",
	"sz000691",
	"sz000692",
	"sz000695",
	"sz000697",
	"sz000698",
	"sz000700",
	"sz000701",
	"sz000702",
	"sz000703",
	"sz000705",
	"sz000707",
	"sz000708",
	"sz000709",
	"sz000710",
	"sz000711",
	"sz000712",
	"sz000713",
	"sz000715",
	"sz000716",
	"sz000717",
	"sz000718",
	"sz000720",
	"sz000721",
	"sz000723",
	"sz000725",
	"sz000726",
	"sz000727",
	"sz000728",
	"sz000729",
	"sz000731",
	"sz000732",
	"sz000733",
	"sz000735",
	"sz000736",
	"sz000737",
	"sz000738",
	"sz000739",
	"sz000748",
	"sz000750",
	"sz000751",
	"sz000752",
	"sz000753",
	"sz000755",
	"sz000756",
	"sz000758",
	"sz000759",
	"sz000760",
	"sz000761",
	"sz000762",
	"sz000766",
	"sz000767",
	"sz000768",
	"sz000776",
	"sz000777",
	"sz000778",
	"sz000779",
	"sz000780",
	"sz000782",
	"sz000783",
	"sz000785",
	"sz000786",
	"sz000788",
	"sz000789",
	"sz000790",
	"sz000791",
	"sz000792",
	"sz000793",
	"sz000795",
	"sz000796",
	"sz000797",
	"sz000798",
	"sz000799",
	"sz000800",
	"sz000801",
	"sz000802",
	"sz000803",
	"sz000806",
	"sz000807",
	"sz000809",
	"sz000810",
	"sz000811",
	"sz000812",
	"sz000813",
	"sz000815",
	"sz000816",
	"sz000818",
	"sz000819",
	"sz000820",
	"sz000821",
	"sz000822",
	"sz000823",
	"sz000825",
	"sz000826",
	"sz000828",
	"sz000829",
	"sz000830",
	"sz000831",
	"sz000833",
	"sz000835",
	"sz000836",
	"sz000837",
	"sz000838",
	"sz000839",
	"sz000848",
	"sz000850",
	"sz000851",
	"sz000852",
	"sz000856",
	"sz000858",
	"sz000859",
	"sz000860",
	"sz000861",
	"sz000862",
	"sz000868",
	"sz000869",
	"sz000875",
	"sz000876",
	"sz000877",
	"sz000878",
	"sz000880",
	"sz000881",
	"sz000882",
	"sz000883",
	"sz000885",
	"sz000886",
	"sz000887",
	"sz000888",
	"sz000889",
	"sz000890",
	"sz000892",
	"sz000893",
	"sz000895",
	"sz000897",
	"sz000898",
	"sz000899",
	"sz000900",
	"sz000901",
	"sz000902",
	"sz000903",
	"sz000905",
	"sz000906",
	"sz000908",
	"sz000909",
	"sz000910",
	"sz000911",
	"sz000912",
	"sz000913",
	"sz000915",
	"sz000916",
	"sz000917",
	"sz000918",
	"sz000919",
	"sz000920",
	"sz000921",
	"sz000922",
	"sz000923",
	"sz000925",
	"sz000926",
	"sz000927",
	"sz000928",
	"sz000929",
	"sz000930",
	"sz000931",
	"sz000932",
	"sz000933",
	"sz000935",
	"sz000936",
	"sz000937",
	"sz000938",
	"sz000939",
	"sz000948",
	"sz000949",
	"sz000950",
	"sz000951",
	"sz000952",
	"sz000953",
	"sz000955",
	"sz000957",
	"sz000958",
	"sz000959",
	"sz000960",
	"sz000961",
	"sz000962",
	"sz000963",
	"sz000965",
	"sz000966",
	"sz000967",
	"sz000968",
	"sz000969",
	"sz000970",
	"sz000971",
	"sz000972",
	"sz000973",
	"sz000975",
	"sz000976",
	"sz000977",
	"sz000978",
	"sz000979",
	"sz000980",
	"sz000982",
	"sz000983",
	"sz000985",
	"sz000987",
	"sz000988",
	"sz000989",
	"sz000990",
	"sz000993",
	"sz000995",
	"sz000996",
	"sz000997",
	"sz000998",
	"sz000999",
	"sz001696",
	"sz001896",
	"sz002001",
	"sz002002",
	"sz002003",
	"sz002004",
	"sz002005",
	"sz002006",
	"sz002007",
	"sz002008",
	"sz002009",
	"sz002010",
	"sz002011",
	"sz002012",
	"sz002013",
	"sz002014",
	"sz002015",
	"sz002016",
	"sz002017",
	"sz002018",
	"sz002019",
	"sz002020",
	"sz002021",
	"sz002022",
	"sz002023",
	"sz002024",
	"sz002025",
	"sz002026",
	"sz002027",
	"sz002028",
	"sz002029",
	"sz002030",
	"sz002031",
	"sz002032",
	"sz002033",
	"sz002034",
	"sz002035",
	"sz002036",
	"sz002037",
	"sz002038",
	"sz002039",
	"sz002040",
	"sz002041",
	"sz002042",
	"sz002043",
	"sz002044",
	"sz002045",
	"sz002046",
	"sz002047",
	"sz002048",
	"sz002049",
	"sz002050",
	"sz002051",
	"sz002052",
	"sz002053",
	"sz002054",
	"sz002055",
	"sz002056",
	"sz002057",
	"sz002058",
	"sz002059",
	"sz002060",
	"sz002061",
	"sz002062",
	"sz002063",
	"sz002064",
	"sz002065",
	"sz002066",
	"sz002067",
	"sz002068",
	"sz002069",
	"sz002070",
	"sz002071",
	"sz002072",
	"sz002073",
	"sz002074",
	"sz002076",
	"sz002077",
	"sz002078",
	"sz002079",
	"sz002080",
	"sz002081",
	"sz002082",
	"sz002083",
	"sz002084",
	"sz002085",
	"sz002086",
	"sz002087",
	"sz002088",
	"sz002089",
	"sz002090",
	"sz002091",
	"sz002092",
	"sz002093",
	"sz002094",
	"sz002095",
	"sz002096",
	"sz002097",
	"sz002098",
	"sz002099",
	"sz002100",
	"sz002101",
	"sz002102",
	"sz002103",
	"sz002104",
	"sz002105",
	"sz002106",
	"sz002107",
	"sz002108",
	"sz002109",
	"sz002110",
	"sz002111",
	"sz002112",
	"sz002113",
	"sz002114",
	"sz002115",
	"sz002116",
	"sz002117",
	"sz002118",
	"sz002119",
	"sz002120",
	"sz002121",
	"sz002122",
	"sz002123",
	"sz002124",
	"sz002125",
	"sz002126",
	"sz002127",
	"sz002128",
	"sz002129",
	"sz002130",
	"sz002131",
	"sz002132",
	"sz002133",
	"sz002134",
	"sz002135",
	"sz002136",
	"sz002137",
	"sz002138",
	"sz002139",
	"sz002140",
	"sz002141",
	"sz002142",
	"sz002143",
	"sz002144",
	"sz002145",
	"sz002146",
	"sz002147",
	"sz002148",
	"sz002149",
	"sz002150",
	"sz002151",
	"sz002152",
	"sz002153",
	"sz002154",
	"sz002155",
	"sz002156",
	"sz002157",
	"sz002158",
	"sz002159",
	"sz002160",
	"sz002161",
	"sz002162",
	"sz002163",
	"sz002164",
	"sz002165",
	"sz002166",
	"sz002167",
	"sz002168",
	"sz002169",
	"sz002170",
	"sz002171",
	"sz002172",
	"sz002173",
	"sz002174",
	"sz002175",
	"sz002176",
	"sz002177",
	"sz002178",
	"sz002179",
	"sz002180",
	"sz002181",
	"sz002182",
	"sz002183",
	"sz002184",
	"sz002185",
	"sz002186",
	"sz002187",
	"sz002188",
	"sz002189",
	"sz002190",
	"sz002191",
	"sz002192",
	"sz002193",
	"sz002194",
	"sz002195",
	"sz002196",
	"sz002197",
	"sz002198",
	"sz002199",
	"sz002200",
	"sz002201",
	"sz002202",
	"sz002203",
	"sz002204",
	"sz002205",
	"sz002206",
	"sz002207",
	"sz002208",
	"sz002209",
	"sz002210",
	"sz002211",
	"sz002212",
	"sz002213",
	"sz002214",
	"sz002215",
	"sz002216",
	"sz002217",
	"sz002218",
	"sz002219",
	"sz002220",
	"sz002221",
	"sz002222",
	"sz002223",
	"sz002224",
	"sz002225",
	"sz002226",
	"sz002227",
	"sz002228",
	"sz002229",
	"sz002230",
	"sz002231",
	"sz002232",
	"sz002233",
	"sz002234",
	"sz002235",
	"sz002236",
	"sz002237",
	"sz002238",
	"sz002239",
	"sz002240",
	"sz002241",
	"sz002242",
	"sz002243",
	"sz002244",
	"sz002245",
	"sz002246",
	"sz002247",
	"sz002248",
	"sz002249",
	"sz002250",
	"sz002251",
	"sz002252",
	"sz002253",
	"sz002254",
	"sz002255",
	"sz002256",
	"sz002258",
	"sz002259",
	"sz002260",
	"sz002261",
	"sz002262",
	"sz002263",
	"sz002264",
	"sz002265",
	"sz002266",
	"sz002267",
	"sz002268",
	"sz002269",
	"sz002270",
	"sz002271",
	"sz002272",
	"sz002273",
	"sz002274",
	"sz002275",
	"sz002276",
	"sz002277",
	"sz002278",
	"sz002279",
	"sz002280",
	"sz002281",
	"sz002282",
	"sz002283",
	"sz002284",
	"sz002285",
	"sz002286",
	"sz002287",
	"sz002288",
	"sz002289",
	"sz002290",
	"sz002291",
	"sz002292",
	"sz002293",
	"sz002294",
	"sz002295",
	"sz002296",
	"sz002297",
	"sz002298",
	"sz002299",
	"sz002300",
	"sz002301",
	"sz002302",
	"sz002303",
	"sz002304",
	"sz002305",
	"sz002306",
	"sz002307",
	"sz002308",
	"sz002309",
	"sz002310",
	"sz002311",
	"sz002312",
	"sz002313",
	"sz002314",
	"sz002315",
	"sz002316",
	"sz002317",
	"sz002318",
	"sz002319",
	"sz002320",
	"sz002321",
	"sz002322",
	"sz002323",
	"sz002324",
	"sz002325",
	"sz002326",
	"sz002327",
	"sz002328",
	"sz002329",
	"sz002330",
	"sz002331",
	"sz002332",
	"sz002333",
	"sz002334",
	"sz002335",
	"sz002336",
	"sz002337",
	"sz002338",
	"sz002339",
	"sz002340",
	"sz002341",
	"sz002342",
	"sz002343",
	"sz002344",
	"sz002345",
	"sz002346",
	"sz002347",
	"sz002348",
	"sz002349",
	"sz002350",
	"sz002351",
	"sz002352",
	"sz002353",
	"sz002354",
	"sz002355",
	"sz002356",
	"sz002357",
	"sz002358",
	"sz002359",
	"sz002360",
	"sz002361",
	"sz002362",
	"sz002363",
	"sz002364",
	"sz002365",
	"sz002366",
	"sz002367",
	"sz002368",
	"sz002369",
	"sz002370",
	"sz002371",
	"sz002372",
	"sz002373",
	"sz002374",
	"sz002375",
	"sz002376",
	"sz002377",
	"sz002378",
	"sz002379",
	"sz002380",
	"sz002381",
	"sz002382",
	"sz002383",
	"sz002384",
	"sz002385",
	"sz002386",
	"sz002387",
	"sz002388",
	"sz002389",
	"sz002390",
	"sz002391",
	"sz002392",
	"sz002393",
	"sz002394",
	"sz002395",
	"sz002396",
	"sz002397",
	"sz002398",
	"sz002399",
	"sz002400",
	"sz002401",
	"sz002402",
	"sz002403",
	"sz002404",
	"sz002405",
	"sz002406",
	"sz002407",
	"sz002408",
	"sz002409",
	"sz002410",
	"sz002411",
	"sz002412",
	"sz002413",
	"sz002414",
	"sz002415",
	"sz002416",
	"sz002417",
	"sz002418",
	"sz002419",
	"sz002420",
	"sz002421",
	"sz002422",
	"sz002423",
	"sz002424",
	"sz002425",
	"sz002426",
	"sz002427",
	"sz002428",
	"sz002429",
	"sz002430",
	"sz002431",
	"sz002432",
	"sz002433",
	"sz002434",
	"sz002435",
	"sz002436",
	"sz002437",
	"sz002438",
	"sz002439",
	"sz002440",
	"sz002441",
	"sz002442",
	"sz002443",
	"sz002444",
	"sz002445",
	"sz002446",
	"sz002447",
	"sz002448",
	"sz002449",
	"sz002450",
	"sz002451",
	"sz002452",
	"sz002453",
	"sz002454",
	"sz002455",
	"sz002456",
	"sz002457",
	"sz002458",
	"sz002459",
	"sz002460",
	"sz002461",
	"sz002462",
	"sz002463",
	"sz002464",
	"sz002465",
	"sz002466",
	"sz002467",
	"sz002468",
	"sz002469",
	"sz002470",
	"sz002471",
	"sz002472",
	"sz002473",
	"sz002474",
	"sz002475",
	"sz002476",
	"sz002477",
	"sz002478",
	"sz002479",
	"sz002480",
	"sz002481",
	"sz002482",
	"sz002483",
	"sz002484",
	"sz002485",
	"sz002486",
	"sz002487",
	"sz002488",
	"sz002489",
	"sz002490",
	"sz002491",
	"sz002492",
	"sz002493",
	"sz002494",
	"sz002495",
	"sz002496",
	"sz002497",
	"sz002498",
	"sz002499",
	"sz002500",
	"sz002501",
	"sz002502",
	"sz002503",
	"sz002504",
	"sz002505",
	"sz002506",
	"sz002507",
	"sz002508",
	"sz002509",
	"sz002510",
	"sz002511",
	"sz002512",
	"sz002513",
	"sz002514",
	"sz002515",
	"sz002516",
	"sz002517",
	"sz002518",
	"sz002519",
	"sz002520",
	"sz002521",
	"sz002522",
	"sz002523",
	"sz002524",
	"sz002526",
	"sz002527",
	"sz002528",
	"sz002529",
	"sz002530",
	"sz002531",
	"sz002532",
	"sz002533",
	"sz002534",
	"sz002535",
	"sz002536",
	"sz002537",
	"sz002538",
	"sz002539",
	"sz002540",
	"sz002541",
	"sz002542",
	"sz002543",
	"sz002544",
	"sz002545",
	"sz002546",
	"sz002547",
	"sz002548",
	"sz002549",
	"sz002550",
	"sz002551",
	"sz002552",
	"sz002553",
	"sz002554",
	"sz002555",
	"sz002556",
	"sz002557",
	"sz002558",
	"sz002559",
	"sz002560",
	"sz002561",
	"sz002565",
	"sz002566",
]

