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
        label="귀하의 거주지역을 선택해주세요.",
        widget=widgets.RadioSelect,
        choices=[
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
        label="귀하의 혼인상태를 선택해주십시오",
        widget=widgets.RadioSelect,
        choices=[
            [1, "결혼 안함"],
            [2, "결혼함"],
            [3, "이혼/사별함"],
            [4, "기타"]
        ]
    )
    graduated_level = models.IntegerField(
        label="귀하의 최종 학력을 선택해주세요",
        widget=widgets.RadioSelect,
        choices=[
            [1, "무학"],
            [2, "초등학교 졸업 이하"],
            [3, "중학교 졸업 이하"],
            [4, "고등학교 졸업 이하"],
            [5, "전문대/대학교 졸업 이하"],
            [6, "대학원 수료 이상"]
        ]
    )
    vocation = models.IntegerField(
        label="귀하의 직업을 선택해주세요",
        widget=widgets.RadioSelect,
        choices=[
            [1, "관리자"],
            [2, "전문가 및 관련 종사자"],
            [3, "사무 종사자"],
            [4, "서비스 종사자"],
            [5, "판매 종사자"],
            [6, "농림어업 숙련 종사자"],
            [7, "기능 및 관려기능 종사자"],
            [8, "장치, 기계조작 및 조립 종사자"],
            [9, "단순 노무 종사자"],
            [10, "군인"],
            [11, "기타(직접입력)"]
        ]
    )
    vocation_op = models.StringField(
        label="",
        blank=True,
    )
    income = models.IntegerField(
        label="임금, 부동산 소득, 연금, 이자, 정부 보조금, 친척이나 자녀들의 용돈 등 모든 수입을 합쳐 최근 1년 동안 가구의 총 소득은 대략 얼마입니까? 만일 연간소득을 대답하기 어려운 경우 월 평균 액수를 말씀해 주십시오",
        widget = widgets.RadioSelect,
        choices = [
        [1, "연_____만원"],
        [2, "월_____만원"],
    ]
    )
    income_year_op = models.StringField(
        label="",
        blank=True,
    )
    income_month_op = models.StringField(
        label="",
        blank=True,
    )

    drink_yesno = models.IntegerField(
        label = "지금까지 살아오면서 1잔 이상의 술을 마신 적이 있습니까? [제사, 차례 때 몇 모금 마셔본 것은 제외합니다.]",
        widget = widgets.RadioSelect,
        choices = [
            [1, "술을 마셔 본 적 없다"],
            [2, "있다"],
        ]
    )

    drink_how_often = models.IntegerField(
        label = "술을 얼마나 자주 마십니까?",
        widget = widgets.RadioSelect,
        choices = [
            [1, "최근 1년간 전혀 마시지 않았다"],
            [2, "한 달에 1번 미만"],
            [3, "한 달에 1번 정도"],
            [4, "한 달에 2~4번"],
            [5, "일주일에 2~3번 정도"],
            [6, "일주일에 4번 이상"],
        ]
    )

    drink_how_much = models.IntegerField(
        label = "한 번에 술을 얼마나 마십니까? [소주, 양주 구분없이 각각의 술잔으로 계산합니다. 단 캔맥주 1개(355cc)는 맥주 1.6잔과 같습니다.]",
        widget = widgets.RadioSelect,
        choices = [
            [1, "1~2잔"],
            [2, "3~4잔"],
            [3, "5~6잔"],
            [4, "7~9잔"],
            [5, "10잔 이상"],
        ]
    )

    strong_exercise_yesno = models.IntegerField(
        label = "본인의 일은 최소 10분 이상 계속 숨이 차거나 심장이 빠르게 뛰는 강도 높은 신체활동을 포함하고 있습니까? [강도 높은 신체활동: 건설 현장의 노동, 빠르게 걷기, 물건 나르기, 청소, 육아]",
        widget = widgets.RadioSelect,
        choices = [
            [1, "예"],
            [2, "아니요"],
        ]
    )


    strong_exercise_hours = models.IntegerField(
        label = "",
        choices = range(169)
    )

    strong_exercise_mins = models.IntegerField(
        label = "",
        choices = range(60)
    )

    walk_or_bike = models.IntegerField(
        label = "평소 장소를 이동할 때 최소 10분 이상 계속 걷거나 자전거 이용을 하십니까?",
        widget = widgets.RadioSelect,
        choices = [
            [1, "예"],
            [2, "아니요"],
        ]
    )

    sports_or_leisure_hours = models.IntegerField(
        label="",
        choices=range(169)
    )

    sports_or_leisure_mins = models.IntegerField(
        label="",
        choices=range(60)
    )

    health_ok = models.IntegerField(
        label = "평소에 ____님의 건강은 어떻다고 생각하십니까?",
        widget = widgets.RadioSelect,
        choices = [
            [1, "매우 좋음"],
            [2, "좋음"],
            [3, "보통"],
            [4, "나쁨"],
            [5, "매우 나쁨"],
        ]
    )

    discomfort_yesno = models.IntegerField(
        label = "최근 2주 동안 만성,급성질환 및 사고 중독 등으로 몸이 아프거나 불편을 느꼈던 적이 있습니까?",
        widget = widgets.RadioSelect,
        choices = [
            [1, "예"],
            [2, "아니요"]
        ]
    )

    discomfort_days = models.IntegerField(
        label = "",
        choices = range(15)
    )

    stress_how_much = models.IntegerField(
        label  = "평소 일상생활 중에 스트레스를 어느 정도 느끼고 있습니까?",
        widget = widgets.RadioSelect,
        choices = [
            [1, "대단히 많이 느낀다"],
            [2, "많이 느끼는 편이다"],
            [3, "조금 느끼는 편이다"],
            [4, "거의 느끼지 않는다"],
        ]
    )

    distress_yesno = models.IntegerField(
        label = "최근 1년 동안 연속적으로 2주 이상 일상생활에 지장이 있을 정도로 슬프거나 절망감 등을 느낀 적이 있습니까?",
        widget = widgets.RadioSelect,
        choices = [
            [1, "예"],
            [2, "아니요"]
        ]
    )

    suicide_thought_yesno = models.IntegerField(
        label = "최근 1년 동안 심각하게 자살을 생각한 적이 있습니까?",
        widget = widgets.RadioSelect,
        choices=[
            [1, "예"],
            [2, "아니요"]
        ]
    )

    suicide_plan_yesno = models.IntegerField(
        label="최근 1년 동안 자살하기 위해 구체적인 계획을 세운 적이 있습니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "예"],
            [2, "아니요"]
        ]
    )

    suicide_tryout_yesno = models.IntegerField(
        label="최근 1년 동안 실제로 자살시도를 해 본 적이 있습니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "예"],
            [2, "아니요"]
        ]
    )

    mental_advice_yesno = models.IntegerField(
        label = "최근 1년 동안 정신적인 문제 때문에 방문, 전화, 인터넷 등을 통해 상담을 받아본 적이 있습니까?",
        widget = widgets.RadioSelect,
        choices=[
            [1, "예"],
            [2, "아니요"]
        ]
    )

    cigarette_current_use = models.IntegerField(
        label="귀하께서는 일반담배(궐련) 사용 경험이 있다고 하셨습니다. 현재도 주로 사용하고 있습니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "지금도 사용하고 있다 "],
            [2, "이제는 사용하지 않고 있다"]
        ]
    )
    cessation_time_cigarette = models.IntegerField(
        label="<금연답변시> 앞서 선생님은 과거 일반담배(궐련)을 피웠으나 지금은 그만두셨다고 답변하셨습니다. 금연(궐련 중단)시기는 언제였습니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "2020년 2월 이전(코로나 19 확산 이전)"],
            [2, "2020년 2월 이후(코로나19 대유행 이후)"]
        ]
    )
    first_smoking_cigarette = models.IntegerField(
        label="",
        choices = range(100)
    )
    smoking_usually_cigarette = models.IntegerField(
        label="",
        choices = range(100)
    )
    smoking_amount_cigarette = models.IntegerField(
        label="",
        choices = range(1000)
    )

# PAGES
class BQ_1(Page):
    form_model = 'player'
    form_fields = [
        'region',
        'marriage_stat',
        'graduated_level',
        'vocation',
        'vocation_op',
        'income',
        'income_year_op',
        'income_month_op',
    ]

class HealthInfo(Page):
        form_model = 'player'
        form_fields = [
            'drink_yesno',
            'drink_how_often',
            'drink_how_much',
            'strong_exercise_yesno',
            'strong_exercise_hours',
            'strong_exercise_mins',
            'walk_or_bike',
            'sports_or_leisure_hours',
            'sports_or_leisure_mins',
            'health_ok',
            'discomfort_yesno',
            'discomfort_days',
            'stress_how_much',
            'distress_yesno',
            'suicide_thought_yesno',
            'suicide_plan_yesno',
            'suicide_tryout_yesno',
            'mental_advice_yesno',

        ]


class TobaccoUsage_Cigarette(Page):
    form_model = 'player'
    form_fields = [
        'cigarette_current_use',
        'cessation_time_cigarette',
        'first_smoking_cigarette',
        'smoking_usually_cigarette',
        'smoking_amount_cigarette',
    ]


page_sequence = [BQ_1, HealthInfo, TobaccoUsage_Cigarette]
