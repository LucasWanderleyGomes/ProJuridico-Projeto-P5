from blog.api.viewsets import BlogPostViewSet
from rest_framework.routers import SimpleRouter

blogPostRouter = SimpleRouter()
blogPostRouter.register('blogPosts', BlogPostViewSet)