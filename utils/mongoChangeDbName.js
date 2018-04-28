/* 批量修改mongodb数据库名, 由字典的key改为value */
dic = {
    "temp_ACX": "Acx",
    "temp_BTCBOX": "Btcbox",
    "temp_BitBay": "Bitbay",
    "temp_CCEX": "Ccex",
    "temp_CEXIO": "Cexio",
    "temp_GDAX": "Gdax",
    "temp_GetBTC": "Getbtc",
    "temp_HitBtc": "Hitbtc",
    "temp_ItBit": "Itbit",
    "temp_LakeBTC": "Lakebtc",
    "temp_OKCoin": "Okcoin",
    "temp_WEX": "wex",
    "temp_YoBit": "Yobit",
    "temp_bitFlyer": "Bitflyer",
    "temp_bitz": "Bitz",
}

for (key in dic) {
    var temp = 'temp_' + key;
    var db_obj = db.getSiblingDB(key)
    var colls = db_obj.getCollectionNames();
    for (index in colls) {
        var old = key + '.' + colls[index]
        var temp_name = temp + '.' + colls[index]
        db.adminCommand({ renameCollection: old, to: temp_name })
    }

    if (db_obj.stats()["collections"] == 0) {
        db_obj.dropDatabase()
    } else {
        print(db_obj + ' failed')
    }
    for (i in colls) {
        var temp_name = temp + '.' + colls[i]
        var new_name = dic[key] + '.' + colls[i]
        db.adminCommand({ renameCollection: temp_name, to: new_name })
    }
    print(db_obj + ' succeed')
}

