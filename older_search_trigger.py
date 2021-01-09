from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('articles', '0012_auto_20201106_2314'),
    ]

    migration = '''
        CREATE TRIGGER search_vector_update BEFORE INSERT OR UPDATE
        ON articles_article FOR EACH ROW EXECUTE FUNCTION
        tsvector_update_trigger(search_vector, 'pg_catalog.turkish', title, message, user__username, tags__name, comments__content);

        UPDATE articles_article set ID = ID;
    '''

    reverse_migration = '''
        DROP TRIGGER search_vector ON articles_article;
    '''

    operations = [
        migrations.RunSQL(migration, reverse_migration)
    ]
