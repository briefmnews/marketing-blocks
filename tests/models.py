# This file emulates a model editorial.Issue for testing purposes. It can be removed when
# marketing_blocks app is moved into briefme-core and regular editorial fixture are available.


class Meta:
    model_name = "issue"


class Issue:
    @property
    def _meta(self):
        return Meta()
