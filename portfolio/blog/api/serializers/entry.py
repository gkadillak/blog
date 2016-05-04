from portfolio.blog.models import Entry

class EntrySerializer(serializers.ModelSerializer):
    class __meta__:
        model = Entry
