from base import *
import dj_database_url

DEBUG = True

# Database
DATABASES = {
    'default': dj_database_url.config('CLEARDB_DATABASE_URL')
}

# Stripe environment variables
STRIPE_PUBLISHABLE = os.getenv('STRIPE_PUBLISHABLE', 'pk_test_4ccy0JKl31lgweIUCX4wEwVA')
STRIPE_SECRET = os.getenv('STRIPE_SECRET', 'sk_test_W1BKv914iKkctKh7kiSH9LOg')

# PayPal Settings
SITE_URL = 'https://renanclothestore.herokuapp.com/'
PAYPAL_NOTIFY_URL = 'http://127.0.0.1/a-very-hard-to-guess-url/'
PAYPAL_RECEIVER_EMAIL = 'renandias@yahoo.com.br'


