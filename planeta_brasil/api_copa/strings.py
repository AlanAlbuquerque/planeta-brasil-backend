#coding: utf-8


def translation(lang=None):

    if isinstance(lang, int):
        _lang = {1: 'pt', 2: 'en', 3: 'es'}
        lang = _lang[lang]

    lang = lang or 'pt'

    messages = {
        'pt': {
            'success': 'Sucessso!',
            'email_has_guess_match': u'Seu palpite para este jogo já foi registrado.',
            'guess_match_registered_success': u'Palpite registrado com sucesso.',
        },
        'en': {
            'success': 'Sucesss!',
            'email_has_guess_match': u'Your guess this game has already been registered.',
            'guess_match_registered_success': u'Prediction successfully registered.',

        },
        'es': {
            'success': 'Éxito!',
            'email_has_guess_match': u'Su conjetura este juego ya ha sido registrada.',
            'guess_match_registered_success': u'Predicción registrado correctamente.',

        },
    }

    return messages[lang]
