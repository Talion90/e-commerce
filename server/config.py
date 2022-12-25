import os


class AppCfg:
    host = os.environ.get("APP_HOST", "localhost")
    port = int(os.environ.get("APP_PORT", 8000))

    @property
    def settings(self) -> dict:
        return dict(host=self.host, port=self.port)
