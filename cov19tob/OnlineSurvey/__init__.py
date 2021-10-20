from otree.api import *


doc = """
IRB에 있는 기초설문을 oTree로 옮긴 것입니다.
"""


class Constants(BaseConstants):
    name_in_url = 'BQ'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    region = models.IntegerField(
        label = "귀하의 거주지역을 선택해주세요.",
        widget = widgets.RadioSelect,
        choices = [
            [1, "서울"],
            [2, "인천"],
            [3, "경기도"],
            [4, "강원도"],
            [5, "세종"],
            [6, "충청남도"],
            [7, "충청북도"],
            [8, "대전"],
            [9, "대구"],
            [10, "경상북도"],
            [11, "경상남도"],
            [12, "울산"],
            [13, "부산"],
            [14, "전라북도"],
            [15, "전라남도"],
            [16, "광주"],
            [17, "제주도"]
        ]
    )

    marriage_stat = models.IntegerField(
        label = "귀하의 혼인상태를 선택해주십시오",
        widget=widgets.RadioSelect,
        choices=[
            [1, "결혼 안함"],
            [2, "결혼함"],
            [3, "이혼/사별함"],
            [4, "기타"],
        ]
    )


# PAGES
class BQ_1(Page):
    form_model = 'player'
    form_fields = [
        'region',
        'marriage_stat',
<<<<<<< HEAD
=======
        # 'tot_tobacco_pcs',
        # 'recent_tobacco_yesno',
        # 'recent_liq_tobacco_yesno',
        # 'main_tobacco_type_1',
        # 'main_tobacco_type_2',
        # 'main_tobacco_type_3',
        # 'main_tobacco_type_4',
        # 'main_tobacco_type_5',
        # 'main_tobacco_type_6',
        # 'main_tobacco_type_7',
        # 'main_tobacco_type_8',
        # 'main_tobacco_type_9',
        # 'main_tobacco_type_10',
        # 'main_tobacco_type_11',
>>>>>>> 9dc3c5c876af3d6a603dc0ae5884788f143cfca9
    ]




page_sequence = [BQ_1]
