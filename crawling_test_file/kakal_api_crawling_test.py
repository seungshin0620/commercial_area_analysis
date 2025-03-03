import json
import requests
import pandas as pd


class KakaoLocalAPI:
    """
    Kakao Local API 컨트롤러
    """

    def __init__(self, rest_api_key):
        """
        Rest API키 초기화 및 기능 별 URL 설정
        """

        # REST API 키 설정
        self.rest_api_key = rest_api_key
        self.headers = {"Authorization": "KakaoAK {}".format(rest_api_key)}

        # 서비스 별 URL 설정

        # 01 주소 검색
        self.URL_01 = "https://dapi.kakao.com/v2/local/search/address.json"
        # 02 좌표-행정구역정보 변환
        self.URL_02 = "https://dapi.kakao.com/v2/local/geo/coord2regioncode.json"
        # 03 좌표-주소 변환
        self.URL_03 = "https://dapi.kakao.com/v2/local/geo/coord2address.json"
        # 04 좌표계 변환
        self.URL_04 = "https://dapi.kakao.com/v2/local/geo/transcoord.json"
        # 05 키워드 검색
        self.URL_05 = "https://dapi.kakao.com/v2/local/search/keyword.json"
        # 06 카테고리 검색
        self.URL_06 = "https://dapi.kakao.com/v2/local/search/category.json"

    def search_address(self, query, analyze_type=None, page=None, size=None):
        """
        01 주소 검색
        """
        params = {"query": f"{query}"}

        if analyze_type != None:
            params["analyze_type"] = f"{analyze_type}"

        if page != None:
            params['page'] = f"{page}"

        if size != None:
            params['size'] = f"{size}"

        res = requests.get(self.URL_01, headers=self.headers, params=params)
        document = json.loads(res.text)

        return document

    def geo_coord2regioncode(self, x, y, input_coord=None, output_coord=None):
        """
        02 좌표-행정구역정보 변환
        """
        params = {"x": f"{x}",
                  "y": f"{y}"}

        if input_coord != None:
            params['input_coord'] = f"{input_coord}"

        if output_coord != None:
            params['output_coord'] = f"{output_coord}"

        res = requests.get(self.URL_02, headers=self.headers, params=params)
        document = json.loads(res.text)

        return document

    def geo_coord2address(self, x, y, input_coord=None):
        """
        03 좌표-주소 변환
        """
        params = {"x": f"{x}",
                  "y": f"{y}"}

        if input_coord != None:
            params['input_coord'] = f"{input_coord}"

        res = requests.get(self.URL_03, headers=self.headers, params=params)
        document = json.loads(res.text)

        return document

    def geo_transcoord(self, x, y, output_coord, input_coord=None):
        """
        04 좌표계 변환
        """
        params = {"x": f"{x}",
                  "y": f"{y}",
                  "output_coord": f"{output_coord}"}

        if input_coord != None:
            params['input_coord'] = f"{input_coord}"

        res = requests.get(self.URL_04, headers=self.headers, params=params)
        document = json.loads(res.text)

        return document

    def search_keyword(self, query, category_group_code=None, x=None, y=None, radius=None, rect=None, page=None,
                       size=None, sort=None):
        """
        05 키워드 검색
        """
        params = {"query": f"{query}"}

        if category_group_code != None:
            params['category_group_code'] = f"{category_group_code}"
        if x != None:
            params['x'] = f"{x}"
        if y != None:
            params['y'] = f"{y}"
        if radius != None:
            params['radius'] = f"{radius}"
        if rect != None:
            params['rect'] = f"{rect}"
        if page != None:
            params['page'] = f"{page}"
        if size != None:
            params['size'] = f"{params}"
        if sort != None:
            params['sort'] = f"{sort}"

        res = requests.get(self.URL_05, headers=self.headers, params=params)
        document = json.loads(res.text)

        return document

    def search_category(self, category_group_code, x, y, radius=None, rect=None, page=None, size=None, sort=None):
        """
        06 카테고리 검색
        """
        params = {'category_group_code': f"{category_group_code}",
                  'x': f"{x}",
                  'y': f"{y}"}

        if radius != None:
            params['radius'] = f"{radius}"
        if rect != None:
            params['rect'] = f"{rect}"
        if page != None:
            params['page'] = f"{page}"
        if size != None:
            params['size'] = f"{size}"
        if sort != None:
            params['sort'] = f"{sort}"

        res = requests.get(self.URL_06, headers=self.headers, params=params)
        document = json.loads(res.text)

        return document


# REST API 키
rest_api_key = "52756ac9cbee83797b5dd4e41ff78344"  # 여기서 개인적으로 받은 카카오 api 키 발급받아야 함

kakao = KakaoLocalAPI(rest_api_key)

df = pd.read_csv('price_output.csv', encoding='utf-8')

INF_ID = list()
INF_TOURIST = list()
INF_ADDRESS = list()
INF_MT1_list = list()
INF_CS2_list = list()
INF_PS3_list = list()
INF_SC4_list = list()
INF_AC5_list = list()
INF_PK6_list = list()
INF_OL7_list = list()
INF_SW8_list = list()
INF_BK9_list = list()
INF_CT1_list = list()
INF_AG2_list = list()
INF_PO3_list = list()
INF_AT4_list = list()
INF_AD5_list = list()
INF_FD6_list = list()
INF_CE7_list = list()
INF_HP8_list = list()
INF_PM9_list = list()

for i in range(len(df)):
    id_ = df.loc[i, 'INF_ID']
    tourist = df.loc[i, 'INF_TOURIST']
    addr = df.loc[i, 'INF_ADDRESS']
    x_coordinate = df.loc[i, 'INF_X']
    y_coordinate = df.loc[i, 'INF_Y']
    result_01 = kakao.search_keyword(query=addr, x=x_coordinate, y=y_coordinate, radius=330)
    INF_MT1 = 0
    INF_CS2 = 0
    INF_PS3 = 0
    INF_SC4 = 0
    INF_AC5 = 0
    INF_PK6 = 0
    INF_OL7 = 0
    INF_SW8 = 0
    INF_BK9 = 0
    INF_CT1 = 0
    INF_AG2 = 0
    INF_PO3 = 0
    INF_AT4 = 0
    INF_AD5 = 0
    INF_FD6 = 0
    INF_CE7 = 0
    INF_HP8 = 0
    INF_PM9 = 0
    print(result_01)
    test = result_01['documents']
    for j in range(len(test)):
        category_group_code = test[j]['category_group_code']
        if category_group_code == 'MT1':
            INF_MT1 += 1
        elif category_group_code == 'CS2':
            INF_CS2 += 1
        elif category_group_code == 'PS3':
            INF_PS3 += 1
        elif category_group_code == 'SC4':
            INF_SC4 += 1
        elif category_group_code == 'AC5':
            INF_AC5 += 1
        elif category_group_code == 'PK6':
            INF_PK6 += 1
        elif category_group_code == 'OL7':
            INF_OL7 += 1
        elif category_group_code == 'SW8':
            INF_SW8 += 1
        elif category_group_code == 'BK9':
            INF_BK9 += 1
        elif category_group_code == 'CT1':
            INF_CT1 += 1
        elif category_group_code == 'AG2':
            INF_AG2 += 1
        elif category_group_code == 'PO3':
            INF_PO3 += 1
        elif category_group_code == 'AT4':
            INF_AT4 += 1
        elif category_group_code == 'AD5':
            INF_AD5 += 1
        elif category_group_code == 'FD6':
            INF_FD6 += 1
        elif category_group_code == 'CE7 ':
            INF_CE7 += 1
        elif category_group_code == 'HP8':
            INF_HP8 += 1
        elif category_group_code == 'PM9':
            INF_PM9 += 1
    INF_ID.append(id_)
    INF_TOURIST.append(tourist)
    INF_ADDRESS.append(addr)
    INF_MT1_list.append(INF_MT1)
    INF_CS2_list.append(INF_CS2)
    INF_PS3_list.append(INF_PS3)
    INF_SC4_list.append(INF_SC4)
    INF_AC5_list.append(INF_AC5)
    INF_PK6_list.append(INF_PK6)
    INF_OL7_list.append(INF_OL7)
    INF_SW8_list.append(INF_SW8)
    INF_BK9_list.append(INF_BK9)
    INF_CT1_list.append(INF_CT1)
    INF_AG2_list.append(INF_AG2)
    INF_PO3_list.append(INF_PO3)
    INF_AT4_list.append(INF_AT4)
    INF_AD5_list.append(INF_AD5)
    INF_FD6_list.append(INF_FD6)
    INF_CE7_list.append(INF_CE7)
    INF_HP8_list.append(INF_HP8)
    INF_PM9_list.append(INF_PM9)

df_new = pd.DataFrame(
    {
        "INF_ID": INF_ID,
        "INF_TOURIST": INF_TOURIST,
        "INF_ADDRESS": INF_ADDRESS,
        "INF_MT1": INF_MT1_list,
        "INF_CS2": INF_CS2_list,
        "INF_PS3": INF_PS3_list,
        "INF_SC4": INF_SC4_list,
        "INF_AC5": INF_AC5_list,
        "INF_PK6": INF_PK6_list,
        "INF_OL7": INF_OL7_list,
        "INF_SW8": INF_SW8_list,
        "INF_BK9": INF_BK9_list,
        "INF_CT1": INF_CT1_list,
        "INF_AG2": INF_AG2_list,
        "INF_PO3": INF_PO3_list,
        "INF_AT4": INF_AT4_list,
        "INF_AD5": INF_AD5_list,
        "INF_FD6": INF_FD6_list,
        "INF_CE7": INF_CE7_list,
        "INF_HP8": INF_HP8_list,
        "INF_PM9": INF_PM9_list
    }
)
df_new.to_csv('Jeju_TB_INFRASTRUCTURE.csv', index=False)
