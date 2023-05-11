import sentry_sdk
sentry_sdk.init(
    dsn="https://99d223746f844262b4cf4bcfa207537f@o4505166541946880.ingest.sentry.io/4505166551515136",

    # Set traces_sample_rate to 1.0 to capture 100%
    # of transactions for performance monitoring.
    # We recommend adjusting this value in production.
    traces_sample_rate=1.0
)
# Отправка без ошибки
with sentry_sdk.configure_scope() as scope:
    #Создание tag
    scope.set_tag('tag_lab','working')
    a = 5
    b = 7
    c = a + b
    #Создание tag
    scope.set_tag('tag_for_lab',c)
    try:
        print(c/0)
    except Exception:
        sentry_sdk.capture_message("Exception")


# Exception ZeroDivisionError
#division_by_zero = 1 / 0