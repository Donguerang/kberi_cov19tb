from os import environ

SESSION_CONFIGS =[
    dict(
        name='online_survey',
        display_name='코로나19와 금연전략 설문조사',
        app_sequence=[
            'introduction',
            'SQ',
            'OnlineSurvey',
        ],
        num_demo_participants=1,
    )
    ]


SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)
LANGUAGE_CODE = 'en'


SECRET_KEY = '3368883363321'
