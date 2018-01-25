from django.conf.urls import url,include
from snippets import views
from rest_framework.urlpatterns import format_suffix_patterns
from rest_framework import renderers
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view
from rest_framework.documentation import include_docs_urls
from rest_framework.authtoken import views as token_views

'''
snippet_list=views.SnippetViewSet.as_view({
    'get':'list',
    'post':'create'
})

snippet_detail=views.SnippetViewSet.as_view({
    'get':'retrieve',
    'put':'update',
    'patch':'partial_update',
    'delete':'destroy'
})

snippet_highlight=views.SnippetViewSet.as_view({
    'get':'highlight',
},renderer_classes=[renderers.StaticHTMLRenderer])

user_list=views.UserViewSet.as_view({
    'get':'list',
})

user_detail=views.UserViewSet.as_view({
    'get':'retrieve'
})
'''

router=DefaultRouter()
router.register(r'snippets',views.SnippetViewSet)
router.register(r'users',views.UserViewSet)

schema_view=get_schema_view(title='Pastebin API')

urlpatterns=[
    #url(r'^users/$',user_list,name='user-list'),
    #url(r'^users/(?P<pk>\d+)/$',user_detail,name='user-detail'),
    #url(r'^snippets/$',snippet_list,name='snippet-list'),
    #url(r'^snippets/(?P<pk>\d+)/$',snippet_detail,name='snippet-detail'),
    #url(r'^snippets/(?P<pk>\d+)/highlight/$',snippet_highlight,name='snippet-highlight'),
    #url(r'^api/$',views.api_root),
    url(r'^schema/$',schema_view),
    url(r'^',include(router.urls)),
    url(r'^docs/',include_docs_urls(title='Web API Guide')),
    url(r'^api-token-auth/',token_views.obtain_auth_token), #post username and password to get token
]

#urlpatterns=format_suffix_patterns(urlpatterns)