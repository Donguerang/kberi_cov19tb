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

# BQ_1에 해당하는 질문"

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

# 일반담배(궐련형) 담배에 해당하는 질문

    smoking_current_usage_cigarette = models.IntegerField(
        label="귀하께서는 일반담배(궐련) 사용 경험이 있다고 하셨습니다. 현재도 주로 사용하고 있습니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "지금도 사용하고 있다"],
            [2, "이제는 사용하지 않고 있다"],

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
    smoking_days_cigarette = models.IntegerField(
        label="",
        choices = range(31)
    )
    smoking_daily_amount_cigarette = models.IntegerField(
        label="",
        choices = range(1000)
    )
    smoking_period_year_cigarette = models.IntegerField(
        label="",
        choices = range(100)
    )
    smoking_period_month_cigarette = models.IntegerField(
        label="",
        choices = range(13)
    )
    smoking_previous_amount_cigarette = models.IntegerField(
        label="",
        choices = range(1000)
    )
    smoking_morning_cigarette = models.IntegerField(
        label="(과거 일반담배(궐련) 흡연자는 흡연당시 기준으로 작성) 아침에 일어나서 얼마 만에 첫 일반담배(궐련)를 피우십니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "5분 이내"],
            [2, "6분~30분 사이"],
            [3, "31분~1시간 사이"],
            [4, "1시간 이후"],
        ]
    )
    smoking_area_cigarette = models.IntegerField(
        label="(과거 일반담배(궐련) 흡연자는 흡연당시 기준으로 작성) 금연구역(도서관, 극장, 병원 등)에서 일반담배(궐련)를 참기가 어렵습니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "예"],
            [2, "아니요"],
        ]
    )
    smoking_tasty_cigarette = models.IntegerField(
        label="(과거 일반담배(궐련) 흡연자는 흡연당시 기준으로 작성) 하루 중 일반담배(궐련) 맛이 가장 좋은 때는 언제입니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "아침 첫 담배"],
            [2, "그 외의 담배"],
        ]
    )
    smoking_amount_multiple_choice_cigarette = models.IntegerField(
        label="(과거 일반담배(궐련) 흡연자는 흡연당시 기준으로 작성) 하루에 보통 몇 개비나 피우십니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "10개비 이하"],
            [2, "11~20 개비"],
            [3, "21~30 개비"],
            [4, "31개비 이상"],
        ]
    )
    smoking_morning_frequency_cigarette = models.IntegerField(
        label="(과거 일반담배(궐련) 흡연자는 흡연당시 기준으로 작성) 아침에 일어나서 첫 몇 시간 동안 하루 중 다른 시간보다 더 자주 일반담배(궐련)를 피우십니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "예"],
            [2, "아니요"],
        ]
    )
    smoking_sick_usage_cigarette = models.IntegerField(
        label="(과거 일반담배(궐련) 흡연자는 흡연당시 기준으로 작성) 몸이 아파 하루 종일 누워있을 때에도 일반담배(궐련)를 피우십니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "예"],
            [2, "아니요"],
        ]
    )
    smoking_after_corona_cigarette = models.IntegerField(
        label="2020년 2월 전후(코로나19 유행전후)를 비교하면 일반담배(궐련) 사용량은 어떤 변화가 있었습니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "매우 줄었음"],
            [2, "줄었음"],
            [3, "변화없음"],
            [4, "늘었음"],
            [5, "매우 늘었음"],
        ]
    )
    smoking_corona_increase_cigarette = models.IntegerField(
        label="[증가답변시] 흡연량(일반담배 사용량) 증가이유는?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "스트레스가 증가해서"],
            [2, "집에 있는 시간이 많아져서"],
            [3, "집에 있는 시간이 늘면서 지루해져서"],
            [4, "기타"],
        ]
    )
    smoking_corona_decrease_cigarette = models.IntegerField(
        label="[감소답변시] 흡연량(일반담배 사용량) 감소이유는?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "코로나19에 걸릴 것 같아서 (건강에 대한 우려)"],
            [2, "일정이 변경되어서"],
            [3, "비흡연자와 함께 있어서"],
            [4, "코로나19에 흡연자가 더 취약한 것 같아서"],
            [5, "기타"],
        ]
    )
    smoking_corona_awareness_cigarette = models.IntegerField(
        label="코로나19 유행 이후 일반담배(궐련) 흡연시 주변 사람을 의식하는 정도가 증가했습니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "매우 증가"],
            [2, "증가"],
            [3, "변화 없음"],
            [4, "감소"],
            [5, "매우 감소"],
        ]
    )

# 액상형 전자담배에 해당하는 질문

    smoking_current_usage_vape = models.IntegerField(
        label="귀하께서는 액상형 전자담배(가열담배, 예: 쥴, 탱크형 등) 사용 경험이 있다고 하셨습니다. 현재도 주로 사용하고 있습니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "지금도 사용하고 있다"],
            [2, "이제는 사용하지 않고 있다"],

        ]
    )
    smoking_corona_cessation_vape = models.IntegerField(
        label="앞서 선생님은 과거 액상형 전자담배를 사용했으나 지금은 그만두셨다고 답변하셨습니다. 금연(액상형 전자담배 사용 중단)시기는 언제였습니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "2020년 2월 이전 (코로나19 확산 이전)"],
            [2, "2020년 2월 이후 (코로나19 대유행 이후)"],

        ]
    )
    smoking_first_year_vape = models.IntegerField(
        label="",
        choices=range(100)
    )
    smoking_first_month_vape = models.IntegerField(
        label="",
        choices=range(13)
    )
    smoking_last_year_vape = models.IntegerField(
        label="",
        choices=range(100)
    )
    smoking_last_month_vape = models.IntegerField(
        label="",
        choices=range(13)
    )
    smoking_using_days_vape = models.IntegerField(
        label="",
        choices=range(31)
    )
    smoking_amount_vape = models.IntegerField(
        label="",
        choices=range(100)
    )
    smoking_nicotine_amount_vape = models.IntegerField(
        label="귀하가 현재 사용하는 또는 과거에 사용한 액상형 전자담배(쥴, 탱크형 등) 액상의 니코틴 농도(액상 1ml 기준 니코틴 함유량)는 얼마입니까? (1mg/ml=0.1%)",
        widget=widgets.RadioSelect,
        choices=[
            [1, "니코틴 없음"],
            [2, "1~6mg/ml"],
            [3, "7~12mg/ml"],
            [4, "13~18mg/ml"],
            [5, "19mg/ml 이상"],
            [6, "잘 모름"],
        ]
    )
    smoking_morning_vape = models.IntegerField(
        label="(과거 액상형 전자담배(쥴, 탱크형 등) 사용자는 사용당시 기준으로 작성) 아침에 일어나서 얼마 만에 첫 액상형 전자담배(쥴, 탱크형 등)를 사용하십니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "5분 이내"],
            [2, "6분~30분 사이"],
            [3, "31분~1시간 사이"],
            [4, "1시간 이후"],

        ]
    )
    smoking_area_vape = models.IntegerField(
        label="(과거 액상형 전자담배(쥴, 탱크형 등) 사용자는 사용당시 기준으로 작성) 금연구역(도서관, 극장, 병원 등)에서 액상형 전자담배(쥴, 탱크형 등)를 참기가 어렵습니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "예"],
            [2, "아니요"],
       ]
    )
    smoking_tasty_vape = models.IntegerField(
        label="(과거 액상형 전자담배(쥴, 탱크형 등) 사용자는 사용당시 기준으로 작성) 하루 중 액상형 전자담배(쥴, 탱크형 등) 맛이 가장 좋은 때는 언제입니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "아침 첫 사용시기"],
            [2, "그 외의 사용시기"],

        ]
    )
    smoking_daily_frequency_vape = models.IntegerField(
        label="(과거 액상형 전자담배(쥴, 탱크형 등) 사용자는 사용당시 기준으로 작성) 하루에 보통 몇 번 사용하십니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "10회 이하"],
            [2, "11~20회"],
            [3, "21~30회"],
            [4, "31회 이상"],

        ]
    )
    smoking_morning_frequency_vape = models.IntegerField(
        label="(과거 액상형 전자담배(쥴, 탱크형 등) 사용자는 사용당시 기준으로 작성) 아침에 일어나서 첫 몇 시간 동안 하루 중 다른 시간보다 더 자주 액상형 전자담배(쥴, 탱크형 등)를 사용하십니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "예"],
            [2, "아니요"],

        ]
    )
    smoking_sick_usage_vape = models.IntegerField(
        label="(과거 액상형 전자담배(쥴, 탱크형 등) 사용자는 사용당시 기준으로 작성) 몸이 아파 하루 종일 누워있을 때에도 액상형 전자담배(쥴, 탱크형 등)를 사용하십니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "예"],
            [2, "아니요"],

        ]
    )
    smoking_after_corona_vape = models.IntegerField(
        label="2020년 2월 전후(코로나19 유행전후)를 비교하면 액상형 전자 담배(쥴, 탱크형 등) 사용량은 어떤 변화가 있었습니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "매우 줄었음"],
            [2, "줄었음"],
            [3, "변화없음"],
            [4, "늘었음"],
            [5, "매우 늘었음"],

        ]
    )
    smoking_corona_increase_vape = models.IntegerField(
        label="[증가답변시] 액상형 전자담배 사용량 증가이유는?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "스트레스가 증가해서"],
            [2, "집에 있는 시간이 많아져서"],
            [3, "집에 있는 시간이 늘면서 지루해져서"],
            [4, "기타"],

        ]
    )
    smoking_corona_decrease_vape = models.IntegerField(
        label="[감소답변시] 액상형 전자담배 감소이유는?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "코로나19에 걸릴 것 같아서 (건강에 대한 우려)"],
            [2, "일정이 변경되어서"],
            [3, "비흡연자와 함께 있어서"],
            [4, "코로나19에 흡연자가 더 취약한 것 같아서"],
            [5, "기타"],
        ]
    )
    smoking_corona_awareness_vape = models.IntegerField(
        label="코로나19유행 이후 액상형 전자담배 사용시 주변사람을 의식하는 정도가 증가했습니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "매우 증가"],
            [2, "증가"],
            [3, "변화 없음"],
            [4, "감소"],
            [5, "매우 감소"],
        ]
    )
 # 궐련형 전자담배

    smoking_current_usage_heat = models.IntegerField(
        label="귀하께서는 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등) 사용 경험이 있다고 하셨습니다. 현재도 주로 사용하고 있습니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "지금도 사용하고 있다"],
            [2, "이제는 사용하지 않고 있다"],
        ]
    )
    smoking_corona_cessation_heat = models.IntegerField(
        label="금연(궐련형 전자담배 사용 중단)한지 얼마나 되었습니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "2020년 2월 이전(코로나 19 확산 이전)"],
            [2, "2020년 2월 이후(코로나19 대유행 이후)"],
          ]
    )
    smoking_first_year_heat = models.IntegerField(
        label="",
        choices=range(100)
    )
    smoking_first_month_heat = models.IntegerField(
        label="",
        choices=range(13)
    )
    smoking_last_year_heat = models.IntegerField(
        label="",
        choices=range(100)
    )
    smoking_last_month_heat = models.IntegerField(
        label="",
        choices=range(13)
    )
    smoking_using_days_heat = models.IntegerField(
        label="",
        choices=range(31)
    )
    smoking_amount_heat = models.IntegerField(
        label="",
        choices=range(100)
    )
    smoking_morning_heat = models.IntegerField(
        label="(과거 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등) 흡연자는 흡연당시 기준으로 작성) 아침에 일어나서 얼마 만에 첫 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등)를 사용하십니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "5분 이내"],
            [2, "6분~30분 사이"],
            [3, "31분~1시간 사이"],
            [4, "1시간 이후"],
        ]
    )
    smoking_area_heat = models.IntegerField(
        label="(과거 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등) 사용자는 사용당시 기준으로 작성) 금연구역(도서관, 극장, 병원 등)에서 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등)를 참기가 어렵습니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "예"],
            [2, "아니요"],
          ]
    )

    smoking_tasty_heat = models.IntegerField(
        label="(과거 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등) 사용자는 사용당시 기준으로 작성) 하루 중 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등) 맛이 가장 좋은 때는 언제입니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "아침 첫 사용 시기"],
            [2, "그 외의 사용 시기"],
          ]
    )
    smoking_daily_amount_heat = models.IntegerField(
        label="(과거 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등) 사용자는 사용당시 기준으로 작성) 하루에 보통 몇 개비를 사용하십니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "10개비 이하"],
            [2, "11~20개비"],
            [3, "21~30개비"],
            [4, "31개비 이상"],
        ]
    )
    smoking_morning_frequency_heat = models.IntegerField(
        label="(과거 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등) 사용자는 사용당시 기준으로 작성) 아침에 일어나서 첫 몇 시간 동안 하루 중 다른 시간보다 더 자주 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등)를 사용하십니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "예"],
            [2, "아니요"],
          ]
    )
    smoking_sick_usage_heat = models.IntegerField(
        label="(과거 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등) 사용자는 사용당시 기준으로 작성) 몸이 아파 하루 종일 누워있을 때에도 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등)를 사용하십니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "예"],
            [2, "아니요"],
          ]
    )
    smoking_after_corona_heat = models.IntegerField(
        label="2020년 2월 전후(코로나19 유행전후)를 비교하면 궐련형 전자담배(가열담배, 예: 아이코스, 글로, 릴 등) 사용량은 어떤 변화가 있었습니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "매우 줄었음"],
            [2, "줄었음"],
            [3, "변화 없음"],
            [4, "늘었음"],
            [5, "매우 늘었음"],
        ]
    )
    smoking_corona_increase_heat = models.IntegerField(
        label="[증가답변시] 궐련형 전자담배 사용량 증가이유는?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "스트레스가 증가해서"],
            [2, "집에 있는 시간이 많아져서"],
            [3, "집에 있는 시간이 늘면서 지루해져서"],
            [4, "기타"],
        ]
    )
    smoking_corona_decrease_heat = models.IntegerField(
        label="[감소답변시] 궐련형 전자담배 사용량 감소이유는?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "코로나19에 걸릴 것 같아서 (건강에 대한 우려)"],
            [2, "일정이 변경되어서"],
            [3, "비흡연자와 함께 있어서"],
            [4, "코로나19에 흡연자가 더 취약한 것 같아서"],
            [5, "기타"],
        ]
    )
    smoking_corona_awareness_heat = models.IntegerField(
        label="코로나19유행 이후 궐련형 전자담배 사용시 주변사람을 의식하는 정도가 증가했습니까?",
        widget=widgets.RadioSelect,
        choices=[
            [1, "매우 증가"],
            [2, "증가"],
            [3, "변화 없음"],
            [4, "감소"],
            [5, "매우 감소"],
        ]
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
        'smoking_current_usage_cigarette',
        'cessation_time_cigarette',
        'first_smoking_cigarette',
        'smoking_usually_cigarette',
        'smoking_amount_cigarette',
        'smoking_days_cigarette',
        'smoking_daily_amount_cigarette',
        'smoking_period_year_cigarette',
        'smoking_period_month_cigarette',
        'smoking_previous_amount_cigarette',
        'smoking_morning_cigarette',
        'smoking_area_cigarette',
        'smoking_tasty_cigarette',
        'smoking_amount_multiple_choice_cigarette',
        'smoking_morning_frequency_cigarette',
        'smoking_sick_usage_cigarette',
        'smoking_after_corona_cigarette',
        'smoking_corona_increase_cigarette',
        'smoking_corona_decrease_cigarette',
        'smoking_corona_awareness_cigarette',
    ]
class TobaccoUsage_Vape(Page):
    form_model = 'player'
    form_fields = [
        'smoking_current_usage_vape',
        'smoking_corona_cessation_vape',
        'smoking_first_year_vape',
        'smoking_first_month_vape',
        'smoking_last_year_vape',
        'smoking_last_month_vape',
        'smoking_using_days_vape',
        'smoking_amount_vape',
        'smoking_nicotine_amount_vape',
        'smoking_morning_vape',
        'smoking_area_vape',
        'smoking_tasty_vape',
        'smoking_daily_frequency_vape',
        'smoking_morning_frequency_vape',
        'smoking_sick_usage_vape',
        'smoking_after_corona_vape',
        'smoking_corona_increase_vape',
        'smoking_corona_decrease_vape',
        'smoking_corona_awareness_vape',
    ]
class TobaccoUsage_HeatCigarette(Page):
    form_model = 'player'
    form_fields = [
        'smoking_current_usage_heat',
        'smoking_corona_cessation_heat',
        'smoking_first_year_heat',
        'smoking_first_month_heat',
        'smoking_last_year_heat',
        'smoking_last_month_heat',
        'smoking_using_days_heat',
        'smoking_amount_heat',
        'smoking_morning_heat',
        'smoking_area_heat',
        'smoking_tasty_heat',
        'smoking_daily_amount_heat',
        'smoking_morning_frequency_heat',
        'smoking_sick_usage_heat',
        'smoking_after_corona_heat',
        'smoking_corona_increase_heat',
        'smoking_corona_decrease_heat',
        'smoking_corona_awareness_heat',
    ]


page_sequence = [BQ_1, HealthInfo, TobaccoUsage_Cigarette, TobaccoUsage_Vape, TobaccoUsage_HeatCigarette]
