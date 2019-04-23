class analytics_moodle_uv_router(object):
    """
    A router to control all database operations on models in the
    analytics moodle uv application.
    """
    def db_for_read(self, model, **hints):
        """
        Attempts to read analytics_moodle_uv models go to moodle_dwh.
        """
        if model._meta.app_label == 'analytics_moodle_uv':
            return 'moodle_dwh'
        return None

    def db_for_write(self, model, **hints):
        """
        Attempts to write analytics_moodle_uv models go to moodle_dwh.
        """
        if model._meta.app_label == 'analytics_moodle_uv':
            return 'moodle_dwh'
        return None

    def allow_relation(self, obj1, obj2, **hints):
        """
        Allow relations if a model in the analytics_moodle_uv app is involved.
        """
        if obj1._meta.app_label == 'analytics_moodle_uv' or \
           obj2._meta.app_label == 'analytics_moodle_uv':
           return True
        return None

    def allow_migrate(self, db, app_label, model_name=None, **hints):
        """
        Make sure the analytics_moodle_uv app only appears in the 'moodle_dwh'
        database.
        """
        if app_label == 'analytics_moodle_uv':
            return db == 'moodle_dwh'
        return None