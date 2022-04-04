from myapp.models import Course, CourseTerm

from model_bakery.recipe import Recipe, foreign_key, seq

course_recipe = Recipe(
    Course,
    course_number=seq("course_num"),
    course_identifier=seq("course_identifier"),
    course_name=seq("course"),
)

course_term_recipe = Recipe(
    CourseTerm,
    term_identifier=seq("term_identifier"),
    course = foreign_key(course_recipe)
)