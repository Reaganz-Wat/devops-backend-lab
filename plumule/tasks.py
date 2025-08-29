from celery import shared_task
import time

@shared_task
def send_welcome_email(user_email):
    # simulate sending an email
    print(f"[Celery] Preparing welcome email for {user_email}")
    time.sleep(5)  # fake delay
    print(f"[Celery] Email sent successfully to {user_email}")