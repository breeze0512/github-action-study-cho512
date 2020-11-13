import requests
import json

def parsing_beautifulsoup(url):


    data = requests.get(url)
    covid19Data = json.loads(data.text)

    for i in covid19Data['data47']:
        enName = jp2en(i['name'])
        i['name']+=" (%s)"%enName

    return covid19Data


def extract_dailyCovid_data(data):
    """
    BeautifulSoup Object에서 book data를 추출하는 함수
    :param soup: BeautifulSoup soup Object
    :return: contents(str)
    """

    upload_contents = ''
    new_CovidInfo = data

    for eachData in new_CovidInfo:
        if eachData == 'data47':
            for eachKen in new_CovidInfo[eachData]:
                KenName = eachKen['name']
                newP = eachKen['new']
                cumulative = eachKen['cumulative']
                # url_suffix = eachKen['name'].split(" ")[0]
                # url = url_prefix + url_suffix
                content = f"" + KenName + ": New Patient : " + str(newP) +"<br/>\n"
                upload_contents += content
    return upload_contents

def jp2en(name):
    if "北海道" == name:
        return "Hokkaido"
    elif "青森県" == name:
        return "Aomori"
    elif "岩手県" == name:
        return "Iwate"
    elif "宮城県" == name:
        return "Miyagi"
    elif "秋田県" == name:
        return "Akita"
    elif "山形県" == name:
        return "Yamagata"
    elif "福島県" == name:
        return "Fukushima"
    elif "茨城県" == name:
        return "Ibaraki"
    elif "栃木県" == name:
        return "Tochigi"
    elif "群馬県" == name:
        return "Gunma"
    elif "埼玉県" == name:
        return "Saitama"
    elif "千葉県" == name:
        return "Chiba"
    elif "東京都" == name:
        return "Tokyo"
    elif "神奈川県" == name:
        return "Kanagawa"
    elif "新潟県" == name:
        return "Niigata"
    elif "富山県" == name:
        return "Toyama"
    elif "石川県" == name:
        return "Ishikawa"
    elif "福井県" == name:
        return "Fukui"
    elif "山梨県" == name:
        return "Yamanashi"
    elif "長野県" == name:
        return "Nagano"
    elif "岐阜県" == name:
        return "Gifu"
    elif "静岡県" == name:
        return "Shizuoka"
    elif "愛知県" == name:
        return "Aichi"
    elif "三重県" == name:
        return "Mie"
    elif "滋賀県" == name:
        return "Shiga"
    elif "京都府" == name:
        return "Kyoto"
    elif "大阪府" == name:
        return "Osaka"
    elif "兵庫県" == name:
        return "Hyogo"
    elif "奈良県" == name:
        return "Nara"
    elif "和歌山県" == name:
        return "Wakayama"
    elif "鳥取県" == name:
        return "Tottori"
    elif "島根県" == name:
        return "Shimane"
    elif "岡山県" == name:
        return "Okayama"
    elif "広島県" == name:
        return "Hiroshima"
    elif "山口県" == name:
        return "Yamaguchi"
    elif "徳島県" == name:
        return "Tokushima"
    elif "香川県" == name:
        return "Kagawa"
    elif "愛媛県" == name:
        return "Ehime"
    elif "高知県" == name:
        return "Kochi"
    elif "福岡県" == name:
        return "Fukuoka"
    elif "佐賀県" == name:
        return "Saga"
    elif "長崎県" == name:
        return "Nagasaki"
    elif "熊本県" == name:
        return "Kumamoto"
    elif "大分県" == name:
        return "Oita"
    elif "宮崎県" == name:
        return "Miyazaki"
    elif "鹿児島県" == name:
        return "Kagoshima"
    elif "沖縄県" == name:
        return "Okinawa"
    elif "検閲" == name:
        return "Censorship"
    elif "チャーター機・国職員など" == name:
        return "etc."
    elif "合計" == name:
        return "Total"