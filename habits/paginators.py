from rest_framework.pagination import PageNumberPagination


class CustomPagination(PageNumberPagination):
    """Предоставляет возможность настроить размер страницы и максимальный размер страницы."""
    page_size = 5
    page_size_query_param = 'page_size'
    max_page_size = 10