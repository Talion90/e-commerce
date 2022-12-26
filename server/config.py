import os


class AppCfg:
    host = os.environ.get("APP_HOST", "localhost")
    port = int(os.environ.get("APP_PORT", 8000))

    @classmethod
    def settings(cls) -> dict:
        return dict(host=cls.host, port=cls.port)
