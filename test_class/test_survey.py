import pytest
from survey import AnonymousSurvey


@pytest.fixture
def language_survey():
    question = "what language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)
    return language_survey


def test_store_single_response(language_survey):
    language_survey.store_response("english")

    assert 'english' in language_survey.responses


def test_store_three_responses(language_survey):
    question = "what language did you first learn to speak?"
    language_survey = AnonymousSurvey(question)

    responses = ["english", "spanish", 'portuguese']

    for response in responses:
        language_survey.store_response(response)

    for response in responses:
        assert response in language_survey.responses
