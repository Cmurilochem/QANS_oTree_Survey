from otree.api import *


class C(BaseConstants):
    NAME_IN_URL = 'Turbulence_survey'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    age = models.IntegerField(label='What is your age?', min=13, max=125)
    gender = models.StringField(
        choices=[['Male', 'Male'], ['Female', 'Female']],
        label='What is your gender?',
        widget=widgets.RadioSelect,
    )
    most_communicative = models.StringField(label='Which member do you think is the most communicative?')
    most_critical = models.StringField(label='Which member do you think is the most critical?')
    most_popular = models.StringField(label='Who do you think is the popular?')

# FUNCTIONS
# PAGES
class Demographics(Page):
    form_model = 'player'
    form_fields = ['age', 'gender']


class SocialBehaviour(Page):
    form_model = 'player'
    form_fields = ['most_communicative', 'most_critical', 'most_popular']


class FinalPage(Page):
    form_model = 'player'


page_sequence = [Demographics, SocialBehaviour, FinalPage]
