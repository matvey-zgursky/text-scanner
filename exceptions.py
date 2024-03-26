class UnsupportedOperatingSystemError(Exception):
    """Для неподдерживаемых операционных систем."""
    def __init__(self, os_name):
        super().__init__(f'Операционная система "{os_name}" не поддерживается')