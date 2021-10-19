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

    born_year = models.IntegerField(
        label = "귀하의 출생년도는 몇 년도입니까?",
        choices = range(2001,1962,-1)
    )

    tot_tobacco_pcs = models.IntegerField(
        label = "지금까지 살아오는 동안 피운 일반담배(궐련)의 양은 총 얼마나 됩니까?",
        widget = widgets.RadioSelect,
        choices = [
            [1, "5갑(100개비)미만"],
            [2, "5갑(100개비)이상"],
            [3, "피운 적 없다"],
        ]
    )

    recent_tobacco_yesno = models.IntegerField(
        label = "최근 1달 내에 궐련형 전자담배 (가열담배, (예)아이코스, 글로, 릴)를 피운 적이 있습니까?",
        widget = widgets.RadioSelect,
        choices = [
            [1, "예"],
            [2, "아니오"],
        ]
    )

    recent_liq_tobacco_yesno = models.IntegerField(
        label = "최근 1달 내에 니코틴이 포함된 액상형 전자담배를 사용한 적이 있습니까?",
        widget = widgets.RadioSelect,
        choices=[
            [1, "예"],
            [2, "아니오"],
        ]
    )

    main_tobacco_type_1 = models.BooleanField(
        label = "궐련(일반담배)",
        widget = widgets.CheckboxInput,
        blank = True,
    )

    main_tobacco_type_2 = models.BooleanField(
        label="궐련형 전자담배(아이코스,릴,글로 등)",
        widget=widgets.CheckboxInput,
        blank=True,
    )
    main_tobacco_type_3 = models.BooleanField(
        label="액상형 전자담배(쥴, 릴 베이퍼 등)",
        widget=widgets.CheckboxInput,
        blank=True,
    )
    main_tobacco_type_4 = models.BooleanField(
        label="머금는 담배(스누스)",
        widget=widgets.CheckboxInput,
        blank=True,
    )
    main_tobacco_type_5 = models.BooleanField(
        label="파이프담배",
        widget=widgets.CheckboxInput,
        blank=True,
    )
    main_tobacco_type_6 = models.BooleanField(
        label="엽권련(시가)",
        widget=widgets.CheckboxInput,
        blank=True,
    )
    main_tobacco_type_7 = models.BooleanField(
        label="각련(말아피우는 담배)",
        widget=widgets.CheckboxInput,
        blank=True,
    )
    main_tobacco_type_8 = models.BooleanField(
        label="물담배",
        widget=widgets.CheckboxInput,
        blank=True,
    )
    main_tobacco_type_9 = models.BooleanField(
        label="씹는담배",
        widget=widgets.CheckboxInput,
        blank=True,
    )
    main_tobacco_type_10 = models.BooleanField(
        label="냄새맡는 담배",
        widget=widgets.CheckboxInput,
        blank=True,
    )
    main_tobacco_type_11 = models.BooleanField(
        label="담배를 피우지 않음",
        widget=widgets.CheckboxInput,
        blank=True,
    )

# PAGES
class BQ_1(Page):
    form_model = 'player'
    form_fields = [
        'region',
        'born_year',
        'tot_tobacco_pcs',
        'recent_tobacco_yesno',
        'recent_liq_tobacco_yesno',
        'main_tobacco_type_1',
        'main_tobacco_type_2',
        'main_tobacco_type_3',
        'main_tobacco_type_4',
        'main_tobacco_type_5',
        'main_tobacco_type_6',
        'main_tobacco_type_7',
        'main_tobacco_type_8',
        'main_tobacco_type_9',
        'main_tobacco_type_10',
        'main_tobacco_type_11',
    ]




page_sequence = [BQ_1]
