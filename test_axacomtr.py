import requests


def test_checkpoint1():
    url = 'https://www.axa.com.tr/hakkimizda'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint2():
    url = 'https://www.axa.com.tr/yonetim-kurulu-uyeleri'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint3():
    url = 'https://www.axa.com.tr/faaliyet-raporlari'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint4():
    url = 'https://www.axa.com.tr/mali-tablolar'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint5():
    url = 'https://www.axa.com.tr/'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint6():
    url = 'https://www.axa.com.tr/#popupVideo'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint7():
    url = 'https://www.axa.com.tr/basin-bultenleri'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint8():
    url = 'https://www.axa.com.tr/basin-bultenleri/basin-bulteni-1'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint9():
    url = 'https://www.axa.com.tr/basin-bultenleri/basin-bulteni-2'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint10():
    url = 'https://www.axa.com.tr/basin-bultenleri/basin-bulteni-3'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint11():
    url = 'https://www.axa.com.tr/basin-bultenleri/basin-bulteni-4'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint12():
    url = 'https://www.axa.com.tr/basin-bultenleri/basin-bulteni-5'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint13():
    url = 'https://www.axa.com.tr/basin-bultenleri/basin-bulteni-6'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint14():
    url = 'https://www.axa.com.tr/basin-bultenleri/basin-bulteni-7'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint15():
    url = 'https://www.axa.com.tr/basin-bultenleri/basin-bulteni-8'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint16():
    url = 'https://www.axa.com.tr/basin-bultenleri/basin-bulteni-9'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint17():
    url = 'https://www.axa.com.tr/media/t1/001/592/828/061/2017-FaaliyetRaporu.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint18():
    url = 'https://www.axa.com.tr/gizlilik-politikasi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint19():
    url = 'https://www.axa.com.tr/iletisim'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint20():
    url = 'https://www.axa.com.tr/wwwroot/t1/pdf/axa-sigorta-veri-koruma-beyani.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint21():
    url = 'https://www.axa.com.tr/wwwroot/t1/pdf/axa-kisisel-veri-koruma-politikasi-2019.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint22():
    url = 'https://www.axa.com.tr/aydinlatma-bildirimi'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint23():
    url = 'https://www.axa.com.tr/veri-sahibinin-haklarini-kullanmasi-icin-basvuru'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint24():
    url = 'https://www.axa.com.tr/yasal-bilgilendirmeler'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint25():
    url = 'http://www.axa.com/en/'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint26():
    url = 'https://www.axa.com.tr/media/t1/001/592/827/702/2002-FaaliyetRaporu.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint27():
    url = 'https://www.axa.com.tr/media/t1/001/592/827/751/2003-FaaliyetRaporu.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint28():
    url = 'https://www.axa.com.tr/media/t1/001/592/827/795/2004-FaaliyetRaporu.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint29():
    url = 'https://www.axa.com.tr/media/t1/001/592/827/829/2005-FaaliyetRaporu.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint30():
    url = 'https://www.axa.com.tr/media/t1/001/592/827/851/2006-FaaliyetRaporu.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint31():
    url = 'https://www.axa.com.tr/media/t1/001/592/827/947/2015-FaaliyetRaporu.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint32():
    url = 'https://www.axa.com.tr/media/t1/001/592/827/979/2016-FaaliyetRaporu.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint33():
    url = 'https://www.axa.com.tr/media/t1/001/592/828/061/2017-FaaliyetRaporu.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint34():
    url = 'https://www.axa.com.tr/media/t1/001/612/247/252/Faaliyet%20Raporu%202018.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint35():
    url = 'https://www.axa.com.tr/media/t1/001/592/828/252/axa-2019-faaliyet-raporu.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint36():
    url = 'https://www.axa.com.tr/media/t1/001/624/256/948/AXA%20Holding%202020%20Faaliyet%20Raporu%20Haziran%202021.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint37():
    url = 'https://www.axa.com.tr/media/t1/001/612/425/671/AXA%20HOLDiNG%20FAALiYET%20RAPORU_2018%20final.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint38():
    url = 'https://www.axa.com.tr/media/t1/001/592/828/562/AXA-Holding-2017-Faaliyet-Raporu.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint39():
    url = 'https://www.axa.com.tr/media/t1/001/592/828/533/AXA-Holding-2016-Faaliyet-Raporu.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint40():
    url = 'https://www.axa.com.tr/media/t1/001/592/828/506/AXA-Holding-2015-Faaliyet-Raporu.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint41():
    url = 'https://www.axa.com.tr/media/t1/001/592/828/480/AXA-Holding-2014-Faaliyet-Raporu.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint42():
    url = 'https://www.axa.com.tr/media/t1/001/592/828/456/AXA-Holding-2013-Faaliyet-Raporu.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint43():
    url = 'https://www.axa.com.tr/media/t1/001/592/828/429/AXA-Holding-2012-Faaliyet-Raporu.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint44():
    url = 'https://www.axa.com.tr/media/t1/001/592/830/439/Axa%20Sigorta_AS%20_Hazine_Raporu_31.03.2018.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint45():
    url = 'https://www.axa.com.tr/media/t1/001/592/830/417/axa-sigorta-30.06.2018.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint46():
    url = 'https://www.axa.com.tr/media/t1/001/592/830/387/axa_sigorta_as_hazine_raporu_30_09_2018_final.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint47():
    url = 'https://www.axa.com.tr/media/t1/001/592/830/324/Axa_Sigorta_Hazine_Raporu_31032017.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint48():
    url = 'https://www.axa.com.tr/media/t1/001/592/830/304/Axa_Sigorta_Hazine_Raporu_30062017.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint49():
    url = 'https://www.axa.com.tr/media/t1/001/592/830/279/Axa_Sigorta_Hazine_Raporu_30092017.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint50():
    url = 'https://www.axa.com.tr/media/t1/001/592/830/258/Axa-Sigorta-AS-31-%2012-2017-Rapor.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint51():
    url = 'https://www.axa.com.tr/media/t1/001/592/830/180/Axa_Sigorta_Hazine%20Raporu_31032016.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint52():
    url = 'https://www.axa.com.tr/media/t1/001/592/830/156/Axa-Sigorta-Hazine-Raporu-30062016.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint53():
    url = 'https://www.axa.com.tr/media/t1/001/592/830/135/Axa_Sigorta_Hazine_Raporu_30092016.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint54():
    url = 'https://www.axa.com.tr/media/t1/001/592/830/110/Axa_Sigorta_Hazine_Raporu_31122016.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint55():
    url = 'https://www.axa.com.tr/media/t1/001/592/830/043/Axa-Sigorta-Hazine-Raporu-31032015.1.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint56():
    url = 'https://www.axa.com.tr/media/t1/001/592/830/025/Axa-Sigorta-Hazine-Raporu-30062015.2.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint57():
    url = 'https://www.axa.com.tr/media/t1/001/592/830/003/Axa-Sigorta-Hazine-Raporu-30092015.3.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint58():
    url = 'https://www.axa.com.tr/media/t1/001/592/829/990/Axa_Sigorta_31122015_4.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint59():
    url = 'https://www.axa.com.tr/media/t1/001/592/829/905/Axa-Sigorta-Mali-Tablo-2014-I.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint60():
    url = 'https://www.axa.com.tr/media/t1/001/592/829/885/Axa-Sigorta-Mali-Tablo-2014-II.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint61():
    url = 'https://www.axa.com.tr/media/t1/001/592/829/828/AxaSigortaHazineRaporu.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint62():
    url = 'https://www.axa.com.tr/media/t1/001/592/829/806/Axa-Sigorta-Hazine-Raporu-31122014.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint63():
    url = 'https://www.axa.com.tr/media/t1/001/592/829/746/Axa-Sigorta-Mali-Tablo-2013-I.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint64():
    url = 'https://www.axa.com.tr/media/t1/001/592/829/619/Axa-Sigorta-Mali-Tablo-2013-II.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint65():
    url = 'https://www.axa.com.tr/media/t1/001/592/829/584/Axa-Sigorta-Mali-Tablo-2013-III.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint66():
    url = 'https://www.axa.com.tr/media/t1/001/592/829/492/Axa-Sigorta-Mali-Tablo-2013-IV.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint67():
    url = 'https://www.axa.com.tr/media/t1/001/592/829/444/Axa-Sigorta-Bilanco-2012-I.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint68():
    url = 'https://www.axa.com.tr/media/t1/001/592/829/341/Axa-Sigorta-Bilanco-2012-II.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint69():
    url = 'https://www.axa.com.tr/media/t1/001/592/829/308/Axa-Sigorta-Mali-Tablo-2012-III.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint70():
    url = 'https://www.axa.com.tr/media/t1/001/592/829/208/Axa-Sigorta-Mali-Tablo-2012-IV.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint71():
    url = 'https://www.axa.com.tr/media/t1/001/592/829/142/Axa-Sigorta-Mali-Tablo-2011-I.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint72():
    url = 'https://www.axa.com.tr/media/t1/001/592/828/979/Axa-Sigorta-Mali-Tablo-2011-II.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint73():
    url = 'https://www.axa.com.tr/media/t1/001/592/828/931/Axa-Sigorta-Mali-Tablo-2011-III.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint74():
    url = 'https://www.axa.com.tr/media/t1/001/592/828/717/Axa-Sigorta-Mali-Tablo-2011-IV.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint75():
    url = 'https://www.axa.com.tr/media/t1/001/592/829/093/Axa-Sigorta-Bilanco-2011-I.xls'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint76():
    url = 'https://www.axa.com.tr/media/t1/001/592/829/074/Axa-Sigorta-Gelir-Tablosu-2011-I.xls'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint77():
    url = 'https://www.axa.com.tr/media/t1/001/592/829/053/2011-09-Axa-Sigorta-Nakit-Akim-Tablosu.xls'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint78():
    url = 'https://www.axa.com.tr/media/t1/001/592/829/029/Sigorta-1-1-2011-31-03-2012-ozsermaye-degisim.xlsx'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint79():
    url = 'https://www.axa.com.tr/media/t1/001/592/828/904/Axa-Sigorta-Bilanco-2011-III.xls'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint80():
    url = 'https://www.axa.com.tr/media/t1/001/592/828/895/Axa-Sigorta-Gelir-Tablosu-2011-III.xls'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint81():
    url = 'https://www.axa.com.tr/media/t1/001/592/828/849/Sigorta-1-1-2011-30-09-2012-ozsermaye-degisim.xlsx'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint82():
    url = 'https://www.axa.com.tr/media/t1/001/592/829/425/Axa-Sigorta-Bilanco-2012-I.xlsx'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint83():
    url = 'https://www.axa.com.tr/media/t1/001/592/829/406/Axa-Sigorta-Gelir-Tablosu-2012-I.xlsx'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint84():
    url = 'https://www.axa.com.tr/media/t1/001/592/829/380/Sigorta-1-1-2012-31-03-2012-ozsermaye-degisim.xlsx'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint85():
    url = 'https://www.axa.com.tr/media/t1/001/592/846/681/Axa-Sigorta-Bilanco-2012-III.xlsx'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint86():
    url = 'https://www.axa.com.tr/media/t1/001/592/846/650/Axa-Sigorta-Gelir-Tablosu-2012-III.xlsx'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint87():
    url = 'https://www.axa.com.tr/media/t1/001/592/829/289/Axa-Sigorta-Bilanco-2012-III.xlsx'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint88():
    url = 'https://www.axa.com.tr/media/t1/001/592/829/271/Axa-Sigorta-Gelir-Tablosu-2012-III.xlsx'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint89():
    url = 'https://www.axa.com.tr/media/t1/001/592/829/248/Sigorta-1-1-2012-30-09-2012-ozsermaye-degisim.xlsx'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint90():
    url = 'https://www.axa.com.tr/media/t1/001/592/829/704/Axa-Sigorta-Bilanco-2013-I.xlsx'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint91():
    url = 'https://www.axa.com.tr/media/t1/001/592/829/688/Axa-Sigorta-Gelir-Tablosu-2013-I.xlsx'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint92():
    url = 'https://www.axa.com.tr/media/t1/001/592/829/669/Sigorta-1-1-2013-31-03-2013-ozsermaye-degisim.xlsx'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint93():
    url = 'https://www.axa.com.tr/media/t1/001/592/829/566/Axa-Sigorta-Bilanco-2013-III.xlsx'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint94():
    url = 'https://www.axa.com.tr/media/t1/001/592/829/548/Axa-Sigorta-Gelir-Tablosu-2013-III.xlsx'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint95():
    url = 'https://www.axa.com.tr/media/t1/001/592/829/531/Sigorta-1-1-2013-30-09-2013-ozsermaye-degisim.xlsx'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint96():
    url = 'https://www.axa.com.tr/media/t1/001/592/848/420/Axa%20Sigorta_AS%20_Hazine_Raporu_31.03.2018.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint97():
    url = 'https://www.axa.com.tr/media/t1/001/592/848/392/axa-sigorta-30.06.2018.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint98():
    url = 'https://www.axa.com.tr/media/t1/001/592/848/365/axa_sigorta_as_hazine_raporu_30_09_2018_final.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint99():
    url = 'https://www.axa.com.tr/media/t1/001/592/848/174/Axa_Sigorta_Hazine_Raporu_31032017.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint100():
    url = 'https://www.axa.com.tr/media/t1/001/592/848/149/Axa_Sigorta_Hazine_Raporu_30062017.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint101():
    url = 'https://www.axa.com.tr/media/t1/001/592/848/108/Axa_Sigorta_Hazine_Raporu_30092017.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint102():
    url = 'https://www.axa.com.tr/media/t1/001/592/848/090/Axa-Sigorta-AS-31-%2012-2017-Rapor.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint103():
    url = 'https://www.axa.com.tr/media/t1/001/592/847/936/Axa_Sigorta_Hazine%20Raporu_31032016.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint104():
    url = 'https://www.axa.com.tr/media/t1/001/592/847/914/Axa-Sigorta-Hazine-Raporu-30062016.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint105():
    url = 'https://www.axa.com.tr/media/t1/001/592/847/885/Axa_Sigorta_Hazine_Raporu_30092016.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint106():
    url = 'https://www.axa.com.tr/media/t1/001/592/847/860/Axa_Sigorta_Hazine_Raporu_31122016.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint107():
    url = 'https://www.axa.com.tr/media/t1/001/592/847/763/Axa-Sigorta-Hazine-Raporu-31032015.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint108():
    url = 'https://www.axa.com.tr/media/t1/001/592/847/727/Axa-Sigorta-Hazine-Raporu-30062015.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint109():
    url = 'https://www.axa.com.tr/media/t1/001/592/847/706/Axa-Sigorta-Hazine-Raporu-30092015.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint110():
    url = 'https://www.axa.com.tr/media/t1/001/592/847/688/Axa_Sigorta_31122015_4.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint111():
    url = 'https://www.axa.com.tr/media/t1/001/592/847/608/Axa-Sigorta-Mali-Tablo-2014-I.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint112():
    url = 'https://www.axa.com.tr/media/t1/001/592/847/580/Axa-Sigorta-Mali-Tablo-2014-II.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint113():
    url = 'https://www.axa.com.tr/media/t1/001/592/847/542/AxaSigortaHazineRaporu.3.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint114():
    url = 'https://www.axa.com.tr/media/t1/001/592/847/523/Axa-Sigorta-Hazine-Raporu-31122014.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint115():
    url = 'https://www.axa.com.tr/media/t1/001/592/847/403/Axa-Sigorta-Mali-Tablo-2013-I.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint116():
    url = 'https://www.axa.com.tr/media/t1/001/592/847/374/Axa-Sigorta-Bilanco-2013-I.xlsx'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint117():
    url = 'https://www.axa.com.tr/media/t1/001/592/847/352/Axa-Sigorta-Gelir-Tablosu-2013-I.xlsx'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint118():
    url = 'https://www.axa.com.tr/media/t1/001/592/847/333/Sigorta-1-1-2013-31-03-2013-ozsermaye-degisim.xlsx'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint119():
    url = 'https://www.axa.com.tr/media/t1/001/592/847/259/Axa-Sigorta-Mali-Tablo-2013-II.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint120():
    url = 'https://www.axa.com.tr/media/t1/001/592/847/163/Axa-Sigorta-Mali-Tablo-2013-III.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint121():
    url = 'https://www.axa.com.tr/media/t1/001/592/847/041/Axa-Sigorta-Gelir-Tablosu-2013-III.xlsx'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint122():
    url = 'https://www.axa.com.tr/media/t1/001/592/847/103/Axa-Sigorta-Bilanco-2013-III.xlsx'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint123():
    url = 'https://www.axa.com.tr/media/t1/001/592/847/163/Axa-Sigorta-Mali-Tablo-2013-III.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint124():
    url = 'https://www.axa.com.tr/media/t1/001/592/846/546/Axa-Sigorta-Mali-Tablo-2012-IV.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint125():
    url = 'https://www.axa.com.tr/media/t1/001/592/846/624/Sigorta-1-1-2012-30-09-2012-ozsermaye-degisim.xlsx'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint126():
    url = 'https://www.axa.com.tr/media/t1/001/592/846/705/Axa-Sigorta-Mali-Tablo-2012-III.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint127():
    url = 'https://www.axa.com.tr/media/t1/001/592/846/705/Axa-Sigorta-Mali-Tablo-2012-III.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint128():
    url = 'https://www.axa.com.tr/media/t1/001/592/846/747/Axa-Sigorta-Bilanco-2012-II.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint129():
    url = 'https://www.axa.com.tr/media/t1/001/592/846/805/Sigorta-1-1-2012-31-03-2012-ozsermaye-degisim.xlsx'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint130():
    url = 'https://www.axa.com.tr/media/t1/001/592/846/827/Axa-Sigorta-Gelir-Tablosu-2012-I.xlsx'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint131():
    url = 'https://www.axa.com.tr/media/t1/001/592/846/848/Axa-Sigorta-Bilanco-2012-I.xlsx'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint132():
    url = 'https://www.axa.com.tr/media/t1/001/592/834/075/Axa-Hayat-Sigorta-Hazine.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint133():
    url = 'https://www.axa.com.tr/media/t1/001/592/834/233/Sigorta-1-1-2011-30-09-2012-ozsermaye-degisim.xlsx'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint134():
    url = 'https://www.axa.com.tr/media/t1/001/592/834/262/Axa-Sigorta-Gelir-Tablosu-2011-III.xls'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint135():
    url = 'https://www.axa.com.tr/media/t1/001/592/834/302/Axa-Sigorta-Bilanco-2011-III.xls'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint136():
    url = 'https://www.axa.com.tr/media/t1/001/592/834/302/Axa-Sigorta-Bilanco-2011-III.xls'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint137():
    url = 'https://www.axa.com.tr/media/t1/001/592/834/360/Axa-Sigorta-Mali-Tablo-2011-III.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint138():
    url = 'https://www.axa.com.tr/media/t1/001/592/834/537/Axa-Sigorta-Mali-Tablo-2011-II.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint139():
    url = 'https://www.axa.com.tr/media/t1/001/592/835/087/Sigorta-1-1-2011-31-03-2012-ozsermaye-degisim.xlsx'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint140():
    url = 'https://www.axa.com.tr/media/t1/001/592/835/121/2011-09-Axa-Sigorta-Nakit-Akim-Tablosu.xls'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint141():
    url = 'https://www.axa.com.tr/media/t1/001/592/835/156/Axa-Sigorta-Gelir-Tablosu-2011-I.xls'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint142():
    url = 'https://www.axa.com.tr/media/t1/001/592/835/181/Axa-Sigorta-Bilanco-2011-I.xls'
    response = requests.get(url, verify=False)
    assert response.status_code == 200


def test_checkpoint143():
    url = 'https://www.axa.com.tr/media/t1/001/592/835/214/Axa-Sigorta-Mali-Tablo-2011-I.pdf'
    response = requests.get(url, verify=False)
    assert response.status_code == 200
    
    
def test_checkpoint144():
    url = 'https://www.axahayatemeklilik.com.tr/haberler/axa-japonyada-yaralari-sariyor'
    response = requests.get(url, verify=False)
    assert response.status_code == 200

