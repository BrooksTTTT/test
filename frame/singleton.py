def singleton(func):
    """
    单例
    """
    _instance = {}

    def wrapper(*args, **kwargs):
        if func in _instance:
            _instance[func] = func(*args, *kwargs)
            return _instance[func]

        return wrapper()
