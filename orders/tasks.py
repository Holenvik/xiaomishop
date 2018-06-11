from celery import task
from django.core.mail import send_mail
from .models import Order, OrderItem


@task
def order_created(order_id):
    """
    Задача для отправки уведомления по электронной почте при успешном создании заказа.
    """
    order = Order.objects.get(id=order_id)
    subject = 'Номер заказа  {}'.format(order_id)
    message = 'Здравствуйте, {},\n\nВы успешно создали заказ для Ваших товаров\
                \n\nЕсли Ваш заказ был совершён до 14:00, то мы доставим его сегодня, если после 14:00, то доставка будет осуществлена завтра. Если у Вас имеются вопросы, то звоните менеджеру: +375296452533.\n\nВаш номер заказа {}.'.format(order.first_name,
                                             order.id)
    mail_sent = send_mail(subject,
                          message,
                          'kekscheburek@yandex.ru',
                          [order.email])
    return mail_sent
