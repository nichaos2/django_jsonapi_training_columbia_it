import pytest
from model_bakery import baker
from myapp.models import Course, CourseTerm

# this is a simple test to check how tox works
# TODO: more tests for views , serializers?
class TestModels:

    baker_path = "myapp.tests.baker_recipes"
    course_recipe = f"{baker_path}.course_recipe"
    course_term_recipe = f"{baker_path}.course_term_recipe"

    @pytest.mark.django_db
    def test_course_term(self):

        baker.make_recipe(self.course_term_recipe, 4)
        terms = CourseTerm.objects.all()
        assert 4 == terms.count()
