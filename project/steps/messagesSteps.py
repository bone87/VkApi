# coding=utf-8
from project.api_call.messagesApi import MessagesApi


def send_message(account_id, user_model, message):
    """
    Отправляет сообщение.
    После успешного выполнения возвращает идентификатор отправленного сообщения.
    """
    return MessagesApi(account_id).send(user_model=user_model, text=message)


def send_birthday_message(account_id, user_model):
    if user_model.can_write_private_message == 1:
        birthday_message = 'с днЁм рождения) Здоровья, любви, тепла и чтобы всё сбылось, что сегодня нажелают😉'
        discount_message = 'В честь дня рождения мы дарим вам скидочку 10% на установку Windows или чистку ' \
                           'ноутбука, на выбор😊.\nДействует в течении месяца😉'
        end_dialog = 'Еще раз с праздником!😊'
        message = '{birth}\n\n{discount}\n{end}'.format(birth=birthday_message,
                                                        discount=discount_message,
                                                        end=end_dialog)
        return send_message(account_id=account_id,
                            user_model=user_model,
                            message=message)
